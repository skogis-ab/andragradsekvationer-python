import sys  # sys.exit() för att avsluta programmet - EJ MED I GUIDEN
import numpy
import matplotlib.pyplot as plt

print("Andragradsekvationen ska anges enligt: ax² + bx + c = 0")

a = float(input("Ange a: "))
b = float(input("Ange b: "))
c = float(input("Ange c: "))

# Här kollar vi nollställen och min/max punkter - D står för Diskriminanten
D = b**2 - 4 * a * c
if D == 0:
    print("Dubbelrot, ett nollställe")
    x1 = (-b + numpy.sqrt(D)) / (2 * a)
    print("x = ", x1)  # Nollstället / roten
elif D > 0:
    print("Två nollställen")
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
        return a * x**2 + b * x + c  # Allmäna formen (ax^2 + bx + c)

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
