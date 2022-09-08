def año_bisiesto(x):
    if x%4 == 0:
        print(f"{x} es un año Bisiesto") 
        return True
    elif x%400 == 0 and x%100 == 0:
        print(f"{x} es un año Bisiesto")
        return True
    else:
        print(f"{x} no es un año Bisiesto")

año_bisiesto(2200)        
    