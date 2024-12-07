import fontforge
import os
import re

def adjust_glyph_width(glyph, target_width):
    """Attempts to adjust the glyph's width to the target width."""
    current_width = glyph.width
    if current_width != target_width:
        scale_factor = target_width / current_width
        # Scale horizontally only
        glyph.transform((scale_factor, 0, 0, 1, 0, 0))
        glyph.width = target_width

        # Further refinements might be needed here to adjust
        # control points and maintain curve quality after scaling.

def process_font(regular_font_path):
    """Processes a font file to create a bold version with width adjustments."""
    try:
        # Extract directory, filename, and extension
        dir_name = os.path.dirname(regular_font_path)
        file_name = os.path.basename(regular_font_path)
        extension = os.path.splitext(file_name)[1]

        # Determine parameters based on whether it's an Italic font or not
        if "Italic" in file_name:
            base_name = "Italic"
            bold_font_name_minus = "Bold-Italic"
            bold_font_name = "Bold Italic"
            style_map = 0x21
        else:
            base_name = "Regular"
            bold_font_name_minus = "Bold"
            bold_font_name = "Bold"
            style_map = 0x20

        base = re.sub(r"-{}(.*)".format(base_name), r"\1", file_name)
        bold_font_path = os.path.join(dir_name, f"{base}-{bold_font_name_minus}{extension}")

        # Open the font using FontForge
        font = fontforge.open(regular_font_path)

        # Store original widths for monospace adjustment
        original_widths = {glyph_name: font[glyph_name].width for glyph_name in font}

        # Select glyphs and change weight
        font.selection.all()

        pen = font[0x0041].glyphPen()
        print("hi2")
        for glyph in font.selection.byGlyphs:
            glyph.changeWeight(29)
            # print("hi1")
            # glyph.
            # # glyph.stroke(pen, "circular", 0, 27, 0, "round", "round", 0)
            # glyph.stroke(pen, "circular", "round", "round", 0, 27, 0)

            glyph.removeOverlap()
            glyph.simplify()
            glyph.validate()

        #font.changeWeight(27)

        # Set font metadata
        font.os2_weight = 700
        font.os2_stylemap = style_map
        font.familyname = "Fragment Mono"
        font.fontname = f"FragmentMono-{bold_font_name_minus}"
        font.fullname = f"Fragment Mono {bold_font_name}"
        font.macstyle = 0x01  # Bold

        # Adjust widths to match original widths
        for glyph_name in font:
            adjust_glyph_width(font[glyph_name], original_widths[glyph_name])

        # Generate the bold font
        font.generate(bold_font_path)
        print(f"Generated: {bold_font_path}")

    except Exception as e:
        print(f"Error processing {regular_font_path}: {e}")

    finally:
        if 'font' in locals():
            font.close()

# Directory to search for font files
font_dir = "fonts"

# Find all relevant font files and process them
for root, _, files in os.walk(font_dir):
    for file in files:
        if file.startswith("FragmentMono-Regular.") or file.startswith("FragmentMono-Italic."):
            regular_font_path = os.path.join(root, file)
            process_font(regular_font_path)
