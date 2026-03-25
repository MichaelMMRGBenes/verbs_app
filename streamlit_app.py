import streamlit as st
import streamlit.components.v1 as components
import random
import time
import matplotlib.pyplot as plt
import base64

def play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        # Přidání unikátního ID pomocí timestampu
        unique_id = f"audio_{int(time.time() * 1000)}"
        md = f"""
            <audio id="{unique_id}" autoplay="true" style="display:none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.components.v1.html(md, height=0)
# --- 0. PLACEHOLDER DATA & LOGIC (Replace with your actual logic) ---

WORDS = {
    # Animals & Nature
    "koira": "dog", "kissa": "cat", "hevonen": "horse", "lehmä": "cow", "lammas": "sheep",
    "sika": "pig", "karhu": "bear", "susi": "wolf", "kettu": "fox", "jänis": "hare",
    "lintu": "bird", "kala": "fish", "käärme": "snake", "hyönteinen": "insect", "puu": "tree",
    "kukka": "flower", "metsä": "forest", "järvi": "lake", "meri": "sea", "joki": "river",
    "vuori": "mountain", "mäki": "hill", "saari": "island", "niemi": "peninsula", "ranta": "shore",
    "taivas": "sky", "aurinko": "sun", "kuu": "moon", "tähti": "star", "pilvi": "cloud",
    "sade": "rain", "lumi": "snow", "jää": "ice", "tuuli": "wind", "ukkonen": "thunder",
    "kivi": "stone", "hiekka": "sand", "multa": "soil", "ruoho": "grass", "lehti": "leaf",
    "oksa": "branch", "juuri": "root", "marja": "berry", "sieni": "mushroom", "puro": "brook",
    "lähde": "spring", "suo": "swamp", "tunturi": "fell", "luonto": "nature",
    
    # People & Family
    "mies": "man", "nainen": "woman", "lapsi": "child", "poika": "boy", "tyttö": "girl",
    "vauva": "baby", "isä": "father", "äiti": "mother", "veli": "brother", "sisko": "sister",
    "tytär": "daughter", "isoäiti": "grandmother", "isoisä": "grandfather", "serkku": "cousin",
    "täti": "aunt", "setä": "uncle (paternal)", "eno": "uncle (maternal)", "perhe": "family",
    "suku": "relatives", "ystävä": "friend", "naapuri": "neighbor", "ihminen": "human",
    "henkilö": "person", "vieras": "guest", "isäntä": "host", "emäntä": "hostess", "vaimo": "wife",
    "pari": "couple",
    
    # Body Parts
    "pää": "head", "silmä": "eye", "korva": "ear", "nenä": "nose", "suu": "mouth",
    "huuli": "lip", "hammas": "tooth", "kieli": "tongue", "kaula": "neck",
    "kurkku": "throat", "olkapää": "shoulder", "käsivarsi": "arm", "käsi": "hand",
    "sormi": "finger", "kynsi": "nail", "rinta": "chest", "vatsa": "stomach", "selkä": "back",
    "jalka": "leg", "polvi": "knee", "varvas": "toe", "iho": "skin", "luu": "bone",
    "veri": "blood", "sydän": "heart", "keuhko": "lung", "lihas": "muscle", "naama": "face",
    
    # House & Household
    "talo": "house", "koti": "home", "asunto": "apartment", "huone": "room", "keittiö": "kitchen",
    "kylpyhuone": "bathroom", "makuuhuone": "bedroom", "olohuone": "living room", "eteinen": "hall",
    "parveke": "balcony", "piha": "yard", "ovi": "door", "ikkuna": "window", "seinä": "wall",
    "katto": "roof", "lattia": "floor", "porras": "stair", "lukko": "lock", "avain": "key",
    "pöytä": "table", "tuoli": "chair", "sänky": "bed", "sohva": "sofa", "kaappi": "cabinet",
    "hylly": "shelf", "lamppu": "lamp", "matto": "carpet", "verho": "curtain", "peili": "mirror",
    "taulu": "picture", "kello": "clock", "radio": "radio", "televisio": "television",
    "tietokone": "computer", "puhelin": "telephone", "kone": "machine", "uuni": "oven",
    "hella": "stove", "allas": "basin",
    
    # Kitchen & Food
    "ruoka": "food", "juoma": "drink", "vesi": "water", "maito": "milk", "kahvi": "coffee",
    "tee": "tea", "mehu": "juice", "olut": "beer", "viini": "wine", "leipä": "bread",
    "voi": "butter", "juusto": "cheese", "liha": "meat", "kana": "chicken", "muna": "egg",
    "makkara": "sausage", "peruna": "potato", "riisi": "rice", "pasta": "pasta",
    "vihannes": "vegetable", "hedelmä": "fruit", "omena": "apple", "banaani": "banana",
    "suola": "salt", "sokeri": "sugar", "jauho": "flour", "öljy": "oil", "kastike": "sauce",
    "lautanen": "plate", "kulho": "bowl", "lasi": "glass", "muki": "mug", "kuppi": "cup",
    "veitsi": "knife", "haarukka": "fork", "lusikka": "spoon", "kattila": "pot", "pannu": "pan",

    # Transportation & City
    "auto": "car", "bussi": "bus", "juna": "train", "lentokone": "airplane", "laiva": "ship",
    "vene": "boat", "pyörä": "bicycle", "moottoripyörä": "motorcycle", "tie": "road", "katu": "street",
    "polku": "path", "silta": "bridge", "tunneli": "tunnel", "asema": "station", "satama": "harbor",
    "tori": "market", "puisto": "park", "kaupunki": "city", "kylä": "village", "maa": "country",
    "valtio": "state", "raja": "border", "keskusta": "center", "kauppa": "shop", "pankki": "bank",
    "sairaala": "hospital", "koulu": "school", "kirkko": "church", "tehdas": "factory",
    "hotelli": "hotel", "ravintola": "restaurant", "kahvila": "cafe", "museo": "museum",
    "kirjasto": "library", "teatteri": "theater", "poliisi": "police", "posti": "post", "apteekki": "pharmacy",

    # Time & Abstract
    "aika": "time", "hetki": "moment", "sekunti": "second", "minuutti": "minute", "tunti": "hour",
    "päivä": "day", "viikko": "week", "kuukausi": "month", "vuosi": "year", "vuosisata": "century",
    "aamu": "morning", "ilta": "evening", "yö": "night", "maanantai": "Monday", "tiistai": "Tuesday",
    "keskiviikko": "Wednesday", "torstai": "Thursday", "perjantai": "Friday", "lauantai": "Saturday",
    "sunnuntai": "Sunday", "kevät": "spring", "kesä": "summer", "syksy": "autumn", "talvi": "winter",
    "asia": "thing", "sana": "word", "nimi": "name", "numero": "number", "väri": "color",
    "ääni": "sound", "valo": "light", "elämä": "life", "onni": "happiness", "rakkaus": "love",
    "työ": "work", "raha": "money", "ongelma": "problem", "vastaus": "answer", "kysymys": "question",
}

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
            return [word]
    
    #I to E, need to work on 
    for item in i_to_e:
        if item == word[-len(item):]:
            # usi -> usta
            if word[-3:] == "usi":
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-1] +"tä"
                else:
                    word = word[:-1] + "ta" #tä
                return [word]

            # ni -> nta/ntä
            elif word[-2:] == "ni":
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-1] + "tä"
                else:
                    word = word[:-1] +"ta" 
                return [word]

            # ri -> rtä
            elif word[-2:] == "ri":
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-1] +"tä"
                else:
                    word = word[:-1] +"ta" #tä
                return [word]

            # hi -> hta 
            elif word[-2:] == "hi":            
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-1] +"tä"
                else:
                    word = word[:-1] +"ta" #tä
                return [word]
            #siili, kaali
            elif word[-4:] in ("iili", "aali"):
                if "a" in word[-4:]:
                    word += "a"
                else:
                    word += "ä"
                return [word]
            # li -> ltä
            elif word[-2:] == "li":
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-1] +"tä"
                else:
                    word = word[:-1] +"ta" #tä
                return [word]

            # si -> ttä
            elif word[-2:] == "si":
                if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                    word = word[:-2] +"ttä"
                else:
                    word = word[:-2] +"tta" # checknout to tä
                return [word]

            #i -> e + a/ä
            else:
                if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-5:] for vowel in neutralising_vowels):
                    word = word[:-1] + "eä"
                else:
                    word = word[:-1] + "ea"
                return [word]


        

    #nalle
    if word[-3:] == "lle":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "ä"
        else:
            word += "a"
        return [word]
    #lattia -> lattiaa, miniä -> miniää, teknologia -> teknologiaa 
    elif word[-2:] == "ia":
        word += "a"
        return [word]

    elif word[-2:] == "iä":
        word += "ä"
        return [word]

    elif word[-2:] == "ee":
        word += "tä"
        return [word]

    elif word[-2:] in ("oi","ai"):
        word += "ta"
        return [word]

    #nainen -> naista
    elif word[-3:] == "nen":
        if any(vowel in word[-7:] for vowel in changing_vowels) or any(vowel in word[-7:] for vowel in neutral_vowels) and not any(vowel in word[-7:] for vowel in neutralising_vowels):
            word = word[:-3] + "stä"
        else:
            word = word[:-3] + "sta"
        return [word]

    #ahven -> ahventa
    elif word[-2:] == "en" and word[-3:] != "nen":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "tä"
        else:
            word += "ta"
        return [word]


    #RAKKAUS -> rakkautta
    elif word[-4:] in ("eus", "uus", "kaus","ous"):
        word = word[:-1] + "tta"
        return [word]
    #All thanks to my beautiful girlfriend Maria that helped me with this program <3
    #avaruus and kauneus
    elif word[-3:] in ("eus", "uus","ous"):
        word = word[:-1] + "tta"
        return [word]

    #kokemus
    elif word[-2:] == "us":
        word += "ta"
        return [word]

    elif word[-3:] in ("yys", "eys"):
        word = word[:-1] + "ttä"
        return [word]
    #ymmärys -> ymmärystä
    elif word[-2:] == "ys":
        word += "tä"
        return [word]
    #kevyt
    elif word[-2:] == "yt":
        word += "tä"
        return [word]
    

    #E vene -> venettä, laite -> laitetta
    elif word[-1] == "e" and word[-2:] != "ie":
        if any(vowel in word[-6:] for vowel in changing_vowels) or any(vowel in word[-6:] for vowel in neutral_vowels) and not any(vowel in word[-6:] for vowel in neutralising_vowels):
            word += "ttä"
        else: word += "tta"
        return [word]

    # Loan words
    elif word[-1] == "i" and word not in i_to_e:
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-6:] for vowel in neutral_vowels) and not any(vowel in word[-8:] for vowel in neutralising_vowels):
            word = word +"ä"
            
        else:
            word = word +"a"
        return [word]

    elif word in loan_words:
        if word[-1] == "i":
            word += "a"
        else: word += "ia"
        return [word]

    #auto -> autoa / leipää -> leipää
    elif word[-1] in all_vowels and word[-2] not in all_vowels:
        if word[-1] in changing_vowels:
            word += "ä"
        elif any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "ä"
        elif word[-1] in basic_vowels:
            word += "a"

        return [word]

    #samea
    elif word[-2:] == "ea":
        return [word + "a", word[:-2] + "eata"]

    elif word[-2:] == "eä":
        return [word + "ä", word[:-2] + "eätä"]

    #maa -> maata / yö -> yötä
    elif word[-1] in all_vowels:
        if word[-2] in basic_vowels and not any(vowel in word for vowel in changing_vowels) and word[-2:] not in ("ie"):
            word += "ta"
        else:
            word += "tä"

        return [word]

    elif word[-1] not in all_vowels and word[-2] != "u":
        if any(vowel in word[-6:] for vowel in neutral_vowels) and not any(vowel in word[-6:] for vowel in neutralising_vowels):
            word += "tä" 

        elif any(vowel in word[-6:] for vowel in changing_vowels):
            word += "tä" 
        else: 
            word += "ta"
        return [word]

    #tatar -> tatarta
    elif word[-1] not in all_vowels:
        if word[-2] in basic_vowels and not any(vowel in word for vowel in changing_vowels):
            word += "ta"
        else:
            word += "tä"
        
        return [word]
    #A word ends in a consonant or a relic consonant, the partitive stem ends in a consonant, 
    # and the strong-grade plural stem ends in a diphthong.



    return [word]

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
    exceptions = {"hana":"hanoja", "kaappi":"kaappeja", "maailma":"maailmoja", "keskusta":"keskustoja", "sana":"sanoja","etelä":"eteliä","jänis":"jäniksiä","viikko":"viikkoja","kiuas":"kiukaita","suola":"suoloja","veli":"veljiä","ihana":"ihania","näppäin":"näppäimiä","muna":"munia","appelsiini":"appelsiineja", "voi":"voita","hidas":"hitaita", "laite":"laitteita","kausi": "kausia", "taide":"taiteita","laki":"lakeja","pullo":"pulloja","vuoro":"vuoroja","hana":"hanoja","verkko":"verkkoja","lahje":"lahkeita","kirkko":"kirkkoja","omena":"omenoita","ien":"ikeniä","koe":"kokeita", "rikas":"rikkaita", "mies":"miehiä", "puhelin":"puhelimia", "tytär":"tyttäriä", "kannel":"kanteleita", "sävel":"säveliä", "kyynel":"kyyneleitä", "sammal":"sammaleita", "taival":"taipaleita", "askel":"askeleita", "nivel":"niveliä","ommel":"ompeleita", "tanner":"tantereita", "manner":"mantereita", "seitsemän":"seitsemiä", "jääkiekko":"jääkiekkoja", "matala":"matalia","ihana":"ihania", "ahkera":"ahkeria", "sako":"sakkoja", "musiikki":"musiikkeja"}
    
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
            return [word]
        else:
            if item == word:
                word = exceptions[item]
                return [word]

    for item in i_to_e:
        if len(word) > 5:
            if item == word[-len(item):]:
                if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:]  for vowel in neutral_vowels) and not any(vowel in word[-4:] for vowel in neutralising_vowels):
                    word += "ä"
                else:
                    word += "a"
                return [word]
        else:
            if item == word:
                if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:]  for vowel in neutral_vowels) and not any(vowel in word[-4:] for vowel in neutralising_vowels):
                    word += "ä"
                else:
                    word += "a"
                return [word]
    

        #mansikka/
    if word[-3:] in ("kka","kko") and syllables >= 3 and not any(vowel in word for vowel in changing_vowels):
        return [word[:-2] + "oita", word[:-1] + "oja"]


    elif word[-3:] == "hai":
        word += "ta"
        return [word]


    
    elif word[-3:] in ("yrä") and syllables == 3:
        word = word[:-1] + "öitä"
        return [word]

    elif word[-3:] in ("ävä", "evä", "ärä") and syllables == 3:
        word = word[:-1] + "iä"
        return [word]
    
    elif word[-2:] in ("lä", "rä", "nä", "iä") and syllables >= 3 and not any(vowel in word for vowel in neutralising_vowels):
        word = word[:-1] + "öitä"
        return [word]
        
    elif word[-1] == "ä" and word[-2:] != "ää":
        word = word[:-1] + "iä"
        return [word]
        
    elif word[-4:] == "mmas":
        word = word[:-3] + "paita"
        return [word]
    
    elif word[-3:] == "das":
        word = word[:-3] + "taita"
        return [word]

    elif word[-3:] in ("kke"):
        word = word[:-1] + "eja"
        return [word]

    elif word[-4:] == "aite":
        word = word[:-1] + "teita"
        return [word]

        #varvas -> varpaita
    elif word[-4:] == "rvas":
        word = word[:-3] + "paita"
        return [word]

    elif word[-2:] == "pas":
        word = word[:-1] + "paita"
        return [word]
    
        #taivas -> taivaita
    elif word[-3:] == "vas":
        word = word[:-1] + "ita"
        return [word]

        #kauppias -> kauppiaita
    elif word[-3:] == "ias":
        word = word[:-1] + "ita"
        return [word]


    #mukava, matala
    elif word[-3:] in ("ala", "ava", "isa", "era") and syllables == 3 and word[-4:] != "aala":
        word = word[:-1] + "ia"
        return [word]


    #ravintola
    elif word[-2:] in ("la", "ra", "na", "ia") and syllables >= 3 and not any(vowel in word for vowel in changing_vowels):
        word = word[:-1] + "oita"
        return [word]

    #opiskelija 
    elif word[-3:] == "ija" and syllables >= 3:
        word = word[:-1] + "oita"
        return [word]

    elif word[-3:] == "ijä" and syllables >= 3:
        word = word[:-1] + "äitä"
        return [word]
    

    #korkea
    elif word[-2:] == "ea" and syllables >= 3:
        word = word[:-1] + "ita"
        return [word]
    

    elif word[-2:] == "eä" and syllables >= 3:
        word = word[:-1] + "itä"
        return [word]
    

        #vadelma, majava
    elif word[-2:] in ("ma", "va") and syllables >= 3:
        word = word[:-1] + "ia"
        return [word]

    elif word[-2:] in ("mä", "vä")and syllables >= 3:
        word = word[:-1] + "iä"
        return [word]

        #aja -> ia, opettaja
    elif word[-3:] == "aja" and syllables >= 3:
        word = word[:-1] + "ia"
        return [word]

    elif word[-3:] == "äjä"and syllables >= 3:
        word = word[:-1] + "iä"
        return [word]

        #kännykkä
    elif word[-3:] in ("kkä", "kkö") and syllables >= 3:
        return [word[:-2] + "oitä", word[:-1] + "öjä"]


        # o / u
        #and syllables == 2 
    elif word[-1] == "a" and (get_first_vowel_in_long_word(word) in ("a", "e", "i")) and word[-2:] != "aa":
        word = word[:-1] + "oja"
        return [word]

        #2 syllables words with a ending
        # o / u
        #and syllables == 2 #it doesnt work for kauppa
    elif word[-1] == "a" and (get_first_vowel_in_long_word(word) in ("o", "u")) and word[-2:] != "aa":
        word = word[:-1] + "ia"
        return [word]
        #kenkä, leipä

        #tie -> eitä
    elif word[-2:] == "ie":
        word = word[:-2] + "eitä"
        return [word]

        #uo -> oita
    elif word[-2:] == "uo":
        word = word[:-2] + "oita"
        return [word]

        #yö -> öitä
    elif word[-2:] == "yö":
        word = word[:-2] + "öitä"
        return [word]

        #eo -> eoita
    elif word[-2:] == "eo":
        word = word[:-2] +"eoita"
        return [word]
    
        #io -> ioita
    elif word[-2:] == "io":
        word = word[:-2] +"ioita"
        return [word]

        #iö -> iöitä
    elif word[-2:] == "iö":
        word = word[:-2] +"iöitä"
        return [word]


        #ao -> aoita 
    elif word[-2:] == "ao":
        word = word[:-2] +"aoita"
        return [word]
        #All thanks to my beautiful girlfriend Maria that helped me with this program <3
        #suomalainen 

        #nen -> sia
    elif word[-3:] == "nen":
        if any(vowel in word[-7:] for vowel in changing_vowels) or any(vowel in word[-7:] for vowel in neutral_vowels) and not any(vowel in word[-7:] for vowel in neutralising_vowels):        
            word = word[:-3] +"siä"
        else:
            word = word[:-3] +"sia"
        return [word]

        #vät
    elif word[-3:] == "vät":
        word = word[:-2] +"äitä"
        return [word]
    
    #nyt -> neitä
    elif word[-3:] == "nyt":
        word = word[:-2] +"eitä"
        return [word]
    
    #ut -> ita
    elif word[-2:] == "ut":
        word = word[:-1] +"ita"
        return [word]
    
    #yt -> itä
    elif word[-2:] == "yt":
        word = word[:-1] +"itä"
        return [word]

    #is -> iita
    elif word[-2:] == "is":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        
            word = word[:-1] +"itä"
        else:
            word = word[:-1] +"ita"

        return [word]

    #double vowel
    # puu, syy,  maa
    elif word[-2:] in ("uu", "ii", "aa"):
        word = word[:-1] + "ita"
        return [word]

    #myy, jää
    elif word[-2:] in ("ää","yy", "ee"):
        word = word[:-1] + "itä"
        return [word]

    #kuuloke     
    elif word[-2:] == "ke":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        
            word = word[:-1] + "keitä"
        else:
            word = word[:-1] + "keita"
        return [word]
        

    elif word[-2:] == "de":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        
            word = word[:-2] + "teitä"
        else:
            word = word[:-2] + "teita"
        return [word]
        
    elif word[-3:] == "ste":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        
            word += "itä"
        else:
            word += "ita"
        return [word]
                  

    elif word[-2:] == "te":
        word = word[:-1] + "teita"
        return [word]
        
    #tunne -> tunteita 
    elif word[-3:] == "nne":
        word = word[:-2] + "teita"
        return [word]

    #huone, kone
    elif word[-1] == "e":
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-5:] for vowel in neutralising_vowels):        
            word += "itä"
        else:
            word += "ita"
        return [word]

        #All thanks to my beautiful girlfriend Maria that helped me with this program <3            
        #rakkaus might need change to aus
    elif word[-2:] in ("us", "es","os"):
        word = word[:-1] + "ksia"
        return [word]

    elif word[-3:] in ("has"):
        word = word[:-1] + "ksia"
        return [word]

    #närästys
    elif word[-2:] == "ys":
        word = word[:-1] + "ksiä"
        return [word]
    
    #rikas -> riKKaita
    #kaunis -> kauniita
    elif word[-3:] == "nis":
        word = word[:-1] + "ita"
        return [word]

    #siemen
    elif word[-2:] == "en":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "iä"
        else:
            word += "ia"
        return [word]
    #All thanks to my beautiful girlfriend Maria that helped me with this program <3
    #rasvaton -> rasvatomia
    elif word[-2:] in ("on","an"):
        word = word[:-2] + "tomia"
        return [word]

    #puhelin
    elif word[-3:] in ("lin", "ain"):
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word = word[:-1] + "miä"
        else:
            word = word[:-1] + "mia"
        return [word]


    elif word[-3:] == "tin":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word = word[:-2] + "timiä"
        else: 
            word = word[:-2] + "timia"
        return [word]
    #sydän
    elif word[-3:] == "dän":
        word = word[:-1] + "miä"  
        return [word]

    #työtön -> työtömiä
    elif word[-2:] in ("ön", "än"):
        word = word[:-2] + "tömiä"
        return [word]

    #matala
    elif word[-1:] == "a" and syllables == 3:
        word = word[:-1] + "ia"
        return [word]

    #hämärä
    elif word[-1:] == "ä" and syllables == 3:
        word = word[:-1] + "iä"
        return [word]


    elif word[-2:] == "li" and syllables >= 3:
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word[-6:] for vowel in neutralising_vowels):
            return [word[:-1] + "ejä", word[:-1] + "eitä"]
        else:
            return [word[:-1] + "eja", word[:-1] + "eita"]

    
    #luettelo
    elif word[-2:] == "lo" and syllables >= 3:
        return [word + "ita", word + "ja"]

    elif word[-2:] == "la" and syllables >= 3:
        word = word[-1] + "oita"
        return [word]

    #henkilö
    elif word[-2:] == "lö" and syllables >= 3:
        return [word + "itä", word + "jä"]

    #sopraano
    elif word[-2:] == "no" and syllables >= 3:
        return [word + "ja", word + "ita"]

    #kaveri
    elif word[-2:] == "ri" and syllables >= 3:
        return [word[:-1] + "eita", word[:-1] + "eja"]

    elif word[-2:] == "in":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word = word[:-1] + "mpiä"
        else:
            word = word[:-1] + "mpia"
        return [word]
        

    #numero
    elif word[-2:] == "ro" and syllables >= 3:
        return [word + "ita", word + "ja"]

    
    #u, o, ö, y -> + j + a/ä
    elif word[-1] in ("u", "o"):
        word += "ja"
        return [word]
    
    elif word[-1] in ("y", "ö"):
        word += "jä"
        return [word]

    #i -> e change
    # when there is no change in i -> e sg, there is change in pl, if there is change in i->e > no change in pl
    #kivi

    #pankki        
    elif word[-1] == "i" and word not in i_to_e:
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-8:] for vowel in neutralising_vowels):
            word = word[:-1] + "ejä"
        else:
            word = word[:-1] + "eja"
        return [word]

        #I to E, need to work on 
    #All thanks to my beautiful girlfriend Maria that helped me with this program <3


    elif word[-3:] == "kas":
        word = word[:-2] + "kaita"
        return [word]
    
    elif word[-3:] == "käs":
        word = word[:-2] + "käitä"
        return [word]

    elif word[-3:] == "tar":
        word = word[:-2] + "taria"
        return [word]

    elif word[-2:] == "ar":
        word += "ia"
        return [word]
    
    elif word[-3:] == "pas":
        word = word[:-2] + "paita"
        return [word]

    elif word[-4:] == "rras":
        word = word[:-3] + "taita"
        return [word]

    elif word[-4:] == "ngas":
        word = word[:-3] + "kaita"
        return [word]

    elif word[-4:] == "llas":
        word = word[:-3] + "taita"
        return [word]

    elif word[-2:] == "as":
        word = word[:-1] + "ita"
        return [word]
              

    return [word]


# --- 1. SESSION STATE INIT ---
if "state" not in st.session_state:
    st.session_state.state = {
        "view": "menu",
        "idx": 0,
        "score": {"correct": 0, "wrong": 0},
        "quiz": [],
        "to_repair": [],
        "mode": "Mixed",
        "show_english": False,
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
    /* 1. Hide the specific 'chain' icon container */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
    
    /* 2. Hide older versions of the anchor link */
    .header-anchor {
        display: none !important;
    }

    /* 3. Force the H1 to ignore any reserved space on the right */
    h1 {
        text-align: center !important;
        width: 100% !important;
        padding-right: 0 !important;
        margin-right: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

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
    
    # 1. Get the answer(s). If it's a list, lowercase every item in it.
    raw_ans = partitive_sg(word) if case in ["SG", "Singular"] else partitive_pl(word)
    
    if isinstance(raw_ans, list):
        correct_list = [a.lower() for a in raw_ans]
    else:
        correct_list = [raw_ans.lower()]

    # 2. Store the primary answer for display (usually the first one)
    s["correct_answer"] = " or ".join(correct_list)

    # 3. Check if the user's input matches ANY of the correct answers
    if user_val in correct_list:
        if s["missed_current"]:
            s["score"]["wrong"] += 1
        else:
            s["score"]["correct"] += 1
        s["feedback"] = "correct"
    else:
        s["feedback"] = "wrong"
        s["wrong_sound_played"] = False
        if (word, case) not in s["to_repair"]:
            s["to_repair"].append((word, case))
        s["missed_current"] = True
        s["input_key_suffix"] += 1 # Added the increment here just in case

def next_question():
    s["idx"] += 1
    s["feedback"] = None
    s["missed_current"] = False
    s["show_english"] = False
    s["show_reveal"] = False
    s["input_key_suffix"] += 1
    s["correct_sound_played"] = False
    s["wrong_sound_played"] = False

    
    if s["idx"] >= len(s["quiz"]):
        if s["view"] == "repair":
            s["view"] = "menu" # Finish repairs -> Menu
        else:
            s["view"] = "results" # Finish quiz -> Results
    st.rerun()
# --- 4. LOGIC HANDLERS (Updated for Custom Mode) ---
def start_quiz(word_source, num, mode):
    # 1. Reset everything for a fresh start
    s["idx"] = 0
    s["score"]["correct"] = 0
    s["score"]["wrong"] = 0
    s["to_repair"] = []
    s["feedback"] = None
    s["show_reveal"] = False
    
    # 2. Select words and set mode
    sample_size = min(num, len(word_source))
    selected = random.sample(list(word_source), sample_size)
    
    # 3. Create the quiz list
    s["quiz"] = [(w, mode if mode != "Mixed" else random.choice(["Singular", "Plural"])) for w in selected]
    
    # 4. Change the view
    s["view"] = "game"

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
                st.rerun()
            


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
    
    # 3. Target Word Card - STABILNÍ VERZE (Tlačítko pod kartou)
    word_fi = word
    word_en = WORDS.get(word, "Translation missing")
    
    # Logika textu na kartě pro "Show Answer"
    card_front_text = word_fi
    card_front_label = "FINNISH"
    card_front_color = "#2c3e50"

    if s.get("show_reveal"):
        # Pre-emptively get the correct answer in case handle_submit hasn't run
        word, case = s["quiz"][s["idx"]]
        raw_ans = partitive_sg(word) if case in ["SG", "Singular"] else partitive_pl(word)
        
        # Format the list into a single string separated by " or "
        if isinstance(raw_ans, list):
            display_answer = " or ".join(raw_ans).lower()
        else:
            display_answer = raw_ans.lower()
            
        card_front_text = display_answer
        card_front_label = "CORRECT"
        card_front_color = "#11a20a"

    # ČISTÉ CSS PRO KARTU (Bez triků s neviditelností)
    st.markdown(f"""
    <style>
    .flip-card {{ 
        background-color: transparent; 
        width: 100%; 
        height: 200px; 
        perspective: 1000px; 
        margin-bottom: 10px;
    }}
    .flip-card-inner {{
      position: relative; width: 100%; height: 100%; text-align: center; 
      transition: transform 0.6s; transform-style: preserve-3d;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1); border-radius: 15px; border: 1px solid #ddd;
      transform: {"rotateY(180deg)" if s.get("show_english") else "rotateY(0deg)"};
    }}
    .face-front, .face-back {{
      position: absolute; width: 100%; height: 100%; backface-visibility: hidden;
      display: flex; flex-direction: column; justify-content: center; align-items: center; border-radius: 15px;
    }}
    .face-front {{ background-color: white; color: {card_front_color}; }}
    .face-back {{ background-color: #f8f9fa; color: #9b59b6; transform: rotateY(180deg); }}
    
    /* Styl pro tlačítko Flip, aby vypadalo lépe */
    div.stButton > button[key="flip_btn_visible"] {{
        background-color: #f0f2f6 !important;
        border: 1px solid #d0d0d0 !important;
        color: #555 !important;
        font-weight: bold !important;
    }}
    </style>
    """, unsafe_allow_html=True)

    # A. Vykreslení vizuální karty
    st.markdown(f"""
    <div class="flip-card">
      <div class="flip-card-inner">
        <div class="face-front">
          <p style="color: gray; font-size: 0.8rem; margin: 0;">{card_front_label}</p>
          <h1 style="font-size: 3.5rem; margin: 0; font-weight: 800;">{card_front_text}</h1>
        </div>
        <div class="face-back">
          <p style="color: gray; font-size: 0.8rem; margin: 0;">ENGLISH</p>
          <h1 style="font-size: 3.5rem; margin: 0; font-weight: 800;">{word_en}</h1>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

     # --- 4. SJEDNOCENÁ AKČNÍ ZÓNA ---
    st.markdown("<br>", unsafe_allow_html=True)
    
    container = st.container()

    with container:
        # 1. Flip Card (Vždy nahoře)
        if st.button("Flip Card", key="flip_btn_visible", use_container_width=True):
            s["show_english"] = not s.get("show_english", False)
            st.rerun()

        # 2. Spodní dynamická část (Input / Show Answer / Next Word)
        # Použijeme st.empty(), aby se obsah měnil na stejném místě bez "poskočení"
        action_spot = st.empty()

        with action_spot.container():
            if s.get("show_reveal"):
                # 1. Zobrazíme tlačítko (pokud na něj uživatel klikne, timer se zruší díky rerunu)
                if st.button("Next Word", use_container_width=True, key="next_btn_stable"):
                    s["show_reveal"] = False
                    next_question()
                    st.rerun()

                components.html(f"""
                    <script>
                        parent.setTimeout(() => {{
                            // Najde tlačítko s textem "Next Word" a klikne na něj
                            const buttons = parent.window.document.querySelectorAll("button");
                            for (const btn of buttons) {{
                                if (btn.innerText.includes("Next Word")) {{
                                    btn.click();
                                    break;
                                }}
                            }}
                        }}, 5500);
                    </script>
                """, height=0)

            elif s["feedback"] == "wrong":
                if not s.get("wrong_sound_played"):
                    play_audio("wrong_sound.mp3")
                    s["wrong_sound_played"] = True

                # --- TADY JE ZMĚNA: Zobrazíme input i při chybě ---
                input_key = f"in_{s['input_key_suffix']}"
                st.text_input(
                    "Answer", 
                    key=input_key, 
                    on_change=handle_submit, 
                    label_visibility="collapsed",
                    placeholder="Try again..."
                )
            
                st.error("❌ Not quite right.")
            
                if st.button("Show answer", use_container_width=True, key="reveal_btn_stable"):
                    s["score"]["wrong"] += 1
                    if (word, case) not in s["to_repair"]:
                        s["to_repair"].append((word, case))
                    s["show_reveal"] = True
                    s["feedback"] = None
                    st.rerun()

            elif s["feedback"] == "correct":
                if not s.get("correct_sound_played"):
                    play_audio("correct_sound.mp3")
                    s["correct_sound_played"] = True

                st.success("✅ Correct!")
                time.sleep(1.2)
                next_question()
                st.rerun()

            else:
                # Vstupní pole
                input_key = f"in_{s['input_key_suffix']}"
                st.text_input(
                    "Answer", 
                    key=input_key, 
                    on_change=handle_submit, 
                    label_visibility="collapsed",
                    placeholder="Type the Finnish form..."
                )

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

        correct_sound = "correct_sound.mp3"
        wrong_sound = "wrong_sound.mp3"
           # 6. Feedback Logic (Lose a heart on EVERY wrong submission)
        if s["feedback"] == "correct":
            play_audio("correct_sound.mp3")
            st.success("✅ Correct!")
            time.sleep(1.0)
            
            if s["idx"] + 1 == len(s["quiz"]):
                s["repair_initialized"] = False
                
            next_question()
            st.rerun()

        elif s["feedback"] == "wrong":
            # 1. Okamžité přehrání zvuku
            play_audio("wrong_sound.mp3")
            
            # 2. Zobrazení chyby (aby uživatel viděl, co se děje během sleepu)
            st.error(f"❌ Wrong! Hearts: {s['lives'] - 1}/3") 
            
            # 3. Aktualizace stavu
            s["lives"] -= 1
            s["last_processed_submit"] = s["input_key_suffix"]
            s["feedback"] = None
            
            # 4. Pauza, aby dozněl zvuk a uživatel viděl chybu
            time.sleep(1.0)
            
            # 5. Refresh pro aktualizaci UI (srdíček v sidebaru apod.)
            st.rerun()
            
                
            
            if s["lives"] <= 0:
                st.rerun() 