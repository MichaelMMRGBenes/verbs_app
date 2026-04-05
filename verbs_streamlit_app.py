#verbs streamlit app
import streamlit as st
import streamlit.components.v1 as components
import random
import time
import matplotlib.pyplot as plt
import base64


vocals = "aeiouäöy"
vocals_without_a = "eiouäöy"
changing_vowels = "äyö"
neutralising_vocals = "aou"

diphthongs = {
        "ai","ei","oi","ui","yi","äi","öi",
        "au","eu","iu","ou","äy","öy","ey","iy",
        "ie","uo","yö","io"
    }

exceptions_5_to_4 = ["selvitä", "hävitä"]
exceptions_6_to_4 = ["hävetä", "kiivetä", "ruveta", "todeta"]
exceptions_4_to_6 = ["hapata", "loitota", "helpota", "parata"]

verbs = [
    "ajaa", "ajatella", "alkaa", "aloittaa", "antaa", "asua", "auttaa", "avata", "edustaa", "elää",
    "erehtyä", "erota", "esiintyä", "etsiä", "haaveilla", "hakea", "halata", "hallita", "haluta", "harkita",
    "harjoitella", "harrastaa", "haastatella", "herätä", "herättää", "hiihtää", "hoitaa", "huomata", "huutaa", "hymyillä",
    "hypätä", "häiritä", "ihailla", "ihmetellä", "ilmoittaa", "istua", "itkeä", "jatkaa", "johtaa", "joutua",
    "juhlia", "juoda", "juosta", "jäädä", "kaivata", "kantaa", "katsoa", "kertoa", "kiittää", "kirjoittaa",
    "koettaa", "kokeilla", "kokata", "korjata", "kotiutua", "kouluuntua", "kuivata", "kujertaa",
    "kulua", "kuolla", "kuunnella", "kuulla", "kuvailla", "kylmetä", "kysyä", "kävellä", "käydä", "käyttää",
    "laittaa", "ladata", "lainata", "lakata", "laskea", "laulaa", "leikkiä", "lentää", "levätä", "liikkua",
    "lisätä", "loppua", "lukea", "luvata", "lähettää", "lähteä", "löytää", "mainita", "maistaa", "maksaa",
    "matkustaa", "meinata", "mennä", "merkitä", "miettiä", "muistaa", "muuttaa", "myydä", "myöntää", "nauraa",
    "nauttia", "neuvoa", "neuvotella", "noudattaa", "nousta", "nukkua", "nähdä", "odottaa", "ohjata", "oikaista",
    "olla", "omistaa", "opettaa", "opiskella", "oppia", "osata", "ostaa", "ottaa", "paeta", "paistaa",
    "pakata", "palkata", "panna", "parantaa", "pelata", "pelätä", "pestä", "piirtää", "pimetä", "pitää",
    "poistua", "puhua", "pukea", "purra", "pysähtyä", "päättää", "päästä", "rakastaa", "rakentaa", "ratkaista",
    "reagoida", "remontoida", "riidellä", "riippua", "riittää", "rohjeta", "ruveta", "saada", "saapua", "saattaa",
    "sallia", "sanoa", "saunoa", "seisoa", "selvittää", "siivota", "sijaita", "silittää", "soittaa", "sopia",
    "sulkea", "suositella", "suunnitella", "surra", "syntyä", "syödä", "säästää", "tapahtua", "tapella", "tarjoilla",
    "tarjeta", "tarvita", "tavata", "tavoittaa", "tehdä", "tietää", "tilata", "toivoa", "toimia", "toivottaa",
    "tuoda", "tuomita", "tulla", "tuntea", "tutustua", "tykätä", "työskennellä", "uida", "unohtaa", "uskaltaa",
    "uskoa", "vaatia", "vaihtaa", "valita", "valjeta", "valmistaa", "vanheta", "vastata", "viedä", "voida",
    "vuokrata", "välittää", "väsyä", "ymmärtää", "yrittää", "ystävystyä", "yöpyä", "älytä", "ääntää", "ölistä", "noutaa", "soutaa"
]

