def factorial(num=5):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

def addition(x,y):
    return x+y

def printTable(num):
    for i in range(1,11):
        print(f"{i}*{num}={i*num}")

        
choice=0
while choice!=4:
    choice=int(input("""1.Factorial
    2. add numbers
    3. print table
    4. exit
    choice"""))
    match choice:
        case 1:
            num=int(input("enetr number "))
            ans=factorial(num)
            print(f"Factorial : {ans}")
        case 2:
            num1=int(input("enetr number "))
            num2=int(input("enetr number "))
            ans=addition(num1,num2)
            print(f"addition : {ans}")
        case 3:
            num=int(input("enetr number "))
            printTable(num)
        case 4:
            print("thank you for visiting....")
        case _:
            print("wrong choice")
