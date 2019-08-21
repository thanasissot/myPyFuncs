#python simple calculator

def add(x,y):
    return x + y


def substract(x,y):
    return x - y


def multiply(x,y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("you cant divide by zero silly...")
        print("maybe you wanna try that again!!")

    
operations = {
    "1" : add,
    "2" : substract,
    "3" : multiply,
    "4" : divide    
    
}
        
def calculator():
    print("1.Add\n2.Substract\n3.Multiply\n4.Divide")
    operation = input("Select Operations Form: ")
    x = int(input("Enter first Number:"))
    y = int(input("Enter second Number:"))
    
    print("The result is : " + str(operations[operation](x,y)))
    

