#!/bin/bash

set -e

# Directory to search for font files
font_dir="fonts/"

# Find all files matching the pattern *-Regular.* in the specified directory and its subdirectories
find "$font_dir" -type f -name '*-Regular.*' | while read -r regular_font; do
    # Extract the directory, filename, and extension
    dir=$(dirname "$regular_font")
    filename=$(basename "$regular_font")
    extension="${filename##*.}"
    base="${filename%-Regular.*}"
    
    # Define the output file name
    bold_font="$dir/${base}-Bold.$extension"
    
    # Apply the FontForge command
    fontforge -lang=ff -c ' \
        Open($1); \
        SelectWorthOutputting(); \
        ChangeWeight(26); \
        SetOS2Value("Weight", 700); \
        SetFontNames("FragmentMono-Bold", "Fragment Mono", "Fragment Mono Bold" ); \
        SetMacStyle("Bold"); \
        Generate($2)' \
        "$regular_font" "$bold_font"
done
