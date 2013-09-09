# Small Caps Components Method - Quinn Keaveney

f = CurrentFont()

accentglyphs = ["Aacute", "Abreve", "Acaron", "Acircumflex", "Adieresis", "Adieresismacron", "Adotabove", "Adoublegrave", "Agrave", "Ainvertedbreve", "Amacron", "Aogonek", "Aring", "Aringacute", "Atilde", "AE", "AEacute", "AEmacron", "Cacute", "Ccaron", "Ccedilla", "Ccircumflex", "Cdotaccent", "Dcaron", "Dcedilla", "Dcroat", "Ddotbelow", "Eacute", "Eacutedotbelow", "Ebreve", "Ecaron", "Ecircumflex", "Edieresis", "Edotaccent", "Edoublegrave", "Egrave", "Egravedotbelow", "Einvertedbreve", "Emacron", "Eogonek", "Gacute", "Gbreve", "Gcaron", "Gcircumflex", "Gcommaaccent", "Gdotaccent", "Gstroke", "Hbar", "Hcaron", "Hcircumflex", "Hdotbelow", "Hmacronbelow", "Iacute", "Ibreve", "Icaron", "Icircumflex", "Idieresis", "Idotaccent", "Idotbelow", "Idoublegrave", "Igrave", "Iinvertedbreve", "Imacron", "Iogonek", "Itilde", "Jcaron", "Jcircumflex", "Kcaron", "Kcedilla", "Kcommaaccent", "Khook", "Lacute", "Lcaron", "Lcedilla", "Lcommaaccent", "Ldot", "Ldotbelow", "Ldotbelowmacron", "Lslash", "Mcedilla", "Mdotbelow", "Mmacron", "Nacute", "Ncaron", "Ncedilla", "Ncommaaccent", "Ndescender", "Ndieresis", "Ndotaccent", "Ndotbelow", "Ngrave", "Nmacron", "Ntilde", "Oacute", "Obreve", "Ocaron", "Ocedilla", "Ocircumflex", "Ocommaturnedabove", "Odieresis", "Odotabove", "Odotabovemacron", "Odotbelow", "Odoublegrave", "Ograve", "Ohungarumlaut", "Oinvertedbreve", "Omacron", "Oogonek", "Oogonekmacron", "Oslash", "Oslashacute", "Otilde", "Otildemacron", "Ounderlineaccent", "barredO", "OE", "Pmacron", "Racute", "Rcaron", "Rcedilla", "Rcommaaccent", "Rdotbelow", "Rdotbelowmacron", "Rdoublegrave", "Rinvertedbreve", "Sacute", "Scaron", "Scedilla", "Scircumflex", "Scommaaccent", "Sdotbelow", "Germandbls", "Tbar", "Tcaron", "Tcedilla", "Tcommaaccent", "Tdotbelow", "Uacute", "Ubreve", "Ucaron", "Ucircumflex", "Udieresis", "Udotbelow", "Udoublegrave", "Ugrave", "Uhungarumlaut", "Uinvertedbreve", "Umacron", "Umacronbelow", "Uogonek", "Uring", "Utilde", "Wacute", "Wcircumflex", "Wdieresis", "Wgrave", "Yacute", "Ycircumflex", "Ydieresis", "Ygrave", "Ytilde", "Zacute", "Zcaron", "Zdotaccent", "Eng", "Thorn", "Eth", "Ezh", "Ezhcaron", "Schwa", "aacute", "abreve", "acaron", "acircumflex", "adieresis", "adieresismacron", "adotabove", "adoublegrave", "agrave", "ainvertedbreve", "amacron", "aogonek", "aring", "aringacute", "atilde", "ae", "aeacute", "aemacron", "cacute", "ccaron", "ccedilla", "ccircumflex", "cdotaccent", "dcaron", "dcedilla", "dcroat", "ddotbelow", "dotlessi", "dotlessj", "eacute", "eacutedotbelow", "ebreve", "ecaron", "ecircumflex", "edieresis", "edotaccent", "edoublegrave", "egrave", "egravedotbelow", "einvertedbreve", "emacron", "eogonek", "gacute", "gbreve", "gcaron", "gcircumflex", "gcommaaccent", "gdotaccent", "gstroke", "hbar", "hcaron", "hcircumflex", "hdotbelow", "hmacronbelow", "iacute", "ibreve", "icaron", "icircumflex", "idieresis", "idotaccent", "idotbelow", "idoublegrave", "igrave", "iinvertedbreve", "imacron", "iogonek", "itilde", "jcaron", "jcircumflex", "kcaron", "kcedilla", "kcommaaccent", "kgreenlandic", "khook", "lacute", "lcaron", "lcedilla", "lcommaaccent", "ldot", "ldotbelow", "ldotbelowmacron", "lslash", "mcedilla", "mdotbelow", "mmacron", "nacute", "ncaron", "ncedilla", "ncommaaccent", "ndescender", "ndieresis", "ndotaccent", "ndotbelow", "ngrave", "nmacron", "ntilde", "oacute", "obreve", "ocaron", "ocedilla", "ocircumflex", "ocommaturnedabove", "odieresis", "odotabove", "odotabovemacron", "odotbelow", "odoublegrave", "ograve", "ohungarumlaut", "oinvertedbreve", "omacron", "oogonek", "oogonekmacron", "oslash", "oslashacute", "barredo", "oe", "otilde", "otildemacron", "ounderlineaccent", "pmacron", "racute", "rcaron", "rcedilla", "rcommaaccent", "rdotbelow", "rdotbelowmacron", "rdoublegrave", "rinvertedbreve", "sacute", "scaron", "scedilla", "scircumflex", "scommaaccent", "sdotbelow", "germandbls", "tbar", "tcaron", "tcedilla", "tcommaaccent", "tdotbelow", "uacute", "ubreve", "ucaron", "ucircumflex", "udieresis", "udotbelow", "udoublegrave", "ugrave", "uhungarumlaut", "uinvertedbreve", "umacron", "umacronbelow", "uogonek", "uring", "utilde", "wacute", "wcircumflex", "wdieresis", "wgrave", "yacute", "ycircumflex", "ydieresis", "ygrave", "ytilde", "zacute", "zcaron", "zdotaccent", "eng", "thorn", "eth", "ezh", "ezhcaron", "schwa", "Aacute.sc", "Abreve.sc", "Acaron.sc", "Acircumflex.sc", "Adieresis.sc", "Adieresismacron.sc", "Adotabove.sc", "Adoublegrave.sc", "Agrave.sc", "Ainvertedbreve.sc", "Amacron.sc", "Aogonek.sc", "Aring.sc", "Aringacute.sc", "Atilde.sc", "AE.sc", "AEacute.sc", "AEmacron.sc", "Cacute.sc", "Ccaron.sc", "Ccedilla.sc", "Ccircumflex.sc", "Cdotaccent.sc", "Dcaron.sc", "Dcedilla.sc", "Dcroat.sc", "Ddotbelow.sc", "Eacute.sc", "Eacutedotbelow.sc", "Ebreve.sc", "Ecaron.sc", "Ecircumflex.sc", "Edieresis.sc", "Edotaccent.sc", "Edoublegrave.sc", "Egrave.sc", "Egravedotbelow.sc", "Einvertedbreve.sc", "Emacron.sc", "Eogonek.sc", "Gacute.sc", "Gbreve.sc", "Gcaron.sc", "Gcircumflex.sc", "Gcommaaccent.sc", "Gdotaccent.sc", "Gstroke.sc", "Hbar.sc", "Hcaron.sc", "Hcircumflex.sc", "Hdotbelow.sc", "Hmacronbelow.sc", "Iacute.sc", "Ibreve.sc", "Icaron.sc", "Icircumflex.sc", "Idieresis.sc", "Idotaccent.sc", "Idotbelow.sc", "Idoublegrave.sc", "Igrave.sc", "Iinvertedbreve.sc", "Imacron.sc", "Iogonek.sc", "Itilde.sc", "Jcaron.sc", "Jcircumflex.sc", "Kcaron.sc", "Kcedilla.sc", "Kcommaaccent.sc", "Khook.sc", "Lacute.sc", "Lcaron.sc", "Lcedilla.sc", "Lcommaaccent.sc", "Ldot.sc", "Ldotbelow.sc", "Ldotbelowmacron.sc", "Lslash.sc", "Mcedilla.sc", "Mdotbelow.sc", "Mmacron.sc", "Nacute.sc", "Ncaron.sc", "Ncedilla.sc", "Ncommaaccent.sc", "Ndescender.sc", "Ndieresis.sc", "Ndotaccent.sc", "Ndotbelow.sc", "Ngrave.sc", "Nmacron.sc", "Ntilde.sc", "Oacute.sc", "Obreve.sc", "Ocaron.sc", "Ocedilla.sc", "Ocircumflex.sc", "Ocommaturnedabove.sc", "Odieresis.sc", "Odotabove.sc", "Odotabovemacron.sc", "Odotbelow.sc", "Odoublegrave.sc", "Ograve.sc", "Ohungarumlaut.sc", "Oinvertedbreve.sc", "Omacron.sc", "Oogonek.sc", "Oogonekmacron.sc", "Oslash.sc", "Oslashacute.sc", "Otilde.sc", "Otildemacron.sc", "Ounderlineaccent.sc", "barredO.sc", "OE.sc", "Pmacron.sc", "Racute.sc", "Rcaron.sc", "Rcedilla.sc", "Rcommaaccent.sc", "Rdotbelow.sc", "Rdotbelowmacron.sc", "Rdoublegrave.sc", "Rinvertedbreve.sc", "Sacute.sc", "Scaron.sc", "Scedilla.sc", "Scircumflex.sc", "Scommaaccent.sc", "Sdotbelow.sc", "Germandbls.sc", "Tbar.sc", "Tcaron.sc", "Tcedilla.sc", "Tcommaaccent.sc", "Tdotbelow.sc", "Uacute.sc", "Ubreve.sc", "Ucaron.sc", "Ucircumflex.sc", "Udieresis.sc", "Udotbelow.sc", "Udoublegrave.sc", "Ugrave.sc", "Uhungarumlaut.sc", "Uinvertedbreve.sc", "Umacron.sc", "Umacronbelow.sc", "Uogonek.sc", "Uring.sc", "Utilde.sc", "Wacute.sc", "Wcircumflex.sc", "Wdieresis.sc", "Wgrave.sc", "Yacute.sc", "Ycircumflex.sc", "Ydieresis.sc", "Ygrave.sc", "Ytilde.sc", "Zacute.sc", "Zcaron.sc", "Zdotaccent.sc", "Eng.sc", "Thorn.sc", "Eth.sc", "Ezh.sc", "Ezhcaron.sc", "Schwa.sc"]

accents = ["acute", "grave", "hungarumlaut", "doublegrave", "circumflex", "caron", "dieresis", "tilde", "ring", "macron", "breve", "invertedbreve", "dotaccent", "dotbelow", "underlineaccent", "commaaccent", "cedilla", "altcedilla", "ogonek", "altogonek", "commaabovecmb", "Acute", "Grave", "Hungarumlaut", "Doublegrave", "Circumflex", "Caron", "Dieresis", "Tilde", "Ring", "Macron", "Breve", "Invertedbreve", "Dotaccent", "Dotbelow", "Linebelow", "Commaaccent", "Cedilla", "Altcedilla", "Ogonek", "Altogonek", "Commaabovecmb"]
           
for i in accentglyphs:
    for accent in accents:
        if accent in i:
            accentless = i.replace(accent,'')
            f.newGlyph(accentless)
            f[i].appendComponent(accent)
            f[i].width = f[accentless].width
    
f.update()
print 'Digested by Python.'