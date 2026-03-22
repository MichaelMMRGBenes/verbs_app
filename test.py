import streamlit as st
import streamlit.components.v1 as components
import random
import time
import matplotlib.pyplot as plt

# --- 0. PLACEHOLDER DATA & LOGIC (Replace with your actual logic) ---
WORDS = [
    # --- Příroda a zvířata ---
    "koira", "kissa", "hevonen", "lehmä", "lammas", "sika", "karhu", "susi", "kettu", "jänis",
    "lintu", "kala", "käärme", "hyönteinen", "puu", "kukka", "metsä", "järvi", "meri", "joki",
    "vuori", "mäki", "saari", "niemi", "ranta", "taivas", "aurinko", "kuu", "tähti", "pilvi",
    "sade", "lumi", "jää", "tuuli", "ukkonen", "salam", "kivi", "hiekka", "multa", "ruoho",
    "lehti", "oksa", "juuri", "marja", "sieni", "puro", "lähde", "suo", "tunturi", "luonto",
    
    # --- Lidé a rodina ---
    "mies", "nainen", "lapsi", "poika", "tyttö", "vauva", "isä", "äiti", "veli", "sisko",
    "poika", "tytär", "isoäiti", "isoisä", "serkku", "täti", "setä", "eno", "perhe", "suku",
    "ystävä", "naapuri", "ihminen", "henkilö", "vieras", "isäntä", "emäntä", "vaimo", "mies", "pari",
    
    # --- Tělo ---
    "pää", "silmä", "korva", "nenä", "suu", "huuli", "hammas", "kieli", "kaula",
    "kurkku", "olkapää", "käsivarsi", "käsi", "sormi", "kynsi", "rinta", "vatsa", "selkä", "jalka",
    "polvi", "varvas", "iho", "luu", "veri", "sydän", "keuhko", "lihas", "naama",
    
    # --- Dům a domácnost ---
    "talo", "koti", "asunto", "huone", "keittiö", "kylpyhuone", "makuuhuone", "olohuone", "eteinen", "parveke",
    "piha", "ovi", "ikkuna", "seinä", "katto", "lattia", "porras", "lukko", "avain", "pöytä",
    "tuoli", "sänky", "sohva", "kaappi", "hylly", "lamppu", "matto", "verho", "peili", "taulu",
    "kello", "radio", "televisio", "tietokone", "puhelin", "kone", "uuni", "hella", "kaappi", "allas",
    
    # --- Kuchyně a jídlo ---
    "ruoka", "juoma", "vesi", "maito", "kahvi", "tee", "mehu", "olut", "viini", "leipä",
    "voi", "juusto", "liha", "kala", "kana", "muna", "makkara", "peruna", "riisi", "pasta",
    "vihannes", "hedelmä", "omena", "banaani", "marja", "suola", "sokeri", "jauho", "öljy", "kastike",
    "lautanen", "kulho", "lasi", "muki", "kuppi", "veitsi", "haarukka", "lusikka", "kattila", "pannu",
    
    # --- Oblečení ---
    "vaate", "paita",  "hame", "mekko", "takki", "pipo", "hattu", "huivi", "käsine",
    "sukka", "kenkä", "saapas", "alusvaate", "vyö", "solmio", "nappi", "tasku", "vetoketju", "sateenvarjo",
    
    # --- Doprava a město ---
    "auto", "bussi", "juna", "lentokone", "laiva", "vene", "pyörä", "moottoripyörä", "tie", "katu",
    "polku", "silta", "tunneli", "asema", "satama", "lentokenttä", "tori", "puisto", "kaupunki", "kylä",
    "maa", "valtio", "raja", "keskusta", "kauppa", "pankki", "sairaala", "koulu", "kirkko", "tehdas",
    "hotelli", "ravintola", "kahvila", "elokuvateatteri", "museo", "kirjasto", "teatteri", "poliisi", "posti", "apteekki",
    
    # --- Čas a kalendář ---
    "aika", "hetki", "sekunti", "minuutti", "tunti", "päivä", "viikko", "kuukausi", "vuosi", "vuosisata",
    "aamu", "päivä", "ilta", "yö", "aamupäivä", "iltapäivä", "keskiyö", "maanantai", "tiistai", "keskiviikko",
    "torstai", "perjantai", "lauantai", "sunnuntai", "tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu",
    "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu", "kevät", "kesä", "syys", "talvi",
    
    # --- Abstraktní a ostatní ---
    "asia", "sana", "nimi", "luku", "numero", "väri", "muoto", "ääni", "valo", "pimeys",
    "elämä", "kuolema", "onni", "rakkaus", "viha", "pelko", "ilo", "suru", "työ", "leikki",
    "peli", "urheilu", "musiikki", "taide", "kirja", "lehti", "kuva", "elokuva", "uutinen", "tieto",
    "ajatus", "mieli", "sielu", "voima", "valta", "laki", "oikeus", "raha", "hinta", "palkka",
    "lahja", "ongelma", "vastaus", "kysymys", "syy", "seuraus", "tapa", "mahdollisuus", "virhe", "totuus",
    
    # --- Škola a práce ---
    "opettaja", "oppilas", "luokka", "kynä", "paperi", "vihko", "laukku", "tehtävä", "koe", "arvosana",
    "yliopisto", "kurssi", "ammatti", "johtaja", "työntekijä", "toimisto", "kokous", "asiakas", "projekti", "suunnitelma",
    
    # --- Materiály a předměty ---
    "metalli", "rauta", "kulta", "hopea", "lasi", "muovi", "puu", "paperi", "kangas", "nahka",
    "kivi", "tiili", "betoni", "roska", "jätettä", "pöly", "savu", "tuli", "liekki", "hiili",
    
    # --- Další podstatná jména ---
    "kone", "laite", "työkalu", "vasara", "saha", "naula", "ruuvi", "neula", "lanka",
    "pallo", "lelu", "kortti", "raha", "kolikko", "seteli", "lompakko", "kassi", "pussi", "laatikko",
    "pullo", "tölkki", "kansi", "pohja", "reuna", "pinta", "sisältö", "osa", "kappale", "ryhmä",
    "joukko", "kansa", "kieli", "maa", "maailma", "avaruus", "planeetta", "tähti", "aurinko", "kuu",
    "metsästys", "kalastus", "matka", "loma", "juhla", "joulu", "pääsiäinen", "syntymäpäivä",
    "terveys", "tauti", "kipu", "lääke", "uni", "unelma", "muisto", "kokemus", "seikkailu", "tarina",
    "runo", "laulu", "soitin", "kitara", "piano", "rumpu", "viulu", "huilu", "torvi", "ääni",
    "melu", "hiljaisuus", "haju", "maku", "tunne", "kosketus", "näkö", "kuulo", "liike", "vauhti",
    "suunta", "pohjoinen", "etelä", "itä", "länsi", "vasen", "oikea", "ylä", "ala",
    "sisä", "ulko", "etu", "taka", "alku", "loppu", "reuna", "keskusta", "piste", "viiva",
    "kulma", "ympyrä", "neliö", "pinta-ala", "pituus", "leveys", "korkeus", "paino", "määrä", "summa",
    
    # --- Přídavná jména (použitá jako podstatná jména nebo vlastnosti) ---
    "hyvyys", "pahuus", "kauneus", "kalleus", "nopeus", "pituus", "leveys", "syvyys", "korkeus",
    "viisaus", "tyhmyys", "rehellisyys", "rohkeus", "pelkuruus", "ystävyys", "vapaus", "rauha", "sota", "voitto",
    "tappio", "vaara", "turva", "apu", "kiitos", "anteeksi", "tervehdys", "hyvästi", "onni", "menestys",
    
    # --- Různé ---
    "paita", "hame", "takki", "hattu", "sukka", "kenkä", "saapas", "huivi", "vyö",
    "sormus", "ketju", "kello",  "laukku", "reppu", "salkku", "matkalaukku", "sateenvarjo", "avain",
    "lukko", "ovi", "ikkuna", "portti", "aita", "seinä", "katto", "lattia", "katto", "uuni",
    "liesi", "allas", "hana", "suihku", "amme", "sauna", "kiuas", "löyly", "vihta", "vasta",
    "mökki", "huvila", "kartano", "linna", "torni", "kirkko", "pappila", "koulu", "opisto", "lukio",
    "yliopisto", "virasto", "tehdas", "paja", "halli", "varasto", "kauppa", "myymälä", "tori", "aukio",
    "puisto", "puutarha", "pelto", "niitty", "laidun", "metsä", "viidakko", "aavikko", "saari", "luoto",
    "vuori", "vaara", "kukkula", "laakso", "solu", "puro", "oja", "kanava", "koski", "putous",
    "lähde", "kaivo", "lampi", "järvi", "selkä", "lahti", "salmi", "meri", "valtameri", "ranta",
    "hiekka", "kivi", "kallio", "muta", "savu", "tuli", "hiili", "tuhka", "pöly", "ilma"
]
def get_first_vowel_in_long_word(word):
    vowels = "aeiouyäö"
    last_five = word[-5:]
    return next((ch for ch in last_five if ch in vowels), None)

