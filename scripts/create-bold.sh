#!/bin/bash

set -e

# Directory to search for font files
font_dir="fonts/"

# Find all files matching the pattern *-Regular.* in the specified directory and its subdirectories
find "$font_dir" -type f \( -name 'FragmentMono-Regular.*' -o -name 'FragmentMono-Italic.*' \) | while read -r regular_font; do
    # Extract the directory, filename, and extension
    dir=$(dirname "$regular_font")
    filename=$(basename "$regular_font")
    extension="${filename##*.}"
    
    # Define the output file name
    if [[ "$filename" == *-Italic.* ]]; then
        base_name="Italic"
        bold_font_name_minus="Bold-Italic"
        bold_font_name="Bold Italic"
        style_map=0x21
    else
        base_name="Regular"
        bold_font="$dir/${base}-Bold.$extension"
        bold_font_name_minus="Bold"
        bold_font_name="Bold"
        style_map=0x20
    fi
    
    base="${filename%-${base_name}.*}"
    bold_font="$dir/${base}-${bold_font_name_minus}.$extension"
    
    # Apply the FontForge command
    fontforge -lang=ff -c " \
        Open(\$1); \
        SelectWorthOutputting(); \
        ChangeWeight(27); \
        SetOS2Value(\"Weight\", 700); \
        SetOS2Value(\"StyleMap\", ${style_map}); \
        SetFontNames(\"FragmentMono-${bold_font_name_minus}\", \"Fragment Mono\", \"Fragment Mono ${bold_font_name}\" ); \
        SetMacStyle(\"Bold\"); \
        Generate(\$2)" \
        "$regular_font" "$bold_font"
done
