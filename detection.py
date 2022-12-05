from langdetect import detect

all_languages_codes =   {
  	'ab': 'Abkhazian',
  	'abk': 'Abkhazian',
  	'aa': 'Afar',
  	'aar': 'Afar',
  	'af': 'Afrikaans',
  	'afr': 'Afrikaans',
  	'sq': 'Albanian',
  	'alb/sqi*': 'Albanian',
  	'am': 'Amharic',
  	'amh': 'Amharic',
  	'ar': 'Arabic',
  	'ara': 'Arabic',
  	'an': 'Aragonese',
  	'arg': 'Aragonese',
  	'hy': 'Armenian',
  	'arm/hye*': 'Armenian',
  	'as': 'Assamese',
  	'asm': 'Assamese',
  	'ae': 'Avestan',
  	'ave': 'Avestan',
  	'ay': 'Aymara',
  	'aym': 'Aymara',
  	'az': 'Azerbaijani',
  	'aze': 'Azerbaijani',
  	'ba': 'Bashkir',
  	'bak': 'Bashkir',
  	'eu': 'Basque',
  	'baq/eus*': 'Basque',
  	'be': 'Belarusian',
  	'bel': 'Belarusian',
  	'bn': 'Bengali',
  	'ben': 'Bengali',
  	'bh': 'Bihari',
  	'bih': 'Bihari',
  	'bi': 'Bislama',
  	'bis': 'Bislama',
  	'bs': 'Bosnian',
  	'bos': 'Bosnian',
  	'br': 'Breton',
  	'bre': 'Breton',
  	'bg': 'Bulgarian',
  	'bul': 'Bulgarian',
  	'my': 'Burmese',
  	'bur/mya*': 'Burmese',
  	'ca': 'Catalan',
  	'cat': 'Catalan',
  	'ch': 'Chamorro',
  	'cha': 'Chamorro',
  	'ce': 'Chechen',
  	'che': 'Chechen',
  	'zh': 'Chinese',
  	'zh-cn': 'Chinese (Simplified)',
  	'zh-tw': 'Chinese (Traditional)',
  	'chi/zho*': 'Chinese',
  	'cu': 'Church Slavic; Slavonic; Old Bulgarian',
  	'chu': 'Church Slavic; Slavonic; Old Bulgarian',
  	'cv': 'Chuvash',
  	'chv': 'Chuvash',
  	'kw': 'Cornish',
  	'cor': 'Cornish',
  	'co': 'Corsican',
  	'cos': 'Corsican',
  	'hr': 'Croatian',
  	'scr/hrv*': 'Croatian',
  	'cs': 'Czech',
  	'cze/ces*': 'Czech',
  	'da': 'Danish',
  	'dan': 'Danish',
  	'dv': 'Divehi; Dhivehi; Maldivian',
  	'div': 'Divehi; Dhivehi; Maldivian',
  	'nl': 'Dutch',
  	'dut/nld*': 'Dutch',
  	'dz': 'Dzongkha',
  	'dzo': 'Dzongkha',
  	'en': 'English',
  	'eng': 'English',
  	'eo': 'Esperanto',
  	'epo': 'Esperanto',
  	'et': 'Estonian',
  	'est': 'Estonian',
  	'fo': 'Faroese',
  	'fao': 'Faroese',
  	'fj': 'Fijian',
  	'fij': 'Fijian',
  	'fi': 'Finnish',
  	'fin': 'Finnish',
  	'fr': 'French',
  	'fre/fra*': 'French',
  	'gd': 'Gaelic; Scottish Gaelic',
  	'gla': 'Gaelic; Scottish Gaelic',
  	'gl': 'Galician',
  	'glg': 'Galician',
  	'ka': 'Georgian',
  	'geo/kat*': 'Georgian',
  	'de': 'German',
  	'ger/deu*': 'German',
  	'el': 'Greek, Modern (1453-)',
  	'gre/ell*': 'Greek, Modern (1453-)',
  	'gn': 'Guarani',
  	'grn': 'Guarani',
  	'gu': 'Gujarati',
  	'guj': 'Gujarati',
  	'ht': 'Haitian; Haitian Creole',
  	'hat': 'Haitian; Haitian Creole',
  	'ha': 'Hausa',
  	'hau': 'Hausa',
  	'he': 'Hebrew',
  	'heb': 'Hebrew',
  	'hz': 'Herero',
  	'her': 'Herero',
  	'hi': 'Hindi',
  	'hin': 'Hindi',
  	'ho': 'Hiri Motu',
  	'hmo': 'Hiri Motu',
  	'hu': 'Hungarian',
  	'hun': 'Hungarian',
  	'is': 'Icelandic',
  	'ice/isl*': 'Icelandic',
  	'io': 'Ido',
  	'ido': 'Ido',
  	'id': 'Indonesian',
  	'ind': 'Indonesian',
  	'ia': 'Interlingua (International Auxiliary Language Association)',
  	'ina': 'Interlingua (International Auxiliary Language Association)',
  	'ie': 'Interlingue',
  	'ile': 'Interlingue',
  	'iu': 'Inuktitut',
  	'iku': 'Inuktitut',
  	'ik': 'Inupiaq',
  	'ipk': 'Inupiaq',
  	'ga': 'Irish',
  	'gle': 'Irish',
  	'it': 'Italian',
  	'ita': 'Italian',
  	'ja': 'Japanese',
  	'jpn': 'Japanese',
  	'jv': 'Javanese',
  	'jav': 'Javanese',
  	'kl': 'Kalaallisut',
  	'kal': 'Kalaallisut',
  	'kn': 'Kannada',
  	'kan': 'Kannada',
  	'ks': 'Kashmiri',
  	'kas': 'Kashmiri',
  	'kk': 'Kazakh',
  	'kaz': 'Kazakh',
  	'km': 'Khmer',
  	'khm': 'Khmer',
  	'ki': 'Kikuyu; Gikuyu',
  	'kik': 'Kikuyu; Gikuyu',
  	'rw': 'Kinyarwanda',
  	'kin': 'Kinyarwanda',
  	'ky': 'Kirghiz',
  	'kir': 'Kirghiz',
  	'kv': 'Komi',
  	'kom': 'Komi',
  	'ko': 'Korean',
  	'kor': 'Korean',
  	'kj': 'Kuanyama; Kwanyama',
  	'kua': 'Kuanyama; Kwanyama',
  	'ku': 'Kurdish',
  	'kur': 'Kurdish',
  	'lo': 'Lao',
  	'lao': 'Lao',
  	'la': 'Latin',
  	'lat': 'Latin',
  	'lv': 'Latvian',
  	'lav': 'Latvian',
  	'li': 'Limburgan; Limburger; Limburgish',
  	'lim': 'Limburgan; Limburger; Limburgish',
  	'ln': 'Lingala',
  	'lin': 'Lingala',
  	'lt': 'Lithuanian',
  	'lit': 'Lithuanian',
  	'lb': 'Luxembourgish; Letzeburgesch',
  	'ltz': 'Luxembourgish; Letzeburgesch',
  	'mk': 'Macedonian',
  	'mac/mkd*': 'Macedonian',
  	'mg': 'Malagasy',
  	'mlg': 'Malagasy',
  	'ms': 'Malay',
  	'may/msa*': 'Malay',
  	'ml': 'Malayalam',
  	'mal': 'Malayalam',
  	'mt': 'Maltese',
  	'mlt': 'Maltese',
  	'gv': 'Manx',
  	'glv': 'Manx',
  	'mi': 'Maori',
  	'mao/mri*': 'Maori',
  	'mr': 'Marathi',
  	'mar': 'Marathi',
  	'mh': 'Marshallese',
  	'mah': 'Marshallese',
  	'mo': 'Moldavian',
  	'mol': 'Moldavian',
  	'mn': 'Mongolian',
  	'mon': 'Mongolian',
  	'na': 'Nauru',
  	'nau': 'Nauru',
  	'nv': 'Navaho, Navajo',
  	'nav': 'Navaho, Navajo',
  	'nd': 'Ndebele, North',
  	'nde': 'Ndebele, North',
  	'nr': 'Ndebele, South',
  	'nbl': 'Ndebele, South',
  	'ng': 'Ndonga',
  	'ndo': 'Ndonga',
  	'ne': 'Nepali',
  	'nep': 'Nepali',
  	'se': 'Northern Sami',
  	'sme': 'Northern Sami',
  	'no': 'Norwegian',
  	'nor': 'Norwegian',
  	'nb': 'Norwegian Bokmal',
  	'nob': 'Norwegian Bokmal',
  	'nn': 'Norwegian Nynorsk',
  	'nno': 'Norwegian Nynorsk',
  	'ny': 'Nyanja; Chichewa; Chewa',
  	'nya': 'Nyanja; Chichewa; Chewa',
  	'oc': 'Occitan (post 1500); Provencal',
  	'oci': 'Occitan (post 1500); Provencal',
  	'or': 'Oriya',
  	'ori': 'Oriya',
  	'om': 'Oromo',
  	'orm': 'Oromo',
  	'os': 'Ossetian; Ossetic',
  	'oss': 'Ossetian; Ossetic',
  	'pi': 'Pali',
  	'pli': 'Pali',
  	'pa': 'Panjabi',
  	'pan': 'Panjabi',
  	'fa': 'Persian',
  	'per/fas*': 'Persian',
  	'pl': 'Polish',
  	'pol': 'Polish',
  	'pt': 'Portuguese',
  	'por': 'Portuguese',
  	'ps': 'Pushto',
  	'pus': 'Pushto',
  	'qu': 'Quechua',
  	'que': 'Quechua',
  	'rm': 'Raeto-Romance',
  	'roh': 'Raeto-Romance',
  	'ro': 'Romanian',
  	'rum/ron*': 'Romanian',
  	'rn': 'Rundi',
  	'run': 'Rundi',
  	'ru': 'Russian',
  	'rus': 'Russian',
  	'sm': 'Samoan',
  	'smo': 'Samoan',
  	'sg': 'Sango',
  	'sag': 'Sango',
  	'sa': 'Sanskrit',
  	'san': 'Sanskrit',
  	'sc': 'Sardinian',
  	'srd': 'Sardinian',
  	'sr': 'Serbian',
  	'scc/srp*': 'Serbian',
  	'sn': 'Shona',
  	'sna': 'Shona',
  	'ii': 'Sichuan Yi',
  	'iii': 'Sichuan Yi',
  	'sd': 'Sindhi',
  	'snd': 'Sindhi',
  	'si': 'Sinhala; Sinhalese',
  	'sin': 'Sinhala; Sinhalese',
  	'sk': 'Slovak',
  	'slo/slk*': 'Slovak',
  	'sl': 'Slovenian',
  	'slv': 'Slovenian',
  	'so': 'Somali',
  	'som': 'Somali',
  	'st': 'Sotho, Southern',
  	'sot': 'Sotho, Southern',
  	'es': 'Spanish; Castilian',
  	'spa': 'Spanish; Castilian',
  	'su': 'Sundanese',
  	'sun': 'Sundanese',
  	'sw': 'Swahili',
  	'swa': 'Swahili',
  	'ss': 'Swati',
  	'ssw': 'Swati',
  	'sv': 'Swedish',
  	'swe': 'Swedish',
  	'tl': 'Tagalog',
  	'tgl': 'Tagalog',
  	'ty': 'Tahitian',
  	'tah': 'Tahitian',
  	'tg': 'Tajik',
  	'tgk': 'Tajik',
  	'ta': 'Tamil',
  	'tam': 'Tamil',
  	'tt': 'Tatar',
  	'tat': 'Tatar',
  	'te': 'Telugu',
  	'tel': 'Telugu',
  	'th': 'Thai',
  	'tha': 'Thai',
  	'bo': 'Tibetan',
  	'tib/bod*': 'Tibetan',
  	'ti': 'Tigrinya',
  	'tir': 'Tigrinya',
  	'to': 'Tonga (Tonga Islands)',
  	'ton': 'Tonga (Tonga Islands)',
  	'ts': 'Tsonga',
  	'tso': 'Tsonga',
  	'tn': 'Tswana',
  	'tsn': 'Tswana',
  	'tr': 'Turkish',
  	'tur': 'Turkish',
  	'tk': 'Turkmen',
  	'tuk': 'Turkmen',
  	'tw': 'Twi',
  	'twi': 'Twi',
  	'ug': 'Uighur',
  	'uig': 'Uighur',
  	'uk': 'Ukrainian',
  	'ukr': 'Ukrainian',
  	'ur': 'Urdu',
  	'urd': 'Urdu',
  	'uz': 'Uzbek',
  	'uzb': 'Uzbek',
  	'vi': 'Vietnamese',
  	'vie': 'Vietnamese',
  	'vo': 'Volapuk',
  	'vol': 'Volapuk',
  	'wa': 'Walloon',
  	'wln': 'Walloon',
  	'cy': 'Welsh',
  	'wel/cym*': 'Welsh',
  	'fy': 'Western Frisian',
  	'fry': 'Western Frisian',
  	'wo': 'Wolof',
  	'wol': 'Wolof',
  	'xh': 'Xhosa',
  	'xho': 'Xhosa',
  	'yi': 'Yiddish',
  	'yid': 'Yiddish',
  	'yo': 'Yoruba',
  	'yor': 'Yoruba',
  	'za': 'Zhuang; Chuang',
  	'zha': 'Zhuang; Chuang',
  	'zu': 'Zulu',
  	'zul': 'Zulu'
  }