WORDS = {
    "ajaa": "to drive",    "ajatella": "to think",
    "alkaa": "to begin",    "aloittaa": "to start",
    "antaa": "to give",    "asua": "to live (reside)",
    "auttaa": "to help",    "avata": "to open",
    "edustaa": "to represent",    "elää": "to live",
    "erehtyä": "to make a mistake",    "erota": "to separate",
    "esiintyä": "to perform",    "etsiä": "to search",
    "haaveilla": "to dream",    "hakea": "to apply",
    "halata": "to hug",    "hallita": "to control",
    "haluta": "to want",    "harkita": "to consider",
    "harjoitella": "to practice",    "harrastaa": "to have a hobby",    "haastatella": "to interview",    "herätä": "to wake up",
    "herättää": "to wake (someone)",    "hiihtää": "to ski",
    "hoitaa": "to take care of",    "huomata": "to notice",    "huutaa": "to shout",
    "hymyillä": "to smile",    "hypätä": "to jump",    "häiritä": "to disturb",
    "ihailla": "to admire",    "ihmetellä": "to wonder",    "ilmoittaa": "to announce",
    "istua": "to sit",    "itkeä": "to cry",
    "jatkaa": "to continue",    "johtaa": "to lead",
    "joutua": "to end up",    "juhlia": "to celebrate",
    "juoda": "to drink",    "juosta": "to run",
    "jäädä": "to stay",    "kaivata": "to miss",
    "kantaa": "to carry",    "katsoa": "to watch",
    "kertoa": "to tell",    "kiittää": "to thank",
    "kirjoittaa": "to write",    "koettaa": "to try",
    "kokeilla": "to try",    "kokata": "to cook",
    "korjata": "to fix",    "kotiutua": "to settle in",
    "kouluuntua": "to become educated",    "kuivata": "to dry",
    "kujertaa": "to coo",    "kulua": "to pass (time)",
    "kuolla": "to die",    "kuunnella": "to listen",
    "kuulla": "to hear",    "kuvailla": "to describe",
    "kylmetä": "to get cold",    "kysyä": "to ask",
    "kävellä": "to walk",    "käydä": "to go (visit)",
    "käyttää": "to use",    "laittaa": "to put",
    "ladata": "to download",    "lainata": "to borrow",
    "lakata": "to stop",    "laskea": "to count",
    "laulaa": "to sing",    "leikkiä": "to play",    "lentää": "to fly",
    "levätä": "to rest",    "liikkua": "to move",
    "lisätä": "to add",    "loppua": "to end",
    "lukea": "to read",    "luvata": "to promise",
    "lähettää": "to send",    "lähteä": "to leave",
    "löytää": "to find",    "mainita": "to mention",
    "maistaa": "to taste",    "maksaa": "to pay",
    "matkustaa": "to travel",    "meinata": "to intend",
    "mennä": "to go",    "merkitä": "to mean",
    "miettiä": "to think about",    "muistaa": "to remember",
    "muuttaa": "to move/change",    "myydä": "to sell",
    "myöntää": "to admit",    "nauraa": "to laugh",
    "nauttia": "to enjoy",    "neuvoa": "to advise",
    "neuvotella": "to negotiate",    "noudattaa": "to follow",
    "nousta": "to rise",    "nukkua": "to sleep",
    "nähdä": "to see",    "odottaa": "to wait",
    "ohjata": "to guide",    "oikaista": "to straighten",
    "olla": "to be",    "omistaa": "to own",
    "opettaa": "to teach",    "opiskella": "to study",
    "oppia": "to learn",    "osata": "to be able to",
    "ostaa": "to buy",    "ottaa": "to take",
    "paeta": "to escape",    "paistaa": "to shine/fry",
    "pakata": "to pack",    "palkata": "to hire",
    "panna": "to put",    "parantaa": "to improve",
    "pelata": "to play (games)",    "pelätä": "to fear",
    "pestä": "to wash",    "piirtää": "to draw",
    "pimetä": "to get dark",    "pitää": "to like",
    "poistua": "to leave",    "puhua": "to speak",
    "pukea": "to dress",    "purra": "to bite",
    "pysähtyä": "to stop",    "päättää": "to decide",
    "päästä": "to get to",    "rakastaa": "to love",
    "rakentaa": "to build",    "ratkaista": "to solve",
    "reagoida": "to react",    "remontoida": "to renovate",
    "riidellä": "to argue",    "riippua": "to depend",
    "riittää": "to be enough",    "rohjeta": "to dare",
    "ruveta": "to start",    "saada": "to get",
    "saapua": "to arrive",    "saattaa": "to accompany",
    "sallia": "to allow",    "sanoa": "to say",
    "saunoa": "to sauna",    "seisoa": "to stand",
    "selvittää": "to clarify",    "siivota": "to clean",
    "sijaita": "to be located",    "silittää": "to iron/stroke",
    "soittaa": "to call/play",    "sopia": "to agree",
    "sulkea": "to close",
    "suositella": "to recommend",    "suunnitella": "to plan",
    "surra": "to mourn",    "syntyä": "to be born",    "syödä": "to eat",
    "säästää": "to save",    "tapahtua": "to happen",    "tapella": "to fight",
    "tarjoilla": "to serve",    "tarjeta": "to withstand cold",    "tarvita": "to need",
    "tavata": "to meet",    "tavoittaa": "to reach",
    "tehdä": "to do",    "tietää": "to know",
    "tilata": "to order",    "toivoa": "to hope",
    "toimia": "to function",    "toivottaa": "to wish",
    "tuoda": "to bring",
    "tuomita": "to judge",
    "tulla": "to come",
    "tuntea": "to feel/know",
    "tutustua": "to get to know",
    "tykätä": "to like",
    "työskennellä": "to work",
    "uida": "to swim",
    "unohtaa": "to forget",
    "uskaltaa": "to dare",
    "uskoa": "to believe",
    "vaatia": "to demand",
    "vaihtaa": "to change",
    "valita": "to choose",    "valjeta": "to dawn",
    "valmistaa": "to prepare",    "vanheta": "to age",
    "vastata": "to answer",    "viedä": "to take (away)",
    "voida": "can/may",    "vuokrata": "to rent",
    "välittää": "to care",    "väsyä": "to get tired",
    "ymmärtää": "to understand",
    "yrittää": "to try",
    "ystävystyä": "to become friends",
    "yöpyä": "to stay overnight",
    "älytä": "to realize",
    "ääntää": "to pronounce",
    "ölistä": "to yell",
    "noutaa": "to pick up",
    "soutaa": "to row"
}

def type_recognision(word):


    #saunoa
    if word[-1] in vocals and word[-2] in vocals:
        return ("type 1")
    
    elif word in exceptions_5_to_4 or word in exceptions_6_to_4:
        return ("type 4")
    
    elif word in exceptions_4_to_6:
        return ("type 6")

    #syödä
    elif word[-2:] in ("da", "dä"):
        return ("type 2")

   #opiskella     
    elif word[-3] not in vocals and word[-2] not in vocals and word[-1] in vocals:
        return ("type 3")
    
    #haluata and others - but not etä/eta - thats the 6th type  
    elif word[-2:] in ("ta","tä") and word[-3] in "aouäöy":
        return ("type 4")
    
    elif word[-3:] in ("ita", "itä"):
        return ("type 5")

    elif word[-3:] in ("eta", "etä"):
        return ("type 6")

def syllables_decider(word):
    vowels = "aeiouyäö"

    diphthongs = {
        "ai","ei","oi","ui","yi","äi","öi",
        "au","eu","iu","ou","äy","öy","ey","iy",
        "ie","uo","yö","io"
    }

    word = word.lower()
    count = 0
    i = 0

    while i < len(word):
        if word[i] in vowels:
            count += 1
            if i+2 < len(word) and word[i+1:i+3] in diphthongs:
                i += 1

            # normal diphthong or long vowel
            elif i+1 < len(word) and (
                word[i] == word[i+1] or
                word[i:i+2] in diphthongs
            ):
                i += 1

        i += 1

    return count

def a_checker(word):
    vocals = "aeiouäöy"
    vocals_without_a = "eiouäöy"
    
    for char in word:
        if char in vocals:

            if char not in vocals_without_a:
                return True
                
            else:
                return False
            
def random_pronoun():
    pronouns = ["minä", "sinä", "hän", "me", "te", "he"]
    random.shuffle(pronouns)
    x = pronouns.pop(0)
    return (x)

