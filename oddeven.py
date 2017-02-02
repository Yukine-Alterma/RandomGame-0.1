import random

num = str(input("Enter below or above 50 : "))
color = str(input("Enter either red or black : "))
eoro = str(input("Enter either even or odd : "))

minrange = random.randint(1,50)
maxrange = random.randint(50,100)

prognum = random.randint(1,100)
progsel = random.randint(1,2)

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

print(progsel)            
print(str(progcolor))
print(minrange)
print(maxrange)
print(prognum)

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

if (str(num) == str(progset)):
    print("Placement : You were within the parameters.")
    if (str(color) == str(progcolor)):
        print("Color : Your choice was correct.")
        if (str(eoro) == str(progeoro)):
            print("Even or Odd : Your choice was correct.")
            print("Result : 3/3")
        else:
            print("Even or Odd : Your choice was incorrect.")
            print("Result : 2/3")
    else:
        print("Color : Your choice was incorrect.")
        print("Result : 1/3")
else:
    print("Placement : You were not within the parameters.")
    print("Result : 0/3")
