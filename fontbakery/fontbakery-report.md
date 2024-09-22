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

<details><summary>[1] FragmentMono-Bold-Italic.ttf</summary>
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







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1036, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 392, but got 378 instead</p>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Fur (Latn, 1,230,163 speakers), Mfumte (Latn, 79,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Dan (Latn, 1,099,244 speakers), Dii (Latn, 71,000 speakers), Cicipu (Latn, 44,000 speakers), Mango (Latn, 77,000 speakers), Makaa (Latn, 221,000 speakers), Aghem (Latn, 38,843 speakers), Lugbara (Latn, 2,200,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ekpeye (Latn, 226,000 speakers), Kom (Latn, 360,685 speakers), Dutch (Latn, 31,709,104 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Basaa (Latn, 332,940 speakers), Navajo (Latn, 166,319 speakers), Bete-Bendi (Latn, 100,000 speakers), Igbo (Latn, 27,823,640 speakers), Bafut (Latn, 158,146 speakers), Mundani (Latn, 34,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Nateni (Latn, 100,000 speakers), Ebira (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Sar (Latn, 500,000 speakers), Vute (Latn, 21,000 speakers), South Central Banda (Latn, 244,000 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Zapotec (Latn, 490,000 speakers), Ma’di (Latn, 584,000 speakers).</p>
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
<li>U+02C7 CARON: try adding one of: yi, canadian-aboriginal, tifinagh</li>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, coptic, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, canadian-aboriginal, math, malayalam, coptic, syriac, tifinagh, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: math, greek, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, greek, elbasan</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, greek, yi</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, arabic, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
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
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
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
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, chinese-hongkong, chinese-traditional, japanese, yi, phags-pa</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, chinese-hongkong, chinese-traditional, japanese, yi, phags-pa</li>
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

<details><summary>[26] FragmentMono-Bold-Italic.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>On non-monospaced fonts, the OS/2.panose.bProportion value can be set to any value except 9 (proportion: monospaced) which is the bad value we got in this font.</p>
 [code: bad-panose]



</div>
</details>

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







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1036, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 392, but got 378 instead</p>
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
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* dollar (U+0024): X=481.0,Y=697.0 (should be at cap-height 699?)

* question (U+003F): X=504.5,Y=700.5 (should be at cap-height 699?)

* Q (U+0051): X=411.0,Y=-1.0 (should be at baseline 0?)

* bracketright (U+005D): X=96.0,Y=-1.0 (should be at baseline 0?)

* bracketright (U+005D): X=230.0,Y=-1.0 (should be at baseline 0?)

* bracketright (U+005D): X=379.0,Y=700.0 (should be at cap-height 699?)

* bracketright (U+005D): X=245.0,Y=700.0 (should be at cap-height 699?)

* f (U+0066): X=428.0,Y=700.5 (should be at cap-height 699?)

* g (U+0067): X=408.0,Y=2.0 (should be at baseline 0?)

* g (U+0067): X=408.0,Y=2.0 (should be at baseline 0?)

* braceright (U+007D): X=306.0,Y=700.0 (should be at cap-height 699?)

* braceright (U+007D): X=230.0,Y=700.0 (should be at cap-height 699?)

* sterling (U+00A3): X=283.5,Y=700.0 (should be at cap-height 699?)

* degree (U+00B0): X=271.0,Y=700.5 (should be at cap-height 699?)

* degree (U+00B0): X=465.5,Y=700.5 (should be at cap-height 699?)

* atilde (U+00E3): X=426.0,Y=699.5 (should be at cap-height 699?)

* aring (U+00E5): X=402.5,Y=698.0 (should be at cap-height 699?)

* ae (U+00E6): X=74.0,Y=1.0 (should be at baseline 0?)

* ntilde (U+00F1): X=452.0,Y=699.5 (should be at cap-height 699?)

* otilde (U+00F5): X=437.0,Y=699.5 (should be at cap-height 699?)

* Aogonek (U+0104): X=604.0,Y=-2.0 (should be at baseline 0?)

* Eogonek (U+0118): X=549.0,Y=-2.0 (should be at baseline 0?)

* eogonek (U+0119): X=437.0,Y=-2.0 (should be at baseline 0?)

* gbreve (U+011F): X=408.0,Y=2.0 (should be at baseline 0?)

* gbreve (U+011F): X=408.0,Y=2.0 (should be at baseline 0?)

* gdotaccent (U+0121): X=408.0,Y=2.0 (should be at baseline 0?)

* gdotaccent (U+0121): X=408.0,Y=2.0 (should be at baseline 0?)

* uni0123 (U+0123): X=408.0,Y=2.0 (should be at baseline 0?)

* uni0123 (U+0123): X=408.0,Y=2.0 (should be at baseline 0?)

* Iogonek (U+012E): X=393.0,Y=-2.0 (should be at baseline 0?)

* iogonek (U+012F): X=419.0,Y=-2.0 (should be at baseline 0?)

* uring (U+016F): X=423.5,Y=698.0 (should be at cap-height 699?)

* Uogonek (U+0172): X=426.0,Y=-2.0 (should be at baseline 0?)

* uogonek (U+0173): X=525.0,Y=-2.0 (should be at baseline 0?)

* ring (U+02DA): X=396.5,Y=698.0 (should be at cap-height 699?)

* ogonek (U+02DB): X=352.0,Y=-2.0 (should be at baseline 0?)

* tilde (U+02DC): X=420.0,Y=699.5 (should be at cap-height 699?)

* tildecomb (U+0303): X=420.0,Y=699.5 (should be at cap-height 699?)

* uni030A (U+030A): X=396.5,Y=698.0 (should be at cap-height 699?)

* uni0328 (U+0328): X=352.0,Y=-2.0 (should be at baseline 0?)

* uni2086 (U+2086): X=364.0,Y=1.5 (should be at baseline 0?)

* colonmonetary (U+20A1): X=185.0,Y=-1.0 (should be at baseline 0?)

* lira (U+20A4): X=283.5,Y=700.0 (should be at cap-height 699?)

* uni20A8 (U+20A8): X=371.5,Y=1.5 (should be at baseline 0?)

* uni2113 (U+2113): X=343.5,Y=697.5 (should be at cap-height 699?)

* integral (U+222B): X=111.0,Y=2.0 (should be at baseline 0?)

* uni250A (U+250A): X=260.0,Y=-2.0 (should be at baseline 0?)

* uni250A (U+250A): X=358.0,Y=-2.0 (should be at baseline 0?)

* uni250B (U+250B): X=242.0,Y=-2.0 (should be at baseline 0?)

* uni250B (U+250B): X=376.0,Y=-2.0 (should be at baseline 0?)

* uni301A (U+301A): X=346.0,Y=700.0 (should be at cap-height 699?)

* uni301A (U+301A): X=386.0,Y=700.0 (should be at cap-height 699?)

* uni301B (U+301B): X=65.0,Y=-1.0 (should be at baseline 0?)

* uni301B (U+301B): X=169.0,Y=-1.0 (should be at baseline 0?)

* uni301B (U+301B): X=317.0,Y=700.0 (should be at cap-height 699?)

* uni301B (U+301B): X=213.0,Y=700.0 (should be at cap-height 699?)

* uni301B (U+301B): X=457.0,Y=700.0 (should be at cap-height 699?)

* uni301B (U+301B): X=417.0,Y=700.0 (should be at cap-height 699?)

* iogonek.ss03: X=506.0,Y=-2.0 (should be at baseline 0?)

* iogonek.ss05: X=437.0,Y=-2.0 (should be at baseline 0?)

* aring.sc: X=420.0,Y=700.5 (should be at cap-height 699?)

* eogonek.sc: X=540.0,Y=-2.0 (should be at baseline 0?)

* iogonek.sc: X=382.0,Y=-2.0 (should be at baseline 0?)

* germandbls.sc: X=232.0,Y=2.0 (should be at baseline 0?)

* uogonek.sc: X=420.0,Y=-2.0 (should be at baseline 0?)

* uring.sc: X=413.0,Y=700.5 (should be at cap-height 699?)

* period_question.liga: X=424.5,Y=700.5 (should be at cap-height 699?)

* question_period.liga: X=-33.5,Y=700.5 (should be at cap-height 699?)

* question_question.liga: X=-53.5,Y=700.5 (should be at cap-height 699?)

* question_question.liga: X=444.5,Y=700.5 (should be at cap-height 699?)

* question_question_question.liga: X=-591.5,Y=700.5 (should be at cap-height 699?)

* question_question_question.liga: X=-113.5,Y=700.5 (should be at cap-height 699?)

* question_question_question.liga: X=364.5,Y=700.5 (should be at cap-height 699?)

* bar_braceright.liga: X=256.0,Y=700.0 (should be at cap-height 699?)

* bar_braceright.liga: X=180.0,Y=700.0 (should be at cap-height 699?)

* bar_bracketright.liga: X=46.0,Y=-1.0 (should be at baseline 0?)

* bar_bracketright.liga: X=180.0,Y=-1.0 (should be at baseline 0?)

* bar_bracketright.liga: X=329.0,Y=700.0 (should be at cap-height 699?)

* bar_bracketright.liga: X=195.0,Y=700.0 (should be at cap-height 699?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* Ccedilla (U+00C7): L&lt;&lt;320.0,25.0&gt;--&lt;327.0,25.0&gt;&gt; -&gt; L&lt;&lt;327.0,25.0&gt;--&lt;373.0,25.0&gt;&gt;

* Ccedilla (U+00C7): L&lt;&lt;327.0,25.0&gt;--&lt;373.0,25.0&gt;&gt; -&gt; L&lt;&lt;373.0,25.0&gt;--&lt;399.0,25.0&gt;&gt;

* Lcaron (U+013D): L&lt;&lt;589.0,594.0&gt;--&lt;546.0,594.0&gt;&gt; -&gt; L&lt;&lt;546.0,594.0&gt;--&lt;529.0,594.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;331.0,25.0&gt;--&lt;338.0,25.0&gt;&gt; -&gt; L&lt;&lt;338.0,25.0&gt;--&lt;384.0,25.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;338.0,25.0&gt;--&lt;384.0,25.0&gt;&gt; -&gt; L&lt;&lt;384.0,25.0&gt;--&lt;410.0,25.0&gt;&gt;

* asciitilde_asciitilde.liga: L&lt;&lt;-410.0,248.0&gt;--&lt;-412.0,248.0&gt;&gt; -&gt; L&lt;&lt;-412.0,248.0&gt;--&lt;-429.0,249.0&gt;&gt;

* asciitilde_greater.liga: L&lt;&lt;-448.0,374.0&gt;--&lt;-450.0,374.0&gt;&gt; -&gt; L&lt;&lt;-450.0,374.0&gt;--&lt;-467.0,375.0&gt;&gt;

* bar_braceright.liga: L&lt;&lt;409.0,396.0&gt;--&lt;443.0,396.0&gt;&gt; -&gt; L&lt;&lt;443.0,396.0&gt;--&lt;460.0,396.0&gt;&gt;

* bar_braceright.liga: L&lt;&lt;440.0,303.0&gt;--&lt;429.0,303.0&gt;&gt; -&gt; L&lt;&lt;429.0,303.0&gt;--&lt;391.0,303.0&gt;&gt;

* bar_hyphen_greater.liga: L&lt;&lt;-1065.0,348.0&gt;--&lt;-1054.0,402.0&gt;&gt; -&gt; L&lt;&lt;-1054.0,402.0&gt;--&lt;-1000.0,656.0&gt;&gt;

* bar_hyphen_greater.liga: L&lt;&lt;-1126.0,63.0&gt;--&lt;-1065.0,348.0&gt;&gt; -&gt; L&lt;&lt;-1065.0,348.0&gt;--&lt;-1054.0,402.0&gt;&gt;

* braceright (U+007D): L&lt;&lt;459.0,396.0&gt;--&lt;493.0,396.0&gt;&gt; -&gt; L&lt;&lt;493.0,396.0&gt;--&lt;510.0,396.0&gt;&gt;

* braceright (U+007D): L&lt;&lt;490.0,303.0&gt;--&lt;479.0,303.0&gt;&gt; -&gt; L&lt;&lt;479.0,303.0&gt;--&lt;441.0,303.0&gt;&gt;

* ccedilla (U+00E7): L&lt;&lt;308.0,25.0&gt;--&lt;315.0,25.0&gt;&gt; -&gt; L&lt;&lt;315.0,25.0&gt;--&lt;361.0,25.0&gt;&gt;

* ccedilla (U+00E7): L&lt;&lt;315.0,25.0&gt;--&lt;361.0,25.0&gt;&gt; -&gt; L&lt;&lt;361.0,25.0&gt;--&lt;387.0,25.0&gt;&gt;

* ccedilla.sc: L&lt;&lt;339.0,25.0&gt;--&lt;346.0,25.0&gt;&gt; -&gt; L&lt;&lt;346.0,25.0&gt;--&lt;392.0,25.0&gt;&gt;

* ccedilla.sc: L&lt;&lt;346.0,25.0&gt;--&lt;392.0,25.0&gt;&gt; -&gt; L&lt;&lt;392.0,25.0&gt;--&lt;418.0,25.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;268.0,25.0&gt;--&lt;275.0,25.0&gt;&gt; -&gt; L&lt;&lt;275.0,25.0&gt;--&lt;321.0,25.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;275.0,25.0&gt;--&lt;321.0,25.0&gt;&gt; -&gt; L&lt;&lt;321.0,25.0&gt;--&lt;347.0,25.0&gt;&gt;

* dcaron (U+010F): L&lt;&lt;718.0,624.0&gt;--&lt;675.0,624.0&gt;&gt; -&gt; L&lt;&lt;675.0,624.0&gt;--&lt;658.0,624.0&gt;&gt;

* eng (U+014B): L&lt;&lt;599.0,368.0&gt;--&lt;519.0,11.0&gt;&gt; -&gt; L&lt;&lt;519.0,11.0&gt;--&lt;506.0,-48.0&gt;&gt;

* eng.sc: L&lt;&lt;269.0,-77.0&gt;--&lt;281.0,-77.0&gt;&gt; -&gt; L&lt;&lt;281.0,-77.0&gt;--&lt;302.0,-77.0&gt;&gt;

* equal_exclam_equal.liga: L&lt;&lt;-293.0,185.0&gt;--&lt;-303.0,185.0&gt;&gt; -&gt; L&lt;&lt;-303.0,185.0&gt;--&lt;-358.0,185.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;325.0,185.0&gt;--&lt;315.0,185.0&gt;&gt; -&gt; L&lt;&lt;315.0,185.0&gt;--&lt;260.0,185.0&gt;&gt;

* exclam_exclam.liga: L&lt;&lt;-213.0,185.0&gt;--&lt;-223.0,185.0&gt;&gt; -&gt; L&lt;&lt;-223.0,185.0&gt;--&lt;-278.0,185.0&gt;&gt;

* exclam_exclam.liga: L&lt;&lt;245.0,185.0&gt;--&lt;235.0,185.0&gt;&gt; -&gt; L&lt;&lt;235.0,185.0&gt;--&lt;180.0,185.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;196.0,185.0&gt;--&lt;186.0,185.0&gt;&gt; -&gt; L&lt;&lt;186.0,185.0&gt;--&lt;131.0,185.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;454.0,185.0&gt;--&lt;444.0,185.0&gt;&gt; -&gt; L&lt;&lt;444.0,185.0&gt;--&lt;389.0,185.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;293.0,340.0&gt;--&lt;303.0,340.0&gt;&gt; -&gt; L&lt;&lt;303.0,340.0&gt;--&lt;358.0,340.0&gt;&gt;

* hbar.sc: L&lt;&lt;648.0,514.0&gt;--&lt;688.0,514.0&gt;&gt; -&gt; L&lt;&lt;688.0,514.0&gt;--&lt;704.0,514.0&gt;&gt;

* hbar.sc: L&lt;&lt;685.0,422.0&gt;--&lt;674.0,422.0&gt;&gt; -&gt; L&lt;&lt;674.0,422.0&gt;--&lt;629.0,422.0&gt;&gt;

* lcaron (U+013E): L&lt;&lt;622.0,624.0&gt;--&lt;579.0,624.0&gt;&gt; -&gt; L&lt;&lt;579.0,624.0&gt;--&lt;562.0,624.0&gt;&gt;

* lcaron.sc: L&lt;&lt;518.0,478.0&gt;--&lt;475.0,478.0&gt;&gt; -&gt; L&lt;&lt;475.0,478.0&gt;--&lt;458.0,478.0&gt;&gt;

* lcaron.ss04: L&lt;&lt;586.0,624.0&gt;--&lt;543.0,624.0&gt;&gt; -&gt; L&lt;&lt;543.0,624.0&gt;--&lt;526.0,624.0&gt;&gt;

* lcaron.ss06: L&lt;&lt;593.0,624.0&gt;--&lt;550.0,624.0&gt;&gt; -&gt; L&lt;&lt;550.0,624.0&gt;--&lt;533.0,624.0&gt;&gt;

* less_asciitilde.liga: L&lt;&lt;475.0,346.0&gt;--&lt;477.0,346.0&gt;&gt; -&gt; L&lt;&lt;477.0,346.0&gt;--&lt;494.0,345.0&gt;&gt;

* less_exclam_hyphen_hyphen.liga: L&lt;&lt;-815.0,184.0&gt;--&lt;-825.0,184.0&gt;&gt; -&gt; L&lt;&lt;-825.0,184.0&gt;--&lt;-865.0,184.0&gt;&gt;

* less_exclam_hyphen_hyphen.liga: L&lt;&lt;-825.0,184.0&gt;--&lt;-865.0,184.0&gt;&gt; -&gt; L&lt;&lt;-865.0,184.0&gt;--&lt;-880.0,184.0&gt;&gt;

* less_hyphen_bar.liga: L&lt;&lt;491.0,372.0&gt;--&lt;480.0,318.0&gt;&gt; -&gt; L&lt;&lt;480.0,318.0&gt;--&lt;426.0,64.0&gt;&gt;

* less_hyphen_bar.liga: L&lt;&lt;552.0,656.0&gt;--&lt;491.0,372.0&gt;&gt; -&gt; L&lt;&lt;491.0,372.0&gt;--&lt;480.0,318.0&gt;&gt;

* less_less_asciitilde.liga: L&lt;&lt;496.0,346.0&gt;--&lt;498.0,346.0&gt;&gt; -&gt; L&lt;&lt;498.0,346.0&gt;--&lt;515.0,345.0&gt;&gt;

* numbersign.start: L&lt;&lt;668.0,420.0&gt;--&lt;657.0,420.0&gt;&gt; -&gt; L&lt;&lt;657.0,420.0&gt;--&lt;638.0,420.0&gt;&gt;

* onequarter (U+00BC): L&lt;&lt;536.0,144.0&gt;--&lt;562.0,144.0&gt;&gt; -&gt; L&lt;&lt;562.0,144.0&gt;--&lt;579.0,144.0&gt;&gt;

* onequarter (U+00BC): L&lt;&lt;562.0,65.0&gt;--&lt;551.0,65.0&gt;&gt; -&gt; L&lt;&lt;551.0,65.0&gt;--&lt;519.0,65.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;269.0,377.0&gt;--&lt;260.0,377.0&gt;&gt; -&gt; L&lt;&lt;260.0,377.0&gt;--&lt;198.0,377.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;469.0,377.0&gt;--&lt;460.0,377.0&gt;&gt; -&gt; L&lt;&lt;460.0,377.0&gt;--&lt;398.0,377.0&gt;&gt;

* quotedblleft (U+201C): L&lt;&lt;334.0,712.0&gt;--&lt;365.0,712.0&gt;&gt; -&gt; L&lt;&lt;365.0,712.0&gt;--&lt;382.0,712.0&gt;&gt;

* quotedblleft (U+201C): L&lt;&lt;365.0,634.0&gt;--&lt;354.0,634.0&gt;&gt; -&gt; L&lt;&lt;354.0,634.0&gt;--&lt;329.0,634.0&gt;&gt;

* quotedblleft (U+201C): L&lt;&lt;564.0,712.0&gt;--&lt;595.0,712.0&gt;&gt; -&gt; L&lt;&lt;595.0,712.0&gt;--&lt;612.0,712.0&gt;&gt;

* quotedblleft (U+201C): L&lt;&lt;595.0,635.0&gt;--&lt;584.0,635.0&gt;&gt; -&gt; L&lt;&lt;584.0,635.0&gt;--&lt;559.0,635.0&gt;&gt;

* quoteleft (U+2018): L&lt;&lt;449.0,712.0&gt;--&lt;480.0,712.0&gt;&gt; -&gt; L&lt;&lt;480.0,712.0&gt;--&lt;497.0,712.0&gt;&gt;

* quoteleft (U+2018): L&lt;&lt;480.0,635.0&gt;--&lt;469.0,635.0&gt;&gt; -&gt; L&lt;&lt;469.0,635.0&gt;--&lt;444.0,635.0&gt;&gt;

* quotereversed (U+201B): L&lt;&lt;397.0,462.0&gt;--&lt;413.0,462.0&gt;&gt; -&gt; L&lt;&lt;413.0,462.0&gt;--&lt;430.0,462.0&gt;&gt;

* quotereversed (U+201B): L&lt;&lt;413.0,385.0&gt;--&lt;402.0,385.0&gt;&gt; -&gt; L&lt;&lt;402.0,385.0&gt;--&lt;384.0,385.0&gt;&gt;

* quotesingle (U+0027): L&lt;&lt;369.0,377.0&gt;--&lt;360.0,377.0&gt;&gt; -&gt; L&lt;&lt;360.0,377.0&gt;--&lt;298.0,377.0&gt;&gt;

* scedilla (U+015F): L&lt;&lt;307.0,25.0&gt;--&lt;314.0,25.0&gt;&gt; -&gt; L&lt;&lt;314.0,25.0&gt;--&lt;360.0,25.0&gt;&gt;

* scedilla (U+015F): L&lt;&lt;314.0,25.0&gt;--&lt;360.0,25.0&gt;&gt; -&gt; L&lt;&lt;360.0,25.0&gt;--&lt;386.0,25.0&gt;&gt;

* scedilla.sc: L&lt;&lt;279.0,25.0&gt;--&lt;286.0,25.0&gt;&gt; -&gt; L&lt;&lt;286.0,25.0&gt;--&lt;332.0,25.0&gt;&gt;

* scedilla.sc: L&lt;&lt;286.0,25.0&gt;--&lt;332.0,25.0&gt;&gt; -&gt; L&lt;&lt;332.0,25.0&gt;--&lt;358.0,25.0&gt;&gt;

* tcaron (U+0165): L&lt;&lt;570.0,624.0&gt;--&lt;527.0,624.0&gt;&gt; -&gt; L&lt;&lt;527.0,624.0&gt;--&lt;510.0,624.0&gt;&gt;

* three (U+0033): L&lt;&lt;352.0,318.0&gt;--&lt;299.0,318.0&gt;&gt; -&gt; L&lt;&lt;299.0,318.0&gt;--&lt;281.0,318.0&gt;&gt;

* threequarters (U+00BE): L&lt;&lt;536.0,144.0&gt;--&lt;562.0,144.0&gt;&gt; -&gt; L&lt;&lt;562.0,144.0&gt;--&lt;579.0,144.0&gt;&gt;

* threequarters (U+00BE): L&lt;&lt;562.0,65.0&gt;--&lt;551.0,65.0&gt;&gt; -&gt; L&lt;&lt;551.0,65.0&gt;--&lt;519.0,65.0&gt;&gt;

* u1F167 (U+1F167): L&lt;&lt;-5.0,303.0&gt;--&lt;-9.0,312.0&gt;&gt; -&gt; L&lt;&lt;-9.0,312.0&gt;--&lt;-21.0,337.0&gt;&gt;

* uni00B9 (U+00B9): L&lt;&lt;401.0,712.0&gt;--&lt;459.0,712.0&gt;&gt; -&gt; L&lt;&lt;459.0,712.0&gt;--&lt;476.0,712.0&gt;&gt;

* uni030C.alt: L&lt;&lt;377.0,594.0&gt;--&lt;334.0,594.0&gt;&gt; -&gt; L&lt;&lt;334.0,594.0&gt;--&lt;317.0,594.0&gt;&gt;

* uni0327 (U+0327): L&lt;&lt;268.0,25.0&gt;--&lt;275.0,25.0&gt;&gt; -&gt; L&lt;&lt;275.0,25.0&gt;--&lt;321.0,25.0&gt;&gt;

* uni0327 (U+0327): L&lt;&lt;275.0,25.0&gt;--&lt;321.0,25.0&gt;&gt; -&gt; L&lt;&lt;321.0,25.0&gt;--&lt;347.0,25.0&gt;&gt;

* uni2074 (U+2074): L&lt;&lt;457.0,444.0&gt;--&lt;502.0,444.0&gt;&gt; -&gt; L&lt;&lt;502.0,444.0&gt;--&lt;519.0,444.0&gt;&gt;

* uni2081 (U+2081): L&lt;&lt;343.0,441.0&gt;--&lt;401.0,441.0&gt;&gt; -&gt; L&lt;&lt;401.0,441.0&gt;--&lt;418.0,441.0&gt;&gt;

* uni2084 (U+2084): L&lt;&lt;399.0,173.0&gt;--&lt;444.0,173.0&gt;&gt; -&gt; L&lt;&lt;444.0,173.0&gt;--&lt;461.0,173.0&gt;&gt;

* uni2573 (U+2573): L&lt;&lt;-13.0,766.0&gt;--&lt;45.0,766.0&gt;&gt; -&gt; L&lt;&lt;45.0,766.0&gt;--&lt;52.0,766.0&gt;&gt;

* uni2778 (U+2778): L&lt;&lt;65.0,359.0&gt;--&lt;65.0,359.0&gt;&gt; -&gt; L&lt;&lt;65.0,359.0&gt;--&lt;65.0,359.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* asciitilde_greater.liga: B&lt;&lt;298.0,457.0&gt;-&lt;313.0,450.0&gt;-&lt;326.0,440.0&gt;&gt;/L&lt;&lt;326.0,440.0&gt;--&lt;193.0,607.0&gt;&gt; = 13.897340070112039

* less_asciitilde.liga: B&lt;&lt;-271.0,262.0&gt;-&lt;-285.0,270.0&gt;-&lt;-299.0,281.0&gt;&gt;/L&lt;&lt;-299.0,281.0&gt;--&lt;-166.0,113.0&gt;&gt; = 13.475288027769414

* less_less_asciitilde.liga: B&lt;&lt;-588.0,262.0&gt;-&lt;-602.0,270.0&gt;-&lt;-616.0,281.0&gt;&gt;/L&lt;&lt;-616.0,281.0&gt;--&lt;-483.0,113.0&gt;&gt; = 13.475288027769414

* trademark (U+2122): L&lt;&lt;404.0,318.0&gt;--&lt;410.0,487.0&gt;&gt;/L&lt;&lt;410.0,487.0&gt;--&lt;374.0,319.0&gt;&gt; = 10.061441407597716

* trademark (U+2122): L&lt;&lt;514.0,318.0&gt;--&lt;548.0,478.0&gt;&gt;/L&lt;&lt;548.0,478.0&gt;--&lt;486.0,318.0&gt;&gt; = 9.18445019234265

* uni20A9 (U+20A9): L&lt;&lt;244.0,712.0&gt;--&lt;190.0,222.0&gt;&gt;/L&lt;&lt;190.0,222.0&gt;--&lt;350.0,712.0&gt;&gt; = 11.794593927621209

* uni20A9 (U+20A9): L&lt;&lt;304.0,-14.0&gt;--&lt;350.0,457.0&gt;&gt;/L&lt;&lt;350.0,457.0&gt;--&lt;197.0,-14.0&gt;&gt; = 12.41783349591187

* uni20A9 (U+20A9): L&lt;&lt;457.0,712.0&gt;--&lt;408.0,221.0&gt;&gt;/L&lt;&lt;408.0,221.0&gt;--&lt;563.0,712.0&gt;&gt; = 11.820944205641307

* uni2116 (U+2116): L&lt;&lt;151.0,-14.0&gt;--&lt;158.0,456.0&gt;&gt;/L&lt;&lt;158.0,456.0&gt;--&lt;57.0,-14.0&gt;&gt; = 11.274775744562644

* uni2116 (U+2116): L&lt;&lt;237.0,712.0&gt;--&lt;232.0,236.0&gt;&gt;/L&lt;&lt;232.0,236.0&gt;--&lt;334.0,712.0&gt;&gt; = 11.492932787650968

* uni24C2 (U+24C2): L&lt;&lt;96.0,103.0&gt;--&lt;158.0,396.0&gt;&gt;/L&lt;&lt;158.0,396.0&gt;--&lt;14.0,104.0&gt;&gt; = 14.302465747931969
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Fur (Latn, 1,230,163 speakers), Mfumte (Latn, 79,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Dan (Latn, 1,099,244 speakers), Dii (Latn, 71,000 speakers), Cicipu (Latn, 44,000 speakers), Mango (Latn, 77,000 speakers), Makaa (Latn, 221,000 speakers), Aghem (Latn, 38,843 speakers), Lugbara (Latn, 2,200,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ekpeye (Latn, 226,000 speakers), Kom (Latn, 360,685 speakers), Dutch (Latn, 31,709,104 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Basaa (Latn, 332,940 speakers), Navajo (Latn, 166,319 speakers), Bete-Bendi (Latn, 100,000 speakers), Igbo (Latn, 27,823,640 speakers), Bafut (Latn, 158,146 speakers), Mundani (Latn, 34,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Nateni (Latn, 100,000 speakers), Ebira (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Sar (Latn, 500,000 speakers), Vute (Latn, 21,000 speakers), South Central Banda (Latn, 244,000 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Zapotec (Latn, 490,000 speakers), Ma’di (Latn, 584,000 speakers).</p>
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
<li>U+02C7 CARON: try adding one of: yi, canadian-aboriginal, tifinagh</li>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, coptic, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, canadian-aboriginal, math, malayalam, coptic, syriac, tifinagh, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: math, greek, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, greek, elbasan</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, greek, yi</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, arabic, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
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
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
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
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, chinese-hongkong, chinese-traditional, japanese, yi, phags-pa</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, chinese-hongkong, chinese-traditional, japanese, yi, phags-pa</li>
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







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1036, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 392, but got 378 instead</p>
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
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* ampersand (U+0026): X=370.0,Y=-1.0 (should be at baseline 0?)

* bracketleft (U+005B): X=466.0,Y=700.0 (should be at cap-height 699?)

* bracketleft (U+005B): X=332.0,Y=700.0 (should be at cap-height 699?)

* bracketright (U+005D): X=286.0,Y=700.0 (should be at cap-height 699?)

* bracketright (U+005D): X=152.0,Y=700.0 (should be at cap-height 699?)

* a (U+0061): X=375.0,Y=2.0 (should be at baseline 0?)

* f (U+0066): X=323.0,Y=698.0 (should be at cap-height 699?)

* h (U+0068): X=482.0,Y=522.0 (should be at x-height 524?)

* n (U+006E): X=482.0,Y=522.0 (should be at x-height 524?)

* p (U+0070): X=256.0,Y=2.0 (should be at baseline 0?)

* t (U+0074): X=573.0,Y=1.0 (should be at baseline 0?)

* braceleft (U+007B): X=474.0,Y=700.0 (should be at cap-height 699?)

* braceleft (U+007B): X=397.0,Y=700.0 (should be at cap-height 699?)

* braceright (U+007D): X=221.0,Y=700.0 (should be at cap-height 699?)

* braceright (U+007D): X=144.0,Y=700.0 (should be at cap-height 699?)

* sterling (U+00A3): X=218.5,Y=699.5 (should be at cap-height 699?)

* degree (U+00B0): X=213.0,Y=700.5 (should be at cap-height 699?)

* degree (U+00B0): X=407.5,Y=700.5 (should be at cap-height 699?)

* uni00B5 (U+00B5): X=441.0,Y=-1.0 (should be at baseline 0?)

* onehalf (U+00BD): X=333.0,Y=1.0 (should be at baseline 0?)

* agrave (U+00E0): X=375.0,Y=2.0 (should be at baseline 0?)

* aacute (U+00E1): X=375.0,Y=2.0 (should be at baseline 0?)

* acircumflex (U+00E2): X=375.0,Y=2.0 (should be at baseline 0?)

* atilde (U+00E3): X=375.0,Y=2.0 (should be at baseline 0?)

* adieresis (U+00E4): X=375.0,Y=2.0 (should be at baseline 0?)

* aring (U+00E5): X=375.0,Y=2.0 (should be at baseline 0?)

* aring (U+00E5): X=336.0,Y=698.0 (should be at cap-height 699?)

* ae (U+00E6): X=100.0,Y=1.0 (should be at baseline 0?)

* thorn (U+00FE): X=255.0,Y=2.0 (should be at baseline 0?)

* amacron (U+0101): X=375.0,Y=2.0 (should be at baseline 0?)

* abreve (U+0103): X=375.0,Y=2.0 (should be at baseline 0?)

* aogonek (U+0105): X=375.0,Y=2.0 (should be at baseline 0?)

* uni0122 (U+0122): X=374.0,Y=-251.5 (should be at descender -250?)

* uni0136 (U+0136): X=400.0,Y=-251.5 (should be at descender -250?)

* uni0137 (U+0137): X=414.0,Y=-251.5 (should be at descender -250?)

* uni013B (U+013B): X=406.0,Y=-251.5 (should be at descender -250?)

* uni013C (U+013C): X=397.0,Y=-251.5 (should be at descender -250?)

* uni0145 (U+0145): X=368.0,Y=-251.5 (should be at descender -250?)

* uni0146 (U+0146): X=377.0,Y=-251.5 (should be at descender -250?)

* uni0156 (U+0156): X=388.0,Y=-251.5 (should be at descender -250?)

* uni0157 (U+0157): X=225.0,Y=-251.5 (should be at descender -250?)

* tcaron (U+0165): X=573.0,Y=1.0 (should be at baseline 0?)

* uring (U+016F): X=336.0,Y=698.0 (should be at cap-height 699?)

* uni01CE (U+01CE): X=375.0,Y=2.0 (should be at baseline 0?)

* uni0218 (U+0218): X=383.0,Y=-251.5 (should be at descender -250?)

* uni0219 (U+0219): X=372.0,Y=-251.5 (should be at descender -250?)

* uni021A (U+021A): X=368.0,Y=-251.5 (should be at descender -250?)

* uni021B (U+021B): X=573.0,Y=1.0 (should be at baseline 0?)

* uni021B (U+021B): X=455.0,Y=-251.5 (should be at descender -250?)

* ring (U+02DA): X=309.0,Y=698.0 (should be at cap-height 699?)

* uni030A (U+030A): X=309.0,Y=698.0 (should be at cap-height 699?)

* uni0326 (U+0326): X=342.0,Y=-251.5 (should be at descender -250?)

* uni1E9E (U+1E9E): X=475.0,Y=-1.0 (should be at baseline 0?)

* uni1E9E (U+1E9E): X=277.0,Y=-1.0 (should be at baseline 0?)

* uni1E9E (U+1E9E): X=265.0,Y=1.0 (should be at baseline 0?)

* uni2085 (U+2085): X=202.0,Y=2.0 (should be at baseline 0?)

* uni2087 (U+2087): X=309.0,Y=1.0 (should be at baseline 0?)

* colonmonetary (U+20A1): X=210.5,Y=697.5 (should be at cap-height 699?)

* colonmonetary (U+20A1): X=456.0,Y=701.0 (should be at cap-height 699?)

* lira (U+20A4): X=218.5,Y=699.5 (should be at cap-height 699?)

* uni20BE (U+20BE): X=436.0,Y=701.0 (should be at cap-height 699?)

* uni2113 (U+2113): X=446.0,Y=698.5 (should be at cap-height 699?)

* integral (U+222B): X=169.0,Y=2.0 (should be at baseline 0?)

* uni250A (U+250A): X=260.0,Y=-2.0 (should be at baseline 0?)

* uni250A (U+250A): X=358.0,Y=-2.0 (should be at baseline 0?)

* uni250B (U+250B): X=242.0,Y=-2.0 (should be at baseline 0?)

* uni250B (U+250B): X=376.0,Y=-2.0 (should be at baseline 0?)

* uni301A (U+301A): X=516.0,Y=700.0 (should be at cap-height 699?)

* uni301A (U+301A): X=412.0,Y=700.0 (should be at cap-height 699?)

* uni301A (U+301A): X=272.0,Y=700.0 (should be at cap-height 699?)

* uni301A (U+301A): X=312.0,Y=700.0 (should be at cap-height 699?)

* uni301B (U+301B): X=206.0,Y=700.0 (should be at cap-height 699?)

* uni301B (U+301B): X=102.0,Y=700.0 (should be at cap-height 699?)

* uni301B (U+301B): X=346.0,Y=700.0 (should be at cap-height 699?)

* uni301B (U+301B): X=306.0,Y=700.0 (should be at cap-height 699?)

* usdc (U+E000): X=249.0,Y=698.0 (should be at cap-height 699?)

* usdc (U+E000): X=265.0,Y=701.0 (should be at cap-height 699?)

* usdc (U+E000): X=355.0,Y=701.0 (should be at cap-height 699?)

* usdc (U+E000): X=371.0,Y=698.0 (should be at cap-height 699?)

* uni0157.ss02: X=262.0,Y=-251.5 (should be at descender -250?)

* uni013C.ss04: X=458.0,Y=-251.5 (should be at descender -250?)

* uni013C.ss06: X=369.0,Y=-251.5 (should be at descender -250?)

* uni0123.sc: X=372.0,Y=-251.5 (should be at descender -250?)

* uni0137.sc: X=369.0,Y=-251.5 (should be at descender -250?)

* uni013C.sc: X=381.0,Y=-251.5 (should be at descender -250?)

* uni0146.sc: X=368.0,Y=-251.5 (should be at descender -250?)

* uni0157.sc: X=386.0,Y=-251.5 (should be at descender -250?)

* uni0219.sc: X=368.0,Y=-251.5 (should be at descender -250?)

* germandbls.sc: X=272.0,Y=1.0 (should be at baseline 0?)

* uni021B.sc: X=368.0,Y=-251.5 (should be at descender -250?)

* zero.zero: X=429.5,Y=1.5 (should be at baseline 0?)

* zero.zero: X=188.5,Y=1.0 (should be at baseline 0?)

* braceleft_bar.liga: X=-104.0,Y=700.0 (should be at cap-height 699?)

* braceleft_bar.liga: X=-181.0,Y=700.0 (should be at cap-height 699?)

* bracketleft_bar.liga: X=-102.0,Y=700.0 (should be at cap-height 699?)

* bracketleft_bar.liga: X=-236.0,Y=700.0 (should be at cap-height 699?)

* bar_braceright.liga: X=171.0,Y=700.0 (should be at cap-height 699?)

* bar_braceright.liga: X=94.0,Y=700.0 (should be at cap-height 699?)

* bar_bracketright.liga: X=236.0,Y=700.0 (should be at cap-height 699?)

* bar_bracketright.liga: X=102.0,Y=700.0 (should be at cap-height 699?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* Ccedilla (U+00C7): L&lt;&lt;355.0,26.0&gt;--&lt;363.0,26.0&gt;&gt; -&gt; L&lt;&lt;363.0,26.0&gt;--&lt;405.0,26.0&gt;&gt;

* Ccedilla (U+00C7): L&lt;&lt;363.0,26.0&gt;--&lt;405.0,26.0&gt;&gt; -&gt; L&lt;&lt;405.0,26.0&gt;--&lt;427.0,25.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;346.0,26.0&gt;--&lt;354.0,26.0&gt;&gt; -&gt; L&lt;&lt;354.0,26.0&gt;--&lt;396.0,26.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;354.0,26.0&gt;--&lt;396.0,26.0&gt;&gt; -&gt; L&lt;&lt;396.0,26.0&gt;--&lt;418.0,25.0&gt;&gt;

* ccedilla (U+00E7): L&lt;&lt;343.0,26.0&gt;--&lt;351.0,26.0&gt;&gt; -&gt; L&lt;&lt;351.0,26.0&gt;--&lt;393.0,26.0&gt;&gt;

* ccedilla (U+00E7): L&lt;&lt;351.0,26.0&gt;--&lt;393.0,26.0&gt;&gt; -&gt; L&lt;&lt;393.0,26.0&gt;--&lt;415.0,25.0&gt;&gt;

* ccedilla.sc: L&lt;&lt;331.0,26.0&gt;--&lt;339.0,26.0&gt;&gt; -&gt; L&lt;&lt;339.0,26.0&gt;--&lt;381.0,26.0&gt;&gt;

* ccedilla.sc: L&lt;&lt;339.0,26.0&gt;--&lt;381.0,26.0&gt;&gt; -&gt; L&lt;&lt;381.0,26.0&gt;--&lt;403.0,25.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;320.0,26.0&gt;--&lt;328.0,26.0&gt;&gt; -&gt; L&lt;&lt;328.0,26.0&gt;--&lt;370.0,26.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;328.0,26.0&gt;--&lt;370.0,26.0&gt;&gt; -&gt; L&lt;&lt;370.0,26.0&gt;--&lt;392.0,25.0&gt;&gt;

* equal_exclam_equal.liga: L&lt;&lt;-277.0,184.0&gt;--&lt;-329.0,184.0&gt;&gt; -&gt; L&lt;&lt;-329.0,184.0&gt;--&lt;-341.0,184.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;341.0,184.0&gt;--&lt;289.0,184.0&gt;&gt; -&gt; L&lt;&lt;289.0,184.0&gt;--&lt;277.0,184.0&gt;&gt;

* exclam_exclam.liga: L&lt;&lt;-197.0,184.0&gt;--&lt;-249.0,184.0&gt;&gt; -&gt; L&lt;&lt;-249.0,184.0&gt;--&lt;-261.0,184.0&gt;&gt;

* exclam_exclam.liga: L&lt;&lt;261.0,184.0&gt;--&lt;209.0,184.0&gt;&gt; -&gt; L&lt;&lt;209.0,184.0&gt;--&lt;197.0,184.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;212.0,184.0&gt;--&lt;160.0,184.0&gt;&gt; -&gt; L&lt;&lt;160.0,184.0&gt;--&lt;148.0,184.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;470.0,184.0&gt;--&lt;418.0,184.0&gt;&gt; -&gt; L&lt;&lt;418.0,184.0&gt;--&lt;406.0,184.0&gt;&gt;

* less_exclam_hyphen_hyphen.liga: L&lt;&lt;-799.0,184.0&gt;--&lt;-851.0,184.0&gt;&gt; -&gt; L&lt;&lt;-851.0,184.0&gt;--&lt;-863.0,184.0&gt;&gt;

* scedilla (U+015F): L&lt;&lt;335.0,26.0&gt;--&lt;343.0,26.0&gt;&gt; -&gt; L&lt;&lt;343.0,26.0&gt;--&lt;385.0,26.0&gt;&gt;

* scedilla (U+015F): L&lt;&lt;343.0,26.0&gt;--&lt;385.0,26.0&gt;&gt; -&gt; L&lt;&lt;385.0,26.0&gt;--&lt;407.0,25.0&gt;&gt;

* scedilla.sc: L&lt;&lt;331.0,26.0&gt;--&lt;339.0,26.0&gt;&gt; -&gt; L&lt;&lt;339.0,26.0&gt;--&lt;381.0,26.0&gt;&gt;

* scedilla.sc: L&lt;&lt;339.0,26.0&gt;--&lt;381.0,26.0&gt;&gt; -&gt; L&lt;&lt;381.0,26.0&gt;--&lt;403.0,25.0&gt;&gt;

* uni0327 (U+0327): L&lt;&lt;320.0,26.0&gt;--&lt;328.0,26.0&gt;&gt; -&gt; L&lt;&lt;328.0,26.0&gt;--&lt;370.0,26.0&gt;&gt;

* uni0327 (U+0327): L&lt;&lt;328.0,26.0&gt;--&lt;370.0,26.0&gt;&gt; -&gt; L&lt;&lt;370.0,26.0&gt;--&lt;392.0,25.0&gt;&gt;

* uni2573 (U+2573): L&lt;&lt;-13.0,766.0&gt;--&lt;45.0,766.0&gt;&gt; -&gt; L&lt;&lt;45.0,766.0&gt;--&lt;52.0,766.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* trademark (U+2122): L&lt;&lt;392.0,319.0&gt;--&lt;362.0,487.0&gt;&gt;/L&lt;&lt;362.0,487.0&gt;--&lt;362.0,318.0&gt;&gt; = 10.124671655397806

* trademark (U+2122): L&lt;&lt;502.0,318.0&gt;--&lt;502.0,484.0&gt;&gt;/L&lt;&lt;502.0,484.0&gt;--&lt;473.0,319.0&gt;&gt; = 9.968356170473816

* uni20A9 (U+20A9): L&lt;&lt;150.0,713.0&gt;--&lt;201.0,219.0&gt;&gt;/L&lt;&lt;201.0,219.0&gt;--&lt;257.0,712.0&gt;&gt; = 12.374735641963783

* uni20A9 (U+20A9): L&lt;&lt;363.0,712.0&gt;--&lt;420.0,219.0&gt;&gt;/L&lt;&lt;420.0,219.0&gt;--&lt;470.0,713.0&gt;&gt; = 12.374663780471206

* uni20A9 (U+20A9): L&lt;&lt;364.0,-13.0&gt;--&lt;310.0,460.0&gt;&gt;/L&lt;&lt;310.0,460.0&gt;--&lt;256.0,-13.0&gt;&gt; = 13.025938061958893

* uni2116 (U+2116): L&lt;&lt;140.0,712.0&gt;--&lt;236.0,249.0&gt;&gt;/L&lt;&lt;236.0,249.0&gt;--&lt;236.0,712.0&gt;&gt; = 11.713919247283782

* uni2116 (U+2116): L&lt;&lt;209.0,-14.0&gt;--&lt;116.0,443.0&gt;&gt;/L&lt;&lt;116.0,443.0&gt;--&lt;116.0,-14.0&gt;&gt; = 11.502684579531886
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* Aacute (U+00C1): L&lt;&lt;380.0,928.0&gt;--&lt;533.0,929.0&gt;&gt;

* Agrave (U+00C0): L&lt;&lt;147.0,929.0&gt;--&lt;300.0,928.0&gt;&gt;

* Cacute (U+0106): L&lt;&lt;405.0,928.0&gt;--&lt;558.0,929.0&gt;&gt;

* Eacute (U+00C9): L&lt;&lt;384.0,928.0&gt;--&lt;537.0,929.0&gt;&gt;

* Egrave (U+00C8): L&lt;&lt;151.0,929.0&gt;--&lt;304.0,928.0&gt;&gt;

* Iacute (U+00CD): L&lt;&lt;376.0,928.0&gt;--&lt;529.0,929.0&gt;&gt;

* Igrave (U+00CC): L&lt;&lt;143.0,929.0&gt;--&lt;296.0,928.0&gt;&gt;

* Lacute (U+0139): L&lt;&lt;238.0,928.0&gt;--&lt;391.0,929.0&gt;&gt;

* Nacute (U+0143): L&lt;&lt;376.0,928.0&gt;--&lt;529.0,929.0&gt;&gt;

* Oacute (U+00D3): L&lt;&lt;376.0,928.0&gt;--&lt;529.0,929.0&gt;&gt;

* Ograve (U+00D2): L&lt;&lt;143.0,929.0&gt;--&lt;296.0,928.0&gt;&gt;

* Ohungarumlaut (U+0150): L&lt;&lt;296.0,930.0&gt;--&lt;449.0,931.0&gt;&gt;

* Ohungarumlaut (U+0150): L&lt;&lt;469.0,928.0&gt;--&lt;622.0,929.0&gt;&gt;

* Racute (U+0154): L&lt;&lt;383.0,928.0&gt;--&lt;536.0,929.0&gt;&gt;

* Sacute (U+015A): L&lt;&lt;385.0,928.0&gt;--&lt;538.0,929.0&gt;&gt;

* Uacute (U+00DA): L&lt;&lt;376.0,928.0&gt;--&lt;529.0,929.0&gt;&gt;

* Ugrave (U+00D9): L&lt;&lt;143.0,929.0&gt;--&lt;296.0,928.0&gt;&gt;

* Uhungarumlaut (U+0170): L&lt;&lt;296.0,930.0&gt;--&lt;449.0,931.0&gt;&gt;

* Uhungarumlaut (U+0170): L&lt;&lt;469.0,928.0&gt;--&lt;622.0,929.0&gt;&gt;

* Wacute (U+1E82): L&lt;&lt;392.0,928.0&gt;--&lt;545.0,929.0&gt;&gt;

* Wgrave (U+1E80): L&lt;&lt;159.0,929.0&gt;--&lt;312.0,928.0&gt;&gt;

* Yacute (U+00DD): L&lt;&lt;386.0,928.0&gt;--&lt;539.0,929.0&gt;&gt;

* Ygrave (U+1EF2): L&lt;&lt;153.0,929.0&gt;--&lt;306.0,928.0&gt;&gt;

* Zacute (U+0179): L&lt;&lt;383.0,928.0&gt;--&lt;536.0,929.0&gt;&gt;

* aacute (U+00E1): L&lt;&lt;376.0,753.0&gt;--&lt;529.0,754.0&gt;&gt;

* aacute.sc: L&lt;&lt;382.0,812.0&gt;--&lt;535.0,813.0&gt;&gt;

* acute (U+00B4): L&lt;&lt;350.0,753.0&gt;--&lt;503.0,754.0&gt;&gt;

* acutecomb (U+0301): L&lt;&lt;350.0,753.0&gt;--&lt;503.0,754.0&gt;&gt;

* agrave (U+00E0): L&lt;&lt;143.0,754.0&gt;--&lt;296.0,753.0&gt;&gt;

* agrave.sc: L&lt;&lt;149.0,813.0&gt;--&lt;302.0,812.0&gt;&gt;

* asciicircum (U+005E): L&lt;&lt;172.0,306.0&gt;--&lt;53.0,305.0&gt;&gt;

* cacute (U+0107): L&lt;&lt;388.0,753.0&gt;--&lt;541.0,754.0&gt;&gt;

* cacute.sc: L&lt;&lt;376.0,812.0&gt;--&lt;529.0,813.0&gt;&gt;

* eacute (U+00E9): L&lt;&lt;380.0,753.0&gt;--&lt;533.0,754.0&gt;&gt;

* eacute.sc: L&lt;&lt;376.0,812.0&gt;--&lt;529.0,813.0&gt;&gt;

* egrave (U+00E8): L&lt;&lt;147.0,754.0&gt;--&lt;300.0,753.0&gt;&gt;

* egrave.sc: L&lt;&lt;143.0,813.0&gt;--&lt;296.0,812.0&gt;&gt;

* grave (U+0060): L&lt;&lt;117.0,754.0&gt;--&lt;270.0,753.0&gt;&gt;

* gravecomb (U+0300): L&lt;&lt;117.0,754.0&gt;--&lt;270.0,753.0&gt;&gt;

* guillemotright (U+00BB): L&lt;&lt;320.0,46.0&gt;--&lt;319.0,174.0&gt;&gt;

* guillemotright (U+00BB): L&lt;&lt;58.0,397.0&gt;--&lt;59.0,528.0&gt;&gt;

* guilsinglleft (U+2039): L&lt;&lt;460.0,173.0&gt;--&lt;459.0,50.0&gt;&gt;

* guilsinglright (U+203A): L&lt;&lt;158.0,401.0&gt;--&lt;159.0,524.0&gt;&gt;

* guilsinglright (U+203A): L&lt;&lt;158.0,50.0&gt;--&lt;159.0,171.0&gt;&gt;

* hungarumlaut (U+02DD): L&lt;&lt;270.0,755.0&gt;--&lt;423.0,756.0&gt;&gt;

* hungarumlaut (U+02DD): L&lt;&lt;443.0,753.0&gt;--&lt;596.0,754.0&gt;&gt;

* iacute (U+00ED): L&lt;&lt;396.0,753.0&gt;--&lt;549.0,754.0&gt;&gt;

* iacute.sc: L&lt;&lt;376.0,812.0&gt;--&lt;529.0,813.0&gt;&gt;

* iacute.ss03: L&lt;&lt;371.0,753.0&gt;--&lt;524.0,754.0&gt;&gt;

* iacute.ss05: L&lt;&lt;377.0,753.0&gt;--&lt;530.0,754.0&gt;&gt;

* igrave (U+00EC): L&lt;&lt;163.0,754.0&gt;--&lt;316.0,753.0&gt;&gt;

* igrave.sc: L&lt;&lt;143.0,813.0&gt;--&lt;296.0,812.0&gt;&gt;

* igrave.ss03: L&lt;&lt;138.0,754.0&gt;--&lt;291.0,753.0&gt;&gt;

* igrave.ss05: L&lt;&lt;144.0,754.0&gt;--&lt;297.0,753.0&gt;&gt;

* lacute (U+013A): L&lt;&lt;406.0,958.0&gt;--&lt;559.0,959.0&gt;&gt;

* lacute.sc: L&lt;&lt;226.0,812.0&gt;--&lt;379.0,813.0&gt;&gt;

* lacute.ss04: L&lt;&lt;370.0,958.0&gt;--&lt;523.0,959.0&gt;&gt;

* lacute.ss06: L&lt;&lt;377.0,958.0&gt;--&lt;530.0,959.0&gt;&gt;

* less_bar_greater.liga: L&lt;&lt;-179.0,-44.0&gt;--&lt;-180.0,72.0&gt;&gt;

* less_bar_greater.liga: L&lt;&lt;-179.0,628.0&gt;--&lt;-180.0,743.0&gt;&gt;

* less_bar_greater.liga: L&lt;&lt;-435.0,71.0&gt;--&lt;-436.0,-44.0&gt;&gt;

* less_bar_greater.liga: L&lt;&lt;-435.0,743.0&gt;--&lt;-436.0,627.0&gt;&gt;

* less_equal.liga: L&lt;&lt;-341.0,388.0&gt;--&lt;-340.0,517.0&gt;&gt;

* nacute (U+0144): L&lt;&lt;389.0,753.0&gt;--&lt;542.0,754.0&gt;&gt;

* nacute.sc: L&lt;&lt;376.0,812.0&gt;--&lt;529.0,813.0&gt;&gt;

* oacute (U+00F3): L&lt;&lt;376.0,753.0&gt;--&lt;529.0,754.0&gt;&gt;

* oacute.sc: L&lt;&lt;376.0,812.0&gt;--&lt;529.0,813.0&gt;&gt;

* ograve (U+00F2): L&lt;&lt;143.0,754.0&gt;--&lt;296.0,753.0&gt;&gt;

* ograve.sc: L&lt;&lt;143.0,813.0&gt;--&lt;296.0,812.0&gt;&gt;

* ohungarumlaut (U+0151): L&lt;&lt;296.0,755.0&gt;--&lt;449.0,756.0&gt;&gt;

* ohungarumlaut (U+0151): L&lt;&lt;469.0,753.0&gt;--&lt;622.0,754.0&gt;&gt;

* ohungarumlaut.sc: L&lt;&lt;296.0,814.0&gt;--&lt;449.0,815.0&gt;&gt;

* ohungarumlaut.sc: L&lt;&lt;469.0,812.0&gt;--&lt;622.0,813.0&gt;&gt;

* racute (U+0155): L&lt;&lt;416.0,753.0&gt;--&lt;569.0,754.0&gt;&gt;

* racute.sc: L&lt;&lt;376.0,812.0&gt;--&lt;529.0,813.0&gt;&gt;

* racute.ss02: L&lt;&lt;427.0,753.0&gt;--&lt;580.0,754.0&gt;&gt;

* sacute (U+015B): L&lt;&lt;379.0,753.0&gt;--&lt;532.0,754.0&gt;&gt;

* sacute.sc: L&lt;&lt;376.0,812.0&gt;--&lt;529.0,813.0&gt;&gt;

* u1F150 (U+1F150): L&lt;&lt;60.0,290.0&gt;--&lt;-58.0,289.0&gt;&gt;

* u1F169 (U+1F169): L&lt;&lt;-149.0,536.0&gt;--&lt;125.0,537.0&gt;&gt;

* uacute (U+00FA): L&lt;&lt;376.0,753.0&gt;--&lt;529.0,754.0&gt;&gt;

* uacute.sc: L&lt;&lt;376.0,812.0&gt;--&lt;529.0,813.0&gt;&gt;

* ugrave (U+00F9): L&lt;&lt;143.0,754.0&gt;--&lt;296.0,753.0&gt;&gt;

* ugrave.sc: L&lt;&lt;143.0,813.0&gt;--&lt;296.0,812.0&gt;&gt;

* uhungarumlaut (U+0171): L&lt;&lt;296.0,755.0&gt;--&lt;449.0,756.0&gt;&gt;

* uhungarumlaut (U+0171): L&lt;&lt;469.0,753.0&gt;--&lt;622.0,754.0&gt;&gt;

* uhungarumlaut.sc: L&lt;&lt;296.0,814.0&gt;--&lt;449.0,815.0&gt;&gt;

* uhungarumlaut.sc: L&lt;&lt;469.0,812.0&gt;--&lt;622.0,813.0&gt;&gt;

* uni030B (U+030B): L&lt;&lt;270.0,755.0&gt;--&lt;423.0,756.0&gt;&gt;

* uni030B (U+030B): L&lt;&lt;443.0,753.0&gt;--&lt;596.0,754.0&gt;&gt;

* uni20A6 (U+20A6): L&lt;&lt;514.0,-14.0&gt;--&lt;392.0,-13.0&gt;&gt;

* uni20B9 (U+20B9): L&lt;&lt;577.0,-14.0&gt;--&lt;419.0,-13.0&gt;&gt;

* uni25B6 (U+25B6): L&lt;&lt;21.0,5.0&gt;--&lt;20.0,693.0&gt;&gt;

* uni25B7 (U+25B7): L&lt;&lt;21.0,5.0&gt;--&lt;20.0,693.0&gt;&gt;

* uni2779 (U+2779): L&lt;&lt;42.0,522.0&gt;--&lt;41.0,282.0&gt;&gt;

* uniE0B1 (U+E0B1): L&lt;&lt;-13.0,-310.0&gt;--&lt;-12.0,-172.0&gt;&gt;

* uniE0B3 (U+E0B3): L&lt;&lt;633.0,-172.0&gt;--&lt;632.0,-310.0&gt;&gt;

* wacute (U+1E83): L&lt;&lt;394.0,753.0&gt;--&lt;547.0,754.0&gt;&gt;

* wacute.sc: L&lt;&lt;379.0,812.0&gt;--&lt;532.0,813.0&gt;&gt;

* wgrave (U+1E81): L&lt;&lt;161.0,754.0&gt;--&lt;314.0,753.0&gt;&gt;

* wgrave.sc: L&lt;&lt;146.0,813.0&gt;--&lt;299.0,812.0&gt;&gt;

* yacute (U+00FD): L&lt;&lt;382.0,753.0&gt;--&lt;535.0,754.0&gt;&gt;

* yacute.sc: L&lt;&lt;386.0,812.0&gt;--&lt;539.0,813.0&gt;&gt;

* ygrave (U+1EF3): L&lt;&lt;149.0,754.0&gt;--&lt;302.0,753.0&gt;&gt;

* ygrave.sc: L&lt;&lt;153.0,813.0&gt;--&lt;306.0,812.0&gt;&gt;

* zacute (U+017A): L&lt;&lt;380.0,753.0&gt;--&lt;533.0,754.0&gt;&gt;

* zacute.sc: L&lt;&lt;376.0,812.0&gt;--&lt;529.0,813.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Fur (Latn, 1,230,163 speakers), Mfumte (Latn, 79,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Dan (Latn, 1,099,244 speakers), Dii (Latn, 71,000 speakers), Cicipu (Latn, 44,000 speakers), Mango (Latn, 77,000 speakers), Makaa (Latn, 221,000 speakers), Aghem (Latn, 38,843 speakers), Lugbara (Latn, 2,200,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ekpeye (Latn, 226,000 speakers), Kom (Latn, 360,685 speakers), Dutch (Latn, 31,709,104 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Basaa (Latn, 332,940 speakers), Navajo (Latn, 166,319 speakers), Bete-Bendi (Latn, 100,000 speakers), Igbo (Latn, 27,823,640 speakers), Bafut (Latn, 158,146 speakers), Mundani (Latn, 34,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Nateni (Latn, 100,000 speakers), Ebira (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Sar (Latn, 500,000 speakers), Vute (Latn, 21,000 speakers), South Central Banda (Latn, 244,000 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Zapotec (Latn, 490,000 speakers), Ma’di (Latn, 584,000 speakers).</p>
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
<li>U+02C7 CARON: try adding one of: yi, canadian-aboriginal, tifinagh</li>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, coptic, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, canadian-aboriginal, math, malayalam, coptic, syriac, tifinagh, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: math, greek, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, greek, elbasan</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, greek, yi</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, arabic, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
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
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
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
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, chinese-hongkong, chinese-traditional, japanese, yi, phags-pa</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, chinese-hongkong, chinese-traditional, japanese, yi, phags-pa</li>
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







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1036, but got 1022 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 392, but got 378 instead</p>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Fur (Latn, 1,230,163 speakers), Mfumte (Latn, 79,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Dan (Latn, 1,099,244 speakers), Dii (Latn, 71,000 speakers), Cicipu (Latn, 44,000 speakers), Mango (Latn, 77,000 speakers), Makaa (Latn, 221,000 speakers), Aghem (Latn, 38,843 speakers), Lugbara (Latn, 2,200,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ekpeye (Latn, 226,000 speakers), Kom (Latn, 360,685 speakers), Dutch (Latn, 31,709,104 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Basaa (Latn, 332,940 speakers), Navajo (Latn, 166,319 speakers), Bete-Bendi (Latn, 100,000 speakers), Igbo (Latn, 27,823,640 speakers), Bafut (Latn, 158,146 speakers), Mundani (Latn, 34,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Nateni (Latn, 100,000 speakers), Ebira (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Sar (Latn, 500,000 speakers), Vute (Latn, 21,000 speakers), South Central Banda (Latn, 244,000 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Zapotec (Latn, 490,000 speakers), Ma’di (Latn, 584,000 speakers).</p>
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
<li>U+02C7 CARON: try adding one of: yi, canadian-aboriginal, tifinagh</li>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, coptic, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, canadian-aboriginal, math, malayalam, coptic, syriac, tifinagh, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: math, greek, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, greek, elbasan</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, greek, yi</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, arabic, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
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
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
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
<li>U+301A LEFT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, chinese-hongkong, chinese-traditional, japanese, yi, phags-pa</li>
<li>U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: chinese-simplified, chinese-hongkong, chinese-traditional, japanese, yi, phags-pa</li>
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
| 0 | 0 | 27 | 51 | 455 | 27 | 378 | 0 | 
| 0% | 0% | 3% | 5% | 49% | 3% | 40% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
