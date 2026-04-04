import random
vocals = "aeiouäöy"
vocals_without_a = "eiouäöy"
changing_vowels = "äyö"
neutralising_vocals = "aou"

exceptions_5_to_4 = ["selvitä", "hävitä"]
exceptions_6_to_4 = ["hävetä", "kiivetä", "ruveta", "todeta"]
exceptions_4_to_6 = ["hapata", "loitota", "helpota", "parata"]

verbs = [
    "ajaa", "ajatella", "alkaa", "aloittaa", "antaa", "asua", "auttaa", "avata", "edustaa", "elää",
    "erehtyä", "erota", "esiintyä", "etsiä", "haaveilla", "hakea", "halata", "hallita", "haluta", "harkita",
    "harjoitella", "harrastaa", "haastatella", "herätä", "herättää", "hiihtää", "hoitaa", "huomata", "huutaa", "hymyillä",
    "hypätä", "häiritä", "ihailla", "ihmetellä", "ilmoittaa", "istua", "itkeä", "jatkaa", "johtaa", "joutua",
    "juhlia", "juoda", "juosta", "jäädä", "kaivata", "kantaa", "katsoa", "kertoa", "kiittää", "kirjoittaa",
    "koettaa", "kohtalo", "kokeilla", "kokata", "kokonaan", "korjata", "kotiutua", "kouluuntua", "kuivata", "kujertaa",
    "kuluu", "kuolla", "kuunnella", "kuulla", "kuvailla", "kylmetä", "kysyä", "kävellä", "käydä", "käyttää",
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
    "vuokrata", "välittää", "väsyä", "ymmärtää", "yrittää", "ystävystyä", "yöpyä", "älytä", "ääntää", "ölistä"
]


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
    #sanoa -> sanoin , kysyä -> kysyin
    if word[-2:] in ("ua", "yä", "oa", "öä"):
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
    elif word[-2:] in ("ea", "eä", "ää", "ia", "iä"):
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
            
    #lentää -> lensin, ymmärtää -> ymmärsin        
    elif word[-4:] in ("ltaa", "ltää","rtaa","rtää","ntaa", "ntää") or (word[-3:] in ("taa","tää") and word[-4] in vocals and word[-5] in vocals):
        vocal_ending = "si"
        vartalo = word[:-3]
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
    
def present_type_3_conjugation(word, pronoun):
    exceptions = ["juosta"]

#opiskella, ajatella, mennä
    ending = word[-4:-2]
    #opisk(el), ajat(el), m(en)
    vartalo_to_process = word[:-4]
    #opisk, ajat, m
    vartalo_after_change = (reverse_KPT_change(vartalo_to_process,"type 3"))

    if word == "olla" and pronoun == "hän": return "on"

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




special_verbs = ["selvitä", "hävitä","hävetä","kiivetä", "ruveta","todeta","hapata","loitota", "helpota","parata"]

for verb in verbs:
    verb_conjugation_imperfect(verb)