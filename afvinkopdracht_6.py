# Naam: Bram Bosch
# Datum: 15-10-2017
# Versie: 1.0

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.


def main():
    try
        bestand = "alpaca.fasta" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand\
        
        zoekwoord = input("Geef een zoekwoord op: ")
        
        headers, seqs = lees_inhoud(bestand) 
        except    
        lijstZoekwoord = [i for i, s in enumerate(headers) if zoekwoord in s]
        
        i=0
        index = 0
        print("Het aantal keer dat het zoekwoord voorkomt in de headers is:",len(lijstZoekwoord))
        print("In deze headers staat het zoekwoord:",lijstZoekwoord)
        for item in lijstZoekwoord:
            print(100*"-")
            index = int(lijstZoekwoord[i])
            isDNA = is_dna(seqs, index)
            print("Dit is de header die bij de sequentie hoort:")
            print(headers[index])
            knipt(seqs,index,zoekwoord)
            if type(isDNA) != bool:
                raise TypeError
            if isDNA == True:
                print("Het is een DNA sequentie.")
            else:
                print("Het is geen DNA sequentie of er zitten andere tekens dan alleen ATCG in.")
            i+=1
            #print(i)
    except:
        
       
def lees_inhoud(bestand):
    try
        bestand = open(bestand)
        headers = []
        seqs = []
        seq=""
        for line in bestand:
            if line.startswith(">"):
                line = line.replace("\n","")
                headers.append(line)
                if seqs != "":
                    seqs.append(seq)
                    seq = ""
            else:
                line = line.replace("\n","")
                seq += line
        seqs.append(seq)
        seqs.remove('')
        return headers, seqs
    except FileNotFoundError:
        print("Het opgevraagde bestand kan niet gevonden worden")
    
    
def is_dna(seqs,index):
    
    aantalg = int(seqs[index].count("G"))
    aantalc = int(seqs[index].count("C"))
    aantala = int(seqs[index].count("A"))
    aantalt = int(seqs[index].count("T"))
    totaal = aantalg + aantalc + aantala + aantalt
    #print(totaal)
    #print(len(seqs[index]))
    isDNA= False
    if totaal == len(seqs[index]):
        isDNA = True
    return isDNA


def knipt(seqs,index,zoekwoord):
    try
        enzymen = open("enzymen.txt")
        enzym_list = []
        i=0
        for regel in enzymen:
            enzym, seq = regel.split()
            seq = seq.replace("^","")
            for seq_index in range(0, len(seqs[index])):
                if seqs[index][seq_index:len(seq)+seq_index] == seq:
                    if enzym not in enzym_list:
                        enzym_list.append(enzym)
                        
        print("Deze restrictie enzymen knippen in de sequentie die bij het zoekwoord",zoekwoord,"hoort:")            
        while i < len(enzym_list):
            
            print(enzym_list[i])
            i += 1
    except FileNotFoundError:
        print("Het enzymen bestand kan niet gevonden worden")
    
main()
