import random
def number():
    print("Welcome to the number guessing game:")
    input("Press enter to continue.....")
    guess=0
    f=int(input("Enter the lower limit:"))
    b=int(input("Enter the upper limit:"))
    a=random.randint(f,b)
    while True:
        try:
            print("Hint: Your number would lie between",f,"and",b)
            j=int(input("Enter your number :"))
            guess +=1
            if j < a :
                print("Your option number is smaller")
                f=0+j
            elif j>a:
                print("Your option is bigger number")
                b=0+j
            else :
                print("Congratulation!! You found the number",a,"in",guess,"tries")
                exit()
        except ValueError:
            print("Entered wrong option")
number()