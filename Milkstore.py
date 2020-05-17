def xxnx():
    c=input("                    Hi, what do you like to have?                  ")
    if c=="milk":
        half();
    elif c=="curd":
        company();
    else:
        print("No other item available")


def anything():
    say=input("Do you like to add something else then press y")
    if say=="y":
        xxnx();
    else:
        print("Thanks for shopping!!!!!!!!!!!!!!!!")


def quant():
    price=float(30)
    i=input("Good choice!!!!!!!, Amul 30rs per litre,how many litre do you like to have?")
    j=float(i)
    print("Fine! Your total amount is",j*price)
    anything();

def Mquant():
    rice=int(25)
    ai=input("how many litre do you want?")
    aj=int(ai)
    print("Your total bill is",ai*price)
    anything();


def half():
    company=input("Milk is fresh, which brand milk would you like to have?")
    if company=="Amul":
        quant();
    elif company=="Mahanad":
        Mquant();
    else:
        print("No other brand")
#####    curddd
def iquant():
    price=float(10)
    i=input("how many litre do you want?")
    j=float(i)
    print("Your total bill is",j*price)
    anything();

def iMquant():
    rice=float(15)
    ai=input("how many litre do you want?")
    aj=float(ai)
    print("Your total bill is",aj*rice)
    anything();
def company():
    company=input("Which company:")
    if company=="Amul":
        iquant();
    elif company=="Mahanad":
        iMquant();
    else:
        print("No other brand")
print("***************************************************Welcome to Mahananda milk store*****************************************************")

xxnx();


