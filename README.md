# Fragment Mono including Bold

Fragment Mono is a monospaced coding version of Helvetica created by modifying and extending [Nimbus Sans](https://github.com/twardoch/urw-core35-fonts) by URW Design Studio. 
This fork only adds a bold variant using fontforge.

### [Download the latest fonts](https://github.com/weiweihuanghuang/fragment-mono/releases) or use Fragment Mono on [Google Fonts](https://fonts.google.com/specimen/Fragment+Mono)

[![Sample Image](documentation/FragmentMono.png)](documentation/FragmentMonoSpecimenDocumentation.pdf)

[![Sample Image](documentation/FragmentMonoCharSet.png)](documentation/FragmentMonoSpecimenDocumentation.pdf)

## About

Fragment Mono was designed with direction by [Studio Lin](https://studiolin.org/) and comissioned by [Fragment](https://fragment.dev).

Download a specimen [here](documentation/FragmentMonoSpecimenDocumentation.pdf).

- Coding ligatures has been added based on [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono) and [Fira Code](https://github.com/tonsky/FiraCode).
- Character set has been extended to include up to [GF Latin Plus](https://github.com/googlefonts/glyphsets/tree/main/GF_glyphsets/Latin).
- Small caps have been added.
- Cap height has been reduced to 96% for slightly better line-fitting.
- Drawing quality has been cleaned up and improved.
- Spacing has been matched to SF Mono.

### Alternate Stylistic Set Characters
![Alternate Stylistic Set Characters](documentation/alternates.png)

### Coding Ligatures
![Coding Ligatures](documentation/FragmentMonoCoding.png)

### Javascript
![JavaScript sample](documentation/javascript.png)

### Python
![Python sample](documentation/python.png)

### Ruby
![Ruby sample](documentation/ruby.png)

### PHP
![PHP sample](documentation/php.png)

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at https://weiweihuanghuang.github.io/fragment-mono.

## Changelog

**28 June 2024. Version 1.20**

- Added alternate i and l options in `ss03`–`ss06` (for improved legibility, [see specimen](documentation/FragmentMonoSpecimenDocumentation.pdf)).
- Added alternate 1 with serif in `ss07`.
- Added circled numerals and letters.
- Added [box drawing charaters](https://en.wikipedia.org/wiki/Box-drawing_characters).
- Added [Powerline glyphs](https://github.com/powerline/powerline).

**30 September 2022. Version 1.00**

- Modified Nimbus Sans into monospaced.
- Corrected and improved drawings.
- Updated character set to [GF Latin Plus](https://github.com/googlefonts/glyphsets/tree/main/GF_glyphsets/Latin).
- Added small caps.
- Added coding ligatures based on [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono) and [Fira Code](https://github.com/tonsky/FiraCode).
- Added some icons.
- Added more currency glyphs.

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at
https://scripts.sil.org/OFL

## Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the Google Fonts workflow.

[![][Fontbakery]](https://weiweihuanghuang.github.io/fragment-mono/fontbakery/fontbakery-report.html)
[![][Universal]](https://weiweihuanghuang.github.io/fragment-mono/fontbakery/fontbakery-report.html)
[![][GF Profile]](https://weiweihuanghuang.github.io/fragment-mono/fontbakery/fontbakery-report.html)
[![][Shaping]](https://weiweihuanghuang.github.io/fragment-mono/fontbakery/fontbakery-report.html)

[Fontbakery]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fweiweihuanghuang%2Ffragment-mono%2Fgh-pages%2Fbadges%2Foverall.json
[GF Profile]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fweiweihuanghuang%2Ffragment-mono%2Fgh-pages%2Fbadges%2FGoogleFonts.json
[Outline Correctness]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fweiweihuanghuang%2Ffragment-mono%2Fgh-pages%2Fbadges%2FOutlineCorrectnessChecks.json
[Shaping]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fweiweihuanghuang%2Ffragment-mono%2Fgh-pages%2Fbadges%2FShapingChecks.json
[Universal]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fweiweihuanghuang%2Ffragment-mono%2Fgh-pages%2Fbadges%2FUniversal.json