def reverse_KPT_change(word, verb_type):
    vocals = "aeiouäöy"
    if len(word) >= 3:
        if word[-1] == "k" and word[-2] in vocals:
            word += "k"
            return word
        
        elif word[-1] == "p" and word[-2] in vocals:
            word += "p"
            return word
        
        elif word[-2:] == "lp" and word[-3] in vocals:
            word += "p"
            return word

        elif word[-2:] == "lk" and word[-3] in vocals:
            word += "k"
            return word
        
        elif word[-1] == "t" and word[-2] in vocals:
            word += "t"
            return word
        
        #suunnata → suuntaan
        elif word[-2:] == "nn" and word[-3] in vocals:
            word = word[:-1] + "t"
            return word
        
        #hangata → hankaan
        elif word[-2:] == "ng" and word[-3] in vocals:
            word = word[:-1] + "k"
            return word
        
        #kammata → kampaan
        elif word[-2:] == "mm" and word[-3] in vocals:
            word = word[:-1] + "p"
            return word

        #vallata → valtaan
        elif word[-2:] == "ll" and word[-3] in vocals:
            word = word[:-1] + "t"
            return word
        
        #kerrata → kertaan
        elif word[-2:] == "rr" and word[-3] in vocals:
            word = word[:-1] + "t"
            return word
        
        #pihdata
        elif word[-2:] == "hd":
                word = word[:-1] + "t"
                return word
        #kalveta

        elif word[-2:] == "lv":
                word = word[:-1] + "p"
                return word
        
        #pudota → putoan
        elif word[-1] == "d" and word[-2] in vocals:
            word = word[:-1] + "t"
            return word

        #tavata → tapaan #siivota -> sii,  but kävellä -> kävelen, not käpelen, kuivata -> kuivaan
        elif word[-1] == "v" and word[-2] in vocals and word[-3:-1] not in ("ii","ui") and word != "käv":
            word = word[:-1] + "p"
            return word

        #valjeta → valkenen
        elif word[-2:] == "lj" and verb_type == "type 6":
            word = word[:-1] + "k"
            return word

        #rohjeta → rohkenen   
        elif word[-2:] == "hj" and verb_type == "type 6":
            word = word[:-1] + "k"
            return word
        
        #tarjeta → tarkenen
        elif word[-2:] == "rj" and verb_type == "type 6":
            word = word[:-1] + "k"
            return word
        

        #maata → makaan (NEEDS MORE WORK) #juosta -> juokset
        elif word[-2:] in ("aa","oo"):
            ending_vocal = word[-1]
            word = word[:-1] + "k" + ending_vocal
            return word
    
    
    return word



def KPT_change(word):
    vocals = "aeiouäeöy"

    if word[-2:] in ("kk","tt","pp") and word[-3] in vocals:
        return word[:-1]
    
    elif word[-1:] == "k" and word[-2] in vocals:
        return word[:-1]
    
    elif word[-1:] == "p" and word[-2] in vocals:
        return word[:-1] + "v"

    elif word[-2:] == "ht":
        return word[:-1] + "d"
    
    elif word[-1:] == "t" and word[-2] in vocals:
        return word[:-1] + "d"

    elif word[-2:] == "nk":
        return word[:-1] + "g"

    elif word[-2:] == "lt":
        return word[:-1] + "l"

    elif word[-2:] == "mp":
        return word[:-1] + "m"
     
    elif word[-2:] == "nt":
        return word[:-1] + "n"

    elif word[-2:] == "rt":
        return word[:-1] + "r"
    
    elif word[-3:] == "ulk" and word != "alk":
        return word[:-1] + "j"

    elif word[-3:] == "alk":
        return word[:-1]

    elif word[-2:] == "rk":
        return word[:-1] + "j"
    else:
        return word

def present_type_1_conjugation(word, pronoun):
    vocal_ending = word[-2]
    vartalo = word[:-2]
    if pronoun not in ("hän", "he"):
        vartalo_after_KPT_change = KPT_change(vartalo)
        if pronoun == "minä":
            conjugated_verb = vartalo_after_KPT_change + vocal_ending + "n"
            return conjugated_verb

        elif pronoun == "sinä":
            conjugated_verb = vartalo_after_KPT_change + vocal_ending + "t"
            return conjugated_verb
        elif pronoun == "me":
            conjugated_verb = vartalo_after_KPT_change + vocal_ending + "mme"
            return conjugated_verb
        elif pronoun == "te":
            conjugated_verb = vartalo_after_KPT_change + vocal_ending + "tte"
            return conjugated_verb
        
    elif pronoun == "hän":
        conjugated_verb = vartalo + vocal_ending + vocal_ending
        return conjugated_verb
    
    elif pronoun == "he":
        if any(vowel in word for vowel in changing_vowels):
            conjugated_verb = vartalo + vocal_ending + "vät"
            return conjugated_verb
        else:
            conjugated_verb = vartalo + vocal_ending + "vat"
            return conjugated_verb

