
lan0 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lan1 = lan0 + lan0

print("Witaj w programie do kodowania wiadomosci wedlug szyfru Cezara")
int krok = input ("Podaj twoj krok. max 26 ")

#if krok > 26:
#    print ("Twoj krok jest za duzy. Ale sproboj jeszcze raz")
#    krok = input ("Podaj twoj krok. max 26 ")

print(lan1[krok])
