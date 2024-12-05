def ertekel():    
    het_nap=input("Hét napja: ")
    ora_nev=input("Óra neve: ")
    ertek=int(input("Értékelés(0-5): "))
    joertek=bool(ertek>=0 and ertek<=5)

    while(joertek==False):
        if(ertek<0):
            ertek=int(input("Hiba, nem lehet kisebb, mint 0: "))
            joertek=bool(ertek>=0 and ertek<=5)
        if(ertek>5):
            ertek=int(input("Hiba, nem lehet nagyobb, mint 5: "))
            joertek=bool(ertek>=0 and ertek<=5)
    else:
        print("Köszönjük az összefoglalót!")
        print(f"Összefoglaló:{het_nap},{ora_nev},{ertek} érték.")
