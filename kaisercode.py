
lat0 = "abcdefghijklmnopqrstuvxyz"
lat1 = lat0 + lat0

deu0 = "aäbcdefghijklmnoöpqrsßtuüvwxyz"
deu1 = deu0 + deu0

print("Witaj w programie do kodowania wiadomosci wedlug szyfru Cezara")
klucz = input ("Podaj twoj klucz. max 26 ")

key = int(klucz)

if key > 26:
    print ("Twoj krok jest za duzy. Ale sproboj jeszcze raz")
    krok = input ("Podaj twoj klucz. max 26 ")

print (lat1)
message = input ("Wprowadz twoja wiadomosci do zakodowania: ")
print (lat1)

#Kodowanie wiadomosci
size = len(message)
size0 = int(size)

print("Dlugosc wiadomosci",size0)

for i in range(0,size0):
    message0 = message[i]
    print(message0)
    if message0 == ".":
        message0 = message0
    if message0 == ",":
        message0 = message0
    if message0 == "-":
        message0 = message0
    if message0 == " ":
        message0 = message0

    message1 = message0 + lat1[i]

print(message1)
print(lat1)