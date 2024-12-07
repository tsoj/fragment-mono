import fontforge
import re
from pathlib import Path

def adjust_glyph_width(glyph, target_width):
    """Attempts to adjust the glyph's width to the target width."""
    current_width = glyph.width
    if current_width != target_width:
        scale_factor = target_width / current_width
        # Scale horizontally only
        glyph.transform((scale_factor, 0, 0, 1, 0, 0))
        glyph.width = target_width

def process_font(original_font_path: Path):
    """Processes a font file to create a bold version with width adjustments."""
    try:
        # Determine parameters based on whether it's an Italic font or not
        if "Italic" in original_font_path.stem:
            bold_font_name_minus = "Bold-Italic"
            bold_font_name = "Bold Italic"
            style_map = 0x21
        else:
            bold_font_name_minus = "Bold"
            bold_font_name = "Bold"
            style_map = 0x20

        # Construct the output file path using pathlib
        bold_font_path = original_font_path.with_name(
            re.sub(r"-(Regular|Italic)(\..*)", rf"-{bold_font_name_minus}\2", original_font_path.name)
        )

        # Open the font using FontForge
        font = fontforge.open(str(original_font_path))  # FontForge still expects string paths

        # Store original widths for monospace adjustment
        original_widths = {glyph_name: font[glyph_name].width for glyph_name in font}

        # Select glyphs and change weight
        font.selection.all()
        for glyph in font.selection.byGlyphs:
            glyph.changeWeight(35)
            glyph.removeOverlap()
            glyph.simplify()
            glyph.validate()

        # Set font metadata
        font.os2_weight = 700
        font.os2_stylemap = style_map
        font.familyname = "Fragment Mono"
        font.fontname = f"FragmentMono-{bold_font_name_minus}"
        font.fullname = f"Fragment Mono {bold_font_name}"
        font.macstyle = 0x01  # Bold

        # Adjust widths to match original widths
        for glyph_name in font:
            if glyph_name in original_widths:
                adjust_glyph_width(font[glyph_name], original_widths[glyph_name])

        # Generate the bold font
        font.generate(str(bold_font_path))
        print(f"Generated: {bold_font_path}")

    except Exception as e:
        print(f"Error processing {original_font_path}: {e}")

    finally:
        if 'font' in locals():
            font.close()

# Directory to search for font files
font_dir = Path("fonts")

# Find all relevant font files and process them
original_fonts = list(font_dir.glob("**/FragmentMono-Regular.*")) + list(font_dir.glob("**/FragmentMono-Italic.*"))
for font_path in original_fonts:
    process_font(font_path)
