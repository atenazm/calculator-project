import math
def calculator():
    while True:
        print("/nsinmple calculator")
        print("1.calculat square root")
        print("2.calculat square")
        print("3.sum two numbers")
        print("4.Exit")
        choice = input("choose an number between (1-4) :")
        if choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid option,please try again.")
if __name__ == "__main__" :
    calculator()