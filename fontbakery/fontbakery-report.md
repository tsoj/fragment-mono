## FontBakery report

fontbakery version: 0.12.7



## Experimental checks

These won't break the CI job for now, but will become effective after some time if nobody raises any concern.


<details><summary>[1] FragmentMono-Regular.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[1] FragmentMono-Bold.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[1] FragmentMono-Italic.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>




## All other checks



<details><summary>[1] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check that OS/2.fsSelection bold & italic settings are unique for each NameID1 <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Family 'Fragment Mono' has 2 fonts (should be no more than 1) with the same OS/2.fsSelection bold &amp; italic settings: Bold=False, Italic=False</p>
 [code: unique-fsselection]



</div>
</details>
</div>
</details>

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







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1035, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 391, but got 378 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.7, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



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







* ⚠️ **WARN** <p>The OpenType spec recomments at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 958 instead.
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Basaa (Latn, 332,940 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lugbara (Latn, 2,200,000 speakers), Ma’di (Latn, 584,000 speakers), Nzakara (Latn, 50,000 speakers), Mundani (Latn, 34,000 speakers), Cicipu (Latn, 44,000 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Southern Kisi (Latn, 360,000 speakers), Mango (Latn, 77,000 speakers), Aghem (Latn, 38,843 speakers), Vute (Latn, 21,000 speakers), Yala (Latn, 200,000 speakers), Dan (Latn, 1,099,244 speakers), Dutch (Latn, 31,709,104 speakers), Avokaya (Latn, 100,000 speakers), Dii (Latn, 71,000 speakers), Mfumte (Latn, 79,000 speakers), Ebira (Latn, 2,200,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Koonzime (Latn, 40,000 speakers), Makaa (Latn, 221,000 speakers), Fur (Latn, 1,230,163 speakers), Ngbaka (Latn, 1,020,000 speakers), Bafut (Latn, 158,146 speakers), Ekpeye (Latn, 226,000 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers), Gulay (Latn, 250,478 speakers), Sar (Latn, 500,000 speakers).</p>
 [code: soft-dotted]



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
<li>U+02C7 CARON: try adding one of: yi, tifinagh, canadian-aboriginal</li>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: syriac, coptic, old-permic, tai-le, malayalam, tifinagh, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition</li>
<li>U+2017 DOUBLE LOW LINE: not included in any glyphset definition</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: not included in any glyphset definition</li>
<li>U+2075 SUPERSCRIPT FIVE: not included in any glyphset definition</li>
<li>U+2076 SUPERSCRIPT SIX: not included in any glyphset definition</li>
<li>U+2077 SUPERSCRIPT SEVEN: not included in any glyphset definition</li>
<li>U+2078 SUPERSCRIPT EIGHT: not included in any glyphset definition</li>
<li>U+2079 SUPERSCRIPT NINE: not included in any glyphset definition</li>
<li>U+2080 SUBSCRIPT ZERO: not included in any glyphset definition</li>
<li>U+2081 SUBSCRIPT ONE: not included in any glyphset definition</li>
<li>U+2082 SUBSCRIPT TWO: not included in any glyphset definition</li>
<li>U+2083 SUBSCRIPT THREE: not included in any glyphset definition</li>
<li>U+2084 SUBSCRIPT FOUR: not included in any glyphset definition</li>
<li>U+2085 SUBSCRIPT FIVE: not included in any glyphset definition</li>
<li>U+2086 SUBSCRIPT SIX: not included in any glyphset definition</li>
<li>U+2087 SUBSCRIPT SEVEN: not included in any glyphset definition</li>
<li>U+2088 SUBSCRIPT EIGHT: not included in any glyphset definition</li>
<li>U+2089 SUBSCRIPT NINE: not included in any glyphset definition</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+212E ESTIMATED SYMBOL: not included in any glyphset definition</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: not included in any glyphset definition</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: not included in any glyphset definition</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: not included in any glyphset definition</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: not included in any glyphset definition</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: not included in any glyphset definition</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: not included in any glyphset definition</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: yi, symbols, tai-tham, math</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+2469 CIRCLED NUMBER TEN: try adding one of: yi, mongolian, symbols</li>
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
<li>U+2500 BOX DRAWINGS LIGHT HORIZONTAL: not included in any glyphset definition</li>
<li>U+2501 BOX DRAWINGS HEAVY HORIZONTAL: not included in any glyphset definition</li>
<li>U+2502 BOX DRAWINGS LIGHT VERTICAL: not included in any glyphset definition</li>
<li>U+2503 BOX DRAWINGS HEAVY VERTICAL: not included in any glyphset definition</li>
<li>U+2504 BOX DRAWINGS LIGHT TRIPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+2505 BOX DRAWINGS HEAVY TRIPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+2506 BOX DRAWINGS LIGHT TRIPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+2507 BOX DRAWINGS HEAVY TRIPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+2508 BOX DRAWINGS LIGHT QUADRUPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+2509 BOX DRAWINGS HEAVY QUADRUPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+250A BOX DRAWINGS LIGHT QUADRUPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+250B BOX DRAWINGS HEAVY QUADRUPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+250C BOX DRAWINGS LIGHT DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+250D BOX DRAWINGS DOWN LIGHT AND RIGHT HEAVY: not included in any glyphset definition</li>
<li>U+250E BOX DRAWINGS DOWN HEAVY AND RIGHT LIGHT: not included in any glyphset definition</li>
<li>U+250F BOX DRAWINGS HEAVY DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+2510 BOX DRAWINGS LIGHT DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+2511 BOX DRAWINGS DOWN LIGHT AND LEFT HEAVY: not included in any glyphset definition</li>
<li>U+2512 BOX DRAWINGS DOWN HEAVY AND LEFT LIGHT: not included in any glyphset definition</li>
<li>U+2513 BOX DRAWINGS HEAVY DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+2514 BOX DRAWINGS LIGHT UP AND RIGHT: not included in any glyphset definition</li>
<li>U+2515 BOX DRAWINGS UP LIGHT AND RIGHT HEAVY: not included in any glyphset definition</li>
<li>U+2516 BOX DRAWINGS UP HEAVY AND RIGHT LIGHT: not included in any glyphset definition</li>
<li>U+2517 BOX DRAWINGS HEAVY UP AND RIGHT: not included in any glyphset definition</li>
<li>U+2518 BOX DRAWINGS LIGHT UP AND LEFT: not included in any glyphset definition</li>
<li>U+2519 BOX DRAWINGS UP LIGHT AND LEFT HEAVY: not included in any glyphset definition</li>
<li>U+251A BOX DRAWINGS UP HEAVY AND LEFT LIGHT: not included in any glyphset definition</li>
<li>U+251B BOX DRAWINGS HEAVY UP AND LEFT: not included in any glyphset definition</li>
<li>U+251C BOX DRAWINGS LIGHT VERTICAL AND RIGHT: not included in any glyphset definition</li>
<li>U+251D BOX DRAWINGS VERTICAL LIGHT AND RIGHT HEAVY: not included in any glyphset definition</li>
<li>U+251E BOX DRAWINGS UP HEAVY AND RIGHT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+251F BOX DRAWINGS DOWN HEAVY AND RIGHT UP LIGHT: not included in any glyphset definition</li>
<li>U+2520 BOX DRAWINGS VERTICAL HEAVY AND RIGHT LIGHT: not included in any glyphset definition</li>
<li>U+2521 BOX DRAWINGS DOWN LIGHT AND RIGHT UP HEAVY: not included in any glyphset definition</li>
<li>U+2522 BOX DRAWINGS UP LIGHT AND RIGHT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+2523 BOX DRAWINGS HEAVY VERTICAL AND RIGHT: not included in any glyphset definition</li>
<li>U+2524 BOX DRAWINGS LIGHT VERTICAL AND LEFT: not included in any glyphset definition</li>
<li>U+2525 BOX DRAWINGS VERTICAL LIGHT AND LEFT HEAVY: not included in any glyphset definition</li>
<li>U+2526 BOX DRAWINGS UP HEAVY AND LEFT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+2527 BOX DRAWINGS DOWN HEAVY AND LEFT UP LIGHT: not included in any glyphset definition</li>
<li>U+2528 BOX DRAWINGS VERTICAL HEAVY AND LEFT LIGHT: not included in any glyphset definition</li>
<li>U+2529 BOX DRAWINGS DOWN LIGHT AND LEFT UP HEAVY: not included in any glyphset definition</li>
<li>U+252A BOX DRAWINGS UP LIGHT AND LEFT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+252B BOX DRAWINGS HEAVY VERTICAL AND LEFT: not included in any glyphset definition</li>
<li>U+252C BOX DRAWINGS LIGHT DOWN AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+252D BOX DRAWINGS LEFT HEAVY AND RIGHT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+252E BOX DRAWINGS RIGHT HEAVY AND LEFT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+252F BOX DRAWINGS DOWN LIGHT AND HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2530 BOX DRAWINGS DOWN HEAVY AND HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2531 BOX DRAWINGS RIGHT LIGHT AND LEFT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+2532 BOX DRAWINGS LEFT LIGHT AND RIGHT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+2533 BOX DRAWINGS HEAVY DOWN AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+2534 BOX DRAWINGS LIGHT UP AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+2535 BOX DRAWINGS LEFT HEAVY AND RIGHT UP LIGHT: not included in any glyphset definition</li>
<li>U+2536 BOX DRAWINGS RIGHT HEAVY AND LEFT UP LIGHT: not included in any glyphset definition</li>
<li>U+2537 BOX DRAWINGS UP LIGHT AND HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2538 BOX DRAWINGS UP HEAVY AND HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2539 BOX DRAWINGS RIGHT LIGHT AND LEFT UP HEAVY: not included in any glyphset definition</li>
<li>U+253A BOX DRAWINGS LEFT LIGHT AND RIGHT UP HEAVY: not included in any glyphset definition</li>
<li>U+253B BOX DRAWINGS HEAVY UP AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+253C BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+253D BOX DRAWINGS LEFT HEAVY AND RIGHT VERTICAL LIGHT: not included in any glyphset definition</li>
<li>U+253E BOX DRAWINGS RIGHT HEAVY AND LEFT VERTICAL LIGHT: not included in any glyphset definition</li>
<li>U+253F BOX DRAWINGS VERTICAL LIGHT AND HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2540 BOX DRAWINGS UP HEAVY AND DOWN HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2541 BOX DRAWINGS DOWN HEAVY AND UP HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2542 BOX DRAWINGS VERTICAL HEAVY AND HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2543 BOX DRAWINGS LEFT UP HEAVY AND RIGHT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+2544 BOX DRAWINGS RIGHT UP HEAVY AND LEFT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+2545 BOX DRAWINGS LEFT DOWN HEAVY AND RIGHT UP LIGHT: not included in any glyphset definition</li>
<li>U+2546 BOX DRAWINGS RIGHT DOWN HEAVY AND LEFT UP LIGHT: not included in any glyphset definition</li>
<li>U+2547 BOX DRAWINGS DOWN LIGHT AND UP HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2548 BOX DRAWINGS UP LIGHT AND DOWN HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2549 BOX DRAWINGS RIGHT LIGHT AND LEFT VERTICAL HEAVY: not included in any glyphset definition</li>
<li>U+254A BOX DRAWINGS LEFT LIGHT AND RIGHT VERTICAL HEAVY: not included in any glyphset definition</li>
<li>U+254B BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+254C BOX DRAWINGS LIGHT DOUBLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+254D BOX DRAWINGS HEAVY DOUBLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+254E BOX DRAWINGS LIGHT DOUBLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+254F BOX DRAWINGS HEAVY DOUBLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+2550 BOX DRAWINGS DOUBLE HORIZONTAL: not included in any glyphset definition</li>
<li>U+2551 BOX DRAWINGS DOUBLE VERTICAL: not included in any glyphset definition</li>
<li>U+2552 BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE: not included in any glyphset definition</li>
<li>U+2553 BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE: not included in any glyphset definition</li>
<li>U+2554 BOX DRAWINGS DOUBLE DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+2555 BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE: not included in any glyphset definition</li>
<li>U+2556 BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE: not included in any glyphset definition</li>
<li>U+2557 BOX DRAWINGS DOUBLE DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+2558 BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE: not included in any glyphset definition</li>
<li>U+2559 BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE: not included in any glyphset definition</li>
<li>U+255A BOX DRAWINGS DOUBLE UP AND RIGHT: not included in any glyphset definition</li>
<li>U+255B BOX DRAWINGS UP SINGLE AND LEFT DOUBLE: not included in any glyphset definition</li>
<li>U+255C BOX DRAWINGS UP DOUBLE AND LEFT SINGLE: not included in any glyphset definition</li>
<li>U+255D BOX DRAWINGS DOUBLE UP AND LEFT: not included in any glyphset definition</li>
<li>U+255E BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE: not included in any glyphset definition</li>
<li>U+255F BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE: not included in any glyphset definition</li>
<li>U+2560 BOX DRAWINGS DOUBLE VERTICAL AND RIGHT: not included in any glyphset definition</li>
<li>U+2561 BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE: not included in any glyphset definition</li>
<li>U+2562 BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE: not included in any glyphset definition</li>
<li>U+2563 BOX DRAWINGS DOUBLE VERTICAL AND LEFT: not included in any glyphset definition</li>
<li>U+2564 BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE: not included in any glyphset definition</li>
<li>U+2565 BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE: not included in any glyphset definition</li>
<li>U+2566 BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+2567 BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE: not included in any glyphset definition</li>
<li>U+2568 BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE: not included in any glyphset definition</li>
<li>U+2569 BOX DRAWINGS DOUBLE UP AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+256A BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE: not included in any glyphset definition</li>
<li>U+256B BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE: not included in any glyphset definition</li>
<li>U+256C BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+256D BOX DRAWINGS LIGHT ARC DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+256E BOX DRAWINGS LIGHT ARC DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+256F BOX DRAWINGS LIGHT ARC UP AND LEFT: not included in any glyphset definition</li>
<li>U+2570 BOX DRAWINGS LIGHT ARC UP AND RIGHT: not included in any glyphset definition</li>
<li>U+2571 BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT: not included in any glyphset definition</li>
<li>U+2572 BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT: not included in any glyphset definition</li>
<li>U+2573 BOX DRAWINGS LIGHT DIAGONAL CROSS: not included in any glyphset definition</li>
<li>U+2574 BOX DRAWINGS LIGHT LEFT: not included in any glyphset definition</li>
<li>U+2575 BOX DRAWINGS LIGHT UP: not included in any glyphset definition</li>
<li>U+2576 BOX DRAWINGS LIGHT RIGHT: not included in any glyphset definition</li>
<li>U+2577 BOX DRAWINGS LIGHT DOWN: not included in any glyphset definition</li>
<li>U+2578 BOX DRAWINGS HEAVY LEFT: not included in any glyphset definition</li>
<li>U+2579 BOX DRAWINGS HEAVY UP: not included in any glyphset definition</li>
<li>U+257A BOX DRAWINGS HEAVY RIGHT: not included in any glyphset definition</li>
<li>U+257B BOX DRAWINGS HEAVY DOWN: not included in any glyphset definition</li>
<li>U+257C BOX DRAWINGS LIGHT LEFT AND HEAVY RIGHT: not included in any glyphset definition</li>
<li>U+257D BOX DRAWINGS LIGHT UP AND HEAVY DOWN: not included in any glyphset definition</li>
<li>U+257E BOX DRAWINGS HEAVY LEFT AND LIGHT RIGHT: not included in any glyphset definition</li>
<li>U+257F BOX DRAWINGS HEAVY UP AND LIGHT DOWN: not included in any glyphset definition</li>
<li>U+2580 UPPER HALF BLOCK: not included in any glyphset definition</li>
<li>U+2581 LOWER ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2582 LOWER ONE QUARTER BLOCK: not included in any glyphset definition</li>
<li>U+2583 LOWER THREE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+2584 LOWER HALF BLOCK: not included in any glyphset definition</li>
<li>U+2585 LOWER FIVE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+2586 LOWER THREE QUARTERS BLOCK: not included in any glyphset definition</li>
<li>U+2587 LOWER SEVEN EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+2588 FULL BLOCK: not included in any glyphset definition</li>
<li>U+2589 LEFT SEVEN EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+258A LEFT THREE QUARTERS BLOCK: not included in any glyphset definition</li>
<li>U+258B LEFT FIVE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+258C LEFT HALF BLOCK: not included in any glyphset definition</li>
<li>U+258D LEFT THREE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+258E LEFT ONE QUARTER BLOCK: not included in any glyphset definition</li>
<li>U+258F LEFT ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2590 RIGHT HALF BLOCK: not included in any glyphset definition</li>
<li>U+2591 LIGHT SHADE: not included in any glyphset definition</li>
<li>U+2592 MEDIUM SHADE: not included in any glyphset definition</li>
<li>U+2593 DARK SHADE: not included in any glyphset definition</li>
<li>U+2594 UPPER ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2595 RIGHT ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2596 QUADRANT LOWER LEFT: not included in any glyphset definition</li>
<li>U+2597 QUADRANT LOWER RIGHT: not included in any glyphset definition</li>
<li>U+2598 QUADRANT UPPER LEFT: not included in any glyphset definition</li>
<li>U+2599 QUADRANT UPPER LEFT AND LOWER LEFT AND LOWER RIGHT: not included in any glyphset definition</li>
<li>U+259A QUADRANT UPPER LEFT AND LOWER RIGHT: not included in any glyphset definition</li>
<li>U+259B QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER LEFT: not included in any glyphset definition</li>
<li>U+259C QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER RIGHT: not included in any glyphset definition</li>
<li>U+259D QUADRANT UPPER RIGHT: not included in any glyphset definition</li>
<li>U+259E QUADRANT UPPER RIGHT AND LOWER LEFT: not included in any glyphset definition</li>
<li>U+259F QUADRANT UPPER RIGHT AND LOWER LEFT AND LOWER RIGHT: not included in any glyphset definition</li>
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
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: yi, phags-pa, chinese-hongkong, chinese-traditional, chinese-simplified, japanese</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: yi, phags-pa, chinese-hongkong, chinese-traditional, chinese-simplified, japanese</li>
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
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



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

<details><summary>[19] FragmentMono-Bold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>On non-monospaced fonts, the OS/2.panose.bProportion value can be set to any value except 9 (proportion: monospaced) which is the bad value we got in this font.</p>
 [code: bad-panose]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking head.macStyle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.head.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>head macStyle BOLD bit should be set.</p>
 [code: bad-BOLD]





</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsSelection value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2 fsSelection REGULAR bit should be unset.</p>
 [code: bad-REGULAR]



* 🔥 **FAIL** <p>OS/2 fsSelection BOLD bit should be set.</p>
 [code: bad-BOLD]





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







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1035, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 391, but got 378 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.7, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



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
<pre><code>- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

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
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* Ccedilla (U+00C7): L&lt;&lt;354.0,25.0&gt;--&lt;362.0,25.0&gt;&gt; -&gt; L&lt;&lt;362.0,25.0&gt;--&lt;404.0,25.0&gt;&gt;

* Ccedilla (U+00C7): L&lt;&lt;362.0,25.0&gt;--&lt;404.0,25.0&gt;&gt; -&gt; L&lt;&lt;404.0,25.0&gt;--&lt;425.0,25.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;345.0,25.0&gt;--&lt;353.0,25.0&gt;&gt; -&gt; L&lt;&lt;353.0,25.0&gt;--&lt;395.0,25.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;353.0,25.0&gt;--&lt;395.0,25.0&gt;&gt; -&gt; L&lt;&lt;395.0,25.0&gt;--&lt;416.0,25.0&gt;&gt;

* ccedilla (U+00E7): L&lt;&lt;342.0,25.0&gt;--&lt;350.0,25.0&gt;&gt; -&gt; L&lt;&lt;350.0,25.0&gt;--&lt;392.0,25.0&gt;&gt;

* ccedilla (U+00E7): L&lt;&lt;350.0,25.0&gt;--&lt;392.0,25.0&gt;&gt; -&gt; L&lt;&lt;392.0,25.0&gt;--&lt;413.0,25.0&gt;&gt;

* ccedilla.sc: L&lt;&lt;330.0,25.0&gt;--&lt;338.0,25.0&gt;&gt; -&gt; L&lt;&lt;338.0,25.0&gt;--&lt;380.0,25.0&gt;&gt;

* ccedilla.sc: L&lt;&lt;338.0,25.0&gt;--&lt;380.0,25.0&gt;&gt; -&gt; L&lt;&lt;380.0,25.0&gt;--&lt;401.0,25.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;320.0,25.0&gt;--&lt;328.0,25.0&gt;&gt; -&gt; L&lt;&lt;328.0,25.0&gt;--&lt;370.0,25.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;328.0,25.0&gt;--&lt;370.0,25.0&gt;&gt; -&gt; L&lt;&lt;370.0,25.0&gt;--&lt;391.0,25.0&gt;&gt;

* equal_exclam_equal.liga: L&lt;&lt;-278.0,185.0&gt;--&lt;-329.0,185.0&gt;&gt; -&gt; L&lt;&lt;-329.0,185.0&gt;--&lt;-340.0,185.0&gt;&gt;

* estimated (U+212E): L&lt;&lt;559.0,252.0&gt;--&lt;559.0,251.0&gt;&gt; -&gt; L&lt;&lt;559.0,251.0&gt;--&lt;559.0,231.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;340.0,185.0&gt;--&lt;289.0,185.0&gt;&gt; -&gt; L&lt;&lt;289.0,185.0&gt;--&lt;278.0,185.0&gt;&gt;

* exclam_exclam.liga: L&lt;&lt;-198.0,185.0&gt;--&lt;-249.0,185.0&gt;&gt; -&gt; L&lt;&lt;-249.0,185.0&gt;--&lt;-260.0,185.0&gt;&gt;

* exclam_exclam.liga: L&lt;&lt;260.0,185.0&gt;--&lt;209.0,185.0&gt;&gt; -&gt; L&lt;&lt;209.0,185.0&gt;--&lt;198.0,185.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;211.0,185.0&gt;--&lt;160.0,185.0&gt;&gt; -&gt; L&lt;&lt;160.0,185.0&gt;--&lt;149.0,185.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;469.0,185.0&gt;--&lt;418.0,185.0&gt;&gt; -&gt; L&lt;&lt;418.0,185.0&gt;--&lt;407.0,185.0&gt;&gt;

* less_exclam_hyphen_hyphen.liga: L&lt;&lt;-800.0,185.0&gt;--&lt;-851.0,185.0&gt;&gt; -&gt; L&lt;&lt;-851.0,185.0&gt;--&lt;-862.0,185.0&gt;&gt;

* scedilla (U+015F): L&lt;&lt;334.0,25.0&gt;--&lt;342.0,25.0&gt;&gt; -&gt; L&lt;&lt;342.0,25.0&gt;--&lt;384.0,25.0&gt;&gt;

* scedilla (U+015F): L&lt;&lt;342.0,25.0&gt;--&lt;384.0,25.0&gt;&gt; -&gt; L&lt;&lt;384.0,25.0&gt;--&lt;405.0,25.0&gt;&gt;

* scedilla.sc: L&lt;&lt;330.0,25.0&gt;--&lt;338.0,25.0&gt;&gt; -&gt; L&lt;&lt;338.0,25.0&gt;--&lt;380.0,25.0&gt;&gt;

* scedilla.sc: L&lt;&lt;338.0,25.0&gt;--&lt;380.0,25.0&gt;&gt; -&gt; L&lt;&lt;380.0,25.0&gt;--&lt;401.0,25.0&gt;&gt;

* summation (U+2211): L&lt;&lt;468.0,316.0&gt;--&lt;468.0,304.0&gt;&gt; -&gt; L&lt;&lt;468.0,304.0&gt;--&lt;468.0,299.0&gt;&gt;

* summation (U+2211): L&lt;&lt;468.0,321.0&gt;--&lt;468.0,316.0&gt;&gt; -&gt; L&lt;&lt;468.0,316.0&gt;--&lt;468.0,304.0&gt;&gt;

* uni0327 (U+0327): L&lt;&lt;320.0,25.0&gt;--&lt;328.0,25.0&gt;&gt; -&gt; L&lt;&lt;328.0,25.0&gt;--&lt;370.0,25.0&gt;&gt;

* uni0327 (U+0327): L&lt;&lt;328.0,25.0&gt;--&lt;370.0,25.0&gt;&gt; -&gt; L&lt;&lt;370.0,25.0&gt;--&lt;391.0,25.0&gt;&gt;

* uni2571 (U+2571): L&lt;&lt;568.0,765.0&gt;--&lt;575.0,765.0&gt;&gt; -&gt; L&lt;&lt;575.0,765.0&gt;--&lt;632.0,765.0&gt;&gt;

* uni2572 (U+2572): L&lt;&lt;-13.0,765.0&gt;--&lt;44.0,765.0&gt;&gt; -&gt; L&lt;&lt;44.0,765.0&gt;--&lt;51.0,765.0&gt;&gt;

* uni2572 (U+2572): L&lt;&lt;631.0,-120.0&gt;--&lt;574.0,-120.0&gt;&gt; -&gt; L&lt;&lt;574.0,-120.0&gt;--&lt;567.0,-120.0&gt;&gt;

* uni2573 (U+2573): L&lt;&lt;568.0,765.0&gt;--&lt;575.0,765.0&gt;&gt; -&gt; L&lt;&lt;575.0,765.0&gt;--&lt;632.0,765.0&gt;&gt;

* uni2573 (U+2573): L&lt;&lt;632.0,-120.0&gt;--&lt;575.0,-120.0&gt;&gt; -&gt; L&lt;&lt;575.0,-120.0&gt;--&lt;568.0,-120.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* trademark (U+2122): L&lt;&lt;392.0,319.0&gt;--&lt;361.0,493.0&gt;&gt;/L&lt;&lt;361.0,493.0&gt;--&lt;361.0,319.0&gt;&gt; = 10.10187643897049

* trademark (U+2122): L&lt;&lt;503.0,319.0&gt;--&lt;503.0,490.0&gt;&gt;/L&lt;&lt;503.0,490.0&gt;--&lt;473.0,319.0&gt;&gt; = 9.950626687951587

* uni20A9 (U+20A9): L&lt;&lt;149.0,712.0&gt;--&lt;200.0,214.0&gt;&gt;/L&lt;&lt;200.0,214.0&gt;--&lt;256.0,712.0&gt;&gt; = 12.263201809650722

* uni20A9 (U+20A9): L&lt;&lt;362.0,712.0&gt;--&lt;419.0,214.0&gt;&gt;/L&lt;&lt;419.0,214.0&gt;--&lt;469.0,712.0&gt;&gt; = 12.26291075721907

* uni20A9 (U+20A9): L&lt;&lt;363.0,-13.0&gt;--&lt;309.0,464.0&gt;&gt;/L&lt;&lt;309.0,464.0&gt;--&lt;255.0,-13.0&gt;&gt; = 12.917632757437346

* uni2116 (U+2116): L&lt;&lt;140.0,712.0&gt;--&lt;237.0,244.0&gt;&gt;/L&lt;&lt;237.0,244.0&gt;--&lt;237.0,712.0&gt;&gt; = 11.709609311488988

* uni2116 (U+2116): L&lt;&lt;209.0,-13.0&gt;--&lt;115.0,448.0&gt;&gt;/L&lt;&lt;115.0,448.0&gt;--&lt;115.0,-13.0&gt;&gt; = 11.5248802007634
</code></pre>
 [code: found-jaggy-segments]



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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Basaa (Latn, 332,940 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lugbara (Latn, 2,200,000 speakers), Ma’di (Latn, 584,000 speakers), Nzakara (Latn, 50,000 speakers), Mundani (Latn, 34,000 speakers), Cicipu (Latn, 44,000 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Southern Kisi (Latn, 360,000 speakers), Mango (Latn, 77,000 speakers), Aghem (Latn, 38,843 speakers), Vute (Latn, 21,000 speakers), Yala (Latn, 200,000 speakers), Dan (Latn, 1,099,244 speakers), Dutch (Latn, 31,709,104 speakers), Avokaya (Latn, 100,000 speakers), Dii (Latn, 71,000 speakers), Mfumte (Latn, 79,000 speakers), Ebira (Latn, 2,200,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Koonzime (Latn, 40,000 speakers), Makaa (Latn, 221,000 speakers), Fur (Latn, 1,230,163 speakers), Ngbaka (Latn, 1,020,000 speakers), Bafut (Latn, 158,146 speakers), Ekpeye (Latn, 226,000 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers), Gulay (Latn, 250,478 speakers), Sar (Latn, 500,000 speakers).</p>
 [code: soft-dotted]



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
<li>U+02C7 CARON: try adding one of: yi, tifinagh, canadian-aboriginal</li>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: syriac, coptic, old-permic, tai-le, malayalam, tifinagh, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition</li>
<li>U+2017 DOUBLE LOW LINE: not included in any glyphset definition</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: not included in any glyphset definition</li>
<li>U+2075 SUPERSCRIPT FIVE: not included in any glyphset definition</li>
<li>U+2076 SUPERSCRIPT SIX: not included in any glyphset definition</li>
<li>U+2077 SUPERSCRIPT SEVEN: not included in any glyphset definition</li>
<li>U+2078 SUPERSCRIPT EIGHT: not included in any glyphset definition</li>
<li>U+2079 SUPERSCRIPT NINE: not included in any glyphset definition</li>
<li>U+2080 SUBSCRIPT ZERO: not included in any glyphset definition</li>
<li>U+2081 SUBSCRIPT ONE: not included in any glyphset definition</li>
<li>U+2082 SUBSCRIPT TWO: not included in any glyphset definition</li>
<li>U+2083 SUBSCRIPT THREE: not included in any glyphset definition</li>
<li>U+2084 SUBSCRIPT FOUR: not included in any glyphset definition</li>
<li>U+2085 SUBSCRIPT FIVE: not included in any glyphset definition</li>
<li>U+2086 SUBSCRIPT SIX: not included in any glyphset definition</li>
<li>U+2087 SUBSCRIPT SEVEN: not included in any glyphset definition</li>
<li>U+2088 SUBSCRIPT EIGHT: not included in any glyphset definition</li>
<li>U+2089 SUBSCRIPT NINE: not included in any glyphset definition</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+212E ESTIMATED SYMBOL: not included in any glyphset definition</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: not included in any glyphset definition</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: not included in any glyphset definition</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: not included in any glyphset definition</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: not included in any glyphset definition</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: not included in any glyphset definition</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: not included in any glyphset definition</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: yi, symbols, tai-tham, math</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+2469 CIRCLED NUMBER TEN: try adding one of: yi, mongolian, symbols</li>
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
<li>U+2500 BOX DRAWINGS LIGHT HORIZONTAL: not included in any glyphset definition</li>
<li>U+2501 BOX DRAWINGS HEAVY HORIZONTAL: not included in any glyphset definition</li>
<li>U+2502 BOX DRAWINGS LIGHT VERTICAL: not included in any glyphset definition</li>
<li>U+2503 BOX DRAWINGS HEAVY VERTICAL: not included in any glyphset definition</li>
<li>U+2504 BOX DRAWINGS LIGHT TRIPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+2505 BOX DRAWINGS HEAVY TRIPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+2506 BOX DRAWINGS LIGHT TRIPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+2507 BOX DRAWINGS HEAVY TRIPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+2508 BOX DRAWINGS LIGHT QUADRUPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+2509 BOX DRAWINGS HEAVY QUADRUPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+250A BOX DRAWINGS LIGHT QUADRUPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+250B BOX DRAWINGS HEAVY QUADRUPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+250C BOX DRAWINGS LIGHT DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+250D BOX DRAWINGS DOWN LIGHT AND RIGHT HEAVY: not included in any glyphset definition</li>
<li>U+250E BOX DRAWINGS DOWN HEAVY AND RIGHT LIGHT: not included in any glyphset definition</li>
<li>U+250F BOX DRAWINGS HEAVY DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+2510 BOX DRAWINGS LIGHT DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+2511 BOX DRAWINGS DOWN LIGHT AND LEFT HEAVY: not included in any glyphset definition</li>
<li>U+2512 BOX DRAWINGS DOWN HEAVY AND LEFT LIGHT: not included in any glyphset definition</li>
<li>U+2513 BOX DRAWINGS HEAVY DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+2514 BOX DRAWINGS LIGHT UP AND RIGHT: not included in any glyphset definition</li>
<li>U+2515 BOX DRAWINGS UP LIGHT AND RIGHT HEAVY: not included in any glyphset definition</li>
<li>U+2516 BOX DRAWINGS UP HEAVY AND RIGHT LIGHT: not included in any glyphset definition</li>
<li>U+2517 BOX DRAWINGS HEAVY UP AND RIGHT: not included in any glyphset definition</li>
<li>U+2518 BOX DRAWINGS LIGHT UP AND LEFT: not included in any glyphset definition</li>
<li>U+2519 BOX DRAWINGS UP LIGHT AND LEFT HEAVY: not included in any glyphset definition</li>
<li>U+251A BOX DRAWINGS UP HEAVY AND LEFT LIGHT: not included in any glyphset definition</li>
<li>U+251B BOX DRAWINGS HEAVY UP AND LEFT: not included in any glyphset definition</li>
<li>U+251C BOX DRAWINGS LIGHT VERTICAL AND RIGHT: not included in any glyphset definition</li>
<li>U+251D BOX DRAWINGS VERTICAL LIGHT AND RIGHT HEAVY: not included in any glyphset definition</li>
<li>U+251E BOX DRAWINGS UP HEAVY AND RIGHT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+251F BOX DRAWINGS DOWN HEAVY AND RIGHT UP LIGHT: not included in any glyphset definition</li>
<li>U+2520 BOX DRAWINGS VERTICAL HEAVY AND RIGHT LIGHT: not included in any glyphset definition</li>
<li>U+2521 BOX DRAWINGS DOWN LIGHT AND RIGHT UP HEAVY: not included in any glyphset definition</li>
<li>U+2522 BOX DRAWINGS UP LIGHT AND RIGHT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+2523 BOX DRAWINGS HEAVY VERTICAL AND RIGHT: not included in any glyphset definition</li>
<li>U+2524 BOX DRAWINGS LIGHT VERTICAL AND LEFT: not included in any glyphset definition</li>
<li>U+2525 BOX DRAWINGS VERTICAL LIGHT AND LEFT HEAVY: not included in any glyphset definition</li>
<li>U+2526 BOX DRAWINGS UP HEAVY AND LEFT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+2527 BOX DRAWINGS DOWN HEAVY AND LEFT UP LIGHT: not included in any glyphset definition</li>
<li>U+2528 BOX DRAWINGS VERTICAL HEAVY AND LEFT LIGHT: not included in any glyphset definition</li>
<li>U+2529 BOX DRAWINGS DOWN LIGHT AND LEFT UP HEAVY: not included in any glyphset definition</li>
<li>U+252A BOX DRAWINGS UP LIGHT AND LEFT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+252B BOX DRAWINGS HEAVY VERTICAL AND LEFT: not included in any glyphset definition</li>
<li>U+252C BOX DRAWINGS LIGHT DOWN AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+252D BOX DRAWINGS LEFT HEAVY AND RIGHT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+252E BOX DRAWINGS RIGHT HEAVY AND LEFT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+252F BOX DRAWINGS DOWN LIGHT AND HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2530 BOX DRAWINGS DOWN HEAVY AND HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2531 BOX DRAWINGS RIGHT LIGHT AND LEFT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+2532 BOX DRAWINGS LEFT LIGHT AND RIGHT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+2533 BOX DRAWINGS HEAVY DOWN AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+2534 BOX DRAWINGS LIGHT UP AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+2535 BOX DRAWINGS LEFT HEAVY AND RIGHT UP LIGHT: not included in any glyphset definition</li>
<li>U+2536 BOX DRAWINGS RIGHT HEAVY AND LEFT UP LIGHT: not included in any glyphset definition</li>
<li>U+2537 BOX DRAWINGS UP LIGHT AND HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2538 BOX DRAWINGS UP HEAVY AND HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2539 BOX DRAWINGS RIGHT LIGHT AND LEFT UP HEAVY: not included in any glyphset definition</li>
<li>U+253A BOX DRAWINGS LEFT LIGHT AND RIGHT UP HEAVY: not included in any glyphset definition</li>
<li>U+253B BOX DRAWINGS HEAVY UP AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+253C BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+253D BOX DRAWINGS LEFT HEAVY AND RIGHT VERTICAL LIGHT: not included in any glyphset definition</li>
<li>U+253E BOX DRAWINGS RIGHT HEAVY AND LEFT VERTICAL LIGHT: not included in any glyphset definition</li>
<li>U+253F BOX DRAWINGS VERTICAL LIGHT AND HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2540 BOX DRAWINGS UP HEAVY AND DOWN HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2541 BOX DRAWINGS DOWN HEAVY AND UP HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2542 BOX DRAWINGS VERTICAL HEAVY AND HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2543 BOX DRAWINGS LEFT UP HEAVY AND RIGHT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+2544 BOX DRAWINGS RIGHT UP HEAVY AND LEFT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+2545 BOX DRAWINGS LEFT DOWN HEAVY AND RIGHT UP LIGHT: not included in any glyphset definition</li>
<li>U+2546 BOX DRAWINGS RIGHT DOWN HEAVY AND LEFT UP LIGHT: not included in any glyphset definition</li>
<li>U+2547 BOX DRAWINGS DOWN LIGHT AND UP HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2548 BOX DRAWINGS UP LIGHT AND DOWN HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2549 BOX DRAWINGS RIGHT LIGHT AND LEFT VERTICAL HEAVY: not included in any glyphset definition</li>
<li>U+254A BOX DRAWINGS LEFT LIGHT AND RIGHT VERTICAL HEAVY: not included in any glyphset definition</li>
<li>U+254B BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+254C BOX DRAWINGS LIGHT DOUBLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+254D BOX DRAWINGS HEAVY DOUBLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+254E BOX DRAWINGS LIGHT DOUBLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+254F BOX DRAWINGS HEAVY DOUBLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+2550 BOX DRAWINGS DOUBLE HORIZONTAL: not included in any glyphset definition</li>
<li>U+2551 BOX DRAWINGS DOUBLE VERTICAL: not included in any glyphset definition</li>
<li>U+2552 BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE: not included in any glyphset definition</li>
<li>U+2553 BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE: not included in any glyphset definition</li>
<li>U+2554 BOX DRAWINGS DOUBLE DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+2555 BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE: not included in any glyphset definition</li>
<li>U+2556 BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE: not included in any glyphset definition</li>
<li>U+2557 BOX DRAWINGS DOUBLE DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+2558 BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE: not included in any glyphset definition</li>
<li>U+2559 BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE: not included in any glyphset definition</li>
<li>U+255A BOX DRAWINGS DOUBLE UP AND RIGHT: not included in any glyphset definition</li>
<li>U+255B BOX DRAWINGS UP SINGLE AND LEFT DOUBLE: not included in any glyphset definition</li>
<li>U+255C BOX DRAWINGS UP DOUBLE AND LEFT SINGLE: not included in any glyphset definition</li>
<li>U+255D BOX DRAWINGS DOUBLE UP AND LEFT: not included in any glyphset definition</li>
<li>U+255E BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE: not included in any glyphset definition</li>
<li>U+255F BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE: not included in any glyphset definition</li>
<li>U+2560 BOX DRAWINGS DOUBLE VERTICAL AND RIGHT: not included in any glyphset definition</li>
<li>U+2561 BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE: not included in any glyphset definition</li>
<li>U+2562 BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE: not included in any glyphset definition</li>
<li>U+2563 BOX DRAWINGS DOUBLE VERTICAL AND LEFT: not included in any glyphset definition</li>
<li>U+2564 BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE: not included in any glyphset definition</li>
<li>U+2565 BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE: not included in any glyphset definition</li>
<li>U+2566 BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+2567 BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE: not included in any glyphset definition</li>
<li>U+2568 BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE: not included in any glyphset definition</li>
<li>U+2569 BOX DRAWINGS DOUBLE UP AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+256A BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE: not included in any glyphset definition</li>
<li>U+256B BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE: not included in any glyphset definition</li>
<li>U+256C BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+256D BOX DRAWINGS LIGHT ARC DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+256E BOX DRAWINGS LIGHT ARC DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+256F BOX DRAWINGS LIGHT ARC UP AND LEFT: not included in any glyphset definition</li>
<li>U+2570 BOX DRAWINGS LIGHT ARC UP AND RIGHT: not included in any glyphset definition</li>
<li>U+2571 BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT: not included in any glyphset definition</li>
<li>U+2572 BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT: not included in any glyphset definition</li>
<li>U+2573 BOX DRAWINGS LIGHT DIAGONAL CROSS: not included in any glyphset definition</li>
<li>U+2574 BOX DRAWINGS LIGHT LEFT: not included in any glyphset definition</li>
<li>U+2575 BOX DRAWINGS LIGHT UP: not included in any glyphset definition</li>
<li>U+2576 BOX DRAWINGS LIGHT RIGHT: not included in any glyphset definition</li>
<li>U+2577 BOX DRAWINGS LIGHT DOWN: not included in any glyphset definition</li>
<li>U+2578 BOX DRAWINGS HEAVY LEFT: not included in any glyphset definition</li>
<li>U+2579 BOX DRAWINGS HEAVY UP: not included in any glyphset definition</li>
<li>U+257A BOX DRAWINGS HEAVY RIGHT: not included in any glyphset definition</li>
<li>U+257B BOX DRAWINGS HEAVY DOWN: not included in any glyphset definition</li>
<li>U+257C BOX DRAWINGS LIGHT LEFT AND HEAVY RIGHT: not included in any glyphset definition</li>
<li>U+257D BOX DRAWINGS LIGHT UP AND HEAVY DOWN: not included in any glyphset definition</li>
<li>U+257E BOX DRAWINGS HEAVY LEFT AND LIGHT RIGHT: not included in any glyphset definition</li>
<li>U+257F BOX DRAWINGS HEAVY UP AND LIGHT DOWN: not included in any glyphset definition</li>
<li>U+2580 UPPER HALF BLOCK: not included in any glyphset definition</li>
<li>U+2581 LOWER ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2582 LOWER ONE QUARTER BLOCK: not included in any glyphset definition</li>
<li>U+2583 LOWER THREE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+2584 LOWER HALF BLOCK: not included in any glyphset definition</li>
<li>U+2585 LOWER FIVE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+2586 LOWER THREE QUARTERS BLOCK: not included in any glyphset definition</li>
<li>U+2587 LOWER SEVEN EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+2588 FULL BLOCK: not included in any glyphset definition</li>
<li>U+2589 LEFT SEVEN EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+258A LEFT THREE QUARTERS BLOCK: not included in any glyphset definition</li>
<li>U+258B LEFT FIVE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+258C LEFT HALF BLOCK: not included in any glyphset definition</li>
<li>U+258D LEFT THREE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+258E LEFT ONE QUARTER BLOCK: not included in any glyphset definition</li>
<li>U+258F LEFT ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2590 RIGHT HALF BLOCK: not included in any glyphset definition</li>
<li>U+2591 LIGHT SHADE: not included in any glyphset definition</li>
<li>U+2592 MEDIUM SHADE: not included in any glyphset definition</li>
<li>U+2593 DARK SHADE: not included in any glyphset definition</li>
<li>U+2594 UPPER ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2595 RIGHT ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2596 QUADRANT LOWER LEFT: not included in any glyphset definition</li>
<li>U+2597 QUADRANT LOWER RIGHT: not included in any glyphset definition</li>
<li>U+2598 QUADRANT UPPER LEFT: not included in any glyphset definition</li>
<li>U+2599 QUADRANT UPPER LEFT AND LOWER LEFT AND LOWER RIGHT: not included in any glyphset definition</li>
<li>U+259A QUADRANT UPPER LEFT AND LOWER RIGHT: not included in any glyphset definition</li>
<li>U+259B QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER LEFT: not included in any glyphset definition</li>
<li>U+259C QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER RIGHT: not included in any glyphset definition</li>
<li>U+259D QUADRANT UPPER RIGHT: not included in any glyphset definition</li>
<li>U+259E QUADRANT UPPER RIGHT AND LOWER LEFT: not included in any glyphset definition</li>
<li>U+259F QUADRANT UPPER RIGHT AND LOWER LEFT AND LOWER RIGHT: not included in any glyphset definition</li>
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
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: yi, phags-pa, chinese-hongkong, chinese-traditional, chinese-simplified, japanese</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: yi, phags-pa, chinese-hongkong, chinese-traditional, chinese-simplified, japanese</li>
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
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



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







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1035, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 391, but got 378 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.7, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



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







* ⚠️ **WARN** <p>The OpenType spec recomments at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 958 instead.
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Basaa (Latn, 332,940 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lugbara (Latn, 2,200,000 speakers), Ma’di (Latn, 584,000 speakers), Nzakara (Latn, 50,000 speakers), Mundani (Latn, 34,000 speakers), Cicipu (Latn, 44,000 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Southern Kisi (Latn, 360,000 speakers), Mango (Latn, 77,000 speakers), Aghem (Latn, 38,843 speakers), Vute (Latn, 21,000 speakers), Yala (Latn, 200,000 speakers), Dan (Latn, 1,099,244 speakers), Dutch (Latn, 31,709,104 speakers), Avokaya (Latn, 100,000 speakers), Dii (Latn, 71,000 speakers), Mfumte (Latn, 79,000 speakers), Ebira (Latn, 2,200,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Koonzime (Latn, 40,000 speakers), Makaa (Latn, 221,000 speakers), Fur (Latn, 1,230,163 speakers), Ngbaka (Latn, 1,020,000 speakers), Bafut (Latn, 158,146 speakers), Ekpeye (Latn, 226,000 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers), Gulay (Latn, 250,478 speakers), Sar (Latn, 500,000 speakers).</p>
 [code: soft-dotted]



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
<li>U+02C7 CARON: try adding one of: yi, tifinagh, canadian-aboriginal</li>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: syriac, coptic, old-permic, tai-le, malayalam, tifinagh, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition</li>
<li>U+2017 DOUBLE LOW LINE: not included in any glyphset definition</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: not included in any glyphset definition</li>
<li>U+2075 SUPERSCRIPT FIVE: not included in any glyphset definition</li>
<li>U+2076 SUPERSCRIPT SIX: not included in any glyphset definition</li>
<li>U+2077 SUPERSCRIPT SEVEN: not included in any glyphset definition</li>
<li>U+2078 SUPERSCRIPT EIGHT: not included in any glyphset definition</li>
<li>U+2079 SUPERSCRIPT NINE: not included in any glyphset definition</li>
<li>U+2080 SUBSCRIPT ZERO: not included in any glyphset definition</li>
<li>U+2081 SUBSCRIPT ONE: not included in any glyphset definition</li>
<li>U+2082 SUBSCRIPT TWO: not included in any glyphset definition</li>
<li>U+2083 SUBSCRIPT THREE: not included in any glyphset definition</li>
<li>U+2084 SUBSCRIPT FOUR: not included in any glyphset definition</li>
<li>U+2085 SUBSCRIPT FIVE: not included in any glyphset definition</li>
<li>U+2086 SUBSCRIPT SIX: not included in any glyphset definition</li>
<li>U+2087 SUBSCRIPT SEVEN: not included in any glyphset definition</li>
<li>U+2088 SUBSCRIPT EIGHT: not included in any glyphset definition</li>
<li>U+2089 SUBSCRIPT NINE: not included in any glyphset definition</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+212E ESTIMATED SYMBOL: not included in any glyphset definition</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: not included in any glyphset definition</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: not included in any glyphset definition</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: not included in any glyphset definition</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: not included in any glyphset definition</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: not included in any glyphset definition</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: not included in any glyphset definition</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: yi, symbols, tai-tham, math</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+2469 CIRCLED NUMBER TEN: try adding one of: yi, mongolian, symbols</li>
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
<li>U+2500 BOX DRAWINGS LIGHT HORIZONTAL: not included in any glyphset definition</li>
<li>U+2501 BOX DRAWINGS HEAVY HORIZONTAL: not included in any glyphset definition</li>
<li>U+2502 BOX DRAWINGS LIGHT VERTICAL: not included in any glyphset definition</li>
<li>U+2503 BOX DRAWINGS HEAVY VERTICAL: not included in any glyphset definition</li>
<li>U+2504 BOX DRAWINGS LIGHT TRIPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+2505 BOX DRAWINGS HEAVY TRIPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+2506 BOX DRAWINGS LIGHT TRIPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+2507 BOX DRAWINGS HEAVY TRIPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+2508 BOX DRAWINGS LIGHT QUADRUPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+2509 BOX DRAWINGS HEAVY QUADRUPLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+250A BOX DRAWINGS LIGHT QUADRUPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+250B BOX DRAWINGS HEAVY QUADRUPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+250C BOX DRAWINGS LIGHT DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+250D BOX DRAWINGS DOWN LIGHT AND RIGHT HEAVY: not included in any glyphset definition</li>
<li>U+250E BOX DRAWINGS DOWN HEAVY AND RIGHT LIGHT: not included in any glyphset definition</li>
<li>U+250F BOX DRAWINGS HEAVY DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+2510 BOX DRAWINGS LIGHT DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+2511 BOX DRAWINGS DOWN LIGHT AND LEFT HEAVY: not included in any glyphset definition</li>
<li>U+2512 BOX DRAWINGS DOWN HEAVY AND LEFT LIGHT: not included in any glyphset definition</li>
<li>U+2513 BOX DRAWINGS HEAVY DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+2514 BOX DRAWINGS LIGHT UP AND RIGHT: not included in any glyphset definition</li>
<li>U+2515 BOX DRAWINGS UP LIGHT AND RIGHT HEAVY: not included in any glyphset definition</li>
<li>U+2516 BOX DRAWINGS UP HEAVY AND RIGHT LIGHT: not included in any glyphset definition</li>
<li>U+2517 BOX DRAWINGS HEAVY UP AND RIGHT: not included in any glyphset definition</li>
<li>U+2518 BOX DRAWINGS LIGHT UP AND LEFT: not included in any glyphset definition</li>
<li>U+2519 BOX DRAWINGS UP LIGHT AND LEFT HEAVY: not included in any glyphset definition</li>
<li>U+251A BOX DRAWINGS UP HEAVY AND LEFT LIGHT: not included in any glyphset definition</li>
<li>U+251B BOX DRAWINGS HEAVY UP AND LEFT: not included in any glyphset definition</li>
<li>U+251C BOX DRAWINGS LIGHT VERTICAL AND RIGHT: not included in any glyphset definition</li>
<li>U+251D BOX DRAWINGS VERTICAL LIGHT AND RIGHT HEAVY: not included in any glyphset definition</li>
<li>U+251E BOX DRAWINGS UP HEAVY AND RIGHT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+251F BOX DRAWINGS DOWN HEAVY AND RIGHT UP LIGHT: not included in any glyphset definition</li>
<li>U+2520 BOX DRAWINGS VERTICAL HEAVY AND RIGHT LIGHT: not included in any glyphset definition</li>
<li>U+2521 BOX DRAWINGS DOWN LIGHT AND RIGHT UP HEAVY: not included in any glyphset definition</li>
<li>U+2522 BOX DRAWINGS UP LIGHT AND RIGHT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+2523 BOX DRAWINGS HEAVY VERTICAL AND RIGHT: not included in any glyphset definition</li>
<li>U+2524 BOX DRAWINGS LIGHT VERTICAL AND LEFT: not included in any glyphset definition</li>
<li>U+2525 BOX DRAWINGS VERTICAL LIGHT AND LEFT HEAVY: not included in any glyphset definition</li>
<li>U+2526 BOX DRAWINGS UP HEAVY AND LEFT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+2527 BOX DRAWINGS DOWN HEAVY AND LEFT UP LIGHT: not included in any glyphset definition</li>
<li>U+2528 BOX DRAWINGS VERTICAL HEAVY AND LEFT LIGHT: not included in any glyphset definition</li>
<li>U+2529 BOX DRAWINGS DOWN LIGHT AND LEFT UP HEAVY: not included in any glyphset definition</li>
<li>U+252A BOX DRAWINGS UP LIGHT AND LEFT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+252B BOX DRAWINGS HEAVY VERTICAL AND LEFT: not included in any glyphset definition</li>
<li>U+252C BOX DRAWINGS LIGHT DOWN AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+252D BOX DRAWINGS LEFT HEAVY AND RIGHT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+252E BOX DRAWINGS RIGHT HEAVY AND LEFT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+252F BOX DRAWINGS DOWN LIGHT AND HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2530 BOX DRAWINGS DOWN HEAVY AND HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2531 BOX DRAWINGS RIGHT LIGHT AND LEFT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+2532 BOX DRAWINGS LEFT LIGHT AND RIGHT DOWN HEAVY: not included in any glyphset definition</li>
<li>U+2533 BOX DRAWINGS HEAVY DOWN AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+2534 BOX DRAWINGS LIGHT UP AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+2535 BOX DRAWINGS LEFT HEAVY AND RIGHT UP LIGHT: not included in any glyphset definition</li>
<li>U+2536 BOX DRAWINGS RIGHT HEAVY AND LEFT UP LIGHT: not included in any glyphset definition</li>
<li>U+2537 BOX DRAWINGS UP LIGHT AND HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2538 BOX DRAWINGS UP HEAVY AND HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2539 BOX DRAWINGS RIGHT LIGHT AND LEFT UP HEAVY: not included in any glyphset definition</li>
<li>U+253A BOX DRAWINGS LEFT LIGHT AND RIGHT UP HEAVY: not included in any glyphset definition</li>
<li>U+253B BOX DRAWINGS HEAVY UP AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+253C BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+253D BOX DRAWINGS LEFT HEAVY AND RIGHT VERTICAL LIGHT: not included in any glyphset definition</li>
<li>U+253E BOX DRAWINGS RIGHT HEAVY AND LEFT VERTICAL LIGHT: not included in any glyphset definition</li>
<li>U+253F BOX DRAWINGS VERTICAL LIGHT AND HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2540 BOX DRAWINGS UP HEAVY AND DOWN HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2541 BOX DRAWINGS DOWN HEAVY AND UP HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2542 BOX DRAWINGS VERTICAL HEAVY AND HORIZONTAL LIGHT: not included in any glyphset definition</li>
<li>U+2543 BOX DRAWINGS LEFT UP HEAVY AND RIGHT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+2544 BOX DRAWINGS RIGHT UP HEAVY AND LEFT DOWN LIGHT: not included in any glyphset definition</li>
<li>U+2545 BOX DRAWINGS LEFT DOWN HEAVY AND RIGHT UP LIGHT: not included in any glyphset definition</li>
<li>U+2546 BOX DRAWINGS RIGHT DOWN HEAVY AND LEFT UP LIGHT: not included in any glyphset definition</li>
<li>U+2547 BOX DRAWINGS DOWN LIGHT AND UP HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2548 BOX DRAWINGS UP LIGHT AND DOWN HORIZONTAL HEAVY: not included in any glyphset definition</li>
<li>U+2549 BOX DRAWINGS RIGHT LIGHT AND LEFT VERTICAL HEAVY: not included in any glyphset definition</li>
<li>U+254A BOX DRAWINGS LEFT LIGHT AND RIGHT VERTICAL HEAVY: not included in any glyphset definition</li>
<li>U+254B BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+254C BOX DRAWINGS LIGHT DOUBLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+254D BOX DRAWINGS HEAVY DOUBLE DASH HORIZONTAL: not included in any glyphset definition</li>
<li>U+254E BOX DRAWINGS LIGHT DOUBLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+254F BOX DRAWINGS HEAVY DOUBLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+2550 BOX DRAWINGS DOUBLE HORIZONTAL: not included in any glyphset definition</li>
<li>U+2551 BOX DRAWINGS DOUBLE VERTICAL: not included in any glyphset definition</li>
<li>U+2552 BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE: not included in any glyphset definition</li>
<li>U+2553 BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE: not included in any glyphset definition</li>
<li>U+2554 BOX DRAWINGS DOUBLE DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+2555 BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE: not included in any glyphset definition</li>
<li>U+2556 BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE: not included in any glyphset definition</li>
<li>U+2557 BOX DRAWINGS DOUBLE DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+2558 BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE: not included in any glyphset definition</li>
<li>U+2559 BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE: not included in any glyphset definition</li>
<li>U+255A BOX DRAWINGS DOUBLE UP AND RIGHT: not included in any glyphset definition</li>
<li>U+255B BOX DRAWINGS UP SINGLE AND LEFT DOUBLE: not included in any glyphset definition</li>
<li>U+255C BOX DRAWINGS UP DOUBLE AND LEFT SINGLE: not included in any glyphset definition</li>
<li>U+255D BOX DRAWINGS DOUBLE UP AND LEFT: not included in any glyphset definition</li>
<li>U+255E BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE: not included in any glyphset definition</li>
<li>U+255F BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE: not included in any glyphset definition</li>
<li>U+2560 BOX DRAWINGS DOUBLE VERTICAL AND RIGHT: not included in any glyphset definition</li>
<li>U+2561 BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE: not included in any glyphset definition</li>
<li>U+2562 BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE: not included in any glyphset definition</li>
<li>U+2563 BOX DRAWINGS DOUBLE VERTICAL AND LEFT: not included in any glyphset definition</li>
<li>U+2564 BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE: not included in any glyphset definition</li>
<li>U+2565 BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE: not included in any glyphset definition</li>
<li>U+2566 BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+2567 BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE: not included in any glyphset definition</li>
<li>U+2568 BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE: not included in any glyphset definition</li>
<li>U+2569 BOX DRAWINGS DOUBLE UP AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+256A BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE: not included in any glyphset definition</li>
<li>U+256B BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE: not included in any glyphset definition</li>
<li>U+256C BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL: not included in any glyphset definition</li>
<li>U+256D BOX DRAWINGS LIGHT ARC DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+256E BOX DRAWINGS LIGHT ARC DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+256F BOX DRAWINGS LIGHT ARC UP AND LEFT: not included in any glyphset definition</li>
<li>U+2570 BOX DRAWINGS LIGHT ARC UP AND RIGHT: not included in any glyphset definition</li>
<li>U+2571 BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT: not included in any glyphset definition</li>
<li>U+2572 BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT: not included in any glyphset definition</li>
<li>U+2573 BOX DRAWINGS LIGHT DIAGONAL CROSS: not included in any glyphset definition</li>
<li>U+2574 BOX DRAWINGS LIGHT LEFT: not included in any glyphset definition</li>
<li>U+2575 BOX DRAWINGS LIGHT UP: not included in any glyphset definition</li>
<li>U+2576 BOX DRAWINGS LIGHT RIGHT: not included in any glyphset definition</li>
<li>U+2577 BOX DRAWINGS LIGHT DOWN: not included in any glyphset definition</li>
<li>U+2578 BOX DRAWINGS HEAVY LEFT: not included in any glyphset definition</li>
<li>U+2579 BOX DRAWINGS HEAVY UP: not included in any glyphset definition</li>
<li>U+257A BOX DRAWINGS HEAVY RIGHT: not included in any glyphset definition</li>
<li>U+257B BOX DRAWINGS HEAVY DOWN: not included in any glyphset definition</li>
<li>U+257C BOX DRAWINGS LIGHT LEFT AND HEAVY RIGHT: not included in any glyphset definition</li>
<li>U+257D BOX DRAWINGS LIGHT UP AND HEAVY DOWN: not included in any glyphset definition</li>
<li>U+257E BOX DRAWINGS HEAVY LEFT AND LIGHT RIGHT: not included in any glyphset definition</li>
<li>U+257F BOX DRAWINGS HEAVY UP AND LIGHT DOWN: not included in any glyphset definition</li>
<li>U+2580 UPPER HALF BLOCK: not included in any glyphset definition</li>
<li>U+2581 LOWER ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2582 LOWER ONE QUARTER BLOCK: not included in any glyphset definition</li>
<li>U+2583 LOWER THREE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+2584 LOWER HALF BLOCK: not included in any glyphset definition</li>
<li>U+2585 LOWER FIVE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+2586 LOWER THREE QUARTERS BLOCK: not included in any glyphset definition</li>
<li>U+2587 LOWER SEVEN EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+2588 FULL BLOCK: not included in any glyphset definition</li>
<li>U+2589 LEFT SEVEN EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+258A LEFT THREE QUARTERS BLOCK: not included in any glyphset definition</li>
<li>U+258B LEFT FIVE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+258C LEFT HALF BLOCK: not included in any glyphset definition</li>
<li>U+258D LEFT THREE EIGHTHS BLOCK: not included in any glyphset definition</li>
<li>U+258E LEFT ONE QUARTER BLOCK: not included in any glyphset definition</li>
<li>U+258F LEFT ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2590 RIGHT HALF BLOCK: not included in any glyphset definition</li>
<li>U+2591 LIGHT SHADE: not included in any glyphset definition</li>
<li>U+2592 MEDIUM SHADE: not included in any glyphset definition</li>
<li>U+2593 DARK SHADE: not included in any glyphset definition</li>
<li>U+2594 UPPER ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2595 RIGHT ONE EIGHTH BLOCK: not included in any glyphset definition</li>
<li>U+2596 QUADRANT LOWER LEFT: not included in any glyphset definition</li>
<li>U+2597 QUADRANT LOWER RIGHT: not included in any glyphset definition</li>
<li>U+2598 QUADRANT UPPER LEFT: not included in any glyphset definition</li>
<li>U+2599 QUADRANT UPPER LEFT AND LOWER LEFT AND LOWER RIGHT: not included in any glyphset definition</li>
<li>U+259A QUADRANT UPPER LEFT AND LOWER RIGHT: not included in any glyphset definition</li>
<li>U+259B QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER LEFT: not included in any glyphset definition</li>
<li>U+259C QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER RIGHT: not included in any glyphset definition</li>
<li>U+259D QUADRANT UPPER RIGHT: not included in any glyphset definition</li>
<li>U+259E QUADRANT UPPER RIGHT AND LOWER LEFT: not included in any glyphset definition</li>
<li>U+259F QUADRANT UPPER RIGHT AND LOWER LEFT AND LOWER RIGHT: not included in any glyphset definition</li>
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
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: yi, phags-pa, chinese-hongkong, chinese-traditional, chinese-simplified, japanese</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: yi, phags-pa, chinese-hongkong, chinese-traditional, chinese-simplified, japanese</li>
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
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



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




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 17 | 34 | 340 | 20 | 297 | 0 | 
| 0% | 0% | 2% | 5% | 48% | 3% | 42% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
