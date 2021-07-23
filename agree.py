from cs50 import get_string

s = get_string("Do you agree? ")
if s in["y", "yes"]:
    print("Agree")
elif s == "N" or s == "n":
    print("Not Agreed")