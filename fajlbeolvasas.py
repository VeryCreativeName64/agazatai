from Huzas import Huzas


def beolvas(fajlnev,huzas_lista=[]):
    huzasfile=open("huzasok.txt", "r", encoding="UTF-8")
    elso_sor=huzasfile.readline()
    tobbi_sor=huzasfile.readlines()

    for i in range(0,len(tobbi_sor),1):
        sor=tobbi_sor[i].strip()
        sor_lista=sor.split("@")
        huzas=Huzas(int(sor_lista[0]),int(sor_lista[1]),int(sor_lista[2]),int(sor_lista[3]))
        huzas_lista.append(huzas)
    huzasfile.close()
    return huzas_lista

beolvas("huzasok.txt")
    

