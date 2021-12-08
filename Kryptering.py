import bitarray

klartekst = bitarray.bitarray()                 #Lag en bitarray

klartekst.frombytes(input().encode('utf-8'))    #Ta input
klartekstListe = klartekst.tolist()             #.tolist() konverterer til en vanlig python list

key = bitarray.bitarray()

key.frombytes(input().encode('utf-8'))
keyListe = key.tolist()

if(len(klartekstListe) != len(keyListe)):
    print("De er ikke like store!!")
    quit()

print(klartekstListe)
print(keyListe)

kryptert = []
for i in range(0, len(klartekstListe)):
    if(klartekstListe[i] == keyListe[i]):
        kryptert.append(0)
    if(klartekstListe[i] != keyListe[i]):
        kryptert.append(1)
kryptertBitarray = bitarray.bitarray(kryptert)
print(kryptertBitarray)