def imperfect_type_1_conjugation(word, pronoun):
    syllables = syllables_decider(word)
    exeptions = ["antaa", "kantaa", "noutaa", "soutaa"]
    #lentää -> lensin, ymmärtää -> ymmärsin        
    if ((word[-4:] in ("ltaa", "ltää","rtaa","rtää","ntaa", "ntää", "nteä", "ntea") or (word[-3:] in ("taa","tää") and word[-4] in vocals and word[-5] in vocals))) and word not in exeptions:
        vocal_ending = "si"
        vartalo = word[:-3]
        if pronoun == "minä":
            conjugated_verb = vartalo + vocal_ending + "n"
            return conjugated_verb

        elif pronoun == "sinä":
            conjugated_verb = vartalo + vocal_ending + "t"
            return conjugated_verb
        
        elif pronoun == "me":
            conjugated_verb = vartalo + vocal_ending + "mme"
            return conjugated_verb
        
        elif pronoun == "te":
            conjugated_verb = vartalo + vocal_ending + "tte"
            return conjugated_verb
            
        elif pronoun == "hän":
            conjugated_verb = vartalo + vocal_ending
            return conjugated_verb
        
        elif pronoun == "he":
            if any(vowel in word for vowel in changing_vowels):
                conjugated_verb = vartalo + vocal_ending + "vät"
                return conjugated_verb
            else:
                conjugated_verb = vartalo + vocal_ending + "vat"
                return conjugated_verb
            
    #sanoa -> sanoin , kysyä -> kysyin
    elif word[-2:] in ("ua", "yä", "oa", "öä"):
        vocal_ending = word[-2] + "i"
        vartalo = word[:-2]
        if pronoun not in ("hän", "he"):
            vartalo_after_KPT_change = KPT_change(vartalo)
            if pronoun == "minä":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "n"
                return conjugated_verb

            elif pronoun == "sinä":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "t"
                return conjugated_verb
            elif pronoun == "me":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "mme"
                return conjugated_verb
            elif pronoun == "te":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "tte"
                return conjugated_verb
            
        elif pronoun == "hän":
            conjugated_verb = vartalo + vocal_ending
            return conjugated_verb
        
        elif pronoun == "he":
            if any(vowel in word for vowel in changing_vowels):
                conjugated_verb = vartalo + vocal_ending + "vät"
                return conjugated_verb
            else:
                conjugated_verb = vartalo + vocal_ending + "vat"
                return conjugated_verb
            
    #säästää - säästin itkeä - itkin & tanssia -> tanssin    
    elif word[-2:] in ("ea", "eä", "ää", "ia", "iä") and word != "tuntea":
        vocal_ending = "i"
        vartalo = word[:-2]
        if pronoun not in ("hän", "he"):
            vartalo_after_KPT_change = KPT_change(vartalo)
            if pronoun == "minä":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "n"
                return conjugated_verb

            elif pronoun == "sinä":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "t"
                return conjugated_verb
            elif pronoun == "me":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "mme"
                return conjugated_verb
            elif pronoun == "te":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "tte"
                return conjugated_verb
            
        elif pronoun == "hän":
            conjugated_verb = vartalo + vocal_ending
            return conjugated_verb
        
        elif pronoun == "he":
            if any(vowel in word for vowel in changing_vowels):
                conjugated_verb = vartalo + vocal_ending + "vät"
                return conjugated_verb
            else:
                conjugated_verb = vartalo + vocal_ending + "vat"
                return conjugated_verb
            
    #maksaa   -> maksoin 
    elif word[-2:] == "aa" and syllables == 2 and a_checker(word):
        vocal_ending = "oi"
        vartalo = word[:-2]
        if pronoun not in ("hän", "he"):
            vartalo_after_KPT_change = KPT_change(vartalo)
            if pronoun == "minä":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "n"
                return conjugated_verb

            elif pronoun == "sinä":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "t"
                return conjugated_verb
            elif pronoun == "me":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "mme"
                return conjugated_verb
            elif pronoun == "te":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "tte"
                return conjugated_verb
            
        elif pronoun == "hän":
            conjugated_verb = vartalo + vocal_ending
            return conjugated_verb
        
        elif pronoun == "he":
            if any(vowel in word for vowel in changing_vowels):
                conjugated_verb = vartalo + vocal_ending + "vät"
                return conjugated_verb
            else:
                conjugated_verb = vartalo + vocal_ending + "vat"
                return conjugated_verb
                        
    #ostaa -> ostin, rakastaa -> rakastin        
    elif word[-2:] == "aa":
        vocal_ending = "i"
        vartalo = word[:-2]
        if pronoun not in ("hän", "he"):
            vartalo_after_KPT_change = KPT_change(vartalo)
            if pronoun == "minä":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "n"
                return conjugated_verb

            elif pronoun == "sinä":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "t"
                return conjugated_verb
            elif pronoun == "me":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "mme"
                return conjugated_verb
            elif pronoun == "te":
                conjugated_verb = vartalo_after_KPT_change + vocal_ending + "tte"
                return conjugated_verb
            
        elif pronoun == "hän":
            conjugated_verb = vartalo + vocal_ending
            return conjugated_verb
        
        elif pronoun == "he":
            if any(vowel in word for vowel in changing_vowels):
                conjugated_verb = vartalo + vocal_ending + "vät"
                return conjugated_verb
            else:
                conjugated_verb = vartalo + vocal_ending + "vat"
                return conjugated_verb
            
def perfect_type_1_conjugation(word, pronoun):
    
    special_cases = ["tietää", "taitaa"]
    vartalo = word[:-1]

    if word in special_cases:
        vartalo = word[:-3] + "n" 
    if pronoun in ("minä", "sinä", "hän"):
            if any(vowel in word for vowel in changing_vowels):
                return vartalo + "nyt"
            else:
                return vartalo + "nut"
    else:
        return vartalo + "neet"


            

def present_type_2_conjugation(word, pronoun):

    #tehdä or nähdä - exceptions
    if word in ("tehdä","nähdä"):
        vartalo = word[:-3]
        if pronoun == "minä":
            conjugated_verb = vartalo + "en"
            return conjugated_verb

        elif pronoun == "sinä":
            conjugated_verb = vartalo + "et"
            return conjugated_verb
    
        elif pronoun == "me":
            conjugated_verb = vartalo + "emme"
            return conjugated_verb
        
        elif pronoun == "te":
            conjugated_verb = vartalo + "ette"
            return conjugated_verb
            
        elif pronoun == "hän":
            conjugated_verb = vartalo + "kee"
            return conjugated_verb
        
        elif pronoun == "he":
            if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
        
                conjugated_verb = vartalo  + "kevät"
                return conjugated_verb
            
    #syödä
    else:

        vartalo = word[:-2]
        if pronoun == "minä":
            conjugated_verb = vartalo + "n"
            return conjugated_verb

        elif pronoun == "sinä":
            conjugated_verb = vartalo + "t"
            return conjugated_verb
        
        elif pronoun == "me":
            conjugated_verb = vartalo + "mme"
            return conjugated_verb
        
        elif pronoun == "te":
            conjugated_verb = vartalo + "tte"
            return conjugated_verb
            
        elif pronoun == "hän":
            conjugated_verb = vartalo
            return conjugated_verb
        
        elif pronoun == "he":
            if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
        
                conjugated_verb = vartalo  + "vät"
                return conjugated_verb
            
            else:
                conjugated_verb = vartalo + "vat"
                return conjugated_verb
            
def imperfect_type_2_conjugation(word,pronoun):
    #kaydä
    if word == "käydä":
        vartalo = "kävi"
        if pronoun == "minä":
            return vartalo + "n"
        elif pronoun == "sinä":
            return vartalo + "t"
        elif pronoun == "hän":
            return vartalo
        elif pronoun == "me":
            return vartalo + "mme"
        elif pronoun == "te":
            return vartalo + "tte"
        elif pronoun == "he":
            return vartalo + "vät"
        
    #tehdä or nähdä  -> näin, tein  
    elif word in ("nähdä", "tehdä"):
        vartalo = word[:-3]
        if pronoun == "minä":
            return vartalo + "in"
        elif pronoun == "sinä":
            return vartalo + "it"
        elif pronoun == "hän":
            return vartalo + "ki"
        elif pronoun == "me":
            return vartalo + "imme"
        elif pronoun == "te":
            return vartalo + "itte"
        elif pronoun == "he":
            return vartalo + "kivät"
        
    #voida tupakoida  -> tupakoin  
    elif word[-3:] in ("idä", "ida"):
        vartalo = word[:-2]
        if pronoun == "minä":
            return vartalo + "n"
        elif pronoun == "sinä":
            return vartalo + "t"
        elif pronoun == "hän":
            return vartalo
        elif pronoun == "me":
            return vartalo + "mme"
        elif pronoun == "te":
            return vartalo + "tte"
        elif pronoun == "he":
            if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):

                return vartalo + "vät"
            else:
                return vartalo + "vat"
            
    #juoda -> join, syödä -> söin        
    elif syllables_decider(word) == 2:
        vartalo = word[:-2]
        if vartalo[-2:] in diphthongs:
            if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
                vartalo_after_change = vartalo[:-2] + "öi"
            else:
                vartalo_after_change = vartalo[:-2] + "oi"

            if vartalo[-2:] == "ie":
                vartalo_after_change = vartalo[:-2] + "ei"

            if pronoun == "minä":
                return vartalo_after_change + "n"
            
            elif pronoun == "sinä":
                return vartalo_after_change + "t"
            
            elif pronoun == "hän":
                return vartalo_after_change
            
            elif pronoun == "me":
                return vartalo_after_change + "mme"
            
            elif pronoun == "te":
                return vartalo_after_change + "tte"
            
            elif pronoun == "he":
                if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):

                    return vartalo_after_change + "vät"
                else:
                    return vartalo_after_change + "vat"
                
        #myydä -> myin saada -> sain        
        else:
            vartalo = word[:-2]
            vartalo_after_change = vartalo[:-1] + "i"

            if pronoun == "minä":
                return vartalo_after_change + "n"
            
            elif pronoun == "sinä":
                return vartalo_after_change + "t"
            
            elif pronoun == "hän":
                return vartalo_after_change
            
            elif pronoun == "me":
                return vartalo_after_change + "mme"
            
            elif pronoun == "te":
                return vartalo_after_change + "tte"
            
            elif pronoun == "he":
                if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):

                    return vartalo_after_change + "vät"
                else:
                    return vartalo_after_change + "vat"

