import random

def lista():
    lista=[]
    i=0
    while(i<8):
        lista.append(random.randint(-100,895))
        i+=1
    return lista

def konzol_kiir():
        kiir=lista()
        for i in range(len(kiir)):
            if i < len(kiir) - 1:
                print(kiir[i], end="; ")  
            else:
                print(kiir[i])

def tizzel_oszthatoak_szama():
    tizesek = lista()  
    i = 0
    db = 0
    while i < len(tizesek):  
        if tizesek[i] % 10 == 0:  
            db += 1
        i += 1
    eredmeny=(f"Tízzel oszthatók száma: {db}")

    return eredmeny

def fajlba_ir():
    f = open("vegeredmeny.txt", "a", encoding="UTF-8")
    f.write(tizzel_oszthatoak_szama())
    f.close()



