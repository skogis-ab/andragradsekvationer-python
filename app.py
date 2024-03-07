import sys #sys.exit() för att avsluta programmet
import numpy as np
import matplotlib.pyplot as plt
print("Andragradsekvation ska anges i form av ax^2 + bx + c = 0")

a = float(input("Ange a: "))
b = float(input("Ange b: "))
c = float(input("Ange c: "))

#kollar nollställen och min/max punkter
D = b**2 - 4*a*c #Diskriminanten i ekvationen
if D == 0:
    print("Dubbelrot, ett nollställe")
elif D > 0:
    print("Två nollställen")
    
    #rötterna
    x1 = (-b - np.sqrt(D))/(2*a)
    x2 = (-b + np.sqrt(D))/(2*a)
    
    #Min/max punkter
    xsym = -b/(2*a)
    if a > 0:
        minpunkt = a*xsym**2 + b*xsym + c
        print("Minimipunkt", "(",xsym,",", minpunkt,")")
    else:
        maxipunkt = a*xsym**2 + b*xsym + c
        print("Maximipunkt", "(",xsym,",", maxipunkt,")")
    print("rötterna är x1=",x1, "och x2=",x2, "Symetrilinjen är Xsym=",xsym,)
elif D < 0: 
    print("Inga reealla nollställen")
    sys.exit()

#Uträkning av andragradsekvationen
RäknaGraf = input("Vill du räkna med graf? y/n:")
if RäknaGraf == "y":
     #modulen för att rita grafer
    
    def f(x, a, b, c):
        return a * x**2 + b * x + c #Allmäna formen för en andragradsekvation
        # ax^2 + bx + c
    
    xlist = np.linspace(-10, 10, 1000) #Skapar en lista med 1000 värden mellan -10 och 10
    ylist = f(xlist, a, b, c) #Skapar en lista med y-värden för varje x-värde    

    plt.figure(num=0, dpi=120)
    plt.plot(xlist, ylist, label="f(x)")
    plt.title("Andragradsekvation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
else: 
    print("Programmet avslutas")
    sys.exit()