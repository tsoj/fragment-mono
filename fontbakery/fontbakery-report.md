## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[14] FragmentMono-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1040, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 396, but got 378 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nl_Latn (Dutch)</td>
<td align="left">Shaper didn't attach acutecomb to J</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 958 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni2552	Contours detected: 1	Expected: 2

- Glyph name: uni2553	Contours detected: 1	Expected: 2

- Glyph name: uni2555	Contours detected: 1	Expected: 2

- Glyph name: uni2556	Contours detected: 1	Expected: 2

- Glyph name: uni2558	Contours detected: 1	Expected: 2

- Glyph name: uni2559	Contours detected: 1	Expected: 2

- Glyph name: uni255B	Contours detected: 1	Expected: 2

- Glyph name: uni255C	Contours detected: 1	Expected: 2

- Glyph name: uni255E	Contours detected: 1	Expected: 2

- Glyph name: uni2561	Contours detected: 1	Expected: 2

- Glyph name: ltshade	Contours detected: 36	Expected: 46

- Glyph name: shade	Contours detected: 78	Expected: 85

- Glyph name: dkshade	Contours detected: 37	Expected: 73

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: dkshade	Contours detected: 37	Expected: 73

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: ltshade	Contours detected: 36	Expected: 46

- Glyph name: shade	Contours detected: 78	Expected: 85

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- l.002
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
asciitilde_asciitilde_greater.liga, less_numbersign_hyphen_hyphen.liga and semicolon_semicolon_semicolon.liga</p>
 [code: legacy-long-names]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, math, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, todhri, tai-le, hebrew, syriac, malayalam, tifinagh, old-permic, duployan, coptic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, elbasan, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, elbasan, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2017 DOUBLE LOW LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21B0 UPWARDS ARROW WITH TIP LEFTWARDS: try adding math</li>