def syllables_decider(word):
    vowels = "aeiouyäö"
    diphthongs = {"ai","ei","oi","ui","yi","äi","öi","au","eu","iu","ou","äy","öy","ey","iy","ie","uo","yö","io"}

    word = word.lower()
    count = 0
    i = 0

    while i < len(word):
        if word[i] in vowels:
            count += 1
            if i+2 < len(word) and word[i+1:i+3] in diphthongs:
                i += 1
            elif i+1 < len(word) and (word[i] == word[i+1] or word[i:i+2] in diphthongs):
                i += 1
        i += 1
    return count

# --- KEEP your full partitive functions here ---
# (paste your partitive_sg and partitive_pl exactly as they are)


def partitive_sg(word:str) -> str:
    exceptions = {"kuu":"kuuta", "kokous":"kokousta", "vastaus":"vastausta","kuvaus":"kuvausta", "esitys":"esitystä", "ajatus":"ajatusta", "seuraus":"seurausta", "tulos":"tulosta", "kysymys":"kysymystä", "kaappi":"kaappia","penkki":"penkkiä","maalaus":"maalausta","koti":"kotia","historia":"historiaa", "musiikki":"musiikkia","laki":"lakia","appelsiini":"appelsiinia", "suurin":"suurimpaa", "vesi":"vettä", "kieli":"kieltä","kansi":"kantta", "kausi":"kautta", "viini": "viiniä","vastaus":"vastausta",
                  "jälsi": "jälttä", "virsi":"virttä", "yksiö":"yksiötä","työhuone":"työhuonetta","ilmoitus":"ilmoitusta", "päätös":"päätöstä","muutos":"muutosta",
                  "veitsi": "veistä", "suuri":"suurta", "suurin":"suurimpaa","mies":"miestä",
                    "seitsemän":"seitsemää", "vasen":"vasempaa", "kivi":"kiveä", "käsi":"kättä", "veli":"veljeä", "lumi":"lunta",
                      "yksi":"yhtä","uusi":"uutta", "susi":"sutta", "kaksi":"kahta", "uksi":"usta", "kuukausi":"kuukautta", "lapsi":"lasta", "onni":"onnea","veri":"verta", "meri":"merta", "hapsi":"hapsea", "ripsi":"ripseä"}
    
    loan_words = ["stadion", "region", "tradition", "version", "design", "slogan", "organ", "vegan", "internet", "chat", "limit", "laser", "server", "scanner",
                  "diesel", "rock", "punk", "hotelli", "naapuri"]
    
    i_to_e = ["alpi","appi","arki","arpi","hanhi","hanki","happi","hapsi","hauki","heisi","helmi","henki","hetki","hiili","hiiri","hiisi","hiki",
"hirsi","hirvi","huoli","huuli","impi","joki","jouhi","jousi","juoni","juuri","jälki","jälsi","järki","järvi","Jääski","kaali","kaari","kaihi","kaikki","kaksi",
"kampi","kanki","kansi","karhi","kaski","kieli","kiiski","kilpi","kirsi","kivi","koipi","korpi","korsi","koski","kuori","kurki","kusi",
"kuusi","kuusi","kylki","Kymi","kynsi","käki","kärki","käsi","köysi","lahti","laki","lampi","lapsi","lehti","lempi","leski","liemi","liesi",
"lohi","loimi","Louhi","lovi","lumi","luomi","länki","länsi","meri","mesi","mieli","moni","mäki","niemi","niini","nimi","noki","nummi","nuoli",
"nuori","nurmi","närhi","onki","onni","orsi","ovi","paasi","parsi","parvi","peitsi","pieli","pieni","piki","pilvi","polvi","ponsi",
"poski","povi","puoli","pursi","putki","pälvi","reki","reisi","retki","riihi","ripsi","rupi","ruuhi","saari","saarni",
"saksi","salmi","sampi","sappi","sarvi","savi","seimi","sieni","siili","siipi","sini","solki","soppi","sormi","suksi","suoli","Suomi","suomi",
"suoni","susi","suuri","suvi","syli","sylki","sysi","sänki","särki","sääri","sääski","taimi","talvi","tammi","teeri","telki",
"tiili","tilhi","toimi","tonki","torvi","tosi","tuki","tuli","tuohi","tuomi","tuoni","tuppi","tuuli","typpi","tyvi","tyyni",
"tähti","täysi","uksi","uni","uuhi","uusi","varsi","veitsi","veli","veri","vesi","vieri","viiksi","viini","viisi","virpi",
"virsi","vuohi","Vuoksi","vuori","vuosi","vyyhti","väki","yksi","ääni","ääri"]
    all_vowels = "aeiouyöä"
    basic_vowels = "aeiou"
    neutral_vowels = "ei"
    neutralising_vowels = "aou"
    changing_vowels = "äyö"

    #vesi -> vetta, exceptions
    #if len(word) >= len(min(exceptions, key=len)):
    for item in exceptions:
        if item in word[-len(item):]:
            word = word[:-len(item)] + exceptions[item]
            return word
    
    #I to E, need to work on 
    for item in i_to_e:
        if item == word[-len(item):]:
            # usi -> usta
            if word[-3:] == "usi":
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-1] +"tä"
                else:
                    word = word[:-1] + "ta" #tä

            # ni -> nta/ntä
            elif word[-2:] == "ni":
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-1] + "tä"
                else:
                    word = word[:-1] +"ta" 

            # ri -> rtä
            elif word[-2:] == "ri":
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-1] +"tä"
                else:
                    word = word[:-1] +"ta" #tä

            # hi -> hta 
            elif word[-2:] == "hi":            
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-1] +"tä"
                else:
                    word = word[:-1] +"ta" #tä
            #siili, kaali
            elif word[-4:] in ("iili", "aali"):
                if "a" in word[-4:]:
                    word += "a"
                else:
                    word += "ä"
            # li -> ltä
            elif word[-2:] == "li":
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-1] +"tä"
                else:
                    word = word[:-1] +"ta" #tä

            # si -> ttä
            elif word[-2:] == "si":
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-2] +"ttä"
                else:
                    word = word[:-2] +"tta" # checknout to tä

            #i -> e + a/ä
            else:
                if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-5:] for vowel in neutralising_vowels):
                    word = word[:-1] +"eä"
                else:
                    word = word[:-1] +"ea"

            return word
        

    #nalle
    if word[-3:] == "lle":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "ä"
        else:
            word += "a"

    elif word[-2:] == "ee":
        word += "tä"

    elif word[-2:] in ("oi","ai"):
        word += "ta"

    #nainen -> naista
    elif word[-3:] == "nen":
        if any(vowel in word[-7:] for vowel in changing_vowels) or any(vowel in word[-7:] for vowel in neutral_vowels) and not any(vowel in word[-7:] for vowel in neutralising_vowels):
            word = word[:-3] + "stä"
        else:
            word = word[:-3] + "sta"

    #ahven -> ahventa
    elif word[-2:] == "en" and word[-3:] != "nen":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "tä"
        else:
            word += "ta"


    #RAKKAUS -> rakkautta
    elif word[-4:] in ("eus", "uus", "kaus","ous"):
        word = word[:-1] + "tta"
    #All thanks to my beautiful girlfriend Maria that helped me with this program <3
    #avaruus and kauneus
    elif word[-3:] in ("eus", "uus","ous"):
        word = word[:-1] + "tta"

    #kokemus
    elif word[-2:] == "us":
        word += "ta" 

    elif word[-3:] in ("yys", "eys"):
        word = word[:-1] + "ttä"
    #ymmärys -> ymmärystä
    elif word[-2:] == "ys":
        word += "tä"
    #kevyt
    elif word[-2:] == "yt":
        word += "tä"
    

    #E vene -> venettä, laite -> laitetta
    elif word[-1] == "e" and word[-2:] != "ie":
        if any(vowel in word[-6:] for vowel in changing_vowels) or any(vowel in word[-6:] for vowel in neutral_vowels) and not any(vowel in word[-6:] for vowel in neutralising_vowels):
            word += "ttä"
        else: word += "tta"

    # Loan words
    elif word[-1] == "i" and word not in i_to_e:
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-6:] for vowel in neutral_vowels) and not any(vowel in word[-8:] for vowel in neutralising_vowels):
            word = word +"ä"
        else:
            word = word +"a"

    elif word in loan_words:
        if word[-1] == "i":
            word += "a"
        else: word += "ia"

    #auto -> autoa / leipää -> leipää
    elif word[-1] in all_vowels and word[-2] not in all_vowels:
        if word[-1] in changing_vowels:
            word += "ä"
        elif any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "ä"
        elif word[-1] in basic_vowels:
            word += "a"

    #samea
    elif word[-2:] == "ea":
        word += "a"

    elif word[-2:] == "eä":
        word += "ä"

    #maa -> maata / yö -> yötä
    elif word[-1] in all_vowels:
        if word[-2] in basic_vowels and not any(vowel in word for vowel in changing_vowels) and word[-2:] not in ("ie"):
            word += "ta"
        else:
            word += "tä"

    elif word[-1] not in all_vowels and word[-2] != "u":
        if any(vowel in word[-6:] for vowel in neutral_vowels) and not any(vowel in word[-6:] for vowel in neutralising_vowels):
            word += "tä" 

        elif any(vowel in word[-6:] for vowel in changing_vowels):
            word += "tä" 
        else: 
            word += "ta"

    #tatar -> tatarta
    elif word[-1] not in all_vowels:
        if word[-2] in basic_vowels and not any(vowel in word for vowel in changing_vowels):
            word += "ta"
        else:
            word += "tä"
    #A word ends in a consonant or a relic consonant, the partitive stem ends in a consonant, 
    # and the strong-grade plural stem ends in a diphthong.



    return word