def perfect_type_2_conjugation(word, pronoun):
    vartalo = word[:-2]
    if pronoun in ("minä", "sinä", "hän"):
            if any(vowel in word for vowel in changing_vowels):
                return vartalo + "nyt"
            else:
                return vartalo + "nut"
    else:
        return vartalo + "neet"

def present_type_3_conjugation(word, pronoun):
    exceptions = ["juosta"]

#opiskella, ajatella, mennä
    ending = word[-4:-2]
    #opisk(el), ajat(el), m(en)
    vartalo_to_process = word[:-4]
    #opisk, ajat, m
    vartalo_after_change = (reverse_KPT_change(vartalo_to_process,"type 3"))

    if word == "olla" and pronoun == "hän": return "on"
    if word == "olla" and pronoun == "he": return "ovat"

    if word in exceptions:
        ending = ""
        vartalo_after_change = word[:-3] + "ks"

    if pronoun == "minä":
        conjugated_verb = vartalo_after_change + ending + "en"
        return conjugated_verb

    elif pronoun == "sinä":
        conjugated_verb = vartalo_after_change + ending + "et"
        return conjugated_verb
        
    elif pronoun == "me":
        conjugated_verb = vartalo_after_change + ending + "emme"
        return conjugated_verb
        
    elif pronoun == "te":
        conjugated_verb = vartalo_after_change + ending + "ette"
        return conjugated_verb
            
    elif pronoun == "hän":
            conjugated_verb = vartalo_after_change + ending + "ee"
            return conjugated_verb
        
    elif pronoun == "he":
        if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
            conjugated_verb = vartalo_after_change + ending + "evät"
            return conjugated_verb
        
        else:
            conjugated_verb  = vartalo_after_change + ending + "evat"
            return conjugated_verb
        
def imperfect_type_3_conjugation(word, pronoun):
    exceptions = ["juosta"]

    #opiskella, ajatella, mennä
    ending = word[-4:-2]
    #opisk(el), ajat(el), m(en)
    vartalo_to_process = word[:-4]
    #opisk, ajat, m
    vartalo_after_change = (reverse_KPT_change(vartalo_to_process,"type 3"))

    if word in exceptions:
        ending = ""
        vartalo_after_change = word[:-3] + "ks"

    if pronoun == "minä":
        conjugated_verb = vartalo_after_change + ending + "in"
        return conjugated_verb

    elif pronoun == "sinä":
        conjugated_verb = vartalo_after_change + ending + "it"
        return conjugated_verb
        
    elif pronoun == "me":
        conjugated_verb = vartalo_after_change + ending + "imme"
        return conjugated_verb
        
    elif pronoun == "te":
        conjugated_verb = vartalo_after_change + ending + "itte"
        return conjugated_verb
            
    elif pronoun == "hän":
            conjugated_verb = vartalo_after_change + ending + "i"
            return conjugated_verb
        
    elif pronoun == "he":
        if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
            conjugated_verb = vartalo_after_change + ending + "ivät"
            return conjugated_verb
        
        else:
            conjugated_verb  = vartalo_after_change + ending + "ivat"
            return conjugated_verb
        
def perfect_type_3_conjugation(word, pronoun):
    #kävellä
    vartalo = word[:-2]
    if pronoun in ("minä", "sinä", "hän"):
            ending = vartalo[-1]
            if any(vowel in word for vowel in changing_vowels):
                return vartalo + ending + "yt"
            else:
                return vartalo + ending + "ut"
    else:
        ending = vartalo[-1]
        return vartalo + ending + "eet"

#haluata pakata
def present_type_4_conjugation(word, pronoun):
    exceptions = ["pelätä"]
    #hal(u)ata pak(a)ta
    vartalo = word[:-3]
    ending = word[-3]
    if word not in exceptions_5_to_4:
        vartalo_after_change = reverse_KPT_change(vartalo,"type 4")
    else:
        vartalo_after_change = vartalo


    if word in exceptions:
        vartalo_after_change = word[:-3] + "k"

    if pronoun == "minä":
        if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
            conjugated_verb = vartalo_after_change + ending + "än"
            return conjugated_verb
        else:
            conjugated_verb = vartalo_after_change + ending + "an"
            return conjugated_verb


    elif pronoun == "sinä":
        if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
            conjugated_verb = vartalo_after_change + ending + "ät"
            return conjugated_verb
        else:
            conjugated_verb = vartalo_after_change + ending + "at"
            return conjugated_verb
        
    elif pronoun == "me":
        if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
            conjugated_verb = vartalo_after_change + ending + "ämme"
            return conjugated_verb
        else:
            conjugated_verb = vartalo_after_change + ending + "amme"
            return conjugated_verb
        
    elif pronoun == "te":
        if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
            conjugated_verb = vartalo_after_change + ending + "ätte"
            return conjugated_verb
        else:
            conjugated_verb = vartalo_after_change + ending + "atte"
            return conjugated_verb
            
    elif pronoun == "hän":
            conjugated_verb = vartalo_after_change + ending
            if conjugated_verb[-2:] not in ("aa", "ää"):
                if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
                    conjugated_verb += "ä"
                else:
                    conjugated_verb += "a"

                if conjugated_verb[-2:] not in ("aa", "ää"):
                    if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
                        conjugated_verb += "ä"
                    else:
                        conjugated_verb += "a"

                return conjugated_verb
            
            else:
                return conjugated_verb

            
        
    elif pronoun == "he":
        if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
            conjugated_verb = vartalo_after_change + ending + "ävät"
            return conjugated_verb
        
        else:
            conjugated_verb  = vartalo_after_change + ending + "avat"
            return conjugated_verb
        

