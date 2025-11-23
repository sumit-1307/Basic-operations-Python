#Operation 1 : Addition
def addition(inp1, inp2):
    add=inp1+inp2
    print("Addition of given numbers is:",add)
#Operation 2 : Subtraction
def subtraction(inp1, inp2):
    sub=inp1-inp2
    print("Subtraction of given numbers is:",sub)
#Operation 3 : Multiplication
def multiplication(inp1, inp2):
    mul=inp1*inp2
    print("Multiplication of given numbers is:",mul)
#Operation 4 : Division
def division(inp1, inp2):
    div=inp1/inp2
    print("Division of given numbers is:",div)

print("Task 1: Performing basic Mathematical Operations")
inp1=int(input("Enter First number:"))
inp2=int(input("Enter Second number:"))
addition(inp1, inp2)
subtraction(inp1, inp2)
multiplication(inp1, inp2)
division(inp1, inp2)