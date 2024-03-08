import sys  # sys.exit() för att avsluta programmet - EJ MED I GUIDEN
import os # för att rensa terminalen - EJ MED I GUIDEN
import numpy
import matplotlib.pyplot as plt

def clear(): # EJ MED I GUIDEN
    return os.system('cls' if os.name == 'nt' else 'clear') # EJ MED I GUIDEN

clear() # EJ MED I GUIDEN
print("Andragradsekvationen ska anges enligt: ax² + bx + c = 0")

a = float(input("Ange a: "))
b = float(input("Ange b: "))
c = float(input("Ange c: "))
clear() # EJ MED I GUIDEN

# Här kollar vi nollställen, min/max punkter samt symetrilinjen 
xsym = -b/(2*a) # symetrilinjen
print("Symetrilinjen har x =", xsym)

extrempunkt = a*xsym**2 + b*xsym + c # Extrempunkten per formlen ax² + bx + c där x är symetrilinjen
if a > 0:
    print("Minimipunkt: ", "(",xsym,",", extrempunkt,")")
elif a < 0:
    maxipunkt = a*xsym**2 + b*xsym + c
    print("Maximipunkt: ", "(",xsym,",", extrempunkt,")")
    
D = b**2 - 4 * a * c # D står för Diskriminant, per formeln b² - 4ac
if D == 0:
    print("Ett nollställe:")
    x1 = (-b + numpy.sqrt(D)) / (2 * a)
    print("x = ", x1)  # Nollstället / roten
elif D > 0:
    print("Två nollställen:")
    x1 = (-b - numpy.sqrt(D)) / (2 * a)  # Första nollstället / första roten
    x2 = (-b + numpy.sqrt(D)) / (2 * a)  # Andra nollstället / andra roten
    print("x = ", x1)
    print("x = ", x2)
elif D < 0:
    print("Inga reela rötter")

# Grafuträkning av andragradsekvationen, observera att frågan om man vill räkna med graf eller inte ej är med i guiden.
räknaGraf = input("Vill du visa en graf? y/n:") # EJ MED I GUIDEN
if räknaGraf == "y": # EJ MED I GUIDEN

    # Funktion som räknar ut Y med respektive variabel
    def f(x, a, b, c):
        return a * x**2 + b * x + c  # Allmäna formen (ax² + bx + c)

    xlist = numpy.linspace(
        -10, 10, 1000
    )  # Skapar en lista med 1000 värden mellan -10 och 10
    ylist = f(xlist, a, b, c)  # Skapar ett y-värde för varje x-värde

    # Modulen som ritar grafen och självaste grafen
    plt.figure(num=0, dpi=120)
    plt.plot(xlist, ylist, label="f(x)")
    plt.title("Andragradsekvation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)  # Lägger till ett rutsystem som grafen visas i
    plt.show()  # Denna visar grafen

else: # EJ MED I GUIDEN
    # Om vill du inte vill räkna med graf - EJ MED I GUIDEN
    print("Programmet avslutas") # EJ MED I GUIDEN
    sys.exit() # EJ MED I GUIDEN

# Hjälp från Viktor & Filip S från TE23E