def imperfect_type_4_conjugation(word, pronoun):
    exceptions = ["pelätä"]
    #hal(u)ata pak(a)ta
    vartalo = word[:-3]
    ending = word[-3]
    if word not in exceptions_5_to_4:
        vartalo_after_change = reverse_KPT_change(vartalo,"type 4")
    else:
        vartalo_after_change = vartalo


    if word in exceptions:
        vartalo_after_change = word[:-3] + "k"

    if pronoun == "minä":
        conjugated_verb = vartalo_after_change + ending + "sin"
        return conjugated_verb



    elif pronoun == "sinä":
        conjugated_verb = vartalo_after_change + ending + "sit"
        return conjugated_verb
        
    elif pronoun == "me":
        conjugated_verb = vartalo_after_change + ending + "simme"
        return conjugated_verb
        
    elif pronoun == "te":
        conjugated_verb = vartalo_after_change + ending + "sitte"
        return conjugated_verb
            
    elif pronoun == "hän":
            conjugated_verb = vartalo_after_change + ending + "si"
            return conjugated_verb
                    
    elif pronoun == "he":
        if any(vowel in word for vowel in changing_vowels) or not any(vowel in word for vowel in neutralising_vocals):
            conjugated_verb = vartalo_after_change + ending + "sivät"
            return conjugated_verb
        
        else:
            conjugated_verb  = vartalo_after_change + ending + "sivat"
            return conjugated_verb
     
def perfect_type_4_conjugation(word, pronoun):
    #kiivetä -> kiivennyt
    vartalo = word[:-2]
    if pronoun in ("minä", "sinä", "hän"):
            if any(vowel in word for vowel in changing_vowels):
                return vartalo + "nnyt"
            else:
                return vartalo +  "nnut"
    else:
        return vartalo + "nneet"

def present_type_5_conjugation(word, pronoun):
    #tarvita -> tarvitse
    vartalo = word[:-1]
    vartalo_after_change = vartalo + "se"

    if pronoun == "minä":
        conjugated_verb = vartalo_after_change + "n"
        return conjugated_verb

    elif pronoun == "sinä":
        conjugated_verb = vartalo_after_change + "t"
        return conjugated_verb
    
    elif pronoun == "me":
        conjugated_verb = vartalo_after_change + "mme"
        return conjugated_verb
    
    elif pronoun == "te":
        conjugated_verb = vartalo_after_change + "tte"
        return conjugated_verb
        
    elif pronoun == "hän":
        conjugated_verb = vartalo_after_change + "e"
        return conjugated_verb
    
    elif pronoun == "he":
        if any(vowel in word for vowel in changing_vowels):
            conjugated_verb = vartalo_after_change + "vät"
            return conjugated_verb
        else:
            conjugated_verb = vartalo_after_change + "vat"
            return conjugated_verb
        
def imperfect_type_5_conjugation(word, pronoun):
    #tarvita -> tarvitse
    vartalo = word[:-1]
    vartalo_after_change = vartalo + "si"

    if pronoun == "minä":
        conjugated_verb = vartalo_after_change + "n"
        return conjugated_verb

    elif pronoun == "sinä":
        conjugated_verb = vartalo_after_change + "t"
        return conjugated_verb
    
    elif pronoun == "me":
        conjugated_verb = vartalo_after_change + "mme"
        return conjugated_verb
    
    elif pronoun == "te":
        conjugated_verb = vartalo_after_change + "tte"
        return conjugated_verb
        
    elif pronoun == "hän":
        conjugated_verb = vartalo_after_change
        return conjugated_verb
    
    elif pronoun == "he":
        if any(vowel in word for vowel in changing_vowels):
            conjugated_verb = vartalo_after_change + "vät"
            return conjugated_verb
        else:
            conjugated_verb = vartalo_after_change + "vat"
            return conjugated_verb
        
def perfect_type_5_conjugation(word, pronoun):
    #häiritä -> häirinnyt
    vartalo = word[:-2]
    if pronoun in ("minä", "sinä", "hän"):
            if any(vowel in word for vowel in changing_vowels):
                return vartalo + "nnyt"
            else:
                return vartalo +  "nnut"
    else:
        return vartalo + "nneet"
        
def present_type_6_conjugation(word, pronoun):
    exceptions = ["aueta","kyetä", "vaieta","paeta"]
    #Vanheta  -> vanhenen
    vartalo = word[:-3]
    ending = word[-3]
    vartalo_after_KPT_change = reverse_KPT_change(vartalo,"type 6")

    if word in exceptions:
        vartalo_after_KPT_change = word[:-3] + "k"

    if pronoun == "minä":
        conjugated_verb = vartalo_after_KPT_change + ending + "nen"
        return conjugated_verb

    elif pronoun == "sinä":
        conjugated_verb = vartalo_after_KPT_change + ending + "net"
        return conjugated_verb
    
    elif pronoun == "me":
        conjugated_verb = vartalo_after_KPT_change + ending + "nemme"
        return conjugated_verb
    
    elif pronoun == "te":
        conjugated_verb = vartalo_after_KPT_change + ending + "nette"
        return conjugated_verb
        
    elif pronoun == "hän":
        conjugated_verb = vartalo_after_KPT_change + ending + "nee"
        return conjugated_verb
    
    elif pronoun == "he":
        if any(vowel in word for vowel in changing_vowels):
            conjugated_verb = vartalo_after_KPT_change + ending + "nevät"
            return conjugated_verb
        else:
            conjugated_verb = vartalo_after_KPT_change + ending + "nevat"
            return conjugated_verb

def imperfect_type_6_conjugation(word, pronoun):
    exceptions = ["aueta","kyetä", "vaieta","paeta"]
    #Vanheta  -> vanhenen
    vartalo = word[:-3]
    ending = word[-3]
    vartalo_after_KPT_change = reverse_KPT_change(vartalo,"type 6")

    if word in exceptions:
        vartalo_after_KPT_change = word[:-3] + "k"

    if pronoun == "minä":
        conjugated_verb = vartalo_after_KPT_change + ending + "nin"
        return conjugated_verb

    elif pronoun == "sinä":
        conjugated_verb = vartalo_after_KPT_change + ending + "nit"
        return conjugated_verb
    
    elif pronoun == "me":
        conjugated_verb = vartalo_after_KPT_change + ending + "nimme"
        return conjugated_verb
    
    elif pronoun == "te":
        conjugated_verb = vartalo_after_KPT_change + ending + "nitte"
        return conjugated_verb
        
    elif pronoun == "hän":
        conjugated_verb = vartalo_after_KPT_change + ending + "ni"
        return conjugated_verb
    
    elif pronoun == "he":
        if any(vowel in word for vowel in changing_vowels):
            conjugated_verb = vartalo_after_KPT_change + ending + "nivät"
            return conjugated_verb
        else:
            conjugated_verb = vartalo_after_KPT_change + ending + "nivat"
            return conjugated_verb
        
