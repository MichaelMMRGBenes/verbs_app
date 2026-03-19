import random
#All thanks to my beautiful girlfriend Maria that helped me with this program <3
def get_first_vowel_in_long_word(word):
    vowels = "aeiouyäö"
    last_five = word[-5:]

    first_vowel = next((ch for ch in last_five if ch in vowels), None)
    return first_vowel

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

def sg_pl(decision:str):
    if decision == "s":
        return "singular"
    elif decision == "p":
        return "plural"
    elif decision == "b":
        return "both"


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
    exceptions = {"appelsiini":"appelsiineja", "voi":"voita","hidas":"hitaita", "laite":"laitteita","kausi": "kausia", "taide":"taiteita","laki":"lakeja","hotelli":"hotelleja","pullo":"pulloja","vuoro":"vuoroja","hana":"hanoja","verkko":"verkkoja","lahje":"lahkeita","kirkko":"kirkkoja","omena":"omenoita","ien":"ikeniä","koe":"kokeita", "rikas":"rikkaita", "mies":"miehiä", "puhelin":"puhelimia", "tytär":"tyttäriä", "kannel":"kanteleita", "sävel":"säveliä", "kyynel":"kyyneleitä", "sammal":"sammaleita", "taival":"taipaleita", "askel":"askeleita", "nivel":"niveliä","ommel":"ompeleita", "tanner":"tantereita", "manner":"mantereita", "seitsemän":"seitsemiä", "jääkiekko":"jääkiekkoja", "matala":"matalia","ihana":"ihania", "ahkera":"ahkeria", "sako":"sakkoja", "musiikki":"musiikkeja"}
    
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


    for item in exceptions:
        if item in word[-len(item):]:
            word = word[:-len(item)] + exceptions[item]
            return word

    for item in i_to_e:
        if item == word[-len(item):]:
            if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:]  for vowel in neutral_vowels) and not any(vowel in word[-5:] for vowel in neutralising_vowels):
                word += "ä"
            else:
                word += "a"
            return word
    

    #mansikka/
    if word[-3:] in ("kka","kko") and syllables >= 3 and not any(vowel in word for vowel in changing_vowels):
        word = word[:-2] + "oita"
        
    elif word[-4:] == "mmas":
        word = word[:-3] + "paita"
    
    elif word[-4:] == "idas":
        word = word[:-3] + "taita"

    elif word[-4:] == "aite":
        word = word[:-1] + "teita"
    

    #mukava, matala
    elif word[-3:] in ("ala", "ava", "ana", "ara", "isa", "era") and syllables == 3 and word[-4:] != "aala":
        word = word[:-1] + "ia"

    elif word[-3:] in ("ävä", "evä", "ärä") and syllables == 3:
        word = word[:-1] + "iä"
        
    #ravintola
    elif word[-2:] in ("la", "ra", "na", "ia") and syllables >= 3 and not any(vowel in word for vowel in changing_vowels):
        word = word[:-1] + "oita"

    #opiskelija 
    elif word[-3:] == "ija" and syllables >= 3:
        word = word[:-1] + "oita"

    elif word[-3:] == "ijä" and syllables >= 3:
        word = word[:-1] + "äitä"

    elif word[-2:] in ("lä", "rä", "nä", "iä") and syllables >= 3:
        word = word[:-1] + "öitä"

    #korkea
    elif word[-2:] == "ea" and syllables >= 3:
        word = word[:-1] + "ita"

    elif word[-2:] == "eä" and syllables >= 3:
        word = word[:-1] + "itä"
    #vadelma, majava
    elif word[-2:] in ("ma", "va"):
        word = word[:-1] + "ia"

    elif word[-2:] in ("mä", "vä"):
        word = word[:-1] + "iä"

    #aja -> ia, opettaja
    elif word[-3:] == "aja":
        word = word[:-1] + "ia" 

    elif word[-3:] == "äjä":
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
    #and syllables == 2 
    elif word[-1] == "ä" and word[-2:] != "ää":
        word = word[:-1] + "iä"

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

    #hai
    elif word[-3:] == "hai":
        word += "ta"

    #double vowel
    # puu, syy,  maa
    elif word[-2:] in ("uu", "ii", "aa"):
        word = word[:-1] + "ita"

    #myy, jää
    elif word[-2:] in ("ää","yy", "ee"):
        word = word[:-1] + "itä"

    #kuuloke     
    elif word[-2:] == "ke":
        word = word[:-1] + "keita"

    #huone, kone
    elif word[-1] == "e":
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-5:] for vowel in neutralising_vowels):        
            word += "itä"
        else:
            word += "ita"