def partitive_pl(word) -> str:

    all_vowels = "aeiouyöä"
    basic_vowels = "aeiou"
    neutral_vowels = "ei"
    neutralising_vowels = "aou"
    changing_vowels = "äyö"
    syllables = syllables_decider(word)
    #si/ us might be exception - file

    #ravintola
#All thanks to my beautiful girlfriend Maria that helped me with this program <3    
    #koe, rikas, mies, puhelin
    #Leimu contribution# - näppäin <3 saippuakauppias
    exceptions = {"hana":"hanoja", "kaappi":"kaappeja", "maailma":"maailmoja", "keskusta":"keskustoja", "sana":"sanoja","etelä":"eteliä","jänis":"jäniksiä","viikko":"viikkoja","kiuas":"kiukaita","suola":"suoloja","veli":"veljiä","ihana":"ihania","näppäin":"näppäimiä","muna":"munia","appelsiini":"appelsiineja", "voi":"voita","hidas":"hitaita", "laite":"laitteita","kausi": "kausia", "taide":"taiteita","laki":"lakeja","hotelli":"hotelleja","pullo":"pulloja","vuoro":"vuoroja","hana":"hanoja","verkko":"verkkoja","lahje":"lahkeita","kirkko":"kirkkoja","omena":"omenoita","ien":"ikeniä","koe":"kokeita", "rikas":"rikkaita", "mies":"miehiä", "puhelin":"puhelimia", "tytär":"tyttäriä", "kannel":"kanteleita", "sävel":"säveliä", "kyynel":"kyyneleitä", "sammal":"sammaleita", "taival":"taipaleita", "askel":"askeleita", "nivel":"niveliä","ommel":"ompeleita", "tanner":"tantereita", "manner":"mantereita", "seitsemän":"seitsemiä", "jääkiekko":"jääkiekkoja", "matala":"matalia","ihana":"ihania", "ahkera":"ahkeria", "sako":"sakkoja", "musiikki":"musiikkeja"}
    
    i_to_e = ["alpi","uni", "appi","arki","arpi","hanhi","hanki","happi","hapsi","hauki","heisi","helmi","henki","hetki","hiili","hiiri","hiisi","hiki",
"hirsi","hirvi","huoli","huuli","impi","joki","jouhi","jousi","juoni","juuri","jälki","jälsi","järki","järvi","Jääski","kaali","kaari","kaihi","kaikki","kaksi",
"kampi","kanki","kansi","karhi","kaski","kieli","kiiski","kilpi","kirsi","kivi","koipi","korpi","korsi","koski","kuori","kurki","kusi",
"kuusi","kuusi","kylki","Kymi","kynsi","käki","kärki","käsi","köysi","lahti","laki","lampi","lapsi","lehti","lempi","leski","liemi","liesi",
"lohi","loimi","Louhi","lovi","lumi","luomi","länki","länsi","meri","mesi","mieli","moni","mäki","niemi","niini","nimi","noki","nummi","nuoli",
"nuori","nurmi","närhi","onki","onni","orsi","ovi","paasi","parsi","parvi","peitsi","pieli","pieni","piki","pilvi","polvi","ponsi",
"poski","povi","puoli","pursi","putki","pälvi","reki","reisi","retki","riihi","ripsi","rupi","ruuhi","saari","saarni",
"saksi","salmi","sampi","sappi","sarvi","savi","seimi","sieni","siili","siipi","sini","solki","soppi","sormi","suksi","suoli","Suomi","suomi",
"suoni","susi","suuri","suvi","syli","sylki","sysi","sänki","särki","sääri","sääski","taimi","talvi","tammi","teeri","telki",
"tiili","tilhi","toimi","tonki","torvi","tosi","tuki","tuli","tuohi","tuomi","tuoni","tuppi","tuuli","typpi","tyvi","tyyni",
"tähti","täysi","uksi","uuhi","uusi","varsi","veitsi","veli","veri","vesi","vieri","viiksi","viisi","virpi",
"virsi","vuohi","Vuoksi","vuori","vuosi","vyyhti","väki","yksi","ääni","ääri"]


    for item in exceptions:
        if len(item) > 3 and item in word[-len(item):]:
            word = word[:-len(item)] + exceptions[item]
            return word
        else:
            if item == word:
                word = exceptions[item]
                return word

    for item in i_to_e:
        if len(word) > 5:
            if item == word[-len(item):]:
                if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:]  for vowel in neutral_vowels) and not any(vowel in word[-4:] for vowel in neutralising_vowels):
                    word += "ä"
                else:
                    word += "a"
                return word
        else:
            if item == word:
                if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:]  for vowel in neutral_vowels) and not any(vowel in word[-4:] for vowel in neutralising_vowels):
                    word += "ä"
                else:
                    word += "a"
                return word
    

        #mansikka/
    if word[-3:] in ("kka","kko") and syllables >= 3 and not any(vowel in word for vowel in changing_vowels):
        word = word[:-2] + "oita"

    elif word[-3:] == "hai":
        word += "ta"


    
    elif word[-3:] in ("yrä") and syllables == 3:
        word = word[:-1] + "öitä"

    elif word[-3:] in ("ävä", "evä", "ärä") and syllables == 3:
        word = word[:-1] + "iä"
    
    elif word[-2:] in ("lä", "rä", "nä", "iä") and syllables >= 3 and not any(vowel in word for vowel in neutralising_vowels):
        word = word[:-1] + "öitä" 
        
    elif word[-1] == "ä" and word[-2:] != "ää":
        word = word[:-1] + "iä"
        
    elif word[-4:] == "mmas":
        word = word[:-3] + "paita"
    
    elif word[-3:] == "das":
        word = word[:-3] + "taita"

    elif word[-3:] in ("kke"):
        word = word[:-1] + "eja"

    elif word[-4:] == "aite":
        word = word[:-1] + "teita"

        #varvas -> varpaita
    elif word[-4:] == "rvas":
        word = word[:-3] + "paita"

    elif word[-2:] == "pas":
        word = word[:-1] + "paita"
        #taivas -> taivaita
    elif word[-3:] == "vas":
        word = word[:-1] + "ita"

        #kauppias -> kauppiaita
    elif word[-3:] == "ias":
        word = word[:-1] + "ita"

  


    

        #mukava, matala
    elif word[-3:] in ("ala", "ava", "isa", "era") and syllables == 3 and word[-4:] != "aala":
        word = word[:-1] + "ia"



       
        #ravintola
    elif word[-2:] in ("la", "ra", "na", "ia") and syllables >= 3 and not any(vowel in word for vowel in changing_vowels):
        word = word[:-1] + "oita"

        #opiskelija 
    elif word[-3:] == "ija" and syllables >= 3:
        word = word[:-1] + "oita"

    elif word[-3:] == "ijä" and syllables >= 3:
        word = word[:-1] + "äitä"



        #korkea
    elif word[-2:] == "ea" and syllables >= 3:
        word = word[:-1] + "ita"

    elif word[-2:] == "eä" and syllables >= 3:
        word = word[:-1] + "itä"
        #vadelma, majava
    elif word[-2:] in ("ma", "va") and syllables >= 3:
        word = word[:-1] + "ia"

    elif word[-2:] in ("mä", "vä")and syllables >= 3:
        word = word[:-1] + "iä"

        #aja -> ia, opettaja
    elif word[-3:] == "aja" and syllables >= 3:
        word = word[:-1] + "ia" 

    elif word[-3:] == "äjä"and syllables >= 3:
        word = word[:-1] + "iä" 

        #kännykkä
    elif word[-3:] in ("kkä", "kkö") and syllables >= 3:
        word = word[:-2] + "öitä"

        # o / u
        #and syllables == 2 
    elif word[-1] == "a" and (get_first_vowel_in_long_word(word) in ("a", "e", "i")) and word[-2:] != "aa":
        word = word[:-1] + "oja"

        #2 syllables words with a ending
        # o / u
        #and syllables == 2 #it doesnt work for kauppa
    elif word[-1] == "a" and (get_first_vowel_in_long_word(word) in ("o", "u")) and word[-2:] != "aa":
        word = word[:-1] + "ia"

        #kenkä, leipä

        #tie -> eitä
    elif word[-2:] == "ie":
        word = word[:-2] + "eitä"
        #uo -> oita
    elif word[-2:] == "uo":
        word = word[:-2] + "oita"

        #yö -> öitä
    elif word[-2:] == "yö":
        word = word[:-2] + "öitä"

        #eo -> eoita
    elif word[-2:] == "eo":
        word = word[:-2] +"eoita"
        #io -> ioita
    elif word[-2:] == "io":
        word = word[:-2] +"ioita"
        #iö -> iöitä
    elif word[-2:] == "iö":
        word = word[:-2] +"iöitä"
        #ao -> aoita 
    elif word[-2:] == "ao":
        word = word[:-2] +"aoita"
        #All thanks to my beautiful girlfriend Maria that helped me with this program <3
        #suomalainen 

        #nen -> sia
    elif word[-3:] == "nen":
        if any(vowel in word[-7:] for vowel in changing_vowels) or any(vowel in word[-7:] for vowel in neutral_vowels) and not any(vowel in word[-7:] for vowel in neutralising_vowels):        
            word = word[:-3] +"siä"
        else:
            word = word[:-3] +"sia"

        #vät
    elif word[-3:] == "vät":
        word = word[:-2] +"äitä"
    #nyt -> neitä
    elif word[-3:] == "nyt":
        word = word[:-2] +"eitä"
    #ut -> ita
    elif word[-2:] == "ut":
        word = word[:-1] +"ita"
    #yt -> itä
    elif word[-2:] == "yt":
        word = word[:-1] +"itä"
    #is -> iita
    elif word[-2:] == "is":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        
            word = word[:-1] +"itä"
        else:
            word = word[:-1] +"ita"

    #double vowel
    # puu, syy,  maa
    elif word[-2:] in ("uu", "ii", "aa"):
        word = word[:-1] + "ita"

    #myy, jää
    elif word[-2:] in ("ää","yy", "ee"):
        word = word[:-1] + "itä"

    #kuuloke     
    elif word[-2:] == "ke":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        
            word = word[:-1] + "keitä"
        else:
            word = word[:-1] + "keita"

    elif word[-2:] == "de":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        
            word = word[:-2] + "teitä"
        else:
            word = word[:-2] + "teita"
        
    elif word[-3:] == "ste":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        

            word += "itä"
        else:
            word += "ita"
                  

    elif word[-2:] == "te":
        word = word[:-1] + "teita"
        
    #tunne -> tunteita 
    elif word[-3:] == "nne":
        word = word[:-2] + "teita"

    #huone, kone
    elif word[-1] == "e":
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-5:] for vowel in neutralising_vowels):        
            word += "itä"
        else:
            word += "ita"

        #All thanks to my beautiful girlfriend Maria that helped me with this program <3            
        #rakkaus might need change to aus
    elif word[-2:] in ("us", "es","os"):
        word = word[:-1] + "ksia"

    elif word[-3:] in ("has"):
        word = word[:-1] + "ksia"

    #närästys
    elif word[-2:] == "ys":
        word = word[:-1] + "ksiä"
    
    #rikas -> riKKaita
    #kaunis -> kauniita
    elif word[-3:] == "nis":
        word = word[:-1] + "ita"

    #siemen
    elif word[-2:] == "en":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "iä"
        else:
            word += "ia"
    #All thanks to my beautiful girlfriend Maria that helped me with this program <3
    #rasvaton -> rasvatomia
    elif word[-2:] in ("on","an"):
        word = word[:-2] + "tomia"

    #puhelin
    elif word[-3:] in ("lin", "ain"):
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word = word[:-1] + "miä"
        else:
            word = word[:-1] + "mia"


    elif word[-3:] == "tin":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word = word[:-2] + "timiä"
        else: 
            word = word[:-2] + "timia"
    #sydän
    elif word[-3:] == "dän":
        word = word[:-1] + "miä"  

    #työtön -> työtömiä
    elif word[-2:] in ("ön", "än"):
        word = word[:-2] + "tömiä"
    #matala
    elif word[-1:] == "a" and syllables == 3:
        word = word[:-1] + "ia"

    #hämärä
    elif word[-1:] == "ä" and syllables == 3:
        word = word[:-1] + "iä"


    elif word[-2:] == "li" and syllables >= 3:
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word[-6:] for vowel in neutralising_vowels):
            word = word[:-1] + "ejä"
        else:
            word = word[:-1] + "eja"

    

    #luettelo
    elif word[-2:] == "lo" and syllables >= 3:
        word += "ita"

    elif word[-2:] == "la" and syllables >= 3:
        word = word[-1] + "oita"

    #henkilö
    elif word[-2:] == "lö" and syllables >= 3:
        word += "itä"

    #sopraano
    elif word[-2:] == "no" and syllables >= 3:
        word += "ja"

    #kaveri
    elif word[-2:] == "ri" and syllables >= 3:
        word = word[:-1] + "eita"

    elif word[-2:] == "in":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word = word[:-1] + "mpiä"
        else:
            word = word[:-1] + "mpia"
        

    #numero
    elif word[-2:] == "ro" and syllables >= 3:
        word += "ita"

    
    #u, o, ö, y -> + j + a/ä
    elif word[-1] in ("u", "o"):
        word += "ja"

    elif word[-1] in ("y", "ö"):
        word += "jä"


    #i -> e change
    # when there is no change in i -> e sg, there is change in pl, if there is change in i->e > no change in pl
    #kivi

    #pankki        
    elif word[-1] == "i" and word not in i_to_e:
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-8:] for vowel in neutralising_vowels):
            word = word[:-1] + "ejä"
        else:
            word = word[:-1] + "eja"

        #I to E, need to work on 
    #All thanks to my beautiful girlfriend Maria that helped me with this program <3


    elif word[-3:] == "kas":
        word = word[:-2] + "kaita"
    
    elif word[-3:] == "käs":
        word = word[:-2] + "käitä"

    elif word[-3:] == "tar":
        word = word[:-2] + "taria"

    elif word[-2:] == "ar":
        word += "ia"
    
    elif word[-3:] == "pas":
        word = word[:-2] + "paita"

    elif word[-4:] == "rras":
        word = word[:-3] + "taita"

    elif word[-4:] == "ngas":
        word = word[:-3] + "kaita"

    elif word[-4:] == "llas":
        word = word[:-3] + "taita"

    elif word[-2:] == "as":
        word = word[:-1] + "ita"
              


    #partitive_sg(word:str)

    return word



















