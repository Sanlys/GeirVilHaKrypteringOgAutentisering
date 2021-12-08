import bitarray

def xor(klartekstListe, keyListe):
    kryptert = []                               #Lager en tom liste som skal fylles under
    for i in range(0, len(klartekstListe)):     #Kjører en gang per tegn i klartekstListe, denne listen er like lang som keyListe
        if(klartekstListe[i] == keyListe[i]):   #Linje 6-9 er en XOR operasjon, som fungerer på 1 bit fra hver liste om gangen
            kryptert.append(0)
        else:
            kryptert.append(1)
    return kryptert

klartekst = bitarray.bitarray()                 #Lag en bitarray

klartekst.frombytes(input().encode('utf-8'))    #Ta input
klartekstListe = klartekst.tolist()             #.tolist() konverterer til en vanlig python list

key = bitarray.bitarray()                       #Lag en til bitarray

key.frombytes(input().encode('utf-8'))          #Tar input i utf-8 format og lagrer i en bitarray
keyListe = key.tolist()                         #Gjør om fra bitarray til liste

if(len(klartekstListe) != len(keyListe)):       #Sjekker om de er like store. XOR kryptering kan ikke brukes om de ikke er like store
    print("De er ikke like store!!")
    quit()                                      #Lukker programmet

kryptert = xor(klartekstListe, keyListe)        #Kjører xor funksjonen og lagrer resultatet i kryptert
kryptertBitarray = bitarray.bitarray(kryptert)
print(kryptertBitarray)                         #Skriver ut kryptert tekst i binært format. 

#Den samme xor funksjonen kan brukes på dekryptering:

brukerKey = bitarray.bitarray()                 #Lager en bitarray
brukerKey.frombytes(input("Skriv inn passord\n").encode('utf-8'))    #Tar input i utf-8 format og lagrer i bitarrayen over
brukerKeyListe = brukerKey.tolist()             #Konverterer fra bitarray til liste

outputListe = xor(kryptert, brukerKey)          #Kjører xor'en igjen, med kryptert tekst og passordet brukeren skrev inn. Om passordet er likt som det skrevet før, vil dette reversere xor funskjonen
                                                #XOR:
                                                #0 xor 0 = 0
                                                #0 xor 1 = 1
                                                #1 xor 0 = 1
                                                #1 xor 1 = 0
                                                #Som du ser her, kan du ta output xor en av inputene for å få den andre inputen. Dette vil bare fungere om biten er lik som det den var for å kryptere.
output = bitarray.bitarray(outputListe)         #Konverter output til en bitarray, så jeg kan kovertere til utf-8 senere
print(output)
print(klartekst)
print(output.tobytes().decode('utf-8'))         #Konverterer outputen til utf-8 og printer den