#All thanks to my beautiful girlfriend Maria that helped me with this program <3            
    #rakkaus might need change to aus
    elif word[-2:] == "us":
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
    elif word[-3:] in ("lin"):
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

    #hoteli #might write there a warning - that there is as well other option
    #elif word[-2:] == "li" and syllables >= 3:
    #    word = word[:-1] + "eja"

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

        #I to E, need to work on 
#All thanks to my beautiful girlfriend Maria that helped me with this program <3
    #pankki        
    elif word[-1] == "i":
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-5:] for vowel in neutralising_vowels):
            word = word[:-1] + "ejä"
        else:
            word = word[:-1] + "eja"

    elif word[-3:] == "kas":
        word = word[:-2] + "kaita"

    #partitive_sg(word:str)

    return word

def partitive_sg(word:str) -> str:
    exceptions = {"kaappi":"kaappia","koti":"kotia","historia":"historiaa", "musiikki":"musiikkia","laki":"lakia","appelsiini":"appelsiinia", "suurin":"suurimpaa", "vesi":"vettä", "kieli":"kieltä","kansi":"kantta", "kausi":"kautta", "viini": "viiniä","vastaus":"vastausta",
                  "jälsi": "jälttä", "virsi":"virttä", "yksiö":"yksiötä","työhuone":"työhuonetta",
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
    #All thanks to my beautiful girlfriend Maria that helped me with this program <3
    #avaruus and kauneus
    elif word[-3:] in ("eus", "uus", "aus"):
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
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
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
 
def process_the_word_and_find_partitive (word:str, sg_pl:str) -> str:
    if sg_pl == "both":
        x = random.randint(1,2)
        if x % 2 == 0:
            wanted_partitive = partitive_sg(word)
     
        else:
            wanted_partitive = partitive_pl(word)

    elif sg_pl == "singular":
        wanted_partitive = partitive_sg(word)

    elif sg_pl == "plural":
        wanted_partitive = partitive_pl(word)

    
    return wanted_partitive

def main():
    print("\n\nWelcome!\nIn this little program you can practice your Finnish.\n\nLet's start with the question...\n")
    while True:
        try: 
            pl_or_sg_part = input("Do you want to practive partitive (s)ingular or (p)lural or (b)oth? ")
            if pl_or_sg_part in ("s","p","b"):
                break
            else: 
                print("\nThat is not correct input, please type in s or p and press enter!\n")
        except ValueError:
            print("\nPlease type in only s or p and press enter!")


    while True:
        try: 
            lenght_of_excercise = int(input("How many excercises do you want? "))
            break
        except ValueError:
            print("\nThat is not correct input, please type in number, like 5 or 10!\n")

    print("\nRemember - You can always exit the program by just pressing enter, if you want to practice random word, type (r)")
    type_of_exercise = sg_pl(pl_or_sg_part)


    i = 1
    correct = 0
    wrong = 0
    wrong_words = []
    try:
        with open("practiced_words.txt", "r") as my_file:
            words = [line.strip() for line in my_file if line.strip()]
    except FileNotFoundError:
        words = []

    while lenght_of_excercise >= i:
        print(f"\n{i}. exercise:")

        word_to_practice = input(
            "Write any Finnish word you want to practice for forming the partitive (don't forget the umlaut!): "
        )

        if word_to_practice == "":
            break

        elif word_to_practice == "r":
            if words:
                word_to_practice = random.choice(words)
                print(f"Random word: {word_to_practice}")
            else:
                print("No practiced words saved yet.")
                continue

        else:
            if word_to_practice not in words and len(word_to_practice) < 20:
                with open("practiced_words.txt", "a") as my_file:
                    my_file.write(word_to_practice + "\n")
                words.append(word_to_practice)

        if type_of_exercise == "both":
            current_type = random.choice(["singular", "plural"])
        else:
            current_type = type_of_exercise

        if current_type == "singular":
            partitive = partitive_sg(word_to_practice)
        else:
            partitive = partitive_pl(word_to_practice)


        word_in_partitive = input(f"Please write the {current_type} partitive form of the word {word_to_practice}, don't forget the umlaut!: ")
#WORK IN PROGRESS
        if partitive == word_in_partitive:
            print("\nYes, that is correct! Amazing job!")
            correct += 1
        else:
            while True:
                print(f"\nUnfortunatelly that is not correct.\n\nIf you want to try it again, write your new answer\nIf you want to just see the right answer, press Enter ")

                word_in_partitive = input(f"\nPlease write the {current_type} partitive form of the word {word_to_practice}, don't forget the umlaut!: ")
                if word_in_partitive == "":
                    print(f"\nThe right answer is {partitive}.")
                    exit = input("\nPress Enter to continue practicing. ")
                    if exit == "":
                        break
                if partitive == word_in_partitive:
                    print("\nYes, that is correct! You corrected yourself!")
                    break
            wrong += 1
            wrong_words.append(word_to_practice)
        i += 1

    print(f"\nOut of {lenght_of_excercise} exercises were {(correct/lenght_of_excercise)*100:.2f} % correct and {(wrong/lenght_of_excercise)*100:.2f} % wrong.")
    if len(wrong_words)> 0:
        decision = input("Do you want to practice the words you had wrong? (y)es or (n)o? ")
        if decision == "y":
            while len(wrong_words) > 0:
                random.shuffle(wrong_words)
                word_to_practice = wrong_words.pop()
                print(f"\nTry this word again: {word_to_practice}")
                if type_of_exercise == "both":
                    current_type = random.choice(["singular", "plural"])
                else:
                    current_type = type_of_exercise

                if current_type == "singular":
                    partitive = partitive_sg(word_to_practice)
                else:
                    partitive = partitive_pl(word_to_practice)

                word_in_partitive = input(f"Please write the {current_type} partitive form of the word {word_to_practice}, don't forget the umlaut!: ")

                if partitive == word_in_partitive:
                    print("\nYes, that is correct! Amazing job!")

                else:
                    print(f"\nUnfortunately that is not correct, the right answer is {partitive}.")
    again = (input("\nDo you want to practice more? (y)es or (n)o? "))
    if again == "y":
        print("Okay! Lets practice a bit more!")
        main()
    else:
                     
        print("\nThat's everything for today, thanks for using my short program!\nMichael Beneš, author of the program\n")
        #All thanks to my beautiful girlfriend Maria that helped me with this program <3
        while True:
            end = input("Press enter to exit the program")
            if end == "":
                break



def run_tests():
    print("\n--- RUNNING TESTS ---\n")

    tests_sg = {
"metsä":"metsää",
"joki":"jokea",
"lammas":"lammasta",
"vuori":"vuorta",
"saari":"saarta",
"kaupunki":"kaupunkia",
"puutarha":"puutarhaa",
"opiskelija":"opiskelijaa",
"laulaja":"laulajaa",
"kirjasto":"kirjastoa",
"koulu":"koulua",
"ruoka":"ruokaa",
"juoma":"juomaa",
"kahvila":"kahvilaa",
"ravintola":"ravintolaa",
"hotelli":"hotellia",
"matkustaja":"matkustajaa",
"lento":"lentoa",
"asema":"asemaa",
"linja-auto":"linja-autoa",
"lentokenttä":"lentokenttää",
"tietokone":"tietokonetta",
"puhelin":"puhelinta",
"sähköposti":"sähköpostia",
"verkkosivu":"verkkosivua",
"kirje":"kirjettä",
"laite":"laitetta",
"huone":"huonetta",
"kone":"konetta",
"työhuone":"työhuonetta",
"perhe":"perhettä",
"lapsi":"lasta",
"ystävä":"ystävää",
"naapuri":"naapuria",
"opettaja":"opettajaa",
"johtaja":"johtajaa",
"pelaaja":"pelaajaa",
"kirjailija":"kirjailijaa",
"lukija":"lukijaa",
"kuuntelija":"kuuntelijaa",
"pankki":"pankkia",
"merkki":"merkkiä",
"hylly":"hyllyä",
"katto":"kattoa",
"tori":"toria",
"meri":"merta",
"veri":"verta",
"uni":"unta",
"onni":"onnea",
"peli":"peliä",
"laki":"lakia",
"sää":"säätä",
"tie":"tietä",
"yö":"yötä",
"historia":"historiaa",
"taide":"taidetta",
"musiikki":"musiikkia",
"fysiikka":"fysiikkaa",
"ajatus":"ajatusta",
"kysymys":"kysymystä",
"vastaus":"vastausta",
"kokemus":"kokemusta",
"elämys":"elämystä",
"päivä":"päivää",
"viikko":"viikkoa",
"kuukausi":"kuukautta",
"vuosi":"vuotta",
"hetki":"hetkeä",
"aika":"aikaa",
"tapahtuma":"tapahtumaa",
"projekti":"projektia",
"tehtävä":"tehtävää",
"harjoitus":"harjoitusta",
"kirjahylly":"kirjahyllyä",
"tietokoneohjelma":"tietokoneohjelmaa",
"ravintolaketju":"ravintolaketjua",
"kauppakeskus":"kauppakeskusta",
"linja-autoasema":"linja-autoasemaa",
"rautatieasema":"rautatieasemaa",
"kaupunki":"kaupunkia",
"maalaiskylä":"maalaiskylää",
"taimitarha":"taimitarhaa",
"museo":"museota",
"teatteri":"teatteria",
"elokuva":"elokuvaa",
"näyttely":"näyttelyä",
"kirjallinen":"kirjallista",
"yliopisto":"yliopistoa",
"ammattikoulu":"ammattikoulua",
"päiväkoti":"päiväkotia",
"kouluvierailu":"kouluvierailua",
"matkakohde":"matkakohdetta",
"lomamatka":"lomamatkaa",
"tehtaanrakennus":"tehtaanrakennusta",
"puutarhakaluste":"puutarhakalustetta",
"pöytäliina":"pöytäliinaa",
"ruokapöytä":"ruokapöytää",
"keittiö":"keittiötä",
"olohuone":"olohuonetta",
"makuuhuone":"makuuhuonetta",
"vaatekaappi":"vaatekaappia",
"kenkäkaappi":"kenkäkaappia",
"lastenhuone":"lastenhuonetta",
"vessa":"vessaa",
"sauna":"saunaa",
"terassi":"terassia",
"parveke":"parveketta",
"piha":"pihaa",
"puutarha":"puutarhaa",
"kasvihuone":"kasvihuonetta",
"laituri":"laituria",
"vene":"venettä",
"laiva":"laivaa",
"juna":"junaa",
"bussi":"bussia",
"auto":"autoa",
"pyörä":"pyörää",
"moottoripyörä":"moottoripyörää",
"lentokone":"lentokonetta",
"taksi":"taksia",
"hevonen":"hevosta",
"lehmä":"lehmää","sika":"sikaa","lammas":"lammasta","kana":"kanaa",
"koira":"koiraa","kissa":"kissaa","hamsteri":"hamsteria",
"papukaija":"papukaijaa","akvaario":"akvaariota",
"lämmitin":"lämmitintä","jäähdytin":"jäähdytintä",
    "talo":"taloa","kukka":"kukkaa","kenkä":"kenkää","leipä":"leipää","maa":"maata",
    "puu":"puuta","tie":"tietä","yö":"yötä","koulu":"koulua","omena":"omenaa",
    "kirja":"kirjaa","kala":"kalaa","tyttö":"tyttöä","lapsi":"lasta","mies":"miestä",
    "nainen":"naista","rikas":"rikasta","kaunis":"kaunista","järvi":"järveä","kivi":"kiveä",
    "käsi":"kättä","vesi":"vettä","kieli":"kieltä","ahven":"ahventa","perhe":"perhettä",
    "ystävä":"ystävää","opettaja":"opettajaa","opiskelija":"opiskelijaa","auto":"autoa",
    "juna":"junaa","lentokone":"lentokonetta","kauppa":"kauppaa","kaupunki":"kaupunkia",
    "kylä":"kylää","sydän":"sydäntä","pöytä":"pöytää","tuoli":"tuolia","ovi":"ovea",
    "ikkuna":"ikkunaa","koira":"koiraa","kissa":"kissaa","hevonen":"hevosta","lintu":"lintua",
    "puhelin":"puhelinta","numero":"numeroa","kirjasto":"kirjastoa","sairaala":"sairaalaa",
    "ravintola":"ravintolaa","hotelli":"hotellia","työhuone":"työhuonetta","sähköposti":"sähköpostia",

    # i-type + consonant gradation
    "lumi":"lunta","susi":"sutta","kansi":"kantta","hirsi":"hirttä","varsi":"vartta",
    "veitsi":"veistä","kurki":"kurkea","särki":"särkeä","järki":"järkeä","merkki":"merkkiä",

    # -nen
    "ihminen":"ihmistä","suomalainen":"suomalaista","punainen":"punaista","sininen":"sinistä",

    # -us / -ys
    "rakkaus":"rakkautta","kauneus":"kauneutta","kysymys":"kysymystä","vastaus":"vastausta",

    # more variety
    "kirjekuori":"kirjekuorta","tietokone":"tietokonetta","vesipullo":"vesipulloa",
    "autokauppa":"autokauppaa","kirjahylly":"kirjahyllyä","koulukirja":"koulukirjaa",
    "talonmies":"talonmiestä","yövuoro":"yövuoroa","kesäloma":"kesälomaa","talvitakki":"talvitakkia",
    "pääkaupunki":"pääkaupunkia","linja-auto":"linja-autoa","sähköjohto":"sähköjohtoa",
    "puutarha":"puutarhaa","lentokenttä":"lentokenttää","vesihana":"vesihanaa",
    "kirjoituspöytä":"kirjoituspöytää","tietoverkko":"tietoverkkoa","matkapuhelin":"matkapuhelinta",
    "työpäivä":"työpäivää","opintotuki":"opintotukea","sähkölasku":"sähkölaskua",
    "pankkitili":"pankkitiliä","postilaatikko":"postilaatikkoa","sanomalehti":"sanomalehteä",
    "elokuvateatteri":"elokuvateatteria","kahvikuppi":"kahvikuppia","vesilasi":"vesilasia",
"paperi":"paperia","banaani":"banaania","appelsiini":"appelsiinia","kahvi":"kahvia",
"tee":"teetä","juusto":"juustoa","voi":"voita","sokeri":"sokeria","maito":"maitoa",
"vesipullo":"vesipulloa","kahvikuppi":"kahvikuppia","ruokalista":"ruokalistaa",

"ovi":"ovea","sormi":"sormea","polvi":"polvea","silmä":"silmää","hammas":"hammasta",
"jalka":"jalkaa","kävely":"kävelyä","hyppy":"hyppyä","lento":"lentoa",

"ystävällinen":"ystävällistä","iloinen":"iloista","surullinen":"surullista",
"kaunis":"kaunista","ruma":"rumaa","nopea":"nopeaa","hidas":"hidasta",

"kirje":"kirjettä","laite":"laitetta","huone":"huonetta","kone":"konetta",
"perhe":"perhettä","vene":"venettä","lause":"lausetta","alue":"aluetta",

"päivä":"päivää","viikko":"viikkoa","kuukausi":"kuukautta","vuosi":"vuotta",
"hetki":"hetkeä","aika":"aikaa",

"musiikki":"musiikkia","taide":"taidetta","historia":"historiaa","fysiikka":"fysiikkaa","opettaja":"opettajaa","johtaja":"johtajaa","pelaaja":"pelaajaa",

"kirjailija":"kirjailijaa","lukija":"lukijaa","kuuntelija":"kuuntelijaa",

"pankki":"pankkia","merkki":"merkkiä","hylly":"hyllyä","katto":"kattoa",

"tori":"toria","meri":"merta","veri":"verta","uni":"unta","onni":"onnea",

"peli":"peliä","laki":"lakia","sää":"säätä","tie":"tietä","yö":"yötä",

"ruoka":"ruokaa","juoma":"juomaa","kahvila":"kahvilaa","ravintola":"ravintolaa",

"lentokenttä":"lentokenttää","rautatieasema":"rautatieasemaa",
"kauppakeskus":"kauppakeskusta","linja-autoasema":"linja-autoasemaa",

"työpaikka":"työpaikkaa","toimisto":"toimistoa","yritys":"yritystä",

"harjoitus":"harjoitusta","kysymys":"kysymystä","vastaus":"vastausta",

"tapahtuma":"tapahtumaa","kokemus":"kokemusta","elämys":"elämystä",

"pöytäliina":"pöytäliinaa","kirjahylly":"kirjahyllyä","tietokoneohjelma":"tietokoneohjelmaa"
    }

    tests_pl = {"paperi":"papereita","banaani":"banaaneja","appelsiini":"appelsiineja","kahvi":"kahveja",
"tee":"teitä","juusto":"juustoja","voi":"voita","sokeri":"sokereita","maito":"maitoja",

"ovi":"ovia","sormi":"sormia","polvi":"polvia","silmä":"silmiä","hammas":"hampaita",
"jalka":"jalkoja","kävely":"kävelyjä","hyppy":"hyppyjä","lento":"lentoja",

"ystävällinen":"ystävällisiä","iloinen":"iloisia","surullinen":"surullisia",
"kaunis":"kauniita","ruma":"rumia","nopea":"nopeita","hidas":"hitaita",

"kirje":"kirjeitä","laite":"laitteita","huone":"huoneita","kone":"koneita",
"perhe":"perheitä","vene":"veneitä","lause":"lauseita","alue":"alueita",

"päivä":"päiviä","viikko":"viikkoja","kuukausi":"kuukausia","vuosi":"vuosia",
"hetki":"hetkiä","aika":"aikoja",

"musiikki":"musiikkeja","taide":"taiteita","historia":"historioita","fysiikka":"fysiikkoja",

"opettaja":"opettajia","johtaja":"johtajia","pelaaja":"pelaajia",
"kirjailija":"kirjailijoita","lukija":"lukijoita","kuuntelija":"kuuntelijoita",

"pankki":"pankkeja","merkki":"merkkejä","hylly":"hyllyjä","katto":"kattoja",

"tori":"toreja","meri":"meriä","veri":"veriä","uni":"unia","onni":"onnia",

"peli":"pelejä","laki":"lakeja","sää":"säitä","tie":"teitä","yö":"öitä",

"ruoka":"ruokia","juoma":"juomia","kahvila":"kahviloita","ravintola":"ravintoloita",

"lentokenttä":"lentokenttiä","rautatieasema":"rautatieasemia",
"kauppakeskus":"kauppakeskuksia","linja-autoasema":"linja-autoasemia",

"työpaikka":"työpaikkoja","toimisto":"toimistoja","yritys":"yrityksiä",

"harjoitus":"harjoituksia","kysymys":"kysymyksiä","vastaus":"vastauksia",

"tapahtuma":"tapahtumia","kokemus":"kokemuksia","elämys":"elämyksiä",

"pöytäliina":"pöytäliinoja","kirjahylly":"kirjahyllyjä","tietokoneohjelma":"tietokoneohjelmia",
    "talo":"taloja","kukka":"kukkia","kenkä":"kenkiä","leipä":"leipiä","maa":"maita",
    "puu":"puita","tie":"teitä","yö":"öitä","koulu":"kouluja","omena":"omenoita",
    "kirja":"kirjoja","kala":"kaloja","tyttö":"tyttöjä","lapsi":"lapsia","mies":"miehiä",
    "nainen":"naisia","rikas":"rikkaita","kaunis":"kauniita","järvi":"järviä","kivi":"kiviä",
    "käsi":"käsiä","vesi":"vesiä","kieli":"kieliä","ahven":"ahvenia","perhe":"perheitä",
    "ystävä":"ystäviä","opettaja":"opettajia","opiskelija":"opiskelijoita","auto":"autoja",
    "juna":"junia","lentokone":"lentokoneita","kauppa":"kauppoja","kaupunki":"kaupunkeja",
    "kylä":"kyliä","sydän":"sydämiä","pöytä":"pöytiä","tuoli":"tuoleja","ovi":"ovia",
    "ikkuna":"ikkunoita","koira":"koiria","kissa":"kissoja","hevonen":"hevosia","lintu":"lintuja",
    "puhelin":"puhelimia","numero":"numeroita","kirjasto":"kirjastoja","sairaala":"sairaaloita",
    "ravintola":"ravintoloita","hotelli":"hotelleja","työhuone":"työhuoneita","sähköposti":"sähköposteja",

    # i-type
    "lumi":"lumia","susi":"susia","kansi":"kansia","hirsi":"hirsiä","varsi":"varsia",
    "veitsi":"veitsiä","kurki":"kurkia","särki":"särkiä","järki":"järkiä","merkki":"merkkejä",

    # -nen
    "ihminen":"ihmisiä","suomalainen":"suomalaisia","punainen":"punaisia","sininen":"sinisiä",

    # -us / -ys
    "rakkaus":"rakkauksia","kauneus":"kauneuksia","kysymys":"kysymyksiä","vastaus":"vastauksia",

    # compounds
    "kirjekuori":"kirjekuoria","tietokone":"tietokoneita","vesipullo":"vesipulloja",
    "autokauppa":"autokauppoja","kirjahylly":"kirjahyllyjä","koulukirja":"koulukirjoja",
    "talonmies":"talonmiehiä","yövuoro":"yövuoroja","kesäloma":"kesälomia","talvitakki":"talvitakkeja",
    "pääkaupunki":"pääkaupunkeja","linja-auto":"linja-autoja","sähköjohto":"sähköjohtoja",
    "puutarha":"puutarhoja","lentokenttä":"lentokenttiä","vesihana":"vesihanoja",
    "kirjoituspöytä":"kirjoituspöytiä","tietoverkko":"tietoverkkoja","matkapuhelin":"matkapuhelimia",
    "työpäivä":"työpäiviä","opintotuki":"opintotukia","sähkölasku":"sähkölaskuja",
    "pankkitili":"pankkitilejä","postilaatikko":"postilaatikoita","sanomalehti":"sanomalehtiä",
    "elokuvateatteri":"elokuvateattereita","kahvikuppi":"kahvikuppeja","vesilasi":"vesilaseja"
    }

    correct = 0
    total = 0

    print("---- Singular tests ----")
    for word, expected in tests_sg.items():
        result = partitive_sg(word)
        total += 1
        if result == expected:
            print(f"✅ {word} → {result}")
            correct += 1
        else:
            print(f"❌ {word} → {result} (should be {expected})")

    print("\n---- Plural tests ----")
    for word, expected in tests_pl.items():
        result = partitive_pl(word)
        total += 1
        if result == expected:
            print(f"✅ {word} → {result}")
            correct += 1
        else:
            print(f"❌ {word} → {result} (should be {expected})")

    print(f"\nResult: {correct}/{total} correct ({(correct/total)*100:.2f}%)\n")

if False:
    main()
else:
    run_tests()


#Change To git hub