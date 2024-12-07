
#!/bin/bash

set -e

# Directory to search for font files
font_dir="fonts/"

# Find all files matching the pattern *-Regular.* or *-Italic.*
find "$font_dir" -type f \( -name 'FragmentMono-Regular.*' -o -name 'FragmentMono-Italic.*' \) | while read -r regular_font; do
    # Extract the directory, filename, and extension
    dir=$(dirname "$regular_font")
    filename=$(basename "$regular_font")
    extension="${filename##*.}"

    # Define the output file name and style properties
    if [[ "$filename" == *-Italic.* ]]; then
        base_name="Italic"
        bold_font_name_minus="Bold-Italic"
        bold_font_name="Bold Italic"
        style_map=0x21
        mac_style=0x03 # Bold+Italic
    else
        base_name="Regular"
        bold_font="$dir/${base}-Bold.$extension"
        bold_font_name_minus="Bold"
        bold_font_name="Bold"
        style_map=0x20
        mac_style=0x01 # Bold
    fi

    base="${filename%-${base_name}.*}"
    bold_font="$dir/${base}-${bold_font_name_minus}.$extension"

    # FontForge script to generate bold and italic
    fontforge -lang=ff -c "
        Open(\$1)

        # Get the original monospace width from the space character
        Select(\$2)
        original_width = \$width

        # Select all glyphs and expand stroke for bold effect
        SelectWorthOutputting()
        ExpandStroke(27, \"round\", \"round\")

        # Enforce monospacing by resetting all widths to the original
        foreach
            SetWidth(original_width)
        endloop

        # Update font metadata
        SetOS2Value(\"Weight\", 700)
        SetOS2Value(\"StyleMap\", ${style_map})
        SetFontNames(\"FragmentMono-${bold_font_name_minus}\", \"Fragment Mono\", \"Fragment Mono ${bold_font_name}\" )
        SetMacStyle(${mac_style})

        Generate(\$3)
    " "$regular_font" "space" "$bold_font"
done
