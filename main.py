import sys
import filegenerator

input = input("Enter Decklist: ")
try:
    decklist = eval(input)
except:
    print("Invalid List")
    sys.exit()

decklist.pop(0)
print("deck:", decklist)
filegenerator.filegenerator(decklist)