import sys #sys.exit() för att avsluta programmet
import numpy
import matplotlib.pyplot as plt
print("Andragradsekvation ska anges i form av ax^2 + bx + c = 0")

a = float(input("Ange a: "))
b = float(input("Ange b: "))
c = float(input("Ange c: "))

# Här kollar vi nollställen och min/max punkter
D = b**2 - 4*a*c # D står för Diskriminanten
if D == 0:
    print("Dubbelrot, ett nollställe")
    print("x = ", -b/(2*a))
elif D < 0: 
    print("Inga reela rötter")
elif D > 0:
    print("Två nollställen")

    # Rötter
    x1 = (-b - numpy.sqrt(D))/(2*a)
    x2 = (-b + numpy.sqrt(D))/(2*a)
    print("x = ", x1)
    print("x = ", x2)

# Grafuträkning av andragradsekvationen    
räknaGraf = input("Vill du räkna med graf? y/n:")
if räknaGraf == "y":
     
    # Funktion som räknar ut Y med respektive variabel
    def f(x, a, b, c):
        return a * x**2 + b * x + c # Allmäna formen (ax^2 + bx + c)
    
    xlist = numpy.linspace(-10, 10, 1000) # Skapar en lista med 1000 värden mellan -10 och 10
    ylist = f(xlist, a, b, c) # Skapar ett y-värde för varje x-värde    

    # Modulen som ritar grafen och självaste grafen
    plt.figure(num=0, dpi=120)
    plt.plot(xlist, ylist, label="f(x)")
    plt.title("Andragradsekvation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True) # Lägger till ett rutsystem som grafen visas i
    plt.show() # Denna visar grafen
else: 
    # Om vill du räkna med graf = n (nej)
    print("Programmet avslutas")
    sys.exit()