import random


def mainprog():
    correct = 0

#Player choosing
    num = str(input("Enter below or above 50 : "))
    color = str(input("Enter either red or black : "))
    eoro = str(input("Enter either even or odd : "))

    minrange = random.randint(1,50)
    maxrange = random.randint(50,100)

    prognum = random.randint(1,100)
    progsel = random.randint(1,2)

#AI choosing
    if (int(prognum) >= 50):
        progset = "above"
    elif (int(prognum) < 50):
        progset = "below"

    if (progsel == 1):
        progcolor = "black"
    elif (progsel == 2):
        progcolor = "red"

    mod = (prognum % 2)
    print(mod)
    if mod == 0:
        print("The number is even.")
        progeoro = "even"
    elif mod != 0:
        print("The number is odd.")
        progeoro = "odd"

#print(progsel)            
#print(str(progcolor))
#print(minrange)
#print(maxrange)
#print(prognum)


# Checks to see where the selections sit
    if (str(num) == str(progset)):
        print("Placement : You were within the parameters.")
        correct+=1
    else:
        print("Placement : You were not within the parameters.")

    if (str(color) == str(progcolor)):
        print("Color : Your choice was correct.")
        correct+=1
    else:
        print("Color : Your choice was incorrect.")

    if (str(eoro) == str(progeoro)):
        print("Even or Odd : Your choice was correct.")
        correct+=1
    else:
        print("Even or Odd : Your choice was incorrect.")

    print("Your answers : ")
    print("Above or Below : "+num)
    print("Red or Black : "+color)
    print("Even or Odd : "+eoro)
    print("\n")

    print("Computer's Answers : ")
    print("Above or Below : "+progset)
    print("Red or Black : "+progcolor)
    print("Even or Odd : "+progeoro)
    print("\n")

    print("Your results : "+str(correct)+"/3")

    restart()

def restart():
    restart = input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        mainprog()
    if restart == "n" or restart == "no":
        print ("Terminating Script...")
        print ("Thanks for playing!")

def main():
    window.mainloop()

mainprog()
