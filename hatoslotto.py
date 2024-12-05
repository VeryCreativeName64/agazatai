from Huzas import Huzas
import fajlbeolvasas

huzasok=fajlbeolvasas.beolvas("huzasok.txt",[])

def huzasok_szama():
    db=0
    for i in range(0,len(huzasok)):
            db+=huzasok[i].szam
       

    print(f"A húzások száma: {db}")

def huzasid():
    osszeg=0
    i=0
    db=0
    while(i<len(huzasok)):
        if(huzasok[i].het==43):
                osszeg+=huzasok[i].szam
                db+=1
        i+=1
    
    return osszeg / len(huzasok)


    
           
                
