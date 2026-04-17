def greet():
    print("Hello World")

greet()

def greet(name):
    print("hello my name is " , name)

greet("raja")

def raja(name = "Tumhara Baap"):
    print(name)
raja() 


#Example 
def check_even(num):
    if num % 2  == 0:
        print("even")
    else:
        print("odd")    

check_even(5)


# simple calculator
def add(a ,b):
    return a+b

def substract(a ,b):
    return a -b

def multiply(a ,b):
    return a*b

def devide(a ,b):
    if b == 0:
        return "Cannot devide by zero"
    return a /b;

while True:
    print("\n--- Calculator ---")
    print("1. ADD")
    print("2. Substract")
    print("3. multiply")
    print("4. Devide")
    print("5. Exit")

    choice = input("Enter Your Choice")

    if choice == 5:
        
        print("Good Bye")
        break;
     
    num1 = float(input("Enter Your First Number"))
    num2 = float(input("Enter Your Second Number"))

    if choice == "1":
        print("result",add(num1 , num2))
    elif choice == "2":
        print("result" ,substract(num1 , num2))
    elif choice == "3":
        print("result" , multiply(num1 , num2))
    elif choice == "4":
        print("result" , devide(num1 , num2))
    else:
        print("Invalid Choice")







