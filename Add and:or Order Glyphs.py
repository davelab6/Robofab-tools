# add and/or order all glyphs - Quinn Keaveney
f = CurrentFont()

# My glyphs
f.glyphOrder = ['T.sc|', 'aring|å', 'utilde|ũ', 'ldotbelowmacron|ḹ', 'plus.sinf|', 'I.sc|', 'Hcircumflex|Ĥ', 'multiply.ordn|', 'dollar|$', 'four|4', 'ddotbelow|ḍ', 'uni25A3|▣', 'Kcedilla|', 'Yacute|Ý', 'linebelow.cap|', 'minus.subs|', 'obreve|ŏ', 'Ygrave|Ỳ', 'uni2198|↘', 'quotedblright|”', 'kcommaaccent|ķ', 'integral|∫', 'g.sinf|', 's.sinf|', 'ccaron|č', 'anglebracketleft.sc|', 'Tdotbelow.sc|', 'Ldotbelowmacron|Ḹ', 'N.sc|', 'one.sups|¹', 'doublegrave.cap|', 'Euro|€', 'copyright.cap|', 'E.sc|', 'slash|/', 'circumflex.cap|', 'period.ordn|', 'zero.subs|₀', 'ocaron|ǒ', 'dollar.LP|', 'P|P', 'acute.cap|', 'lcedilla|', 'questiondown.sc|', 'AEmacron|Ǣ', 'guillemotleft|«', 'Egrave.sc|', 'Ograve.sc|', 'Khook.sc|', 'uni25A1|□', 'adieresismacron|ǟ', 'Aogonek.sc|', 'uni25A0|■', 'uni25C0|◀', 'less.LP|', 'Rcedilla|', 'n.sups|ⁿ', 'six.sinf|', 'amacron|ā', 'p|p', 'Sacute.sc|', 'Ezh|Ʒ', 'jcaron|ǰ', 'o.sups|', 'four.OT|', 'commaabovecmb|̓', 'H.sc|', 'exclamdown.sc|', 'exclamdown.cap|', 'Kcommaaccent|Ķ', 'Ddotbelow.sc|', 'Obreve.sc|', 'Otilde|Õ', 'Agrave.sc|', 'perthousand|‰', 'sdotbelow|ṣ', 'barredO|Ɵ', 'divide.ordn|', 'equal|=', 'dotlessj|ȷ', 'dotlessi|ı', 'Scaron|Š', 'd.sups|', 'one.LP|', 'tdotbelow|ṭ', 'egrave|è', 'ccedilla|ç', 'one.LT|', 'Dcaron.sc|', 'kcaron|ǩ', 'Iacute.sc|', 'parenleft.subs|₍', 'section|§', 'Cacute|Ć', 'ring.cap|', 'Olinebelow.sc|', 'Icircumflex|Î', 'comma.sups|', 'ntilde|ñ', 'barredo|ɵ', 'Ytilde.sc|', 'Wdieresis.sc|', 'lessequal|≤', 'Hbar.sc|', 'gcommaaccent|ģ', 'three.sups|³', 'nine.subs|₉', 'degree|°', 'bracketright.sc|', 'K|K', 'punctuationspace| ', 'Zdotaccent.sc|', 'Ainvertedbreve|Ȃ', 'emspace| ', 'acircumflex|â', 'Eogonek.sc|', 'Uhungarumlaut|Ű', 'Aring|Å', 'two.OT|', 'Cdotaccent|Ċ', 'sterling.LP|', 'Oogonekmacron.sc|', 'k|k', 'Rcaron|Ř', 'equal.LP|', 'ndotaccent|ṅ', 'two.subs|₂', 'Agrave|À', 'published|', 'uni2191|↑', 'Ldot|Ŀ', 'Edotaccent|Ė', 'Abreve|Ă', 'uni25E5|◥', 'uni25E4|◤', 'Einvertedbreve|Ȇ', 'divide|÷', 'uni25E3|◣', 'uni25E2|◢', 'ocircumflex|ô', 'rcedilla|', 'comma.subs|', 'Hdotbelow.sc|', 'asciitilde|~', 'nine.sups|⁹', 'Lacute|Ĺ', 'Iinvertedbreve.sc|', 'summation|∑', 'Adotaccent.sc|', 'Gdotaccent.sc|', 'iinvertedbreve|ȋ', 'Racute.sc|', 'Gdotaccent|Ġ', 'Gbreve|Ğ', 'guillemotright.sc|', 'odotbelow|ọ', 'parenleft.cap|', 'two|2', 'dcaron|ď', 'divide.sinf|', 'ogonek.cap|', 'estimated|℮', 'odotaccentmacron|ȱ', 'rdotbelow|ṛ', 'a.sups|', 'E|E', 'scaron|š', 'plus.subs|', 'quotesinglbase|‚', 'F|F', 'dotaccent.cap|', 'K.sc|', 'zero.LP|', 'five.LP|', 'bracketleft|[', 'c_t|', 'V|V', 'asciicircum|^', 'P.sc|', 'j.sups|', 'm.sups|', 'greaterequal|≥', 'i.sinf|', 'f|f', 'ordmasculine|º', 'X.sc|', 'f_i|ﬁ', 'mu|µ', 'guilsinglleft.sc|', 'paragraph|¶', 'nine|9', 'three|3', 'v|v', 'plus.sups|⁺', 'oe|œ', 'Atilde.sc|', 'copyright.sc|', 'emdash.cap|', 'Eogonek|Ę', 'cdotaccent|ċ', 'Udoublegrave|Ȕ', 'adoublegrave|ȁ', 'mmacron|', 'Tbar.sc|', 'Pmacron.sc|', 'currency|¤', 'Icaron|Ǐ', 'Uring|Ů', 'parenright.cap|', 'Rdotbelowmacron|Ṝ', 'endash.cap|', 'Wcircumflex.sc|', 'litre|ℓ', 'at.cap|', 'minus.ordn|', 'tbar|ŧ', 'e.sups|', 'z.sups|', 'kgreenlandic|ĸ', 'minus.sups|⁻', 'hyphen.sc|', 'lacute|ĺ', 'parenleft.sc|', 'Lcommaaccent.sc|', 'dieresis.cap|', 'ygrave|ỳ', 'A|A', 'product|∏', 'Ntilde.sc|', 'umacron|ū', 'Ecaron.sc|', 'Edoublegrave.sc|', 'Idoublegrave|Ȉ', 'ndotbelow|ṇ', 'ncedilla|', 'Ucaron|Ǔ', 'bracketleft.sc|', 't.sinf|', 'Edieresis.sc|', 'anglebracketright.cap|', 'Eng.sc|', 'Udieresis.sc|', 'a|a', 'Kcommaaccent.sc|', 'fourperemspace| ', 'eng|ŋ', 'infinity.LP|', 'Ngrave.sc|', 'oogonek|ǫ', 'q|q', 'o.sinf|', 'hcaron|ȟ', 'barredO.sc|', 'i.sups|', 'colonmonitary.LP|', 'oacute|ó', 'Utilde.sc|', 'six|6', 'Hmacronbelow|', 'Odotbelow|Ọ', 'ograve|ò', 'Icircumflex.sc|', 'uring|ů', 'D.sc|', 'caron.cap|', 'plus.ordn|', 'comma|,', 'Umacronbelow|', 'X|X', 'Emacron.sc|', 'ogonek|˛', 'bracketright.cap|', 'braceright.sc|', 'Gacute|Ǵ', 'guilsinglright.cap|', 'thinspace| ', 'tilde|˜', 'Scedilla|Ş', 'otilde|õ', 'Gacute.sc|', 'Lacute.sc|', 'gcircumflex|ĝ', 'n.sinf|', 'Ccaron.sc|', 'six.LT|', 'four.LP|', 'Scommaaccent.sc|', 'six.LP|', 'four.LT|', 'section.LP|', 'guillemotright|»', 'ecircumflex|ê', 'greater|>', 'uacute|ú', 'Idotaccent|İ', 'rdotbelowmacron|ṝ', 'L|L', 'numbersign.LP|', 'Gcaron.sc|', 'Idoublegrave.sc|', 'ccircumflex|ĉ', 'dcroat|đ', 'bar|uni007C', 'one|1', 'cedilla|¸', 'Odotbelow.sc|', 'Ecircumflex.sc|', 'omacron|ō', 'Uring.sc|', 'Nacute.sc|', 'one.subs|₁', 'ydieresis|ÿ', 'l|l', 'logicalnot|¬', 'Ncedilla|', 'minus.LP|', 'Sdotbelow|Ṣ', 'ncommaaccent|ņ', 'idoublegrave|ȉ', 'exclamdown|¡', 'four.sinf|', 'minus.sinf|', 'Tdotbelow|Ṭ', 'endash|–', 'commaaccent.cap|', 'Eng|Ŋ', 'Oinvertedbreve|Ȏ', 'Ibreve|Ĭ', 'aeacute|ǽ', 'published.sc|', 'zero.ordn|', 'Gstroke.sc|', 'agrave|à', 'servicemark|℠', 'c.sups|', 'z.sinf|', 'v.sinf|', 'Adieresis|Ä', 'germandbls|ß', 'Odieresis|Ö', 'space| ', 'figurespace| ', 'radical|√', 'quoteright|’', 'commaaccent|', 'ucircumflex|û', 'parenleft|(', 'Oacute.sc|', 'Ezhcaron.sc|', 'V.sc|', 'six.OT|', 'Ecaron|Ě', 'C.sc|', 'parenleft.sups|⁽', 'G|G', 'Odoublegrave|Ȍ', 'grave.cap|', 'ndieresis|', 'quoteleft|‘', 'five.LT|', 'Tcommaaccent|Ț', 'Ncommaaccent|Ņ', 'W|W', 'Obreve|Ŏ', 'r.sups|', 'g|g', 'imacron|ī', 'three.sinf|', 'Gstroke|Ǥ', 'oogonekmacron|ǭ', 'Kcedilla.sc|', 'ocommaaccent|', 'w|w', 'wacute|ẃ', 'hyphen.cap|', 'notequal|≠', 'rdoublegrave|ȑ', 'Acircumflex.sc|', 'Tbar|Ŧ', 'Rdoublegrave.sc|', 'ezhcaron|ǯ', 'one.sinf|', 'Itilde|Ĩ', 'Otildemacron.sc|', 'ring|˚', 'Ubreve|Ŭ', 'Ycircumflex|Ŷ', 'Scaron.sc|', 'Zcaron.sc|', 'Lcaron|Ľ', 'Ndescender|', 'uni2605|★', 'zero.sinf|', 'Ndotaccent|Ṅ', 'Q|Q', 'dotbelow.cap|', 'Khook|Ƙ', 'anglebracketleft.cap|', 'Wgrave|Ẁ', 'Dcedilla.sc|', 'B|B', 'Adieresismacron|Ǟ', 'iacute|í', 'Rcommaaccent|Ŗ', 'Ydieresis|Ÿ', 'Udotbelow.sc|', 'R|R', 'zerowidthspace|​', 'Hmacronbelow.sc|', 'Ccedilla.sc|', 'Ldotbelow|Ḷ', 'Odoublegrave.sc|', 'Aogonek|Ą', 'f_f|ﬀ', 'b|b', 'udotbelow|ụ', 'f_b|', 'odoublegrave|ȍ', 'f_l|ﬂ', 'f_h|', 'bracketleft.cap|', 'f_j|', 'f_k|', 'percent.LP|', 'r|r', 'ainvertedbreve|ȃ', 'Jcircumflex|Ĵ', 'bullet.cap|', 'Ccedilla|Ç', 'minus|−', 'dcedilla|ḑ', 'tcaron|ť', 'Otilde.sc|', 'guilsinglright.sc|', 'lcommaaccent|ļ', 'Hcircumflex.sc|', 'increment|∆', 'O.sc|', 'Lslash|Ł', 'adotaccent|ȧ', 'ldot|ŀ', 'uni25C9|◉', 'abreve|ă', 'h.sinf|', 'Adoublegrave|Ȁ', 'Cacute.sc|', 'Thorn.sc|', 'zero|0', 'Uacute|Ú', 'Ocaron|Ǒ', 'itilde|ĩ', 'Udieresis|Ü', 'Odotaccent|Ȯ', 'S.sc|', 'Emacron|Ē', 'edotaccent|ė', 'Egravedotbelow|', 'periodcentered.sc|', 'acaron|ǎ', 'Nacute|Ń', 'Oslashacute|Ǿ', 'quotedbl|"', 'invertedbreve.cap|', 'A.sc|', 'ohungarumlaut|ő', 'onehalf|½', 'threeperemspace| ', 'numbersign|#', 'Omacron.sc|', 'M|M', 'numero|№', 'Ldot.sc|', 'Mcedilla.sc|', 'f_f_b|', 'eight|8', 'b.sinf|', 'Abreve.sc|', 'f_f_f|', 'f_f_i|ﬃ', 'f_f_h|', 'f_f_k|', 'f_f_j|', 'Gcircumflex|Ĝ', 'Oogonek|Ǫ', 'Dcedilla|Ḑ', 'germandbls.sc|', 'Mmacron.sc|', 'uni25CE|◎', 'uni25CD|◍', 'Ocedilla.sc|', 'Ocircumflex|Ô', 'm|m', 'Euro.LP|', 'Ocedilla|', 'seven.ordn|', 'nine.sinf|', 'Ainvertedbreve.sc|', 'parenright.sc|', 'Odieresis.sc|', 'Ugrave.sc|', 'perthousand.LP|', 'eight.sups|⁸', 'Thorn|Þ', 'Ezh.sc|', 'Ntilde|Ñ', 'Uogonek|Ų', 'questiondown|¿', 'g.sups|', 'Atilde|Ã', 'aemacron|ǣ', 'altogonek|', 'Oogonekmacron|Ǭ', 'Sacute|Ś', 'Acaron|Ǎ', 'Schwa.sc|', 'Dcroat.sc|', 'Idotbelow|Ị', 'altcedilla.cap|', 'greater.LP|', 'copyright|©', 'zdotaccent|ż', 'Ncommaaccent.sc|', 'hcircumflex|ĥ', 'Scommaaccent|Ș', 'yen|¥', 'Gcaron|Ǧ', 's_t|ﬆ', 'Zacute|Ź', 'Eacutedotbelow.sc|', 'Ytilde|Ỹ', 'Rdotbelowmacron.sc|', 'parenleft.ordn|', 'seven.sinf|', 'Itilde.sc|', 'H|H', 'Uogonek.sc|', 'cacute|ć', 'F.sc|', 'Ocommaaccent.sc|', 'gcaron|ǧ', 'rinvertedbreve|ȓ', 'f.sinf|', 'egravedotbelow|', 'six.ordn|', 'l.sups|', 'Ncaron|Ň', 'Idieresis|Ï', 'four.subs|₄', 'Rcaron.sc|', 'edieresis|ë', 'lozenge|◊', 'h|h', 'Ngrave|', 'Mmacron|', 'U.sc|', 'uinvertedbreve|ȗ', 'b.sups|', 'dotaccent|˙', 'braceleft.sc|', 'L.sc|', 'x|x', 'interrobang|‽', 'eacute|é', 'Einvertedbreve.sc|', 'Ibreve.sc|', 'udieresis|ü', 'ordfeminine|ª', 'p.sinf|', 'Ndotaccent.sc|', 'schwa|ə', 'rcaron|ř', 'Ccaron|Č', 'ocedilla|', 'ampersand.sc|', 'Cdotaccent.sc|', 'edoublegrave|ȅ', 'tilde.cap|', 'Imacron.sc|', 'braceleft|{', 'four.sups|⁴', 'grave|`', 'x.sups|', 'k.sinf|', 'macron|¯', 'uni2197|↗', 'Nmacron|', 'onequarter|¼', 'tcommaaccent|ț', 'Q.sc|', 'Edotaccent.sc|', 'Acircumflex|Â', 'Icaron.sc|', 'sacute|ś', 'uni2190|←', 'Oslash|Ø', 'gbreve|ğ', 'seven.sups|⁷', 'd.sinf|', 'quotedblleft|“', 'period.sinf|', 'Aringacute|Ǻ', 'Ncaron.sc|', 'AEacute|Ǽ', 'Lcaron.sc|', 'S|S', 'Eacute|É', 'equal.subs|', 'zacute|ź', 'Rdoublegrave|Ȑ', 'exclam|!', 'parenright.ordn|', 'Tcaron|Ť', 'oslashacute|ǿ', 'c|c', 'Uinvertedbreve.sc|', 'f.sups|', 'C|C', 'uni2199|↙', 'invertedbreve|̑', 'Lcommaaccent|Ļ', 'Uinvertedbreve|Ȗ', 'seven.LP|', 'Ugrave|Ù', 'two.LP|', 'Idieresis.sc|', 'eth|ð', 'hbar|ħ', 'Uacute.sc|', 'pmacron|', 'Iogonek.sc|', 'Racute|Ŕ', 'uhungarumlaut|ű', 'Egrave|È', 'seven.subs|₇', 'hyphen|-', 'Utilde|Ũ', 'nine.OT|', 'period|.', 'igrave|ì', 'gstroke|ǥ', 'Odotaccent.sc|', 'colon|:', 'Ndescender.sc|', 'u.sups|', 'ae|æ', 'Z.sc|', 'Ecircumflex|Ê', 'udoublegrave|ȕ', 'anglebracketleft|〈', 'partialdiff|∂', 'J.sc|', 'G.sc|', 'trademark|™', 'Aacute|Á', 'cent|¢', 'e.sinf|', 'a.sinf|', 'icaron|ǐ', 'divide.sups|', 'lslash|ł', 'pi|π', 'Ycircumflex.sc|', 'wdieresis|ẅ', 'ycircumflex|ŷ', 'B.sc|', 'Otildemacron|Ȭ', 'florin.LP|', 'parenright.sups|⁾', 'Umacronbelow.sc|', 'Amacron|Ā', 'Hcaron|Ȟ', 'breve|˘', 'interrobangdown|⸘', 'Mcedilla|', 'Oacute|Ó', 'Sdotbelow.sc|', 'Gbreve.sc|', 'linebelow|uni0329|̩', 'Scircumflex.sc|', 'Ezhcaron|Ǯ', 'n|n', 'x.sinf|', 'Ldotbelowmacron.sc|', 'Yacute.sc|', 'Ucircumflex|Û', 'u.sinf|', 'idieresis|ï', 'Iinvertedbreve|Ȋ', 'braceright|}', 'threequarters|¾', 'Gcircumflex.sc|', 'brokenbar|¦', 'published.cap|', 'six.subs|₆', 'Lslash.sc|', 'y.sups|', 'Dcaron|Ď', 'Oogonek.sc|', 'Ucircumflex.sc|', 'ugrave|ù', 'Oinvertedbreve.sc|', 'atilde|ã', 'Jcircumflex.sc|', 'Wgrave.sc|', 'guillemotright.cap|', 'Adieresis.sc|', 'einvertedbreve|ȇ', 'Aring.sc|', 'hmacronbelow|ẖ', 'uni25BC|▼','Ndotbelow|Ṇ', 's|s', 'Rdotbelow.sc|', 'c.sinf|', 'three.ordn|', 'Dcroat|Đ', 'Jcaron.sc|', 'Rcedilla.sc|', 'Oslashacute.sc|', 'anglebracketright|〉', 'sterling|£', 'racute|ŕ', 'infinity|∞', 'I|I', 'hungarumlaut.cap|', 'Udoublegrave.sc|', 'florin|ƒ', 'Lcedilla.sc|', 'parenleft.sinf|', 'uni25B6|▶', 'q.sinf|', 'Nmacron.sc|', 'Y|Y', 'ldotbelow|ḷ', 'Eth|Ð', 'uni25CF|●', 'emdash|—','plus.LP|', 'interrobangdown.sc|', 'otildemacron|ȭ', 'five.sinf|', 'i|i', 'lessequal.LP|', 'tcedilla|ţ', 'dotbelow|uni0323|̣', 'icircumflex|î', 'guillemotleft.cap|', 'daggerdbl|‡', 'y|y', 'ncaron|ň', 'Hcaron.sc|', 'equal.sups|⁼', 'Ocommaaccent|uniE017', 'plusminus|±', 'cedilla.cap|', 'Olinebelow|', 's.sups|', 'Wacute|Ẃ', 'OE.sc|', 'three.subs|₃', 'equal.ordn|', 'Igrave.sc|', 'p.sups|', 'Wdieresis|Ẅ', 'eight.sinf|', 'Ebreve.sc|', 'periodcentered.cap|', 'Zcaron|Ž', 'Gcommaaccent.sc|', 'zero.OT|', 'nine.ordn|', 'at.sc|', 'Eacutedotbelow|', 'two.LT|', 'Rinvertedbreve|Ȓ', 'parenright.subs|₎', 'Tcaron.sc|', 'eight.LT|', 'Mdotbelow.sc|', 'six.sups|⁶', 'yacute|ý', 'oslash|ø', 'enspace| ', 'y.sinf|', 'Udotbelow|Ụ', 'D|D', 'Uhungarumlaut.sc|', 'uni2620|☠', 'notequal.LP|', 'Tcedilla|Ţ', 'interrobangdown.cap|', 'Ocaron.sc|', 'five|5', 'T|T', 'khook|ƙ', 'breve.cap|', 'Hbar|Ħ', 'daggerdbl.sc|', 'quotedblbase|„', 'ecaron|ě', 'acute|´', 'ampersand|&', 'multiply.sinf|', 'd|d', 'Scircumflex|Ŝ', 'lcaron|ľ', 'OE|Œ', 'aringacute|ǻ', 'Igrave|Ì', 'macron.cap|', 'Ocircumflex.sc|', 't|t', 'seven.LT|', 'circumflex|ˆ', 'divide.subs|', 'aogonek|ą', 'parenright|)', 'braceleft.cap|', 'Schwa|Ə', 'scircumflex|ŝ', 'four.ordn|', 'eight.subs|₈', 'braceright.cap|', 'ezh|ʒ', 'questiondown.cap|', 'jcircumflex|ĵ', 'adieresis|ä','Pmacron|', 'Ohungarumlaut.sc|', 'Oslash.sc|', 'AEacute.sc|', 'registered.cap|', 'eogonek|ę', 'Umacron|Ū', 'seven.OT|', 'Ygrave.sc|', 'm.sinf|', 'Ndotbelow.sc|', 'Ndieresis|', 'Eacute.sc|', 'gacute|ǵ', 'five.subs|₅', 'Lcedilla|', 'ellipsis|…', 'bullet.sc|', 'Adoublegrave.sc|', 'guilsinglright|›', 'Amacron.sc|', 'AE.sc|', 'germandbls.cap|ẞ', 'zcaron|ž', 'odieresis|ö', 'registered.sc|', 'scommaaccent|ș', 'ebreve|ĕ', 'Ldotbelow.sc|', 'O|O', 'comma.sinf|', 'Aringacute.sc|', 'daggerdbl.cap|', 'Jcaron|', 'caron|ˇ', 'comma.ordn|', 'ndescender|', 'w.sups|', 'one.OT|', 'cent.LP|', 'Idotbelow.sc|', 'olinebelow|', 'anglebracketright.sc|', 'rcommaaccent|ŗ', 'idotaccent|', 'guilsinglleft|‹', 'o|o', 'Edieresis|Ë', 'plus|+', 'Edoublegrave|Ȅ', 'periodcentered|·', 'emacron|ē', 'three.OT|', 'mcedilla|', 'greaterequal.LP|', 'dagger|†', 'Ncedilla.sc|', 'Kcaron|Ǩ', 'ngrave|', 'equal.sinf|', 'j.sinf|', 'R.sc|', 'oinvertedbreve|ȏ', 'Ccircumflex.sc|', 'multiply|×', 'v.sups|', 'Odotaccentmacron|Ȱ', 'Rdotbelow|Ṛ', 'Kcaron.sc|', 'eight.ordn|', 'Mdotbelow|Ṃ', 'hungarumlaut|˝', 'Gcommaaccent|Ģ', 'Aacute.sc|', 'k.sups|', 'altcedilla|', 'endash.sc|', 'three.LP|', 'yen.LP|', 'Scedilla.sc|', 'Ebreve|Ĕ', 'question|?', 'f_f_l|ﬄ', 'Eth.sc|', 'Ucaron.sc|', 'fraction|⁄', 'dagger.sc|', 'uni2196|↖', 'mdotbelow|ṃ', 'Y.sc|', 'idotbelow|ị', 'Omacron|Ō', 'Iogonek|Į', 'uni25B2|▲', 'M.sc|', 'registered|®', 'J|J', 'colonmonitary|₡', 'Zacute.sc|', 'period.sups|', 'dieresis|¨', 'Acaron.sc|', 'Tcommaaccent.sc|', 'altogonek.cap|', 'w.sinf|', 'multiply.LP|', 'Z|Z', 'r.sinf|', 'uni25CB|○', 'iogonek|į', 'Ograve|Ò', 'j|j', 'seven|7', 'hairspace| ', 'ucaron|ǔ', 'Ubreve.sc|', 'h.sups|', 'five.sups|⁵', 'Wacute.sc|', 'uni2193|↓', 'uni2192|→', 'two.sinf|', 'uogonek|ų', 't.sups|', 'z|z', 'Adotaccent|Ȧ', 'commaabovecmb.cap|', 'ohm|Ω', 'nacute|ń', 'doublegrave|̏', 'semicolon|;', 'Zdotaccent|Ż', 'eight.LP|', 'Rinvertedbreve.sc|', 'Hdotbelow|Ḥ', 'five.ordn|', 'emdash.sc|', 'at|@', 'l.sinf|', 'two.ordn|', 'guillemotleft.sc|', 'Rcommaaccent.sc|', 'three.LT|', 'two.sups|²', 'q.sups|', 'Iacute|Í', 'guilsinglleft.cap|', 'nine.LT|', 'Umacron.sc|', 'Ndieresis.sc|', 'Tcedilla.sc|', 'percent|%', 'hdotbelow|ḥ', 'five.OT|', 'divide.LP|', 'one.ordn|', 'umacronbelow|', 'ibreve|ĭ', 'zero.sups|⁰', 'ubreve|ŭ', 'kcedilla|', 'bracketright|]', 'period.subs|', 'gdotaccent|ġ', 'Wcircumflex|Ŵ', 'zero.LT|', 'AE|Æ', 'approxequal|≈', 'Imacron|Ī', 'Ydieresis.sc|', 'scedilla|ş', 'asterisk|*', 'aacute|á', 'sixperemspace| ', 'nmacron|', 'eacutedotbelow|', 'odotaccent|ȯ', 'Ccircumflex|Ĉ', 'U|U', 'less|<', 'Adieresismacron.sc|', 'N|N', 'underscore|_', 'parenright.sinf|', 'Egravedotbelow.sc|', 'wgrave|ẁ', 'wcircumflex|ŵ', 'Idotaccent.sc|', 'e|e', 'multiply.subs|', 'bullet|•', 'approxequal.LP|', 'thorn|þ', 'Ohungarumlaut|Ő', 'AEmacron.sc|', 'plusminus.LP|', 'Odotaccentmacron.sc|', 'multiply.sups|', 'Ddotbelow|Ḍ', 'u|u', 'nine.LP|', 'eight.OT|', 'ytilde|ỹ', 'dagger.cap|', 'W.sc|']
                            
                            
f.glyphOrder = ['.notdef', 'space', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A.sc', 'B.sc', 'C.sc', 'D.sc', 'E.sc', 'F.sc', 'G.sc', 'H.sc', 'I.sc', 'J.sc', 'K.sc', 'L.sc', 'M.sc', 'N.sc', 'O.sc', 'P.sc', 'Q.sc', 'R.sc', 'S.sc', 'T.sc', 'U.sc', 'V.sc', 'W.sc', 'X.sc', 'Y.sc', 'Z.sc', 'Aacute', 'Agrave', 'Acircumflex', 'Adieresis', 'Atilde', 'Aring', 'Acaron', 'Amacron', 'Abreve', 'Ainvertedbreve', 'Adoublegrave', 'Adotaccent', 'Aringacute', 'Adieresismacron', 'Aogonek', 'AE', 'AEacute', 'AEmacron', 'Cacute', 'Ccircumflex', 'Ccaron', 'Cdotaccent', 'Ccedilla', 'Dcaron', 'Dcedilla', 'Ddotbelow', 'Dcroat', 'Eacute', 'Egrave', 'Ecircumflex', 'Edieresis', 'Ecaron', 'Emacron', 'Ebreve', 'Einvertedbreve', 'Edoublegrave', 'Edotaccent', 'Eacutedotbelow', 'Egravedotbelow', 'Eogonek', 'Gacute', 'Gcircumflex', 'Gcaron', 'Gbreve', 'Gdotaccent', 'Gcommaaccent', 'Gstroke', 'Hcircumflex', 'Hcaron', 'Hdotbelow', 'Hmacronbelow', 'Hbar', 'Iacute', 'Igrave', 'Icircumflex', 'Idieresis', 'Itilde', 'Icaron', 'Imacron', 'Ibreve', 'Iinvertedbreve', 'Idoublegrave', 'Idotaccent', 'Idotbelow', 'Iogonek', 'Jcircumflex', 'Jcaron', 'Kcaron', 'Kcommaaccent', 'Kcedilla', 'Khook', 'Lacute', 'Lcaron', 'Lcommaaccent', 'Lcedilla', 'Ldotbelow', 'Ldotbelowmacron', 'Ldot', 'Lslash', 'Mmacron', 'Mcedilla', 'Mdotbelow', 'Nacute', 'Ngrave', 'Ndieresis', 'Ntilde', 'Ncaron', 'Nmacron', 'Ndotaccent', 'Ncommaaccent', 'Ncedilla', 'Ndotbelow', 'Ndescender', 'Oacute', 'Ograve', 'Ocircumflex', 'Odieresis', 'Otilde', 'Ocaron', 'Omacron', 'Obreve', 'Oinvertedbreve', 'Ohungarumlaut', 'Odoublegrave', 'Ocommaaccent', 'Otildemacron', 'Odotaccent', 'Odotaccentmacron', 'Ocedilla', 'Odotbelow', 'Olinebelow', 'Oogonek', 'Oogonekmacron', 'Oslash', 'Oslashacute', 'barredO', 'OE', 'Pmacron', 'Racute', 'Rcaron', 'Rinvertedbreve', 'Rdoublegrave', 'Rcommaaccent', 'Rcedilla', 'Rdotbelow', 'Rdotbelowmacron', 'Sacute', 'Scircumflex', 'Scaron', 'Scommaaccent', 'Scedilla', 'Sdotbelow', 'germandbls.cap', 'Tcaron', 'Tcommaaccent', 'Tcedilla', 'Tdotbelow', 'Tbar', 'Uacute', 'Ugrave', 'Ucircumflex', 'Udieresis', 'Utilde', 'Uring', 'Ucaron', 'Umacron', 'Ubreve', 'Uinvertedbreve', 'Uhungarumlaut', 'Udoublegrave', 'Uogonek', 'Udotbelow', 'Umacronbelow', 'Wacute', 'Wgrave', 'Wcircumflex', 'Wdieresis', 'Yacute', 'Ygrave', 'Ycircumflex', 'Ydieresis', 'Ytilde', 'Zacute', 'Zcaron', 'Zdotaccent', 'Eng', 'Thorn', 'Eth', 'Ezh', 'Ezhcaron', 'Schwa', 'aacute', 'agrave', 'acircumflex', 'adieresis', 'atilde', 'aring', 'acaron', 'amacron', 'abreve', 'ainvertedbreve', 'adoublegrave', 'adotaccent', 'aringacute', 'adieresismacron', 'aogonek', 'ae', 'aeacute', 'aemacron', 'cacute', 'ccircumflex', 'ccaron', 'cdotaccent', 'ccedilla', 'dcaron', 'dcedilla', 'ddotbelow', 'dcroat', 'eacute', 'egrave', 'ecircumflex', 'edieresis', 'ecaron', 'emacron', 'ebreve', 'einvertedbreve', 'edoublegrave', 'edotaccent', 'eacutedotbelow', 'egravedotbelow', 'eogonek', 'gacute', 'gcircumflex', 'gcaron', 'gbreve', 'gdotaccent', 'gcommaaccent', 'gstroke', 'hcircumflex', 'hcaron', 'hdotbelow', 'hmacronbelow', 'hbar', 'dotlessi', 'iacute', 'igrave', 'icircumflex', 'idieresis', 'itilde', 'icaron', 'imacron', 'ibreve', 'iinvertedbreve', 'idoublegrave', 'idotaccent', 'idotbelow', 'iogonek', 'dotlessj', 'jcircumflex', 'jcaron', 'kcaron', 'kcommaaccent', 'kcedilla', 'khook', 'kgreenlandic', 'lacute', 'lcaron', 'lcommaaccent', 'lcedilla', 'ldotbelow', 'ldotbelowmacron', 'ldot', 'lslash', 'mmacron', 'mcedilla', 'mdotbelow', 'nacute', 'ngrave', 'ndieresis', 'ntilde', 'ncaron', 'nmacron', 'ndotaccent', 'ncommaaccent', 'ncedilla', 'ndotbelow', 'ndescender', 'oacute', 'ograve', 'ocircumflex', 'odieresis', 'otilde', 'ocaron', 'omacron', 'obreve', 'oinvertedbreve', 'ohungarumlaut', 'odoublegrave', 'ocommaaccent', 'otildemacron', 'odotaccent', 'odotaccentmacron', 'ocedilla', 'odotbelow', 'olinebelow', 'oogonek', 'oogonekmacron', 'oslash', 'oslashacute', 'barredo', 'oe', 'pmacron', 'racute', 'rcaron', 'rinvertedbreve', 'rdoublegrave', 'rcommaaccent', 'rcedilla', 'rdotbelow', 'rdotbelowmacron', 'sacute', 'scircumflex', 'scaron', 'scommaaccent', 'scedilla', 'sdotbelow', 'germandbls', 'tcaron', 'tcommaaccent', 'tcedilla', 'tdotbelow', 'tbar', 'uacute', 'ugrave', 'ucircumflex', 'udieresis', 'utilde', 'uring', 'ucaron', 'umacron', 'ubreve', 'uinvertedbreve', 'uhungarumlaut', 'udoublegrave', 'uogonek', 'udotbelow', 'umacronbelow', 'wacute', 'wgrave', 'wcircumflex', 'wdieresis', 'yacute', 'ygrave', 'ycircumflex', 'ydieresis', 'ytilde', 'zacute', 'zcaron', 'zdotaccent', 'eng', 'thorn', 'eth', 'ezh', 'ezhcaron', 'schwa', 'Aacute.sc', 'Agrave.sc', 'Adoublegrave.sc', 'Abreve.sc', 'Ainvertedbreve.sc', 'Acaron.sc', 'Acircumflex.sc', 'Adieresis.sc', 'Adieresismacron.sc', 'Adotaccent.sc', 'Amacron.sc', 'Atilde.sc', 'Aogonek.sc', 'Aring.sc', 'Aringacute.sc', 'AE.sc', 'AEacute.sc', 'AEmacron.sc', 'Cacute.sc', 'Ccaron.sc', 'Ccircumflex.sc', 'Cdotaccent.sc', 'Ccedilla.sc', 'Dcaron.sc', 'Dcroat.sc', 'Dcedilla.sc', 'Ddotbelow.sc', 'Eacute.sc', 'Eacutedotbelow.sc', 'Egrave.sc', 'Egravedotbelow.sc', 'Edoublegrave.sc', 'Ebreve.sc', 'Einvertedbreve.sc', 'Ecaron.sc', 'Ecircumflex.sc', 'Edieresis.sc', 'Edotaccent.sc', 'Emacron.sc', 'Eogonek.sc', 'Gacute.sc', 'Gbreve.sc', 'Gcaron.sc', 'Gcircumflex.sc', 'Gcommaaccent.sc', 'Gdotaccent.sc', 'Gstroke.sc', 'Hbar.sc', 'Hcaron.sc', 'Hcircumflex.sc', 'Hdotbelow.sc', 'Hmacronbelow.sc', 'Iacute.sc', 'Igrave.sc', 'Idoublegrave.sc', 'Ibreve.sc', 'Icaron.sc', 'Icircumflex.sc', 'Idieresis.sc', 'Idotaccent.sc', 'Idotbelow.sc', 'Iinvertedbreve.sc', 'Imacron.sc', 'Itilde.sc', 'Iogonek.sc', 'Jcaron.sc', 'Jcircumflex.sc', 'Kcaron.sc', 'Kcedilla.sc', 'Kcommaaccent.sc', 'Khook.sc', 'Lacute.sc', 'Lcaron.sc', 'Lcedilla.sc', 'Lcommaaccent.sc', 'Ldot.sc', 'Ldotbelow.sc', 'Ldotbelowmacron.sc', 'Lslash.sc', 'Mdotbelow.sc', 'Mmacron.sc', 'Mcedilla.sc', 'Nacute.sc', 'Ngrave.sc', 'Ncaron.sc', 'Ncommaaccent.sc', 'Ndescender.sc', 'Ndieresis.sc', 'Ndotaccent.sc', 'Ndotbelow.sc', 'Nmacron.sc', 'Ntilde.sc', 'Ncedilla.sc', 'Oacute.sc', 'Ograve.sc', 'Ohungarumlaut.sc', 'Odoublegrave.sc', 'Obreve.sc', 'Oinvertedbreve.sc', 'Ocaron.sc', 'Ocedilla.sc', 'Ocircumflex.sc', 'Ocommaaccent.sc', 'Odieresis.sc', 'Odotaccent.sc', 'Odotaccentmacron.sc', 'Odotbelow.sc', 'Omacron.sc', 'Otilde.sc', 'Otildemacron.sc', 'Olinebelow.sc', 'Oogonek.sc', 'Oogonekmacron.sc', 'Oslash.sc', 'Oslashacute.sc', 'barredO.sc', 'OE.sc', 'Pmacron.sc', 'Racute.sc', 'Rdoublegrave.sc', 'Rcaron.sc', 'Rcedilla.sc', 'Rcommaaccent.sc', 'Rdotbelow.sc', 'Rdotbelowmacron.sc', 'Rinvertedbreve.sc', 'Sacute.sc', 'Scaron.sc', 'Scedilla.sc', 'Scircumflex.sc', 'Scommaaccent.sc', 'Sdotbelow.sc', 'germandbls.sc', 'Tbar.sc', 'Tcaron.sc', 'Tcommaaccent.sc', 'Tcedilla.sc', 'Tdotbelow.sc', 'Uacute.sc', 'Ugrave.sc', 'Uhungarumlaut.sc', 'Udoublegrave.sc', 'Ubreve.sc', 'Uinvertedbreve.sc', 'Ucaron.sc', 'Ucircumflex.sc', 'Udieresis.sc', 'Udotbelow.sc', 'Umacron.sc', 'Umacronbelow.sc', 'Uogonek.sc', 'Uring.sc', 'Utilde.sc', 'Wacute.sc', 'Wcircumflex.sc', 'Wdieresis.sc', 'Wgrave.sc', 'Yacute.sc', 'Ycircumflex.sc', 'Ydieresis.sc', 'Ygrave.sc', 'Ytilde.sc', 'Zacute.sc', 'Zcaron.sc', 'Zdotaccent.sc', 'Eth.sc', 'Thorn.sc', 'Eng.sc', 'Ezh.sc', 'Ezhcaron.sc', 'Schwa.sc', 'acute', 'grave', 'hungarumlaut', 'doublegrave', 'circumflex', 'caron', 'dieresis', 'tilde', 'ring', 'macron', 'macronbelow', 'breve', 'invertedbreve', 'dotaccent', 'dotbelow', 'cedilla', 'altcedilla', 'ogonek', 'altogonek', 'commaabovecmb', 'linebelow', 'commaaccent', 'commaaccentturned', 'stroke', 'baraccent', 'slashaccent', 'acute.cap', 'grave.cap', 'hungarumlaut.cap', 'doublegrave.cap', 'circumflex.cap', 'caron.cap', 'dieresis.cap', 'tilde.cap', 'ring.cap', 'macron.cap', 'breve.cap', 'invertedbreve.cap', 'dotaccent.cap', 'dotbelow.cap', 'linebelow.cap', 'commaaccent.cap', 'commaaccentturned.cap', 'cedilla.cap', 'altcedilla.cap', 'ogonek.cap', 'altogonek.cap', 'commaabovecmb.cap', 'croat.cap', 'acute.sc', 'grave.sc', 'hungarumlaut.sc', 'doublegrave.sc', 'circumflex.sc', 'caron.sc', 'dieresis.sc', 'tilde.sc', 'ring.sc', 'macron.sc', 'breve.sc', 'invertedbreve.sc', 'dotaccent.sc', 'dotbelow.sc', 'linebelow.sc',  'cedilla.sc', 'altcedilla.sc', 'ogonek.sc', 'altogonek.sc', 'commaabovecmb.sc', 'croat.sc', 'commaaccent.sc', 'commaaccentturned.sc'. 'f_i', 'f_l', 'f_j', 'f_f', 'f_b', 'f_h', 'f_k', 'f_f_i', 'f_f_l', 'f_f_j', 'f_f_f', 'f_f_b', 'f_f_h', 'f_f_k', 's_t', 'c_t', 'paragraph', 'period', 'comma', 'colon', 'semicolon', 'exclamdown', 'exclam', 'questiondown', 'question', 'interrobangdown', 'interrobang', 'ellipsis', 'quotesingle', 'quotedbl', 'quoteleft', 'quoteright', 'quotedblleft', 'quotedblright', 'quotesinglbase', 'quotedblbase', 'underscore', 'slash', 'backslash', 'bar', 'brokenbar', 'asterisk', 'guilsinglleft', 'guilsinglright', 'guillemotleft', 'guillemotright', 'periodcentered', 'hyphen', 'endash', 'emdash', 'bullet', 'parenleft', 'parenright', 'bracketleft', 'bracketright', 'braceleft', 'braceright', 'anglebracketleft', 'anglebracketright', 'dagger', 'daggerdbl', 'at', 'copyright', 'registered', 'published', 'ampersand', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'numbersign', 'section', 'Euro', 'dollar', 'cent', 'sterling', 'florin', 'yen', 'colonmonitary', 'plus', 'minus', 'plusminus', 'multiply', 'divide', 'equal', 'notequal', 'approxequal', 'less', 'greater', 'lessequal', 'greaterequal', 'infinity', 'percent', 'perthousand', 'degree', 'logicalnot', 'mu', 'pi', 'partialdiff', 'integral', 'radical', 'increment', 'ohm', 'product', 'summation', 'ordfeminine', 'ordmasculine', 'currency', 'asciitilde', 'asciicircum', 'trademark', 'servicemark', 'litre', 'estimated', 'numero', 'lozenge', 'enspace', 'emspace', 'threeperemspace', 'fourperemspace', 'sixperemspace', 'figurespace', 'punctuationspace', 'hairspace', 'thinspace', 'zerowidthspace', 'nbspace', 'zero.LP', 'one.LP', 'two.LP', 'three.LP', 'four.LP', 'five.LP', 'six.LP', 'seven.LP', 'eight.LP', 'nine.LP', 'numbersign.LP', 'section.LP', 'Euro.LP', 'dollar.LP', 'cent.LP', 'sterling.LP', 'florin.LP', 'yen.LP', 'colonmonitary.LP', 'plus.LP', 'minus.LP', 'plusminus.LP', 'multiply.LP', 'divide.LP', 'equal.LP', 'notequal.LP', 'approxequal.LP', 'less.LP', 'greater.LP', 'lessequal.LP', 'greaterequal.LP', 'infinity.LP', 'percent.LP', 'perthousand.LP', 'zero.OT', 'one.OT', 'two.OT', 'three.OT', 'four.OT', 'five.OT', 'six.OT', 'seven.OT', 'eight.OT', 'nine.OT', 'zero.LT', 'one.LT', 'two.LT', 'three.LT', 'four.LT', 'five.LT', 'six.LT', 'seven.LT', 'eight.LT', 'nine.LT', 'exclamdown.cap', 'questiondown.cap', 'interrobangdown.cap', 'guilsinglleft.cap', 'guilsinglright.cap', 'guillemotleft.cap', 'guillemotright.cap', 'periodcentered.cap', 'hyphen.cap', 'endash.cap', 'emdash.cap', 'bullet.cap', 'parenleft.cap', 'parenright.cap', 'bracketleft.cap', 'bracketright.cap', 'braceleft.cap', 'braceright.cap', 'anglebracketleft.cap', 'anglebracketright.cap', 'dagger.cap', 'daggerdbl.cap', 'at.cap', 'copyright.cap', 'registered.cap', 'published.cap', 'exclamdown.sc', 'questiondown.sc', 'interrobangdown.sc', 'guilsinglleft.sc', 'guilsinglright.sc', 'guillemotleft.sc', 'guillemotright.sc', 'periodcentered.sc', 'hyphen.sc', 'endash.sc', 'emdash.sc', 'bullet.sc', 'parenleft.sc', 'parenright.sc', 'bracketleft.sc', 'bracketright.sc', 'braceleft.sc', 'braceright.sc', 'anglebracketleft.sc', 'anglebracketright.sc', 'dagger.sc', 'daggerdbl.sc', 'at.sc', 'copyright.sc', 'registered.sc', 'published.sc', 'ampersand.sc', 'zero.sups', 'one.sups', 'two.sups', 'three.sups', 'four.sups', 'five.sups', 'six.sups', 'seven.sups', 'eight.sups', 'nine.sups', 'parenleft.sups', 'parenright.sups', 'plus.sups', 'minus.sups', 'multiply.sups', 'divide.sups', 'equal.sups', 'period.sups', 'comma.sups', 'zero.ordn', 'one.ordn', 'two.ordn', 'three.ordn', 'four.ordn', 'five.ordn', 'six.ordn', 'seven.ordn', 'eight.ordn', 'nine.ordn', 'parenleft.ordn', 'parenright.ordn', 'plus.ordn', 'minus.ordn', 'multiply.ordn', 'divide.ordn', 'equal.ordn', 'period.ordn', 'comma.ordn', 'zero.subs', 'one.subs', 'two.subs', 'three.subs', 'four.subs', 'five.subs', 'six.subs', 'seven.subs', 'eight.subs', 'nine.subs', 'parenleft.subs', 'parenright.subs', 'plus.subs', 'minus.subs', 'multiply.subs', 'divide.subs', 'equal.subs', 'period.subs', 'comma.subs', 'zero.sinf', 'one.sinf', 'two.sinf', 'three.sinf', 'four.sinf', 'five.sinf', 'six.sinf', 'seven.sinf', 'eight.sinf', 'nine.sinf', 'parenleft.sinf', 'parenright.sinf', 'plus.sinf', 'minus.sinf', 'multiply.sinf', 'divide.sinf', 'equal.sinf', 'period.sinf', 'comma.sinf', 'a.sups', 'b.sups', 'c.sups', 'd.sups', 'e.sups', 'f.sups', 'g.sups', 'h.sups', 'i.sups', 'j.sups', 'k.sups', 'l.sups', 'm.sups', 'n.sups', 'o.sups', 'p.sups', 'q.sups', 'r.sups', 's.sups', 't.sups', 'u.sups', 'v.sups', 'w.sups', 'x.sups', 'y.sups', 'z.sups','a.ordn', 'b.ordn', 'c.ordn', 'd.ordn', 'e.ordn', 'f.ordn', 'g.ordn', 'h.ordn', 'i.ordn', 'j.ordn', 'k.ordn', 'l.ordn', 'm.ordn', 'n.ordn', 'o.ordn', 'p.ordn', 'q.ordn', 'r.ordn', 's.ordn', 't.ordn', 'u.ordn', 'v.ordn', 'w.ordn', 'x.ordn', 'y.ordn', 'z.ordn', 'a.subs', 'b.subs', 'c.subs', 'd.subs', 'e.subs', 'f.subs', 'g.subs', 'h.subs', 'i.subs', 'j.subs', 'k.subs', 'l.subs', 'm.subs', 'n.subs', 'o.subs', 'p.subs', 'q.subs', 'r.subs', 's.subs', 't.subs', 'u.subs', 'v.subs', 'w.subs', 'x.subs', 'y.subs', 'z.subs', 'a.sinf', 'b.sinf', 'c.sinf', 'd.sinf', 'e.sinf', 'f.sinf', 'g.sinf', 'h.sinf', 'i.sinf', 'j.sinf', 'k.sinf', 'l.sinf', 'm.sinf', 'n.sinf', 'o.sinf', 'p.sinf', 'q.sinf', 'r.sinf', 's.sinf', 't.sinf', 'u.sinf', 'v.sinf', 'w.sinf', 'x.sinf', 'y.sinf', 'z.sinf', 'fraction', 'onequarter', 'onehalf', 'threequarters', 'uni2191', 'uni2197', 'uni2192', 'uni2198', 'uni2193', 'uni2199', 'uni2190', 'uni2196', 'uni25B2', 'uni25E5', 'uni25B6', 'uni25E2', 'uni25BC', 'uni25E3', 'uni25C0', 'uni25E4', 'uni25A0', 'uni25A1', 'uni25A3', 'uni25CF', 'uni25CB', 'uni25CD', 'uni25CE', 'uni25C9', 'uni2605', 'uni2620', 'foundry.mark']

for i in CurrentFont().glyphOrder:
    CurrentFont()[i].mark = 0
for i in f.glyphOrder:
    f[i].mark = 1
f.update() 
print ''
print 'Existing glyphs marked in red.'
print 'Digested by Python.'