<li>U+21B1 UPWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21B2 DOWNWARDS ARROW WITH TIP LEFTWARDS: try adding math</li>
<li>U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21BA ANTICLOCKWISE OPEN CIRCLE ARROW: try adding math</li>
<li>U+21BB CLOCKWISE OPEN CIRCLE ARROW: try adding math</li>
<li>U+21C6 LEFTWARDS ARROW OVER RIGHTWARDS ARROW: try adding math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, symbols, math, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2398 NEXT PAGE: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, symbols, mongolian</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, symbols, mongolian</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, symbols, mongolian</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, symbols, mongolian</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, symbols, mongolian</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, symbols, mongolian</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, symbols, mongolian</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, symbols, mongolian</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, symbols, mongolian</li>
<li>U+2469 CIRCLED NUMBER TEN: try adding one of: yi, symbols, mongolian</li>
<li>U+24B6 CIRCLED LATIN CAPITAL LETTER A: try adding symbols</li>
<li>U+24B7 CIRCLED LATIN CAPITAL LETTER B: try adding symbols</li>
<li>U+24B8 CIRCLED LATIN CAPITAL LETTER C: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+24BA CIRCLED LATIN CAPITAL LETTER E: try adding symbols</li>
<li>U+24BB CIRCLED LATIN CAPITAL LETTER F: try adding symbols</li>
<li>U+24BC CIRCLED LATIN CAPITAL LETTER G: try adding symbols</li>
<li>U+24BD CIRCLED LATIN CAPITAL LETTER H: try adding symbols</li>
<li>U+24BE CIRCLED LATIN CAPITAL LETTER I: try adding symbols</li>
<li>U+24BF CIRCLED LATIN CAPITAL LETTER J: try adding symbols</li>
<li>U+24C0 CIRCLED LATIN CAPITAL LETTER K: try adding symbols</li>
<li>U+24C1 CIRCLED LATIN CAPITAL LETTER L: try adding symbols</li>
<li>U+24C2 CIRCLED LATIN CAPITAL LETTER M: try adding symbols</li>
<li>U+24C3 CIRCLED LATIN CAPITAL LETTER N: try adding symbols</li>
<li>U+24C4 CIRCLED LATIN CAPITAL LETTER O: try adding symbols</li>
<li>U+24C5 CIRCLED LATIN CAPITAL LETTER P: try adding symbols</li>
<li>U+24C6 CIRCLED LATIN CAPITAL LETTER Q: try adding symbols</li>
<li>U+24C7 CIRCLED LATIN CAPITAL LETTER R: try adding symbols</li>
<li>U+24C8 CIRCLED LATIN CAPITAL LETTER S: try adding symbols</li>
<li>U+24C9 CIRCLED LATIN CAPITAL LETTER T: try adding symbols</li>
<li>U+24CA CIRCLED LATIN CAPITAL LETTER U: try adding symbols</li>
<li>U+24CB CIRCLED LATIN CAPITAL LETTER V: try adding symbols</li>
<li>U+24CC CIRCLED LATIN CAPITAL LETTER W: try adding symbols</li>
<li>U+24CD CIRCLED LATIN CAPITAL LETTER X: try adding symbols</li>
<li>U+24CE CIRCLED LATIN CAPITAL LETTER Y: try adding symbols</li>
<li>U+24CF CIRCLED LATIN CAPITAL LETTER Z: try adding symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CE BULLSEYE: try adding symbols</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2717 BALLOT X: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+277F DINGBAT NEGATIVE CIRCLED NUMBER TEN: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, phags-pa, chinese-traditional, yi, japanese, chinese-hongkong</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, phags-pa, chinese-traditional, yi, japanese, chinese-hongkong</li>
<li>U+E000 : not included in any glyphset definition</li>
<li>U+E001 : not included in any glyphset definition</li>
<li>U+E0A0 : not included in any glyphset definition</li>
<li>U+E0A1 : not included in any glyphset definition</li>
<li>U+E0A2 : not included in any glyphset definition</li>
<li>U+E0B0 : not included in any glyphset definition</li>
<li>U+E0B1 : not included in any glyphset definition</li>
<li>U+E0B2 : not included in any glyphset definition</li>
<li>U+E0B3 : not included in any glyphset definition</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+1F150 NEGATIVE CIRCLED LATIN CAPITAL LETTER A: try adding symbols</li>
<li>U+1F151 NEGATIVE CIRCLED LATIN CAPITAL LETTER B: try adding symbols</li>
<li>U+1F152 NEGATIVE CIRCLED LATIN CAPITAL LETTER C: try adding symbols</li>
<li>U+1F153 NEGATIVE CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+1F154 NEGATIVE CIRCLED LATIN CAPITAL LETTER E: try adding symbols</li>
<li>U+1F155 NEGATIVE CIRCLED LATIN CAPITAL LETTER F: try adding symbols</li>
<li>U+1F156 NEGATIVE CIRCLED LATIN CAPITAL LETTER G: try adding symbols</li>
<li>U+1F157 NEGATIVE CIRCLED LATIN CAPITAL LETTER H: try adding symbols</li>
<li>U+1F158 NEGATIVE CIRCLED LATIN CAPITAL LETTER I: try adding symbols</li>
<li>U+1F159 NEGATIVE CIRCLED LATIN CAPITAL LETTER J: try adding symbols</li>
<li>U+1F15A NEGATIVE CIRCLED LATIN CAPITAL LETTER K: try adding symbols</li>
<li>U+1F15B NEGATIVE CIRCLED LATIN CAPITAL LETTER L: try adding symbols</li>
<li>U+1F15C NEGATIVE CIRCLED LATIN CAPITAL LETTER M: try adding symbols</li>
<li>U+1F15D NEGATIVE CIRCLED LATIN CAPITAL LETTER N: try adding symbols</li>
<li>U+1F15E NEGATIVE CIRCLED LATIN CAPITAL LETTER O: try adding symbols</li>
<li>U+1F15F NEGATIVE CIRCLED LATIN CAPITAL LETTER P: try adding symbols</li>
<li>U+1F160 NEGATIVE CIRCLED LATIN CAPITAL LETTER Q: try adding symbols</li>
<li>U+1F161 NEGATIVE CIRCLED LATIN CAPITAL LETTER R: try adding symbols</li>
<li>U+1F162 NEGATIVE CIRCLED LATIN CAPITAL LETTER S: try adding symbols</li>
<li>U+1F163 NEGATIVE CIRCLED LATIN CAPITAL LETTER T: try adding symbols</li>
<li>U+1F164 NEGATIVE CIRCLED LATIN CAPITAL LETTER U: try adding symbols</li>
<li>U+1F165 NEGATIVE CIRCLED LATIN CAPITAL LETTER V: try adding symbols</li>
<li>U+1F166 NEGATIVE CIRCLED LATIN CAPITAL LETTER W: try adding symbols</li>
<li>U+1F167 NEGATIVE CIRCLED LATIN CAPITAL LETTER X: try adding symbols</li>
<li>U+1F168 NEGATIVE CIRCLED LATIN CAPITAL LETTER Y: try adding symbols</li>
<li>U+1F169 NEGATIVE CIRCLED LATIN CAPITAL LETTER Z: try adding symbols</li>
<li>U+1F4C4 PAGE FACING UP: not included in any glyphset definition</li>
<li>U+1F517 LINK SYMBOL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: į̆ į̇ į̈ į̊ į̋ į̒ į̦̀ į̦́ į̦̂ į̦̃ į̦̄ į̦̆ į̦̇ į̦̈ į̦̊ į̦̋ į̦̌ į̦̒ į̧̀ į̧́</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Lugbara (Latn, 2,200,000 speakers), Nzakara (Latn, 50,000 speakers), Fur (Latn, 1,230,163 speakers), Avokaya (Latn, 100,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Gulay (Latn, 250,478 speakers), Dutch (Latn, 31,709,104 speakers), Han (Latn, 6 speakers), Heiltsuk (Latn, 300 speakers), Basaa (Latn, 332,940 speakers), Ma’di (Latn, 584,000 speakers), Kaska (Latn, 125 speakers), Vute (Latn, 21,000 speakers), Bafut (Latn, 158,146 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Koonzime (Latn, 40,000 speakers), Sar (Latn, 500,000 speakers), South Central Banda (Latn, 244,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Yala (Latn, 200,000 speakers), Mango (Latn, 77,000 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Bete-Bendi (Latn, 100,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Kom (Latn, 360,685 speakers), Ejagham (Latn, 120,000 speakers), Cicipu (Latn, 44,000 speakers), Nateni (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Navajo (Latn, 166,319 speakers), Ebira (Latn, 2,200,000 speakers), Ekpeye (Latn, 226,000 speakers), Mundani (Latn, 34,000 speakers), Southern Kisi (Latn, 360,000 speakers), Dan (Latn, 1,099,244 speakers), Teke-Ebo (Latn, 260,000 speakers), Mfumte (Latn, 79,000 speakers), Igbo (Latn, 27,823,640 speakers), Dii (Latn, 71,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* u1F167 (U+1F167): L&lt;&lt;-7.0,315.0&gt;--&lt;-32.0,345.0&gt;&gt; -&gt; L&lt;&lt;-32.0,345.0&gt;--&lt;-39.0,354.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* less_asciitilde_greater.liga: B&lt;&lt;342.0,339.0&gt;-&lt;328.0,331.0&gt;-&lt;312.0,310.0&gt;&gt;/L&lt;&lt;312.0,310.0&gt;--&lt;342.0,339.0&gt;&gt; = 8.667073653095745

* less_asciitilde_greater.liga: L&lt;&lt;119.0,121.0&gt;--&lt;284.0,283.0&gt;&gt;/B&lt;&lt;284.0,283.0&gt;-&lt;255.0,262.0&gt;-&lt;217.0,262.0&gt;&gt; = 8.564642314364727

* less_asciitilde_greater.liga: L&lt;&lt;312.0,310.0&gt;--&lt;342.0,339.0&gt;&gt;/B&lt;&lt;342.0,339.0&gt;-&lt;328.0,331.0&gt;-&lt;312.0,310.0&gt;&gt; = 14.284096771978573

* trademark (U+2122): L&lt;&lt;403.0,332.0&gt;--&lt;348.0,639.0&gt;&gt;/L&lt;&lt;348.0,639.0&gt;--&lt;348.0,332.0&gt;&gt; = 10.15696551936229

* trademark (U+2122): L&lt;&lt;516.0,332.0&gt;--&lt;516.0,639.0&gt;&gt;/L&lt;&lt;516.0,639.0&gt;--&lt;462.0,332.0&gt;&gt; = 9.976036422751434

* uni20A9 (U+20A9): L&lt;&lt;137.0,699.0&gt;--&lt;199.0,93.0&gt;&gt;/L&lt;&lt;199.0,93.0&gt;--&lt;268.0,699.0&gt;&gt; = 12.337420712236526

* uni20A9 (U+20A9): L&lt;&lt;350.0,699.0&gt;--&lt;420.0,93.0&gt;&gt;/L&lt;&lt;420.0,93.0&gt;--&lt;481.0,699.0&gt;&gt; = 12.337157115263608

* uni20A9 (U+20A9): L&lt;&lt;375.0,0.0&gt;--&lt;309.0,579.0&gt;&gt;/L&lt;&lt;309.0,579.0&gt;--&lt;243.0,0.0&gt;&gt; = 13.006111889763387

* uni2116 (U+2116): L&lt;&lt;129.0,699.0&gt;--&lt;250.0,118.0&gt;&gt;/L&lt;&lt;250.0,118.0&gt;--&lt;250.0,699.0&gt;&gt; = 11.764350807103282

* uni2116 (U+2116): L&lt;&lt;220.0,0.0&gt;--&lt;102.0,576.0&gt;&gt;/L&lt;&lt;102.0,576.0&gt;--&lt;102.0,0.0&gt;&gt; = 11.577489206021184
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[14] FragmentMono-Italic.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1040, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 396, but got 378 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nl_Latn (Dutch)</td>
<td align="left">Shaper didn't attach acutecomb to J</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 958 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni2552	Contours detected: 1	Expected: 2

- Glyph name: uni2553	Contours detected: 1	Expected: 2

- Glyph name: uni2555	Contours detected: 1	Expected: 2

- Glyph name: uni2556	Contours detected: 1	Expected: 2

- Glyph name: uni2558	Contours detected: 1	Expected: 2

- Glyph name: uni2559	Contours detected: 1	Expected: 2

- Glyph name: uni255B	Contours detected: 1	Expected: 2

- Glyph name: uni255C	Contours detected: 1	Expected: 2

- Glyph name: uni255E	Contours detected: 1	Expected: 2

- Glyph name: uni2561	Contours detected: 1	Expected: 2

- Glyph name: ltshade	Contours detected: 36	Expected: 46

- Glyph name: shade	Contours detected: 78	Expected: 85

- Glyph name: dkshade	Contours detected: 37	Expected: 73

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: dkshade	Contours detected: 37	Expected: 73

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: ltshade	Contours detected: 36	Expected: 46

- Glyph name: shade	Contours detected: 78	Expected: 85

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- l.002
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
asciitilde_asciitilde_greater.liga, less_numbersign_hyphen_hyphen.liga and semicolon_semicolon_semicolon.liga</p>
 [code: legacy-long-names]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, math, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, todhri, tai-le, hebrew, syriac, malayalam, tifinagh, old-permic, duployan, coptic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, elbasan, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, elbasan, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2017 DOUBLE LOW LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21B0 UPWARDS ARROW WITH TIP LEFTWARDS: try adding math</li>
<li>U+21B1 UPWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21B2 DOWNWARDS ARROW WITH TIP LEFTWARDS: try adding math</li>
<li>U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21BA ANTICLOCKWISE OPEN CIRCLE ARROW: try adding math</li>
<li>U+21BB CLOCKWISE OPEN CIRCLE ARROW: try adding math</li>
<li>U+21C6 LEFTWARDS ARROW OVER RIGHTWARDS ARROW: try adding math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, symbols, math, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2398 NEXT PAGE: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, symbols, mongolian</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, symbols, mongolian</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, symbols, mongolian</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, symbols, mongolian</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, symbols, mongolian</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, symbols, mongolian</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, symbols, mongolian</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, symbols, mongolian</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, symbols, mongolian</li>
<li>U+2469 CIRCLED NUMBER TEN: try adding one of: yi, symbols, mongolian</li>
<li>U+24B6 CIRCLED LATIN CAPITAL LETTER A: try adding symbols</li>
<li>U+24B7 CIRCLED LATIN CAPITAL LETTER B: try adding symbols</li>
<li>U+24B8 CIRCLED LATIN CAPITAL LETTER C: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+24BA CIRCLED LATIN CAPITAL LETTER E: try adding symbols</li>
<li>U+24BB CIRCLED LATIN CAPITAL LETTER F: try adding symbols</li>
<li>U+24BC CIRCLED LATIN CAPITAL LETTER G: try adding symbols</li>
<li>U+24BD CIRCLED LATIN CAPITAL LETTER H: try adding symbols</li>
<li>U+24BE CIRCLED LATIN CAPITAL LETTER I: try adding symbols</li>
<li>U+24BF CIRCLED LATIN CAPITAL LETTER J: try adding symbols</li>
<li>U+24C0 CIRCLED LATIN CAPITAL LETTER K: try adding symbols</li>
<li>U+24C1 CIRCLED LATIN CAPITAL LETTER L: try adding symbols</li>
<li>U+24C2 CIRCLED LATIN CAPITAL LETTER M: try adding symbols</li>
<li>U+24C3 CIRCLED LATIN CAPITAL LETTER N: try adding symbols</li>
<li>U+24C4 CIRCLED LATIN CAPITAL LETTER O: try adding symbols</li>
<li>U+24C5 CIRCLED LATIN CAPITAL LETTER P: try adding symbols</li>
<li>U+24C6 CIRCLED LATIN CAPITAL LETTER Q: try adding symbols</li>
<li>U+24C7 CIRCLED LATIN CAPITAL LETTER R: try adding symbols</li>
<li>U+24C8 CIRCLED LATIN CAPITAL LETTER S: try adding symbols</li>
<li>U+24C9 CIRCLED LATIN CAPITAL LETTER T: try adding symbols</li>
<li>U+24CA CIRCLED LATIN CAPITAL LETTER U: try adding symbols</li>
<li>U+24CB CIRCLED LATIN CAPITAL LETTER V: try adding symbols</li>
<li>U+24CC CIRCLED LATIN CAPITAL LETTER W: try adding symbols</li>
<li>U+24CD CIRCLED LATIN CAPITAL LETTER X: try adding symbols</li>
<li>U+24CE CIRCLED LATIN CAPITAL LETTER Y: try adding symbols</li>
<li>U+24CF CIRCLED LATIN CAPITAL LETTER Z: try adding symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CE BULLSEYE: try adding symbols</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2717 BALLOT X: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+277F DINGBAT NEGATIVE CIRCLED NUMBER TEN: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, phags-pa, chinese-traditional, yi, japanese, chinese-hongkong</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, phags-pa, chinese-traditional, yi, japanese, chinese-hongkong</li>
<li>U+E000 : not included in any glyphset definition</li>
<li>U+E001 : not included in any glyphset definition</li>
<li>U+E0A0 : not included in any glyphset definition</li>
<li>U+E0A1 : not included in any glyphset definition</li>
<li>U+E0A2 : not included in any glyphset definition</li>
<li>U+E0B0 : not included in any glyphset definition</li>
<li>U+E0B1 : not included in any glyphset definition</li>
<li>U+E0B2 : not included in any glyphset definition</li>
<li>U+E0B3 : not included in any glyphset definition</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+1F150 NEGATIVE CIRCLED LATIN CAPITAL LETTER A: try adding symbols</li>
<li>U+1F151 NEGATIVE CIRCLED LATIN CAPITAL LETTER B: try adding symbols</li>
<li>U+1F152 NEGATIVE CIRCLED LATIN CAPITAL LETTER C: try adding symbols</li>
<li>U+1F153 NEGATIVE CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+1F154 NEGATIVE CIRCLED LATIN CAPITAL LETTER E: try adding symbols</li>
<li>U+1F155 NEGATIVE CIRCLED LATIN CAPITAL LETTER F: try adding symbols</li>
<li>U+1F156 NEGATIVE CIRCLED LATIN CAPITAL LETTER G: try adding symbols</li>
<li>U+1F157 NEGATIVE CIRCLED LATIN CAPITAL LETTER H: try adding symbols</li>
<li>U+1F158 NEGATIVE CIRCLED LATIN CAPITAL LETTER I: try adding symbols</li>
<li>U+1F159 NEGATIVE CIRCLED LATIN CAPITAL LETTER J: try adding symbols</li>
<li>U+1F15A NEGATIVE CIRCLED LATIN CAPITAL LETTER K: try adding symbols</li>
<li>U+1F15B NEGATIVE CIRCLED LATIN CAPITAL LETTER L: try adding symbols</li>
<li>U+1F15C NEGATIVE CIRCLED LATIN CAPITAL LETTER M: try adding symbols</li>
<li>U+1F15D NEGATIVE CIRCLED LATIN CAPITAL LETTER N: try adding symbols</li>
<li>U+1F15E NEGATIVE CIRCLED LATIN CAPITAL LETTER O: try adding symbols</li>
<li>U+1F15F NEGATIVE CIRCLED LATIN CAPITAL LETTER P: try adding symbols</li>
<li>U+1F160 NEGATIVE CIRCLED LATIN CAPITAL LETTER Q: try adding symbols</li>
<li>U+1F161 NEGATIVE CIRCLED LATIN CAPITAL LETTER R: try adding symbols</li>
<li>U+1F162 NEGATIVE CIRCLED LATIN CAPITAL LETTER S: try adding symbols</li>
<li>U+1F163 NEGATIVE CIRCLED LATIN CAPITAL LETTER T: try adding symbols</li>
<li>U+1F164 NEGATIVE CIRCLED LATIN CAPITAL LETTER U: try adding symbols</li>
<li>U+1F165 NEGATIVE CIRCLED LATIN CAPITAL LETTER V: try adding symbols</li>
<li>U+1F166 NEGATIVE CIRCLED LATIN CAPITAL LETTER W: try adding symbols</li>
<li>U+1F167 NEGATIVE CIRCLED LATIN CAPITAL LETTER X: try adding symbols</li>
<li>U+1F168 NEGATIVE CIRCLED LATIN CAPITAL LETTER Y: try adding symbols</li>
<li>U+1F169 NEGATIVE CIRCLED LATIN CAPITAL LETTER Z: try adding symbols</li>
<li>U+1F4C4 PAGE FACING UP: not included in any glyphset definition</li>
<li>U+1F517 LINK SYMBOL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: į̆ į̇ į̈ į̊ į̋ į̒ į̦̀ į̦́ į̦̂ į̦̃ į̦̄ į̦̆ į̦̇ į̦̈ į̦̊ į̦̋ į̦̌ į̦̒ į̧̀ į̧́</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Lugbara (Latn, 2,200,000 speakers), Nzakara (Latn, 50,000 speakers), Fur (Latn, 1,230,163 speakers), Avokaya (Latn, 100,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Gulay (Latn, 250,478 speakers), Dutch (Latn, 31,709,104 speakers), Han (Latn, 6 speakers), Heiltsuk (Latn, 300 speakers), Basaa (Latn, 332,940 speakers), Ma’di (Latn, 584,000 speakers), Kaska (Latn, 125 speakers), Vute (Latn, 21,000 speakers), Bafut (Latn, 158,146 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Koonzime (Latn, 40,000 speakers), Sar (Latn, 500,000 speakers), South Central Banda (Latn, 244,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Yala (Latn, 200,000 speakers), Mango (Latn, 77,000 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Bete-Bendi (Latn, 100,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Kom (Latn, 360,685 speakers), Ejagham (Latn, 120,000 speakers), Cicipu (Latn, 44,000 speakers), Nateni (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Navajo (Latn, 166,319 speakers), Ebira (Latn, 2,200,000 speakers), Ekpeye (Latn, 226,000 speakers), Mundani (Latn, 34,000 speakers), Southern Kisi (Latn, 360,000 speakers), Dan (Latn, 1,099,244 speakers), Teke-Ebo (Latn, 260,000 speakers), Mfumte (Latn, 79,000 speakers), Igbo (Latn, 27,823,640 speakers), Dii (Latn, 71,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* bar_equal_greater.liga: L&lt;&lt;-1056.0,431.0&gt;--&lt;-1051.0,454.0&gt;&gt; -&gt; L&lt;&lt;-1051.0,454.0&gt;--&lt;-1011.0,642.0&gt;&gt;

* bar_equal_greater.liga: L&lt;&lt;-1131.0,77.0&gt;--&lt;-1087.0,285.0&gt;&gt; -&gt; L&lt;&lt;-1087.0,285.0&gt;--&lt;-1086.0,289.0&gt;&gt;

* bar_hyphen_greater.liga: L&lt;&lt;-1110.0,77.0&gt;--&lt;-1053.0,345.0&gt;&gt; -&gt; L&lt;&lt;-1053.0,345.0&gt;--&lt;-1042.0,399.0&gt;&gt;

* eng (U+014B): L&lt;&lt;371.0,-37.0&gt;--&lt;379.0,0.0&gt;&gt; -&gt; L&lt;&lt;379.0,0.0&gt;--&lt;456.0,363.0&gt;&gt;

* eng (U+014B): L&lt;&lt;542.0,376.0&gt;--&lt;462.0,0.0&gt;&gt; -&gt; L&lt;&lt;462.0,0.0&gt;--&lt;449.0,-59.0&gt;&gt;

* less_equal_bar.liga: L&lt;&lt;459.0,289.0&gt;--&lt;454.0,266.0&gt;&gt; -&gt; L&lt;&lt;454.0,266.0&gt;--&lt;414.0,78.0&gt;&gt;

* less_equal_bar.liga: L&lt;&lt;534.0,643.0&gt;--&lt;490.0,435.0&gt;&gt; -&gt; L&lt;&lt;490.0,435.0&gt;--&lt;489.0,431.0&gt;&gt;

* less_hyphen_bar.liga: L&lt;&lt;534.0,643.0&gt;--&lt;477.0,375.0&gt;&gt; -&gt; L&lt;&lt;477.0,375.0&gt;--&lt;466.0,321.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* m.sc: L&lt;&lt;432.0,0.0&gt;--&lt;534.0,477.0&gt;&gt;/L&lt;&lt;534.0,477.0&gt;--&lt;299.0,0.0&gt;&gt; = 14.157592127600394

* trademark (U+2122): L&lt;&lt;418.0,332.0&gt;--&lt;428.0,639.0&gt;&gt;/L&lt;&lt;428.0,639.0&gt;--&lt;363.0,332.0&gt;&gt; = 10.08883041066053

* trademark (U+2122): L&lt;&lt;531.0,332.0&gt;--&lt;596.0,639.0&gt;&gt;/L&lt;&lt;596.0,639.0&gt;--&lt;477.0,332.0&gt;&gt; = 9.232951420697566

* u1F15C (U+1F15C): L&lt;&lt;5.0,117.0&gt;--&lt;193.0,499.0&gt;&gt;/L&lt;&lt;193.0,499.0&gt;--&lt;112.0,117.0&gt;&gt; = 14.232165145992498

* u1F15D (U+1F15D): L&lt;&lt;-75.0,509.0&gt;--&lt;-57.0,555.0&gt;&gt;/L&lt;&lt;-57.0,555.0&gt;--&lt;-70.0,496.0&gt;&gt; = 8.944679403915684

* u1F15D (U+1F15D): L&lt;&lt;110.0,191.0&gt;--&lt;98.0,165.0&gt;&gt;/L&lt;&lt;98.0,165.0&gt;--&lt;106.0,202.0&gt;&gt; = 12.574671841451137

* uni20A9 (U+20A9): L&lt;&lt;229.0,699.0&gt;--&lt;162.0,93.0&gt;&gt;/L&lt;&lt;162.0,93.0&gt;--&lt;360.0,699.0&gt;&gt; = 11.784848165590649

* uni20A9 (U+20A9): L&lt;&lt;319.0,0.0&gt;--&lt;375.0,579.0&gt;&gt;/L&lt;&lt;375.0,579.0&gt;--&lt;187.0,0.0&gt;&gt; = 12.464119629827673

* uni20A9 (U+20A9): L&lt;&lt;442.0,699.0&gt;--&lt;382.0,93.0&gt;&gt;/L&lt;&lt;382.0,93.0&gt;--&lt;573.0,699.0&gt;&gt; = 11.83946742345819

* uni2116 (U+2116): L&lt;&lt;164.0,0.0&gt;--&lt;172.0,592.0&gt;&gt;/L&lt;&lt;172.0,592.0&gt;--&lt;45.0,0.0&gt;&gt; = 11.333755455975231

* uni2116 (U+2116): L&lt;&lt;222.0,699.0&gt;--&lt;216.0,102.0&gt;&gt;/L&lt;&lt;216.0,102.0&gt;--&lt;344.0,699.0&gt;&gt; = 11.525493565128695

* uni24C2 (U+24C2): L&lt;&lt;112.0,117.0&gt;--&lt;193.0,499.0&gt;&gt;/L&lt;&lt;193.0,499.0&gt;--&lt;5.0,117.0&gt;&gt; = 14.232165145992472
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[20] FragmentMono-Bold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1040, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 396, but got 378 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs had components with scaling or rotation
or inverted outline direction:</p>
<ul>
<li>i (component dotlessi)</li>
<li>i (component uni0307.i)</li>
<li>j (component uni0237)</li>
<li>j (component uni0307.i)</li>
<li>dcaron (component d)</li>
<li>dcaron (component uni030C.alt)</li>
<li>Dcroat (component Eth)</li>
<li>uni03A9 (component uni2126)</li>
<li>i.ss03 (component dotlessi.ss03)</li>
<li>i.ss03 (component uni0307.i)</li>
<li>i.ss05 (component dotlessi.ss05)</li>
<li>i.ss05 (component uni0307.i)</li>
<li>dcroat.sc (component eth.sc)</li>
</ul>
 [code: transformed-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Are there unwanted tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.tables.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following unwanted font tables were found:</p>
<ul>
<li>FFTM - Table contains redundant FontForge timestamp info</li>
</ul>
<p>They can be removed with the 'fix-unwanted-tables' script provided by gftools.</p>
 [code: unwanted-tables]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nl_Latn (Dutch)</td>
<td align="left">Shaper didn't attach acutecomb to J</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 982 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 1 glyphs (0.10%) have a different width. You should check the widths of: ['nonmarkingreturn']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: threequarters	Contours detected: 5	Expected: 3 or 4

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: perthousand	Contours detected: 5	Expected: 6 or 7

- Glyph name: uni2153	Contours detected: 4	Expected: 3

- Glyph name: threeeighths	Contours detected: 6	Expected: 5

- Glyph name: uni2552	Contours detected: 1	Expected: 2

- Glyph name: uni2553	Contours detected: 1	Expected: 2

- Glyph name: uni2555	Contours detected: 1	Expected: 2

- Glyph name: uni2556	Contours detected: 1	Expected: 2

- Glyph name: uni2558	Contours detected: 1	Expected: 2

- Glyph name: uni2559	Contours detected: 1	Expected: 2

- Glyph name: uni255B	Contours detected: 1	Expected: 2

- Glyph name: uni255C	Contours detected: 1	Expected: 2

- Glyph name: uni255E	Contours detected: 1	Expected: 2

- Glyph name: uni2561	Contours detected: 1	Expected: 2

- Glyph name: ltshade	Contours detected: 36	Expected: 46

- Glyph name: shade	Contours detected: 78	Expected: 85

- Glyph name: dkshade	Contours detected: 37	Expected: 73

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: dkshade	Contours detected: 37	Expected: 73

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: ltshade	Contours detected: 36	Expected: 46

- Glyph name: perthousand	Contours detected: 5	Expected: 6 or 7

- Glyph name: shade	Contours detected: 78	Expected: 85

- Glyph name: threeeighths	Contours detected: 6	Expected: 5

- Glyph name: threequarters	Contours detected: 5	Expected: 3 or 4

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- l.002

- nonmarkingreturn
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
asciitilde_asciitilde_greater.liga, less_numbersign_hyphen_hyphen.liga and semicolon_semicolon_semicolon.liga</p>
 [code: legacy-long-names]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, math, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, todhri, tai-le, hebrew, syriac, malayalam, tifinagh, old-permic, duployan, coptic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, elbasan, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, elbasan, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2017 DOUBLE LOW LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21B0 UPWARDS ARROW WITH TIP LEFTWARDS: try adding math</li>
<li>U+21B1 UPWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21B2 DOWNWARDS ARROW WITH TIP LEFTWARDS: try adding math</li>
<li>U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21BA ANTICLOCKWISE OPEN CIRCLE ARROW: try adding math</li>
<li>U+21BB CLOCKWISE OPEN CIRCLE ARROW: try adding math</li>
<li>U+21C6 LEFTWARDS ARROW OVER RIGHTWARDS ARROW: try adding math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, symbols, math, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2398 NEXT PAGE: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, symbols, mongolian</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, symbols, mongolian</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, symbols, mongolian</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, symbols, mongolian</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, symbols, mongolian</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, symbols, mongolian</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, symbols, mongolian</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, symbols, mongolian</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, symbols, mongolian</li>
<li>U+2469 CIRCLED NUMBER TEN: try adding one of: yi, symbols, mongolian</li>
<li>U+24B6 CIRCLED LATIN CAPITAL LETTER A: try adding symbols</li>
<li>U+24B7 CIRCLED LATIN CAPITAL LETTER B: try adding symbols</li>
<li>U+24B8 CIRCLED LATIN CAPITAL LETTER C: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+24BA CIRCLED LATIN CAPITAL LETTER E: try adding symbols</li>
<li>U+24BB CIRCLED LATIN CAPITAL LETTER F: try adding symbols</li>
<li>U+24BC CIRCLED LATIN CAPITAL LETTER G: try adding symbols</li>
<li>U+24BD CIRCLED LATIN CAPITAL LETTER H: try adding symbols</li>
<li>U+24BE CIRCLED LATIN CAPITAL LETTER I: try adding symbols</li>
<li>U+24BF CIRCLED LATIN CAPITAL LETTER J: try adding symbols</li>
<li>U+24C0 CIRCLED LATIN CAPITAL LETTER K: try adding symbols</li>
<li>U+24C1 CIRCLED LATIN CAPITAL LETTER L: try adding symbols</li>
<li>U+24C2 CIRCLED LATIN CAPITAL LETTER M: try adding symbols</li>
<li>U+24C3 CIRCLED LATIN CAPITAL LETTER N: try adding symbols</li>
<li>U+24C4 CIRCLED LATIN CAPITAL LETTER O: try adding symbols</li>
<li>U+24C5 CIRCLED LATIN CAPITAL LETTER P: try adding symbols</li>
<li>U+24C6 CIRCLED LATIN CAPITAL LETTER Q: try adding symbols</li>
<li>U+24C7 CIRCLED LATIN CAPITAL LETTER R: try adding symbols</li>
<li>U+24C8 CIRCLED LATIN CAPITAL LETTER S: try adding symbols</li>
<li>U+24C9 CIRCLED LATIN CAPITAL LETTER T: try adding symbols</li>
<li>U+24CA CIRCLED LATIN CAPITAL LETTER U: try adding symbols</li>
<li>U+24CB CIRCLED LATIN CAPITAL LETTER V: try adding symbols</li>
<li>U+24CC CIRCLED LATIN CAPITAL LETTER W: try adding symbols</li>
<li>U+24CD CIRCLED LATIN CAPITAL LETTER X: try adding symbols</li>
<li>U+24CE CIRCLED LATIN CAPITAL LETTER Y: try adding symbols</li>
<li>U+24CF CIRCLED LATIN CAPITAL LETTER Z: try adding symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CE BULLSEYE: try adding symbols</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2717 BALLOT X: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+277F DINGBAT NEGATIVE CIRCLED NUMBER TEN: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, phags-pa, chinese-traditional, yi, japanese, chinese-hongkong</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, phags-pa, chinese-traditional, yi, japanese, chinese-hongkong</li>
<li>U+E000 : not included in any glyphset definition</li>
<li>U+E001 : not included in any glyphset definition</li>
<li>U+E0A0 : not included in any glyphset definition</li>
<li>U+E0A1 : not included in any glyphset definition</li>
<li>U+E0A2 : not included in any glyphset definition</li>
<li>U+E0B0 : not included in any glyphset definition</li>
<li>U+E0B1 : not included in any glyphset definition</li>
<li>U+E0B2 : not included in any glyphset definition</li>
<li>U+E0B3 : not included in any glyphset definition</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+1F150 NEGATIVE CIRCLED LATIN CAPITAL LETTER A: try adding symbols</li>
<li>U+1F151 NEGATIVE CIRCLED LATIN CAPITAL LETTER B: try adding symbols</li>
<li>U+1F152 NEGATIVE CIRCLED LATIN CAPITAL LETTER C: try adding symbols</li>
<li>U+1F153 NEGATIVE CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+1F154 NEGATIVE CIRCLED LATIN CAPITAL LETTER E: try adding symbols</li>
<li>U+1F155 NEGATIVE CIRCLED LATIN CAPITAL LETTER F: try adding symbols</li>
<li>U+1F156 NEGATIVE CIRCLED LATIN CAPITAL LETTER G: try adding symbols</li>
<li>U+1F157 NEGATIVE CIRCLED LATIN CAPITAL LETTER H: try adding symbols</li>
<li>U+1F158 NEGATIVE CIRCLED LATIN CAPITAL LETTER I: try adding symbols</li>
<li>U+1F159 NEGATIVE CIRCLED LATIN CAPITAL LETTER J: try adding symbols</li>
<li>U+1F15A NEGATIVE CIRCLED LATIN CAPITAL LETTER K: try adding symbols</li>
<li>U+1F15B NEGATIVE CIRCLED LATIN CAPITAL LETTER L: try adding symbols</li>
<li>U+1F15C NEGATIVE CIRCLED LATIN CAPITAL LETTER M: try adding symbols</li>
<li>U+1F15D NEGATIVE CIRCLED LATIN CAPITAL LETTER N: try adding symbols</li>
<li>U+1F15E NEGATIVE CIRCLED LATIN CAPITAL LETTER O: try adding symbols</li>
<li>U+1F15F NEGATIVE CIRCLED LATIN CAPITAL LETTER P: try adding symbols</li>
<li>U+1F160 NEGATIVE CIRCLED LATIN CAPITAL LETTER Q: try adding symbols</li>
<li>U+1F161 NEGATIVE CIRCLED LATIN CAPITAL LETTER R: try adding symbols</li>
<li>U+1F162 NEGATIVE CIRCLED LATIN CAPITAL LETTER S: try adding symbols</li>
<li>U+1F163 NEGATIVE CIRCLED LATIN CAPITAL LETTER T: try adding symbols</li>
<li>U+1F164 NEGATIVE CIRCLED LATIN CAPITAL LETTER U: try adding symbols</li>
<li>U+1F165 NEGATIVE CIRCLED LATIN CAPITAL LETTER V: try adding symbols</li>
<li>U+1F166 NEGATIVE CIRCLED LATIN CAPITAL LETTER W: try adding symbols</li>
<li>U+1F167 NEGATIVE CIRCLED LATIN CAPITAL LETTER X: try adding symbols</li>
<li>U+1F168 NEGATIVE CIRCLED LATIN CAPITAL LETTER Y: try adding symbols</li>
<li>U+1F169 NEGATIVE CIRCLED LATIN CAPITAL LETTER Z: try adding symbols</li>
<li>U+1F4C4 PAGE FACING UP: not included in any glyphset definition</li>
<li>U+1F517 LINK SYMBOL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: į̆ į̇ į̈ į̊ į̋ į̒ į̦̀ į̦́ į̦̂ į̦̃ į̦̄ į̦̆ į̦̇ į̦̈ į̦̊ į̦̋ į̦̌ į̦̒ į̧̀ į̧́</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Lugbara (Latn, 2,200,000 speakers), Nzakara (Latn, 50,000 speakers), Fur (Latn, 1,230,163 speakers), Avokaya (Latn, 100,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Gulay (Latn, 250,478 speakers), Dutch (Latn, 31,709,104 speakers), Han (Latn, 6 speakers), Heiltsuk (Latn, 300 speakers), Basaa (Latn, 332,940 speakers), Ma’di (Latn, 584,000 speakers), Kaska (Latn, 125 speakers), Vute (Latn, 21,000 speakers), Bafut (Latn, 158,146 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Koonzime (Latn, 40,000 speakers), Sar (Latn, 500,000 speakers), South Central Banda (Latn, 244,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Yala (Latn, 200,000 speakers), Mango (Latn, 77,000 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Bete-Bendi (Latn, 100,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Kom (Latn, 360,685 speakers), Ejagham (Latn, 120,000 speakers), Cicipu (Latn, 44,000 speakers), Nateni (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Navajo (Latn, 166,319 speakers), Ebira (Latn, 2,200,000 speakers), Ekpeye (Latn, 226,000 speakers), Mundani (Latn, 34,000 speakers), Southern Kisi (Latn, 360,000 speakers), Dan (Latn, 1,099,244 speakers), Teke-Ebo (Latn, 260,000 speakers), Mfumte (Latn, 79,000 speakers), Igbo (Latn, 27,823,640 speakers), Dii (Latn, 71,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* a (U+0061): X=450.5,Y=0.5 (should be at baseline 0?)

* h (U+0068): X=443.5,Y=522.5 (should be at x-height 524?)

* t (U+0074): X=529.0,Y=2.0 (should be at baseline 0?)

* t (U+0074): X=518.0,Y=-1.0 (should be at baseline 0?)

* onehalf (U+00BD): X=329.0,Y=1.0 (should be at baseline 0?)

* threequarters (U+00BE): X=226.5,Y=697.5 (should be at cap-height 699?)

* agrave (U+00E0): X=450.5,Y=0.5 (should be at baseline 0?)

* aacute (U+00E1): X=450.5,Y=0.5 (should be at baseline 0?)

* acircumflex (U+00E2): X=450.5,Y=0.5 (should be at baseline 0?)

* atilde (U+00E3): X=450.5,Y=0.5 (should be at baseline 0?)

* adieresis (U+00E4): X=450.5,Y=0.5 (should be at baseline 0?)

* aring (U+00E5): X=450.5,Y=0.5 (should be at baseline 0?)

* amacron (U+0101): X=450.5,Y=0.5 (should be at baseline 0?)

* abreve (U+0103): X=450.5,Y=0.5 (should be at baseline 0?)

* aogonek (U+0105): X=450.5,Y=0.5 (should be at baseline 0?)

* tcaron (U+0165): X=529.0,Y=2.0 (should be at baseline 0?)

* tcaron (U+0165): X=518.0,Y=-1.0 (should be at baseline 0?)

* uni01CE (U+01CE): X=450.5,Y=0.5 (should be at baseline 0?)

* uni021B (U+021B): X=529.0,Y=2.0 (should be at baseline 0?)

* uni021B (U+021B): X=518.0,Y=-1.0 (should be at baseline 0?)

* uni1E9E (U+1E9E): X=254.0,Y=-1.0 (should be at baseline 0?)

* uni1E9E (U+1E9E): X=240.0,Y=2.0 (should be at baseline 0?)

* uni2085 (U+2085): X=200.0,Y=-1.0 (should be at baseline 0?)

* uni2085 (U+2085): X=200.0,Y=-1.0 (should be at baseline 0?)

* uni20BE (U+20BE): X=198.0,Y=698.0 (should be at cap-height 699?)

* uni250A (U+250A): X=256.0,Y=2.0 (should be at baseline 0?)

* uni250A (U+250A): X=362.0,Y=2.0 (should be at baseline 0?)

* uni250B (U+250B): X=238.0,Y=2.0 (should be at baseline 0?)

* uni250B (U+250B): X=380.0,Y=2.0 (should be at baseline 0?)

* uni25B6 (U+25B6): X=17.0,Y=-2.0 (should be at baseline 0?)

* uni25B6 (U+25B6): X=16.0,Y=700.0 (should be at cap-height 699?)

* uni25B7 (U+25B7): X=17.0,Y=-2.0 (should be at baseline 0?)

* uni25B7 (U+25B7): X=16.0,Y=700.0 (should be at cap-height 699?)

* uni25C0 (U+25C0): X=603.0,Y=700.0 (should be at cap-height 699?)

* uni25C0 (U+25C0): X=603.0,Y=-2.0 (should be at baseline 0?)

* uni25C1 (U+25C1): X=603.0,Y=700.0 (should be at cap-height 699?)

* uni25C1 (U+25C1): X=603.0,Y=-2.0 (should be at baseline 0?)

* i.ss03: X=498.53118896484375,Y=1.0 (should be at baseline 0?)

* dotlessi.ss03: X=555.0,Y=1.0 (should be at baseline 0?)

* iacute.ss03: X=555.0,Y=1.0 (should be at baseline 0?)

* icircumflex.ss03: X=555.0,Y=1.0 (should be at baseline 0?)

* idieresis.ss03: X=555.0,Y=1.0 (should be at baseline 0?)

* i.loclTRK.ss03: X=555.0,Y=1.0 (should be at baseline 0?)

* igrave.ss03: X=555.0,Y=1.0 (should be at baseline 0?)

* imacron.ss03: X=555.0,Y=1.0 (should be at baseline 0?)

* iogonek.ss03: X=555.0,Y=1.0 (should be at baseline 0?)

* l.ss04: X=545.0,Y=1.0 (should be at baseline 0?)

* lacute.ss04: X=545.0,Y=1.0 (should be at baseline 0?)

* lcaron.ss04: X=545.0,Y=1.0 (should be at baseline 0?)

* uni013C.ss04: X=545.0,Y=1.0 (should be at baseline 0?)

* lslash.ss04: X=545.0,Y=1.0 (should be at baseline 0?)

* aring.sc: X=351.0,Y=697.0 (should be at cap-height 699?)

* aring.sc: X=351.0,Y=697.0 (should be at cap-height 699?)

* germandbls.sc: X=260.0,Y=-1.0 (should be at baseline 0?)

* germandbls.sc: X=245.0,Y=2.0 (should be at baseline 0?)

* uring.sc: X=344.0,Y=697.0 (should be at cap-height 699?)

* uring.sc: X=344.0,Y=697.0 (should be at cap-height 699?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* Ccedilla (U+00C7): L&lt;&lt;360.0,30.0&gt;--&lt;371.0,29.0&gt;&gt; -&gt; L&lt;&lt;371.0,29.0&gt;--&lt;413.0,29.0&gt;&gt;

* Ccedilla (U+00C7): L&lt;&lt;371.0,29.0&gt;--&lt;413.0,29.0&gt;&gt; -&gt; L&lt;&lt;413.0,29.0&gt;--&lt;441.0,29.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;351.0,30.0&gt;--&lt;362.0,29.0&gt;&gt; -&gt; L&lt;&lt;362.0,29.0&gt;--&lt;404.0,29.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;362.0,29.0&gt;--&lt;404.0,29.0&gt;&gt; -&gt; L&lt;&lt;404.0,29.0&gt;--&lt;432.0,29.0&gt;&gt;

* ccedilla (U+00E7): L&lt;&lt;348.0,30.0&gt;--&lt;359.0,29.0&gt;&gt; -&gt; L&lt;&lt;359.0,29.0&gt;--&lt;401.0,29.0&gt;&gt;

* ccedilla (U+00E7): L&lt;&lt;359.0,29.0&gt;--&lt;401.0,29.0&gt;&gt; -&gt; L&lt;&lt;401.0,29.0&gt;--&lt;429.0,29.0&gt;&gt;

* ccedilla.sc: L&lt;&lt;336.0,30.0&gt;--&lt;347.0,29.0&gt;&gt; -&gt; L&lt;&lt;347.0,29.0&gt;--&lt;389.0,29.0&gt;&gt;

* ccedilla.sc: L&lt;&lt;347.0,29.0&gt;--&lt;389.0,29.0&gt;&gt; -&gt; L&lt;&lt;389.0,29.0&gt;--&lt;417.0,29.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;317.0,30.0&gt;--&lt;328.0,29.0&gt;&gt; -&gt; L&lt;&lt;328.0,29.0&gt;--&lt;370.0,29.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;328.0,29.0&gt;--&lt;370.0,29.0&gt;&gt; -&gt; L&lt;&lt;370.0,29.0&gt;--&lt;398.0,29.0&gt;&gt;

* equal_exclam_equal.liga: L&lt;&lt;-274.0,181.0&gt;--&lt;-289.0,181.0&gt;&gt; -&gt; L&lt;&lt;-289.0,181.0&gt;--&lt;-329.0,181.0&gt;&gt;

* equal_exclam_equal.liga: L&lt;&lt;-289.0,181.0&gt;--&lt;-329.0,181.0&gt;&gt; -&gt; L&lt;&lt;-329.0,181.0&gt;--&lt;-344.0,181.0&gt;&gt;

* estimated (U+212E): L&lt;&lt;562.0,282.0&gt;--&lt;564.0,251.0&gt;&gt; -&gt; L&lt;&lt;564.0,251.0&gt;--&lt;564.0,226.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;329.0,181.0&gt;--&lt;289.0,181.0&gt;&gt; -&gt; L&lt;&lt;289.0,181.0&gt;--&lt;274.0,181.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;344.0,181.0&gt;--&lt;329.0,181.0&gt;&gt; -&gt; L&lt;&lt;329.0,181.0&gt;--&lt;289.0,181.0&gt;&gt;

* exclam_exclam.liga: L&lt;&lt;-194.0,181.0&gt;--&lt;-209.0,181.0&gt;&gt; -&gt; L&lt;&lt;-209.0,181.0&gt;--&lt;-249.0,181.0&gt;&gt;

* exclam_exclam.liga: L&lt;&lt;-209.0,181.0&gt;--&lt;-249.0,181.0&gt;&gt; -&gt; L&lt;&lt;-249.0,181.0&gt;--&lt;-264.0,181.0&gt;&gt;

* exclam_exclam.liga: L&lt;&lt;249.0,181.0&gt;--&lt;209.0,181.0&gt;&gt; -&gt; L&lt;&lt;209.0,181.0&gt;--&lt;194.0,181.0&gt;&gt;

* exclam_exclam.liga: L&lt;&lt;264.0,181.0&gt;--&lt;249.0,181.0&gt;&gt; -&gt; L&lt;&lt;249.0,181.0&gt;--&lt;209.0,181.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;200.0,181.0&gt;--&lt;160.0,181.0&gt;&gt; -&gt; L&lt;&lt;160.0,181.0&gt;--&lt;145.0,181.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;215.0,181.0&gt;--&lt;200.0,181.0&gt;&gt; -&gt; L&lt;&lt;200.0,181.0&gt;--&lt;160.0,181.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;458.0,181.0&gt;--&lt;418.0,181.0&gt;&gt; -&gt; L&lt;&lt;418.0,181.0&gt;--&lt;403.0,181.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;473.0,181.0&gt;--&lt;458.0,181.0&gt;&gt; -&gt; L&lt;&lt;458.0,181.0&gt;--&lt;418.0,181.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;274.0,343.0&gt;--&lt;329.0,343.0&gt;&gt; -&gt; L&lt;&lt;329.0,343.0&gt;--&lt;344.0,343.0&gt;&gt;

* less_exclam_hyphen_hyphen.liga: L&lt;&lt;-796.0,180.0&gt;--&lt;-811.0,180.0&gt;&gt; -&gt; L&lt;&lt;-811.0,180.0&gt;--&lt;-851.0,180.0&gt;&gt;

* less_exclam_hyphen_hyphen.liga: L&lt;&lt;-811.0,180.0&gt;--&lt;-851.0,180.0&gt;&gt; -&gt; L&lt;&lt;-851.0,180.0&gt;--&lt;-866.0,180.0&gt;&gt;

* scedilla (U+015F): L&lt;&lt;340.0,30.0&gt;--&lt;351.0,29.0&gt;&gt; -&gt; L&lt;&lt;351.0,29.0&gt;--&lt;393.0,29.0&gt;&gt;

* scedilla (U+015F): L&lt;&lt;351.0,29.0&gt;--&lt;393.0,29.0&gt;&gt; -&gt; L&lt;&lt;393.0,29.0&gt;--&lt;421.0,29.0&gt;&gt;

* scedilla.sc: L&lt;&lt;337.0,30.0&gt;--&lt;348.0,29.0&gt;&gt; -&gt; L&lt;&lt;348.0,29.0&gt;--&lt;390.0,29.0&gt;&gt;

* scedilla.sc: L&lt;&lt;348.0,29.0&gt;--&lt;390.0,29.0&gt;&gt; -&gt; L&lt;&lt;390.0,29.0&gt;--&lt;418.0,29.0&gt;&gt;

* u1F150 (U+1F150): L&lt;&lt;-96.0,321.0&gt;--&lt;-83.0,320.0&gt;&gt; -&gt; L&lt;&lt;-83.0,320.0&gt;--&lt;-80.0,320.0&gt;&gt;

* uni0327 (U+0327): L&lt;&lt;317.0,30.0&gt;--&lt;328.0,29.0&gt;&gt; -&gt; L&lt;&lt;328.0,29.0&gt;--&lt;370.0,29.0&gt;&gt;

* uni0327 (U+0327): L&lt;&lt;328.0,29.0&gt;--&lt;370.0,29.0&gt;&gt; -&gt; L&lt;&lt;370.0,29.0&gt;--&lt;398.0,29.0&gt;&gt;

* uni252D (U+252D): L&lt;&lt;363.0,376.0&gt;--&lt;655.0,376.0&gt;&gt; -&gt; L&lt;&lt;655.0,376.0&gt;--&lt;673.0,376.0&gt;&gt;

* uni2531 (U+2531): L&lt;&lt;381.0,376.0&gt;--&lt;655.0,376.0&gt;&gt; -&gt; L&lt;&lt;655.0,376.0&gt;--&lt;673.0,376.0&gt;&gt;

* uni2536 (U+2536): L&lt;&lt;257.0,268.0&gt;--&lt;-35.0,268.0&gt;&gt; -&gt; L&lt;&lt;-35.0,268.0&gt;--&lt;-53.0,268.0&gt;&gt;

* uni253A (U+253A): L&lt;&lt;239.0,268.0&gt;--&lt;-35.0,268.0&gt;&gt; -&gt; L&lt;&lt;-35.0,268.0&gt;--&lt;-53.0,268.0&gt;&gt;

* uni2544 (U+2544): L&lt;&lt;239.0,268.0&gt;--&lt;-35.0,268.0&gt;&gt; -&gt; L&lt;&lt;-35.0,268.0&gt;--&lt;-53.0,268.0&gt;&gt;

* uni2545 (U+2545): L&lt;&lt;381.0,376.0&gt;--&lt;655.0,376.0&gt;&gt; -&gt; L&lt;&lt;655.0,376.0&gt;--&lt;673.0,376.0&gt;&gt;

* uni2571 (U+2571): L&lt;&lt;54.0,-124.0&gt;--&lt;45.0,-124.0&gt;&gt; -&gt; L&lt;&lt;45.0,-124.0&gt;--&lt;-17.0,-124.0&gt;&gt;

* uni2571 (U+2571): L&lt;&lt;566.0,769.0&gt;--&lt;575.0,769.0&gt;&gt; -&gt; L&lt;&lt;575.0,769.0&gt;--&lt;637.0,769.0&gt;&gt;

* uni2573 (U+2573): L&lt;&lt;-17.0,770.0&gt;--&lt;45.0,770.0&gt;&gt; -&gt; L&lt;&lt;45.0,770.0&gt;--&lt;54.0,770.0&gt;&gt;

* uni257C (U+257C): L&lt;&lt;257.0,268.0&gt;--&lt;-35.0,268.0&gt;&gt; -&gt; L&lt;&lt;-35.0,268.0&gt;--&lt;-53.0,268.0&gt;&gt;

* uni257E (U+257E): L&lt;&lt;363.0,376.0&gt;--&lt;655.0,376.0&gt;&gt; -&gt; L&lt;&lt;655.0,376.0&gt;--&lt;673.0,376.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* perthousand (U+2030): B&lt;&lt;88.0,128.0&gt;-&lt;88.0,195.0&gt;-&lt;126.0,240.0&gt;&gt;/L&lt;&lt;126.0,240.0&gt;--&lt;17.0,148.0&gt;&gt; = 9.655172384355907

* perthousand (U+2030): L&lt;&lt;596.0,637.0&gt;--&lt;164.0,272.0&gt;&gt;/B&lt;&lt;164.0,272.0&gt;-&lt;192.0,288.0&gt;-&lt;227.0,288.0&gt;&gt; = 10.449833321544796

* trademark (U+2122): L&lt;&lt;388.0,314.0&gt;--&lt;366.0,442.0&gt;&gt;/L&lt;&lt;366.0,442.0&gt;--&lt;366.0,314.0&gt;&gt; = 9.752424941653802

* trademark (U+2122): L&lt;&lt;498.0,314.0&gt;--&lt;498.0,438.0&gt;&gt;/L&lt;&lt;498.0,438.0&gt;--&lt;477.0,314.0&gt;&gt; = 9.612114754365898

* uni20A9 (U+20A9): L&lt;&lt;154.0,716.0&gt;--&lt;201.0,256.0&gt;&gt;/L&lt;&lt;201.0,256.0&gt;--&lt;253.0,717.0&gt;&gt; = 12.269551115701516

* uni20A9 (U+20A9): L&lt;&lt;360.0,-17.0&gt;--&lt;310.0,424.0&gt;&gt;/L&lt;&lt;310.0,424.0&gt;--&lt;260.0,-18.0&gt;&gt; = 12.922484171955949

* uni20A9 (U+20A9): L&lt;&lt;367.0,717.0&gt;--&lt;420.0,256.0&gt;&gt;/L&lt;&lt;420.0,256.0&gt;--&lt;466.0,716.0&gt;&gt; = 12.268949576837326

* uni2116 (U+2116): L&lt;&lt;143.0,716.0&gt;--&lt;232.0,288.0&gt;&gt;/L&lt;&lt;232.0,288.0&gt;--&lt;232.0,716.0&gt;&gt; = 11.746903926197168

* uni2116 (U+2116): L&lt;&lt;206.0,-18.0&gt;--&lt;120.0,403.0&gt;&gt;/L&lt;&lt;120.0,403.0&gt;--&lt;120.0,-18.0&gt;&gt; = 11.545285790012409
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* asciicircum (U+005E): L&lt;&lt;174.0,302.0&gt;--&lt;46.0,301.0&gt;&gt;

* fiveeighths (U+215D): L&lt;&lt;517.0,717.0&gt;--&lt;636.0,716.0&gt;&gt;

* fraction (U+2044): L&lt;&lt;517.0,717.0&gt;--&lt;636.0,716.0&gt;&gt;

* greater_equal.liga: L&lt;&lt;-345.0,615.0&gt;--&lt;-344.0,732.0&gt;&gt;

* greater_equal.liga: L&lt;&lt;348.0,295.0&gt;--&lt;347.0,178.0&gt;&gt;

* greaterequal (U+2265): L&lt;&lt;48.0,130.0&gt;--&lt;47.0,247.0&gt;&gt;

* guillemotleft (U+00AB): L&lt;&lt;564.0,179.0&gt;--&lt;563.0,38.0&gt;&gt;

* guillemotright (U+00BB): L&lt;&lt;316.0,38.0&gt;--&lt;315.0,176.0&gt;&gt;

* guillemotright (U+00BB): L&lt;&lt;316.0,395.0&gt;--&lt;315.0,536.0&gt;&gt;

* guilsinglleft (U+2039): L&lt;&lt;464.0,175.0&gt;--&lt;463.0,43.0&gt;&gt;

* guilsinglright (U+203A): L&lt;&lt;154.0,43.0&gt;--&lt;155.0,173.0&gt;&gt;

* less_bar_greater.liga: L&lt;&lt;-183.0,-51.0&gt;--&lt;-184.0,74.0&gt;&gt;

* less_bar_greater.liga: L&lt;&lt;-183.0,626.0&gt;--&lt;-184.0,750.0&gt;&gt;

* less_bar_greater.liga: L&lt;&lt;-431.0,73.0&gt;--&lt;-432.0,-51.0&gt;&gt;

* less_bar_greater.liga: L&lt;&lt;-431.0,750.0&gt;--&lt;-432.0,625.0&gt;&gt;

* less_equal.liga: L&lt;&lt;-345.0,385.0&gt;--&lt;-344.0,520.0&gt;&gt;

* less_equal.liga: L&lt;&lt;347.0,290.0&gt;--&lt;348.0,173.0&gt;&gt;

* oneeighth (U+215B): L&lt;&lt;517.0,717.0&gt;--&lt;636.0,716.0&gt;&gt;

* onehalf (U+00BD): L&lt;&lt;517.0,717.0&gt;--&lt;636.0,716.0&gt;&gt;

* onequarter (U+00BC): L&lt;&lt;517.0,717.0&gt;--&lt;636.0,716.0&gt;&gt;

* seveneighths (U+215E): L&lt;&lt;517.0,717.0&gt;--&lt;636.0,716.0&gt;&gt;

* slash_equal.liga: L&lt;&lt;-184.0,812.0&gt;--&lt;-61.0,811.0&gt;&gt;

* threeeighths (U+215C): L&lt;&lt;517.0,717.0&gt;--&lt;636.0,716.0&gt;&gt;

* threequarters (U+00BE): L&lt;&lt;517.0,717.0&gt;--&lt;636.0,716.0&gt;&gt;

* triagdn (U+25BC): L&lt;&lt;-41.0,642.0&gt;--&lt;661.0,643.0&gt;&gt;

* u1F169 (U+1F169): L&lt;&lt;-145.0,540.0&gt;--&lt;133.0,541.0&gt;&gt;

* uni20A6 (U+20A6): L&lt;&lt;519.0,-18.0&gt;--&lt;390.0,-17.0&gt;&gt;

* uni20A6 (U+20A6): L&lt;&lt;83.0,716.0&gt;--&lt;212.0,717.0&gt;&gt;

* uni20B3 (U+20B3): L&lt;&lt;603.0,-18.0&gt;--&lt;482.0,-17.0&gt;&gt;

* uni20B9 (U+20B9): L&lt;&lt;588.0,-18.0&gt;--&lt;418.0,-17.0&gt;&gt;

* uni2153 (U+2153): L&lt;&lt;517.0,717.0&gt;--&lt;636.0,716.0&gt;&gt;

* uni2154 (U+2154): L&lt;&lt;517.0,717.0&gt;--&lt;636.0,716.0&gt;&gt;

* uni24CD (U+24CD): L&lt;&lt;106.0,600.0&gt;--&lt;229.0,601.0&gt;&gt;

* uni24CE (U+24CE): L&lt;&lt;121.0,600.0&gt;--&lt;237.0,601.0&gt;&gt;

* uni25B6 (U+25B6): L&lt;&lt;17.0,-2.0&gt;--&lt;16.0,700.0&gt;&gt;

* uni25B7 (U+25B7): L&lt;&lt;17.0,-2.0&gt;--&lt;16.0,700.0&gt;&gt;

* uni25BD (U+25BD): L&lt;&lt;-41.0,642.0&gt;--&lt;661.0,643.0&gt;&gt;

* uni2779 (U+2779): L&lt;&lt;46.0,534.0&gt;--&lt;45.0,278.0&gt;&gt;

* uniE0B1 (U+E0B1): L&lt;&lt;-17.0,-319.0&gt;--&lt;-16.0,-171.0&gt;&gt;

* uniE0B3 (U+E0B3): L&lt;&lt;637.0,-171.0&gt;--&lt;636.0,-319.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts do not contain any pre-production tables. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.tables.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file contains the following pre-production tables: FFTM</p>
 [code: has-debugging-tables]



</div>
</details>
</div>
</details>

<details><summary>[27] FragmentMono-Bold-Italic.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check if OS/2 fsSelection matches head macStyle bold and italic bits. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The OS/2.fsSelection and head.macStyle italic settings do not match.</p>
<ul>
<li>OS/2.fsSelection: ITALIC is set</li>
<li>head.macStyle: ITALIC is not set</li>
</ul>
 [code: fsselection-macstyle-italic]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking post.italicAngle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.post.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Font is not italic, so post.italicAngle should be equal to zero.</p>
 [code: non-zero-upright]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsSelection value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2 fsSelection ITALIC bit should be unset.</p>
 [code: bad-ITALIC]







</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1040, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 396, but got 378 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs had components with scaling or rotation
or inverted outline direction:</p>
<ul>
<li>i (component dotlessi)</li>
<li>i (component uni0307.i)</li>
<li>j (component uni0237)</li>
<li>j (component uni0307.i)</li>
<li>dcaron (component d)</li>
<li>dcaron (component uni030C.alt)</li>
<li>Dcroat (component Eth)</li>
<li>uni03A9 (component uni2126)</li>
<li>i.ss03 (component dotlessi.ss03)</li>
<li>i.ss03 (component uni0307.i)</li>
<li>i.ss05 (component dotlessi.ss05)</li>
<li>i.ss05 (component uni0307.i)</li>
<li>dcroat.sc (component eth.sc)</li>
</ul>
 [code: transformed-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking with fontTools.ttx <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.sanitize.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>WARNING: fsSelection bit 0 (italic) and head table macStyle bit 1 (italic) should match</p>
 





</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Are there unwanted tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.tables.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following unwanted font tables were found:</p>
<ul>
<li>FFTM - Table contains redundant FontForge timestamp info</li>
</ul>
<p>They can be removed with the 'fix-unwanted-tables' script provided by gftools.</p>
 [code: unwanted-tables]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nl_Latn (Dutch)</td>
<td align="left">Shaper didn't attach acutecomb to J</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Font names are incorrect:</p>
<table>
<thead>
<tr>
<th align="left">nameID</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Family Name</td>
<td align="left"><strong>Fragment Mono</strong></td>
<td align="left"><strong>Fragment Mono Bold-Italic</strong></td>
</tr>
<tr>
<td align="left">Subfamily Name</td>
<td align="left"><strong>Bold-Italic</strong></td>
<td align="left"><strong>Regular</strong></td>
</tr>
<tr>
<td align="left">Full Name</td>
<td align="left"><strong>Fragment Mono Bold Italic</strong></td>
<td align="left"><strong>Fragment Mono Bold-Italic Regular</strong></td>
</tr>
<tr>
<td align="left">Postscript Name</td>
<td align="left"><strong>FragmentMono-Bold-Italic</strong></td>
<td align="left"><strong>FragmentMonoBold-Italic-Regular</strong></td>
</tr>
</tbody>
</table>
 [code: bad-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check the OS/2 usWeightClass is appropriate for the font's best SubFamily name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Best SubFamily name is 'Bold-Italic'. Expected OS/2 usWeightClass is 400, got 700.</p>
 [code: bad-value]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 982 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 1 glyphs (0.10%) have a different width. You should check the widths of: ['nonmarkingreturn']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check hhea.caretSlopeRise and hhea.caretSlopeRun <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.hhea.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>hhea.caretSlopeRise and hhea.caretSlopeRun do not match with post.italicAngle.
Got: caretSlopeRise 100 and caretSlopeRun 21
Expected: caretSlopeRise 1000 and caretSlopeRun 213</p>
 [code: caretslope-mismatch]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: uni2154	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni2552	Contours detected: 1	Expected: 2

- Glyph name: uni2553	Contours detected: 1	Expected: 2

- Glyph name: uni2555	Contours detected: 1	Expected: 2

- Glyph name: uni2556	Contours detected: 1	Expected: 2

- Glyph name: uni2558	Contours detected: 1	Expected: 2

- Glyph name: uni2559	Contours detected: 1	Expected: 2

- Glyph name: uni255B	Contours detected: 1	Expected: 2

- Glyph name: uni255C	Contours detected: 1	Expected: 2

- Glyph name: uni255E	Contours detected: 1	Expected: 2

- Glyph name: uni2561	Contours detected: 1	Expected: 2

- Glyph name: ltshade	Contours detected: 36	Expected: 46

- Glyph name: shade	Contours detected: 78	Expected: 85

- Glyph name: dkshade	Contours detected: 37	Expected: 73

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: dkshade	Contours detected: 37	Expected: 73

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: ltshade	Contours detected: 36	Expected: 46

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: shade	Contours detected: 78	Expected: 85

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking with ots-sanitize. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.sanitize.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>ots-sanitize passed this file, however warnings were printed:</p>
<p>WARNING: OS/2: Adjusting head.macStyle (italic) to match fsSelection</p>
 [code: ots-sanitize-warn]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- l.002

- nonmarkingreturn
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
asciitilde_asciitilde_greater.liga, less_numbersign_hyphen_hyphen.liga and semicolon_semicolon_semicolon.liga</p>
 [code: legacy-long-names]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, math, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, todhri, tai-le, hebrew, syriac, malayalam, tifinagh, old-permic, duployan, coptic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, elbasan, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, elbasan, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2017 DOUBLE LOW LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21B0 UPWARDS ARROW WITH TIP LEFTWARDS: try adding math</li>
<li>U+21B1 UPWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21B2 DOWNWARDS ARROW WITH TIP LEFTWARDS: try adding math</li>
<li>U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21BA ANTICLOCKWISE OPEN CIRCLE ARROW: try adding math</li>
<li>U+21BB CLOCKWISE OPEN CIRCLE ARROW: try adding math</li>
<li>U+21C6 LEFTWARDS ARROW OVER RIGHTWARDS ARROW: try adding math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, symbols, math, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2398 NEXT PAGE: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, symbols, mongolian</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, symbols, mongolian</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, symbols, mongolian</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, symbols, mongolian</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, symbols, mongolian</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, symbols, mongolian</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, symbols, mongolian</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, symbols, mongolian</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, symbols, mongolian</li>
<li>U+2469 CIRCLED NUMBER TEN: try adding one of: yi, symbols, mongolian</li>
<li>U+24B6 CIRCLED LATIN CAPITAL LETTER A: try adding symbols</li>
<li>U+24B7 CIRCLED LATIN CAPITAL LETTER B: try adding symbols</li>
<li>U+24B8 CIRCLED LATIN CAPITAL LETTER C: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+24BA CIRCLED LATIN CAPITAL LETTER E: try adding symbols</li>
<li>U+24BB CIRCLED LATIN CAPITAL LETTER F: try adding symbols</li>
<li>U+24BC CIRCLED LATIN CAPITAL LETTER G: try adding symbols</li>
<li>U+24BD CIRCLED LATIN CAPITAL LETTER H: try adding symbols</li>
<li>U+24BE CIRCLED LATIN CAPITAL LETTER I: try adding symbols</li>
<li>U+24BF CIRCLED LATIN CAPITAL LETTER J: try adding symbols</li>
<li>U+24C0 CIRCLED LATIN CAPITAL LETTER K: try adding symbols</li>
<li>U+24C1 CIRCLED LATIN CAPITAL LETTER L: try adding symbols</li>
<li>U+24C2 CIRCLED LATIN CAPITAL LETTER M: try adding symbols</li>
<li>U+24C3 CIRCLED LATIN CAPITAL LETTER N: try adding symbols</li>
<li>U+24C4 CIRCLED LATIN CAPITAL LETTER O: try adding symbols</li>
<li>U+24C5 CIRCLED LATIN CAPITAL LETTER P: try adding symbols</li>
<li>U+24C6 CIRCLED LATIN CAPITAL LETTER Q: try adding symbols</li>
<li>U+24C7 CIRCLED LATIN CAPITAL LETTER R: try adding symbols</li>
<li>U+24C8 CIRCLED LATIN CAPITAL LETTER S: try adding symbols</li>
<li>U+24C9 CIRCLED LATIN CAPITAL LETTER T: try adding symbols</li>
<li>U+24CA CIRCLED LATIN CAPITAL LETTER U: try adding symbols</li>
<li>U+24CB CIRCLED LATIN CAPITAL LETTER V: try adding symbols</li>
<li>U+24CC CIRCLED LATIN CAPITAL LETTER W: try adding symbols</li>
<li>U+24CD CIRCLED LATIN CAPITAL LETTER X: try adding symbols</li>
<li>U+24CE CIRCLED LATIN CAPITAL LETTER Y: try adding symbols</li>
<li>U+24CF CIRCLED LATIN CAPITAL LETTER Z: try adding symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CE BULLSEYE: try adding symbols</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2717 BALLOT X: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+277F DINGBAT NEGATIVE CIRCLED NUMBER TEN: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, phags-pa, chinese-traditional, yi, japanese, chinese-hongkong</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, phags-pa, chinese-traditional, yi, japanese, chinese-hongkong</li>
<li>U+E000 : not included in any glyphset definition</li>
<li>U+E001 : not included in any glyphset definition</li>
<li>U+E0A0 : not included in any glyphset definition</li>
<li>U+E0A1 : not included in any glyphset definition</li>
<li>U+E0A2 : not included in any glyphset definition</li>
<li>U+E0B0 : not included in any glyphset definition</li>
<li>U+E0B1 : not included in any glyphset definition</li>
<li>U+E0B2 : not included in any glyphset definition</li>
<li>U+E0B3 : not included in any glyphset definition</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+1F150 NEGATIVE CIRCLED LATIN CAPITAL LETTER A: try adding symbols</li>
<li>U+1F151 NEGATIVE CIRCLED LATIN CAPITAL LETTER B: try adding symbols</li>
<li>U+1F152 NEGATIVE CIRCLED LATIN CAPITAL LETTER C: try adding symbols</li>
<li>U+1F153 NEGATIVE CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+1F154 NEGATIVE CIRCLED LATIN CAPITAL LETTER E: try adding symbols</li>
<li>U+1F155 NEGATIVE CIRCLED LATIN CAPITAL LETTER F: try adding symbols</li>
<li>U+1F156 NEGATIVE CIRCLED LATIN CAPITAL LETTER G: try adding symbols</li>
<li>U+1F157 NEGATIVE CIRCLED LATIN CAPITAL LETTER H: try adding symbols</li>
<li>U+1F158 NEGATIVE CIRCLED LATIN CAPITAL LETTER I: try adding symbols</li>
<li>U+1F159 NEGATIVE CIRCLED LATIN CAPITAL LETTER J: try adding symbols</li>
<li>U+1F15A NEGATIVE CIRCLED LATIN CAPITAL LETTER K: try adding symbols</li>
<li>U+1F15B NEGATIVE CIRCLED LATIN CAPITAL LETTER L: try adding symbols</li>
<li>U+1F15C NEGATIVE CIRCLED LATIN CAPITAL LETTER M: try adding symbols</li>
<li>U+1F15D NEGATIVE CIRCLED LATIN CAPITAL LETTER N: try adding symbols</li>
<li>U+1F15E NEGATIVE CIRCLED LATIN CAPITAL LETTER O: try adding symbols</li>
<li>U+1F15F NEGATIVE CIRCLED LATIN CAPITAL LETTER P: try adding symbols</li>
<li>U+1F160 NEGATIVE CIRCLED LATIN CAPITAL LETTER Q: try adding symbols</li>
<li>U+1F161 NEGATIVE CIRCLED LATIN CAPITAL LETTER R: try adding symbols</li>
<li>U+1F162 NEGATIVE CIRCLED LATIN CAPITAL LETTER S: try adding symbols</li>
<li>U+1F163 NEGATIVE CIRCLED LATIN CAPITAL LETTER T: try adding symbols</li>
<li>U+1F164 NEGATIVE CIRCLED LATIN CAPITAL LETTER U: try adding symbols</li>
<li>U+1F165 NEGATIVE CIRCLED LATIN CAPITAL LETTER V: try adding symbols</li>
<li>U+1F166 NEGATIVE CIRCLED LATIN CAPITAL LETTER W: try adding symbols</li>
<li>U+1F167 NEGATIVE CIRCLED LATIN CAPITAL LETTER X: try adding symbols</li>
<li>U+1F168 NEGATIVE CIRCLED LATIN CAPITAL LETTER Y: try adding symbols</li>
<li>U+1F169 NEGATIVE CIRCLED LATIN CAPITAL LETTER Z: try adding symbols</li>
<li>U+1F4C4 PAGE FACING UP: not included in any glyphset definition</li>
<li>U+1F517 LINK SYMBOL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: į̆ į̇ į̈ į̊ į̋ į̒ į̦̀ į̦́ į̦̂ į̦̃ į̦̄ į̦̆ į̦̇ į̦̈ į̦̊ į̦̋ į̦̌ į̦̒ į̧̀ į̧́</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Lugbara (Latn, 2,200,000 speakers), Nzakara (Latn, 50,000 speakers), Fur (Latn, 1,230,163 speakers), Avokaya (Latn, 100,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Gulay (Latn, 250,478 speakers), Dutch (Latn, 31,709,104 speakers), Han (Latn, 6 speakers), Heiltsuk (Latn, 300 speakers), Basaa (Latn, 332,940 speakers), Ma’di (Latn, 584,000 speakers), Kaska (Latn, 125 speakers), Vute (Latn, 21,000 speakers), Bafut (Latn, 158,146 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Koonzime (Latn, 40,000 speakers), Sar (Latn, 500,000 speakers), South Central Banda (Latn, 244,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Yala (Latn, 200,000 speakers), Mango (Latn, 77,000 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Bete-Bendi (Latn, 100,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Kom (Latn, 360,685 speakers), Ejagham (Latn, 120,000 speakers), Cicipu (Latn, 44,000 speakers), Nateni (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Navajo (Latn, 166,319 speakers), Ebira (Latn, 2,200,000 speakers), Ekpeye (Latn, 226,000 speakers), Mundani (Latn, 34,000 speakers), Southern Kisi (Latn, 360,000 speakers), Dan (Latn, 1,099,244 speakers), Teke-Ebo (Latn, 260,000 speakers), Mfumte (Latn, 79,000 speakers), Igbo (Latn, 27,823,640 speakers), Dii (Latn, 71,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* dollar (U+0024): X=446.0,Y=697.0 (should be at cap-height 699?)

* Q (U+0051): X=375.0,Y=-2.0 (should be at baseline 0?)

* a (U+0061): X=417.0,Y=1.5 (should be at baseline 0?)

* f (U+0066): X=390.0,Y=699.5 (should be at cap-height 699?)

* t (U+0074): X=491.0,Y=-2.0 (should be at baseline 0?)

* agrave (U+00E0): X=417.0,Y=1.5 (should be at baseline 0?)

* aacute (U+00E1): X=417.0,Y=1.5 (should be at baseline 0?)

* acircumflex (U+00E2): X=417.0,Y=1.5 (should be at baseline 0?)

* atilde (U+00E3): X=417.0,Y=1.5 (should be at baseline 0?)

* adieresis (U+00E4): X=417.0,Y=1.5 (should be at baseline 0?)

* aring (U+00E5): X=417.0,Y=1.5 (should be at baseline 0?)

* amacron (U+0101): X=417.0,Y=1.5 (should be at baseline 0?)

* abreve (U+0103): X=417.0,Y=1.5 (should be at baseline 0?)

* aogonek (U+0105): X=417.0,Y=1.5 (should be at baseline 0?)

* tcaron (U+0165): X=491.0,Y=-2.0 (should be at baseline 0?)

* uni01CE (U+01CE): X=417.0,Y=1.5 (should be at baseline 0?)

* uni021B (U+021B): X=491.0,Y=-2.0 (should be at baseline 0?)

* perthousand (U+2030): X=131.0,Y=698.0 (should be at cap-height 699?)

* uni2086 (U+2086): X=366.0,Y=-2.0 (should be at baseline 0?)

* uni2087 (U+2087): X=263.0,Y=-1.0 (should be at baseline 0?)

* uni2089 (U+2089): X=355.0,Y=2.0 (should be at baseline 0?)

* uni20A8 (U+20A8): X=369.0,Y=-2.0 (should be at baseline 0?)

* Euro (U+20AC): X=308.0,Y=697.0 (should be at cap-height 699?)

* uni2113 (U+2113): X=341.0,Y=701.0 (should be at cap-height 699?)

* partialdiff (U+2202): X=394.0,Y=2.0 (should be at baseline 0?)

* uni250A (U+250A): X=256.0,Y=2.0 (should be at baseline 0?)

* uni250A (U+250A): X=362.0,Y=2.0 (should be at baseline 0?)

* uni250B (U+250B): X=238.0,Y=2.0 (should be at baseline 0?)

* uni250B (U+250B): X=380.0,Y=2.0 (should be at baseline 0?)

* uni25B6 (U+25B6): X=56.0,Y=-2.0 (should be at baseline 0?)

* uni25B6 (U+25B6): X=56.0,Y=700.0 (should be at cap-height 699?)

* uni25B7 (U+25B7): X=56.0,Y=-2.0 (should be at baseline 0?)

* uni25B7 (U+25B7): X=56.0,Y=700.0 (should be at cap-height 699?)

* uni25C0 (U+25C0): X=583.0,Y=700.0 (should be at cap-height 699?)

* uni25C0 (U+25C0): X=583.0,Y=-2.0 (should be at baseline 0?)

* uni25C1 (U+25C1): X=583.0,Y=700.0 (should be at cap-height 699?)

* uni25C1 (U+25C1): X=583.0,Y=-2.0 (should be at baseline 0?)

* usdc (U+E000): X=442.0,Y=697.0 (should be at cap-height 699?)

* usdc (U+E000): X=213.0,Y=1.0 (should be at baseline 0?)

* aring.sc: X=451.0,Y=697.0 (should be at cap-height 699?)

* germandbls.sc: X=214.0,Y=2.0 (should be at baseline 0?)

* uring.sc: X=441.0,Y=697.0 (should be at cap-height 699?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* Ccedilla (U+00C7): L&lt;&lt;335.0,30.0&gt;--&lt;381.0,30.0&gt;&gt; -&gt; L&lt;&lt;381.0,30.0&gt;--&lt;415.0,29.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;346.0,30.0&gt;--&lt;392.0,30.0&gt;&gt; -&gt; L&lt;&lt;392.0,30.0&gt;--&lt;426.0,29.0&gt;&gt;

* asciitilde_asciitilde.liga: L&lt;&lt;-410.0,244.0&gt;--&lt;-412.0,244.0&gt;&gt; -&gt; L&lt;&lt;-412.0,244.0&gt;--&lt;-434.0,245.0&gt;&gt;

* asciitilde_greater.liga: L&lt;&lt;-448.0,370.0&gt;--&lt;-450.0,370.0&gt;&gt; -&gt; L&lt;&lt;-450.0,370.0&gt;--&lt;-472.0,371.0&gt;&gt;

* bar_braceright.liga: L&lt;&lt;409.0,400.0&gt;--&lt;443.0,400.0&gt;&gt; -&gt; L&lt;&lt;443.0,400.0&gt;--&lt;465.0,400.0&gt;&gt;

* bar_braceright.liga: L&lt;&lt;443.0,298.0&gt;--&lt;429.0,298.0&gt;&gt; -&gt; L&lt;&lt;429.0,298.0&gt;--&lt;391.0,298.0&gt;&gt;

* braceright (U+007D): L&lt;&lt;459.0,400.0&gt;--&lt;493.0,400.0&gt;&gt; -&gt; L&lt;&lt;493.0,400.0&gt;--&lt;515.0,400.0&gt;&gt;

* braceright (U+007D): L&lt;&lt;493.0,298.0&gt;--&lt;479.0,298.0&gt;&gt; -&gt; L&lt;&lt;479.0,298.0&gt;--&lt;441.0,298.0&gt;&gt;

* ccedilla (U+00E7): L&lt;&lt;323.0,30.0&gt;--&lt;369.0,30.0&gt;&gt; -&gt; L&lt;&lt;369.0,30.0&gt;--&lt;403.0,29.0&gt;&gt;

* ccedilla.sc: L&lt;&lt;354.0,30.0&gt;--&lt;400.0,30.0&gt;&gt; -&gt; L&lt;&lt;400.0,30.0&gt;--&lt;434.0,29.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;275.0,30.0&gt;--&lt;321.0,30.0&gt;&gt; -&gt; L&lt;&lt;321.0,30.0&gt;--&lt;355.0,29.0&gt;&gt;

* estimated (U+212E): L&lt;&lt;562.0,282.0&gt;--&lt;564.0,251.0&gt;&gt; -&gt; L&lt;&lt;564.0,251.0&gt;--&lt;564.0,226.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;291.0,343.0&gt;--&lt;303.0,344.0&gt;&gt; -&gt; L&lt;&lt;303.0,344.0&gt;--&lt;362.0,344.0&gt;&gt;

* less_asciitilde.liga: L&lt;&lt;475.0,350.0&gt;--&lt;477.0,350.0&gt;&gt; -&gt; L&lt;&lt;477.0,350.0&gt;--&lt;499.0,349.0&gt;&gt;

* less_exclam_hyphen_hyphen.liga: L&lt;&lt;-813.0,180.0&gt;--&lt;-825.0,180.0&gt;&gt; -&gt; L&lt;&lt;-825.0,180.0&gt;--&lt;-865.0,180.0&gt;&gt;

* less_exclam_hyphen_hyphen.liga: L&lt;&lt;-825.0,180.0&gt;--&lt;-865.0,180.0&gt;&gt; -&gt; L&lt;&lt;-865.0,180.0&gt;--&lt;-884.0,180.0&gt;&gt;

* less_less_asciitilde.liga: L&lt;&lt;496.0,350.0&gt;--&lt;498.0,350.0&gt;&gt; -&gt; L&lt;&lt;498.0,350.0&gt;--&lt;520.0,349.0&gt;&gt;

* numbersign.start: L&lt;&lt;619.0,176.0&gt;--&lt;605.0,176.0&gt;&gt; -&gt; L&lt;&lt;605.0,176.0&gt;--&lt;554.0,176.0&gt;&gt;

* numbersign.start: L&lt;&lt;671.0,416.0&gt;--&lt;657.0,416.0&gt;&gt; -&gt; L&lt;&lt;657.0,416.0&gt;--&lt;634.0,416.0&gt;&gt;

* onequarter (U+00BC): L&lt;&lt;541.0,148.0&gt;--&lt;562.0,148.0&gt;&gt; -&gt; L&lt;&lt;562.0,148.0&gt;--&lt;584.0,148.0&gt;&gt;

* onequarter (U+00BC): L&lt;&lt;565.0,60.0&gt;--&lt;551.0,60.0&gt;&gt; -&gt; L&lt;&lt;551.0,60.0&gt;--&lt;522.0,60.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;272.0,373.0&gt;--&lt;260.0,373.0&gt;&gt; -&gt; L&lt;&lt;260.0,373.0&gt;--&lt;194.0,373.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;472.0,373.0&gt;--&lt;460.0,373.0&gt;&gt; -&gt; L&lt;&lt;460.0,373.0&gt;--&lt;394.0,373.0&gt;&gt;

* quotedblleft (U+201C): L&lt;&lt;334.0,716.0&gt;--&lt;365.0,716.0&gt;&gt; -&gt; L&lt;&lt;365.0,716.0&gt;--&lt;387.0,716.0&gt;&gt;

* quotedblleft (U+201C): L&lt;&lt;368.0,631.0&gt;--&lt;354.0,631.0&gt;&gt; -&gt; L&lt;&lt;354.0,631.0&gt;--&lt;329.0,631.0&gt;&gt;

* quotedblleft (U+201C): L&lt;&lt;564.0,716.0&gt;--&lt;595.0,716.0&gt;&gt; -&gt; L&lt;&lt;595.0,716.0&gt;--&lt;617.0,716.0&gt;&gt;

* quotedblleft (U+201C): L&lt;&lt;598.0,631.0&gt;--&lt;584.0,631.0&gt;&gt; -&gt; L&lt;&lt;584.0,631.0&gt;--&lt;559.0,631.0&gt;&gt;

* quoteleft (U+2018): L&lt;&lt;449.0,716.0&gt;--&lt;480.0,716.0&gt;&gt; -&gt; L&lt;&lt;480.0,716.0&gt;--&lt;502.0,716.0&gt;&gt;

* quoteleft (U+2018): L&lt;&lt;483.0,631.0&gt;--&lt;469.0,631.0&gt;&gt; -&gt; L&lt;&lt;469.0,631.0&gt;--&lt;444.0,631.0&gt;&gt;

* quotereversed (U+201B): L&lt;&lt;397.0,466.0&gt;--&lt;413.0,466.0&gt;&gt; -&gt; L&lt;&lt;413.0,466.0&gt;--&lt;435.0,466.0&gt;&gt;

* quotereversed (U+201B): L&lt;&lt;416.0,381.0&gt;--&lt;402.0,381.0&gt;&gt; -&gt; L&lt;&lt;402.0,381.0&gt;--&lt;384.0,381.0&gt;&gt;

* quotesingle (U+0027): L&lt;&lt;372.0,373.0&gt;--&lt;360.0,373.0&gt;&gt; -&gt; L&lt;&lt;360.0,373.0&gt;--&lt;294.0,373.0&gt;&gt;

* scedilla (U+015F): L&lt;&lt;322.0,30.0&gt;--&lt;368.0,30.0&gt;&gt; -&gt; L&lt;&lt;368.0,30.0&gt;--&lt;402.0,29.0&gt;&gt;

* scedilla.sc: L&lt;&lt;294.0,30.0&gt;--&lt;340.0,30.0&gt;&gt; -&gt; L&lt;&lt;340.0,30.0&gt;--&lt;374.0,29.0&gt;&gt;

* threequarters (U+00BE): L&lt;&lt;541.0,148.0&gt;--&lt;562.0,148.0&gt;&gt; -&gt; L&lt;&lt;562.0,148.0&gt;--&lt;584.0,148.0&gt;&gt;

* threequarters (U+00BE): L&lt;&lt;565.0,60.0&gt;--&lt;551.0,60.0&gt;&gt; -&gt; L&lt;&lt;551.0,60.0&gt;--&lt;522.0,60.0&gt;&gt;

* uni00B9 (U+00B9): L&lt;&lt;398.0,716.0&gt;--&lt;459.0,716.0&gt;&gt; -&gt; L&lt;&lt;459.0,716.0&gt;--&lt;481.0,716.0&gt;&gt;

* uni0123 (U+0123): L&lt;&lt;429.0,712.0&gt;--&lt;467.0,712.0&gt;&gt; -&gt; L&lt;&lt;467.0,712.0&gt;--&lt;489.0,712.0&gt;&gt;

* uni0312 (U+0312): L&lt;&lt;412.0,712.0&gt;--&lt;450.0,712.0&gt;&gt; -&gt; L&lt;&lt;450.0,712.0&gt;--&lt;472.0,712.0&gt;&gt;

* uni0327 (U+0327): L&lt;&lt;275.0,30.0&gt;--&lt;321.0,30.0&gt;&gt; -&gt; L&lt;&lt;321.0,30.0&gt;--&lt;355.0,29.0&gt;&gt;

* uni2074 (U+2074): L&lt;&lt;462.0,448.0&gt;--&lt;502.0,448.0&gt;&gt; -&gt; L&lt;&lt;502.0,448.0&gt;--&lt;524.0,448.0&gt;&gt;

* uni2081 (U+2081): L&lt;&lt;340.0,445.0&gt;--&lt;401.0,445.0&gt;&gt; -&gt; L&lt;&lt;401.0,445.0&gt;--&lt;423.0,445.0&gt;&gt;

* uni2084 (U+2084): L&lt;&lt;404.0,177.0&gt;--&lt;444.0,177.0&gt;&gt; -&gt; L&lt;&lt;444.0,177.0&gt;--&lt;466.0,177.0&gt;&gt;

* uni2463 (U+2463): L&lt;&lt;134.0,312.0&gt;--&lt;180.0,312.0&gt;&gt; -&gt; L&lt;&lt;180.0,312.0&gt;--&lt;202.0,312.0&gt;&gt;

* uni252D (U+252D): L&lt;&lt;363.0,376.0&gt;--&lt;655.0,376.0&gt;&gt; -&gt; L&lt;&lt;655.0,376.0&gt;--&lt;673.0,376.0&gt;&gt;

* uni2531 (U+2531): L&lt;&lt;381.0,376.0&gt;--&lt;655.0,376.0&gt;&gt; -&gt; L&lt;&lt;655.0,376.0&gt;--&lt;673.0,376.0&gt;&gt;

* uni2536 (U+2536): L&lt;&lt;257.0,268.0&gt;--&lt;-35.0,268.0&gt;&gt; -&gt; L&lt;&lt;-35.0,268.0&gt;--&lt;-53.0,268.0&gt;&gt;

* uni253A (U+253A): L&lt;&lt;239.0,268.0&gt;--&lt;-35.0,268.0&gt;&gt; -&gt; L&lt;&lt;-35.0,268.0&gt;--&lt;-53.0,268.0&gt;&gt;

* uni2544 (U+2544): L&lt;&lt;239.0,268.0&gt;--&lt;-35.0,268.0&gt;&gt; -&gt; L&lt;&lt;-35.0,268.0&gt;--&lt;-53.0,268.0&gt;&gt;

* uni2545 (U+2545): L&lt;&lt;381.0,376.0&gt;--&lt;655.0,376.0&gt;&gt; -&gt; L&lt;&lt;655.0,376.0&gt;--&lt;673.0,376.0&gt;&gt;

* uni2571 (U+2571): L&lt;&lt;54.0,-124.0&gt;--&lt;45.0,-124.0&gt;&gt; -&gt; L&lt;&lt;45.0,-124.0&gt;--&lt;-17.0,-124.0&gt;&gt;

* uni2571 (U+2571): L&lt;&lt;566.0,769.0&gt;--&lt;575.0,769.0&gt;&gt; -&gt; L&lt;&lt;575.0,769.0&gt;--&lt;637.0,769.0&gt;&gt;

* uni2573 (U+2573): L&lt;&lt;-17.0,770.0&gt;--&lt;45.0,770.0&gt;&gt; -&gt; L&lt;&lt;45.0,770.0&gt;--&lt;54.0,770.0&gt;&gt;

* uni257C (U+257C): L&lt;&lt;257.0,268.0&gt;--&lt;-35.0,268.0&gt;&gt; -&gt; L&lt;&lt;-35.0,268.0&gt;--&lt;-53.0,268.0&gt;&gt;

* uni257E (U+257E): L&lt;&lt;363.0,376.0&gt;--&lt;655.0,376.0&gt;&gt; -&gt; L&lt;&lt;655.0,376.0&gt;--&lt;673.0,376.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* perthousand (U+2030): B&lt;&lt;337.0,603.0&gt;-&lt;337.0,514.0&gt;-&lt;281.0,457.0&gt;&gt;/L&lt;&lt;281.0,457.0&gt;--&lt;702.0,755.0&gt;&gt; = 10.214700188664006

* perthousand (U+2030): B&lt;&lt;71.0,96.0&gt;-&lt;71.0,181.0&gt;-&lt;122.0,237.0&gt;&gt;/L&lt;&lt;122.0,237.0&gt;--&lt;-7.0,146.0&gt;&gt; = 12.475275324896764

* perthousand (U+2030): L&lt;&lt;21.0,273.0&gt;--&lt;232.0,422.0&gt;&gt;/B&lt;&lt;232.0,422.0&gt;-&lt;204.0,410.0&gt;-&lt;171.0,410.0&gt;&gt; = 12.029662134330923

* perthousand (U+2030): L&lt;&lt;676.0,629.0&gt;--&lt;180.0,278.0&gt;&gt;/B&lt;&lt;180.0,278.0&gt;-&lt;205.0,288.0&gt;-&lt;236.0,288.0&gt;&gt; = 13.484155349090974

* trademark (U+2122): L&lt;&lt;400.0,314.0&gt;--&lt;404.0,441.0&gt;&gt;/L&lt;&lt;404.0,441.0&gt;--&lt;377.0,314.0&gt;&gt; = 10.198299782583101

* trademark (U+2122): L&lt;&lt;509.0,314.0&gt;--&lt;534.0,431.0&gt;&gt;/L&lt;&lt;534.0,431.0&gt;--&lt;489.0,314.0&gt;&gt; = 8.97620156837732

* uni20A9 (U+20A9): L&lt;&lt;249.0,716.0&gt;--&lt;198.0,260.0&gt;&gt;/L&lt;&lt;198.0,260.0&gt;--&lt;347.0,716.0&gt;&gt; = 11.71347005320765

* uni20A9 (U+20A9): L&lt;&lt;300.0,-18.0&gt;--&lt;342.0,421.0&gt;&gt;/L&lt;&lt;342.0,421.0&gt;--&lt;200.0,-18.0&gt;&gt; = 12.45947733464245

* uni20A9 (U+20A9): L&lt;&lt;461.0,716.0&gt;--&lt;416.0,259.0&gt;&gt;/L&lt;&lt;416.0,259.0&gt;--&lt;560.0,716.0&gt;&gt; = 11.865872355392595

* uni2116 (U+2116): L&lt;&lt;147.0,-18.0&gt;--&lt;153.0,416.0&gt;&gt;/L&lt;&lt;153.0,416.0&gt;--&lt;60.0,-18.0&gt;&gt; = 11.302699984849689

* uni2116 (U+2116): L&lt;&lt;241.0,716.0&gt;--&lt;236.0,275.0&gt;&gt;/L&lt;&lt;236.0,275.0&gt;--&lt;331.0,716.0&gt;&gt; = 11.50726769541669

* uni24C2 (U+24C2): L&lt;&lt;91.0,99.0&gt;--&lt;148.0,365.0&gt;&gt;/L&lt;&lt;148.0,365.0&gt;--&lt;17.0,100.0&gt;&gt; = 14.210254526184084
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts do not contain any pre-production tables. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.tables.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file contains the following pre-production tables: FFTM</p>
 [code: has-debugging-tables]



</div>
</details>
</div>
</details>

<details><summary>[1] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure Italic styles have Roman counterparts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.family.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Italics missing a Roman counterpart: fonts/ttf/FragmentMono-Bold-Italic.ttf</p>
 [code: missing-roman]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 23 | 53 | 461 | 25 | 388 | 0 | 
| 0% | 0% | 2% | 6% | 49% | 3% | 41% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