def perfect_type_6_conjugation(word, pronoun):
    #rohjeta -> rohjennut -> rohjenneet
    vartalo = word[:-2]
    if pronoun in ("minä", "sinä", "hän"):
            if any(vowel in word for vowel in changing_vowels):
                return vartalo + "nnyt"
            else:
                return vartalo +  "nnut"
    else:
        return vartalo + "nneet"

def verb_conjugation_present(word:str):
    pronoun = random_pronoun()
    verb_type = type_recognision(word)

    if verb_type == "type 1":
        print(f"{word}, {verb_type}: {pronoun} {(present_type_1_conjugation(word, pronoun))}")

    elif verb_type == "type 2":
        print(f"{word}, {verb_type}: {pronoun} {(present_type_2_conjugation(word, pronoun))}")
    
    elif verb_type == "type 3":
        print(f"{word}, {verb_type}: {pronoun} {(present_type_3_conjugation(word, pronoun))}")

    elif verb_type == "type 4":
        print(f"{word}, {verb_type}: {pronoun} {(present_type_4_conjugation(word, pronoun))}")

    elif verb_type == "type 5":
        print(f"{word}, {verb_type}: {pronoun} {(present_type_5_conjugation(word, pronoun))}")

    elif verb_type == "type 6":
        print(f"{word}, {verb_type}: {pronoun} {(present_type_6_conjugation(word, pronoun))}")


def verb_conjugation_imperfect(word:str):
    pronoun = random_pronoun()
    verb_type = type_recognision(word)

    if verb_type == "type 1":
       print(f"{word}, {verb_type}: {pronoun} {(imperfect_type_1_conjugation(word, pronoun))}")

    elif verb_type == "type 2":
        print(f"{word}, {verb_type}: {pronoun} {(imperfect_type_2_conjugation(word, pronoun))}")
    
    elif verb_type == "type 3":
        print(f"{word}, {verb_type}: {pronoun} {(imperfect_type_3_conjugation(word, pronoun))}")

    elif verb_type == "type 4":
        print(f"{word}, {verb_type}: {pronoun} {(imperfect_type_4_conjugation(word, pronoun))}")

    elif verb_type == "type 5":
        print(f"{word}, {verb_type}: {pronoun} {(imperfect_type_5_conjugation(word, pronoun))}")

    elif verb_type == "type 6":
        print(f"{word}, {verb_type}: {pronoun} {(imperfect_type_6_conjugation(word, pronoun))}")


def verb_conjugation_perfect(word:str):
    pronoun = random_pronoun()
    verb_type = type_recognision(word)

    if verb_type == "type 1":
       print(f"{word}, {verb_type}: {pronoun} {present_type_3_conjugation("olla", pronoun)} {(perfect_type_1_conjugation(word, pronoun))}")

    elif verb_type == "type 2":
        print(f"{word}, {verb_type}: {pronoun} {present_type_3_conjugation("olla", pronoun)} {(perfect_type_2_conjugation(word, pronoun))}")
    
    elif verb_type == "type 3":
        print(f"{word}, {verb_type}: {pronoun} {present_type_3_conjugation("olla", pronoun)} {(perfect_type_3_conjugation(word, pronoun))}")

    elif verb_type == "type 4":
        print(f"{word}, {verb_type}: {pronoun} {present_type_3_conjugation("olla", pronoun)} {(perfect_type_4_conjugation(word, pronoun))}")

    elif verb_type == "type 5":
        print(f"{word}, {verb_type}: {pronoun} {present_type_3_conjugation("olla", pronoun)} {(perfect_type_5_conjugation(word, pronoun))}")

    elif verb_type == "type 6":
        print(f"{word}, {verb_type}: {pronoun} {present_type_3_conjugation("olla", pronoun)} {(perfect_type_6_conjugation(word, pronoun))}")

TENSE_COLORS = {"Present": "#2196F3", "Imperfect": "#9C27B0", "Perfect": "#009688"}
TYPE_COLORS = {
    "type 1": "#00BCD4", "type 2": "#3F51B5", "type 3": "#FFD600", 
    "type 4": "#E91E63", "type 5": "#607D8B", "type 6": "#000000"
}

# ==========================================
# 2. SESSION STATE
# ==========================================
if "state" not in st.session_state:
    st.session_state.state = {
        "view": "menu",
        "idx": 0,
        "score": {"correct": 0, "wrong": 0},
        "quiz": [],
        "to_repair": [],
        "feedback": None,
        "correct_answer": "",
        "input_key_suffix": 0,
        "missed_current": False,
        "lives": 3,
        "show_english": False, 
        "show_reveal": False 
    }
s = st.session_state.state

# ==========================================
# 3. CORE LOGIC FUNCTIONS
# ==========================================

def get_correct_conjugation(word, tense, pronoun):
    v_type = type_recognision(word)
    t_idx = int(v_type.split()[-1]) - 1
    
    if tense == "Present":
        funcs = [present_type_1_conjugation, present_type_2_conjugation, present_type_3_conjugation, 
                 present_type_4_conjugation, present_type_5_conjugation, present_type_6_conjugation]
        return funcs[t_idx](word, pronoun)
    elif tense == "Imperfect":
        funcs = [imperfect_type_1_conjugation, imperfect_type_2_conjugation, imperfect_type_3_conjugation, 
                 imperfect_type_4_conjugation, imperfect_type_5_conjugation, imperfect_type_6_conjugation]
        return funcs[t_idx](word, pronoun)
    elif tense == "Perfect":
        auxiliary = present_type_3_conjugation("olla", pronoun)
        funcs = [perfect_type_1_conjugation, perfect_type_2_conjugation, perfect_type_3_conjugation, 
                 perfect_type_4_conjugation, perfect_type_5_conjugation, perfect_type_6_conjugation]
        participle = funcs[t_idx](word, pronoun)
        return f"{auxiliary} {participle}"
    return "error"

def play_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f'<audio autoplay="true" style="display:none;"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
            components.html(md, height=0)
    except: pass