input_sentences = ["That's thirty minutes away. I'll be there in ten.",
	"అది ముప్పై నిమిషాల దూరంలో ఉంది. I'll be there in ten.",
	"అది ముప్పై నిమిషాల దూరంలో ఉంది. నేను పదిలో ఉంటాను.",
	"वह तीस मिनट की दूरी पर है।. I'll be there in ten.",
	"Itu tiga puluh menit lagi. Saya akan berada di sana dalam sepuluh.",
	"Dat is dertig minuten. Ik ben er over tien.",
	"C'est à trente minutes. Je serai là dans dix.",
	"वह तीस मिनट की दूरी पर है। मैं दस में वहाँ जाऊँगा।", "ते तीस मिनिटांचे आहे. मी दहामध्ये तिथे येईन.",
	"那是三十分钟的路程。我会在十点钟到达那里。", "那是三十分鐘的路程。我會在十點鐘到達那裡。", "هذا ثلاثين دقيقة. سأكون هناك في عشرة.",
	"Դա հեռու է երեսուն րոպե: Ես այնտեղ կլինեմ տասը:",
	"তিরিশ মিনিট দূরে। আমি সেখানে দশ জন থাকব।",
	"Hori hogeita hamar minutu falta da. Hamarretan egongo naiz.",
	"Isso é trinta minutos daqui. Eu estarei lá em dez.", "ÇĞİÖŞÜğçıöşü", "Det er tredive minutter væk. Jeg vil være der om ti",
	"Dat is dertig minuten. Ik ben er over tien", "Se on 30 minuutin päässä. Olen siellä kymmenessä"
]

lemmatizer_names = ["Language Code", "Input Sentence"]
format_text = '{:24}' * (len(lemmatizer_names) + 1)

print ('\n', format_text.format("Language Name", *lemmatizer_names),'\n','='*120)
for data in input_sentences:
    language_code = detect(data)    
    sentence = [all_languages_codes.get(language_code), language_code, data]
    print (format_text.format(*sentence))
    