# --- 1. SESSION STATE INIT ---
if "state" not in st.session_state:
    st.session_state.state = {
        "view": "menu",
        "idx": 0,
        "score": {"correct": 0, "wrong": 0},
        "quiz": [],
        "to_repair": [],
        "mode": "Mixed",
        "feedback": None,
        "correct_answer": "",
        "input_key_suffix": 0,
        "missed_current": False
    }

s = st.session_state.state

# Safety checks
if "to_repair" not in s: s["to_repair"] = []

# --- 2. DYNAMIC CSS ---
border_color = "#2196F3" # Blue
bg_color = "#E3F2FD"
if s["view"] == "repair":
    border_color = "#f39c12" # Orange for Repair Mode
    bg_color = "#FFF3E0"

if s["feedback"] == "correct":
    border_color = "#4CAF50"
    bg_color = "#E8F5E9"
elif s["feedback"] == "wrong":
    border_color = "#F44336"
    bg_color = "#FFEBEE"



st.markdown("""
<style>
    /* Hide the anchor link icon next to headers */
    .viewerBadge_link__qRIco, 
    a.header-anchor {
        display: none !important;
    }
    
    /* Global fix to hide all header anchors in Streamlit */
    [data-testid="stMarkdownContainer"] a.header-anchor {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    /* Remove top padding of the main container */
    .block-container {
        padding-top: 1rem !important;
        max-width: 600px;
        margin: auto;
    }
    /* Hide the top decoration bar (optional) */
    header {visibility: hidden;}
    
    .centered-text {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>
div[data-baseweb="base-input"] {{
    border: 2px solid {border_color} !important;
    border-radius: 8px !important;
    background-color: {bg_color} !important;
}}
div[data-baseweb="input"] {{ border: none !important; background-color: transparent !important; }}
[data-testid="stTextInput"] button {{ display: none !important; }}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    /* Styling for the main menu box */
    [data-testid="stVerticalBlock"] > div:has(div.menu-box) {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .main-title {
        text-align: center;
        color: #1e3d59;
        font-family: 'Helvetica Neue', sans-serif;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    /* Center the entire app content */
    .block-container {
        max-width: 600px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        margin: auto;
    }
    /* Style for the centered word */
    .centered-text {
        text-align: center;
    }
    /* Centering the progress bar text */
    .stProgress > div > div > div > div {
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)


# --- 3. AUTO-FOCUS JAVASCRIPT ---
components.html(f"""
<script>
    const doc = window.parent.document;
    const applyFix = () => {{
        const input = doc.querySelector('input[type="text"]');
        if (input && doc.activeElement !== input) {{
            input.focus();
            input.setAttribute("autocomplete", "off");
            input.setAttribute("name", "q_" + Math.floor(Math.random() * 1000000));
        }}
    }};
    setInterval(applyFix, 300);
</script>
""", height=0)
def handle_submit():
    current_key = f"in_{s['input_key_suffix']}"
    user_val = st.session_state.get(current_key, "").strip().lower()
    if not user_val: return

    word, case = s["quiz"][s["idx"]]
    correct = partitive_sg(word).lower() if case in ["SG", "Singular"] else partitive_pl(word).lower()
    s["correct_answer"] = correct

    if user_val == correct:
        if s["missed_current"]:
            s["score"]["wrong"] += 1
        else:
            s["score"]["correct"] += 1
        s["feedback"] = "correct"
    else:
        s["feedback"] = "wrong"
        if (word, case) not in s["to_repair"]:
            s["to_repair"].append((word, case))
        s["missed_current"] = True
        s["input_key_suffix"] += 1

def next_question():
    s["idx"] += 1
    s["feedback"] = None
    s["missed_current"] = False
    s["input_key_suffix"] += 1
    
    if s["idx"] >= len(s["quiz"]):
        if s["view"] == "repair":
            s["view"] = "menu" # Finish repairs -> Menu
        else:
            s["view"] = "results" # Finish quiz -> Results
    st.rerun()
# --- 4. LOGIC HANDLERS (Updated for Custom Mode) ---
def start_quiz(word_list, num, mode):
    # Ensure we don't try to sample more words than available
    sample_size = min(num, len(word_list))
    selected = random.sample(word_list, sample_size)
    
    s["quiz"] = [(w, mode if mode != "Mixed" else random.choice(["Singular", "Plural"])) for w in selected]
    s["to_repair"] = []
    s["idx"], s["score"]["correct"], s["score"]["wrong"] = 0, 0, 0
    s["view"], s["feedback"] = "game", None
    s["repair_initialized"] = False # Reset heart system
    st.rerun()

# --- 5. VIEWS ---
if s["view"] == "menu":


    st.markdown('<h1 class="main-title">Finnish Partitive Quiz</h1>', unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("### Quiz Settings")
        
        # Split into Standard and Custom tabs
        tab1, tab2 = st.tabs(["Random Words", "Custom List"])
        
        with tab1:
            st.write("Use the built-in database of 500+ words.")
            num_std = st.slider("Select number of exercises:", 1, 50, 10, key="slider_std")
            mode_std = st.radio("Choose Case Mode:", ["Singular", "Plural", "Mixed"], horizontal=True, key="radio_std")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Start Standard Quiz", use_container_width=True, type="secondary"):
                start_quiz(WORDS, num_std, mode_std)
            


        with tab2:
            st.write("Enter your own words to practice.")
            
            # 1. Text Area Input
            custom_text = st.text_area(
                "Write words (one per line):", 
                placeholder="koira\nkissa\ntalo...", 
                height=100, 
                key="custom_text_input"
            )
            
            # 2. File Upload Option
            uploaded_file = st.file_uploader(
                "Or upload a .txt file", 
                type=["txt"], 
                key="custom_file_uploader"
            )
            
            # 3. Mode Selection
            mode_cus = st.radio(
                "Choose Case Mode:", 
                ["Singular", "Plural", "Mixed"], 
                horizontal=True, 
                key="radio_cus"
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # 4. Start Button Logic
            if st.button("Start Custom Quiz", use_container_width=True, type="secondary", key="btn_start_custom"):
                word_source = []
                
                # Priority: Check file first
                if uploaded_file is not None:
                    # getvalue() is better for Streamlit reruns
                    file_bytes = uploaded_file.getvalue()
                    content = file_bytes.decode("utf-8")
                    word_source = [w.strip() for w in content.split("\n") if w.strip()]
                    
                # Fallback: Check text area
                elif custom_text.strip():
                    word_source = [w.strip() for w in custom_text.split("\n") if w.strip()]
                
                if word_source:
                    # Initialize game
                    start_quiz(word_source, len(word_source), mode_cus)
                    # FORCE the view to change immediately
                    st.rerun() 
                else:
                    st.warning("⚠️ Please upload a file or type some words first!")


    st.caption("Master the Finnish Partitive case by practicing 500+ words, developed by Michael Beneš", text_alignment="center")

elif s["view"] == "game":
    # 0. Quit Button
    _, col_back = st.columns([5, 1]) 
    with col_back:
        if st.button("Quit", help="Return to Menu", use_container_width=True):
            s["view"] = "menu"
            st.rerun()

    word, case = s["quiz"][s["idx"]]
    
    # 1. Dynamic Color Logic (Labels stay Blue/Gold)
    is_plural = case in ["PL", "Plural"]
    case_label = "PLURAL" if is_plural else "SINGULAR"
    accent_color = "#FFD700" if is_plural else "#2196F3" 

    st.markdown(f"""
        <div style="text-align: center; margin-top: -35px; margin-bottom: -15px;">
            <h1 style="color: {accent_color}; font-size: 3.5rem; font-weight: 800; letter-spacing: 2px;">{case_label}</h1>
        </div>
    """, unsafe_allow_html=True)

    # 2. Progress Bar
    progress = (s["idx"]) / len(s["quiz"])
    st.progress(progress)
    st.markdown(f"<p class='centered-text' style='color: gray; margin-top: -12px; margin-bottom: 5px; font-size: 0.8rem;'>{s['idx']} / {len(s['quiz'])} completed</p>", unsafe_allow_html=True)
    
    # 3. Target Word Card
    st.markdown('<div style="margin-top: -25px;">', unsafe_allow_html=True)
    card_placeholder = st.empty()

    display_text = word
    text_color = "#2c3e50"
    
    if s.get("show_reveal"):
        display_text = s['correct_answer']
        text_color = "#11a20a"  # Your requested Green for revealed answer

    with card_placeholder.container(border=True):
        st.markdown(f"""
            <div class="centered-text" style="margin-top: -5px; margin-bottom: 10px;">
                <h1 style='color:{text_color}; font-size: 5rem; margin: 0;'>{display_text}</h1>
            </div>
        """, unsafe_allow_html=True)

    # 4. Input Field (Hides when revealing)
    input_placeholder = st.empty()
    if not s.get("show_reveal"):
        with input_placeholder:
            input_key = f"in_{s['input_key_suffix']}"
            st.text_input(
                "Answer", 
                key=input_key, 
                on_change=handle_submit, 
                label_visibility="collapsed",
                placeholder="Type the Finnish form..."
            )

    # 5. Success Logic (Fixes the "stops working after correct" issue)
    if s["feedback"] == "correct":
        st.success("✅ Correct!")
        time.sleep(1.2)
        next_question()
        st.rerun()

    # 6. Wrong / Show Answer Logic
    elif s["feedback"] == "wrong" and not s.get("show_reveal"):
        st.error("❌ Not quite right.")
        col_l, col_btn, col_r = st.columns([1, 1.5, 1])
        with col_btn:
            if st.button("Show answer", use_container_width=True):
                s["show_reveal"] = True
                # Increment wrong score ONLY ONCE when button is first pressed
                s["score"]["wrong"] += 1 
                st.rerun()

    # 7. Reveal State: Next Button + 4s Timer
    if s.get("show_reveal"):
        # Custom CSS for Blue Button
        st.markdown("""<style>div.stButton > button:first-child { background-color: #2196F3 !important; color: white !important; font-weight: bold !important; }</style>""", unsafe_allow_html=True)

        col_l, col_btn, col_r = st.columns([1, 1.5, 1])
        with col_btn:
            # If user clicks manually, we move on immediately
            if st.button("Next Word →", use_container_width=True):
                s["show_reveal"] = False
                s["feedback"] = None
                next_question()
                st.rerun()

        # --- SMART TIMER ---
        # We only run the timer if the state hasn't been cleared by the button above
        time.sleep(4.0)
        if s.get("show_reveal"): # Check if user didn't already click 'Next'
            s["show_reveal"] = False
            s["feedback"] = None
            next_question()
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
                    
elif s["view"] == "results":
    st.title("Quiz Results")
   
    c, w = s["score"]["correct"], s["score"]["wrong"]
    
    # Side-by-side layout: Chart and Metrics
    layout_col1, layout_col2 = st.columns([4, 1.5])

    with layout_col1:
        if c + w > 0:
            fig, ax = plt.subplots(figsize=(2.5, 2.5))
            # Removed labels and autopct from here
            patches, texts = ax.pie([c, w], 
                                   colors=["#2ecc71", "#e74c3c"], 
                                   startangle=90)
            
            # Add LEGEND on the side instead of text on the chart
            ax.legend(patches, [f"Correct: {c}", f"Wrong: {w}"], 
                      loc="center left", 
                      bbox_to_anchor=(1, 0.5), 
                      fontsize=8, 
                      frameon=False)
            
            fig.tight_layout()
            st.pyplot(fig)
        else:
            st.info("No data yet.")

    with layout_col2:
        # Small stats box
        with st.container(border=True):
            st.caption("TOTALS")
            st.write(f"**Clean:** {c}")
            st.write(f"**Mistakes:** {w}")

    st.markdown("---")

    # Bottom Buttons
    btn_col1, _, btn_col3 = st.columns([1, 0.5, 1])
    with btn_col1:  
        if st.button("Back to Menu", use_container_width=True):
            s["view"] = "menu"
            st.rerun()
    with btn_col3:
        if s["to_repair"]:
            if st.button("Practice Missed", use_container_width=True):
                s["quiz"] = s["to_repair"].copy()
                s["to_repair"] = []
                s["idx"] = 0
                s["view"] = "repair"
                st.rerun()
                
elif s["view"] == "repair":
    # 0. Session Initialization (Ensures 3 fresh hearts at start)
    if s.get("idx") == 0 and not s.get("repair_initialized"):
        s["lives"] = 3
        s["repair_initialized"] = True
        s["heart_lost_this_turn"] = False
    
    # 1. Game Over Check
    if s.get("lives", 0) <= 0:
        st.error("💔 No more hearts! Returning to menu...")
        time.sleep(2.0)
        s["view"] = "menu"
        s["repair_initialized"] = False # Reset for next time
        st.rerun()

    # 2. Quit Button
    _, col_back = st.columns([5, 1]) 
    with col_back:
        if st.button("Quit", help="Return to Menu", use_container_width=True):
            s["view"] = "menu"
            s["repair_initialized"] = False # Reset flag so hearts reset next time
            st.rerun()

    # 3. Hearts Display
    lives_count = s.get("lives", 3)
    hearts_display = "❤️" * lives_count + "🖤" * (3 - lives_count)
    st.markdown(f"<div style='text-align: center; font-size: 2rem; margin-top: -20px;'>{hearts_display}</div>", unsafe_allow_html=True)

    # 4. Header & Progress
    word, case = s["quiz"][s["idx"]]
    st.markdown(f"""
        <div style="text-align: center; margin-top: -10px; margin-bottom: -15px;">
            <h1 style="color: #f39c12; font-size: 3.5rem; font-weight: 800; letter-spacing: 2px;">REPAIRING</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.progress((s["idx"]) / len(s["quiz"]))
    st.markdown(f"<p class='centered-text' style='color: gray; margin-top: -12px; margin-bottom: 5px; font-size: 0.8rem;'>Mistake {s['idx']+1} / {len(s['quiz'])}</p>", unsafe_allow_html=True)

    # 5. Target Word Card
    with st.container(border=True):
        st.markdown(f"<div class='centered-text' style='margin-bottom: 10px;'><small style='color:gray;'>Form {case}</small><h1 style='color:#2c3e50; font-size: 5rem; margin: 0;'>{word}</h1></div>", unsafe_allow_html=True)
        
        input_key = f"in_{s['input_key_suffix']}"
        st.text_input("Answer", key=input_key, on_change=handle_submit, label_visibility="collapsed", placeholder="Type the correct form...")

           # 6. Feedback Logic (Lose a heart on EVERY wrong submission)
        if s["feedback"] == "correct":
            st.success("✅ Correct!")
            time.sleep(1.0)
            
            if s["idx"] + 1 == len(s["quiz"]):
                s["repair_initialized"] = False
                
            next_question()
            st.rerun()

        elif s["feedback"] == "wrong":
            # Check if this is a NEW wrong submission (using the input key suffix)
            # This ensures 1 submit = 1 heart lost, even if Streamlit reruns
            if not s.get("last_processed_submit") == s["input_key_suffix"]:
                s["lives"] -= 1
                s["last_processed_submit"] = s["input_key_suffix"]
                st.rerun() # Immediate visual update of hearts
            
            st.error(f"❌ Wrong! Hearts: {s['lives']}/3")
            
            if s["lives"] <= 0:
                st.rerun() # Trigger Game Over check at the top