print("Welcome to the Magic 9 Ball...")
print()

print("By: <Neha Tirunagiri>")
print("[COM S 127 <A>]")
print()

print("What would you like to do?")
print()
choice = input("[c]alculator, [p]rediction, [q]uit: ")
print()
while True:
    if choice=="c":
        num1=int(input("enter the num1:"))
        num2=int(input("enter the num2:"))
        opertor=input("enter an opertor:")
        if opertor=="+":
            d=num1+num2
            print(d)
        elif opertor=="-":
            d=num1-num
            print(d)
        elif opertor=="*":
            d=num1*num2
            print(d)
        elif (opertor=="/") and (num2 !=0):
            d=num1/num2
            print(d)

        elif (opertor=="%") and (num2 !=0):
            d=num1%num2
            print(d)

        elif opertor=="**":
            d=num1**num2
            print(d)
        else:
            print("Right hand number (num2) cannot be zero!")
            exit()
    elif choice=="p":
        Question=input("enter your question:")
        length=len(Question) 
        prediction_value=length%10
        if prediction_value==1:
            print("it's good ")
        elif prediction_value==2:
            print("i dont know")
        elif prediction_value==3:
            print("yes it may")
        elif prediction_value==3:
            print("god knows")
        elif prediction_value==4:
            print("no i dont think so")
        elif prediction_value==5:
            print("it's horrible")
        elif prediction_value==6:
            print("mostlikely")
        elif prediction_value==7:
            print("not in near future")
        elif prediction_value==8:
            print("be aware")
        elif prediction_value==9:
            print("hopefully ")
        elif prediction_value==10:
            print("good luck")

    elif choice=="q":
        print("good bye")
        exit()
    else:
        print("invalid choice")
        exit()