def handle_submit():
    current_key = f"in_{s['input_key_suffix']}"
    user_val = st.session_state.get(current_key, "").strip().lower()
    if not user_val: return
    
    verb, tense, pronoun = s["quiz"][s["idx"]]
    correct_ans = get_correct_conjugation(verb, tense, pronoun).lower()
    s["correct_answer"] = correct_ans
    
    if user_val == correct_ans:
        if s["missed_current"]: s["score"]["wrong"] += 1
        else: s["score"]["correct"] += 1
        s["feedback"] = "correct"
        play_audio("correct_sound.mp3")
    else:
        s["feedback"] = "wrong"
        play_audio("wrong_sound.mp3") 
        s["input_key_suffix"] += 1 
        if (verb, tense, pronoun) not in s["to_repair"]: 
            s["to_repair"].append((verb, tense, pronoun))
        s["missed_current"] = True

def next_question():
    s["idx"] += 1
    s.update({"feedback": None, "missed_current": False, "show_english": False, "show_reveal": False})
    s["input_key_suffix"] += 1
    if s["idx"] >= len(s["quiz"]):
        s["view"] = "results"
    

# ==========================================
# 4. UI ENHANCEMENTS (JS/CSS)
# ==========================================
components.html("""
<script>
    const doc = window.parent.document;
    setInterval(() => {
        const input = doc.querySelector('input[type="text"]');
        if (input && doc.activeElement !== input) input.focus();
        if (input) input.setAttribute("autocomplete", "off");
    }, 300);
</script>""", height=0)

# ==========================================
# 5. VIEW LOGIC
# ==========================================
if s["view"] == "menu":
    st.markdown('<h1 style="text-align:center; color:#1e3d59;">Finnish Verb Master</h1>', unsafe_allow_html=True)
    
    with st.container(border=True):
        num = st.slider("Exercises:", 1, 50, 10)
        mode = st.selectbox("Tense:", ["Present", "Imperfect", "Perfect", "Mixed"])
        if st.button("Start Quiz", use_container_width=True):
            if verbs:
                selected_verbs = random.sample(verbs, min(num, len(verbs)))
                pronouns = ["minä", "sinä", "hän", "me", "te", "he"]
                s["quiz"] = [(v, (mode if mode != "Mixed" else random.choice(["Present", "Imperfect", "Perfect"])), random.choice(pronouns)) for v in selected_verbs]
                s.update({"view": "game", "idx": 0, "score": {"correct": 0, "wrong": 0}, "to_repair": []})
                st.rerun()
    st.caption("Developed by Michael Beneš", text_alignment="center")

elif s["view"] in ["game", "repair"]:
    verb, tense, pronoun = s["quiz"][s["idx"]]
    v_type = type_recognision(verb)
    h_col = TENSE_COLORS.get(tense, "#2196F3")
    c_acc = TYPE_COLORS.get(v_type, "#000000")

    if s["feedback"] == "correct": c_acc = "#4CAF50"
    elif s["feedback"] == "wrong": c_acc = "#F44336"

    st.markdown(f"""
    <style>
    .block-container {{ padding-top: 1rem !important; max-width: 600px; margin: auto; }}
    header {{ visibility: hidden; }}
    [data-testid="stVerticalBlock"] {{ gap: 0rem !important; }}
    
    .flip-card {{ height: 220px; perspective: 1000px; margin-top: 15px; margin-bottom: 25px; }}
    .flip-card-inner {{ position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; }}
    .flipped {{ transform: rotateY(180deg); }}
    .face-front, .face-back {{ 
        position: absolute; width: 100%; height: 100%; backface-visibility: hidden; 
        display: flex; flex-direction: column; justify-content: center; align-items: center; 
        border-radius: 20px; border: 5px solid {c_acc}; 
    }}
    .face-front {{ background-color: {c_acc}15; }}
    .face-back {{ transform: rotateY(180deg); background-color: #f8f9fa; }}
    
    div[data-baseweb="base-input"] {{ border: 2px solid {c_acc} !important; border-radius: 10px !important;}}
    .stButton > button {{ margin-top: 5px !important; }}
    </style>""", unsafe_allow_html=True)

    # Header
    cols = st.columns([5, 1])
    with cols[1]:
        if st.button("Quit"): s["view"] = "menu"; st.rerun()

    st.markdown(f'<h1 style="text-align:center; color:{h_col}; margin-bottom:-10px;">{tense.upper()}</h1>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align:center; color:{c_acc}; font-size:1.3rem; font-weight:bold; margin-bottom:10px;">VERB {v_type.upper()}</div>', unsafe_allow_html=True)
    st.progress(s["idx"] / len(s["quiz"]))

    # Card
    is_flipped = "flipped" if (s["show_english"] or s["show_reveal"]) else ""
    st.markdown(f"""
    <div class="flip-card">
        <div class="flip-card-inner {is_flipped}">
            <div class="face-front">
                <div style="color:gray;"><b style="color:{c_acc}; font-size:2.2rem;">{pronoun}</b></div>
                <h1 style="font-size:3.5rem; margin:0;">{verb}</h1>
            </div>
            <div class="face-back">
                <div style="color:gray;">{"CORRECT ANSWER" if s["show_reveal"] else "ENGLISH"}</div>
                <h1 style="font-size:3rem; margin:0;">{s["correct_answer"] if s["show_reveal"] else WORDS.get(verb, "???")}</h1>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    st.button("Flip Card", on_click=lambda: s.update({"show_english": not s["show_english"]}), use_container_width=True)

    # Input & Feedback Area
    if not s["show_reveal"] and s["feedback"] != "correct":
        st.text_input("Answer", key=f"in_{s['input_key_suffix']}", on_change=handle_submit, label_visibility="collapsed", placeholder="Type answer...")

    if s["feedback"] == "wrong" and not s["show_reveal"]:
        st.markdown('<div style="color:#F44336; text-align:center; font-weight:bold; padding:20px; border:1px solid #F44336; border-radius:8px; background:#fff5f5;margin-bottom:20px; margin-top:10px;">❌ Try again!</div>', unsafe_allow_html=True)
        if st.button("Show Answer", use_container_width=True):
            s["show_reveal"] = True
            st.rerun()

    elif s["feedback"] == "correct":
        st.markdown('<div style="color:#4CAF50; text-align:center; font-weight:bold; padding:20px; border:1px solid #4CAF50; border-radius:8px; background:#f6fff6; margin-top:10px;">✅ Correct!</div>', unsafe_allow_html=True)
        st.button("Next Word →", on_click=next_question, use_container_width=True)

    elif s["show_reveal"]:
        st.button("Next Word →", on_click=next_question, use_container_width=True)

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
            s["repair_initialized"] = False
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
            
            time.sleep(1.0)
            st.rerun()

            if s["lives"] <= 0:
                st.rerun() 