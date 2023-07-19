sh = input("Enter Hours:")
sr = input("Enter Rate:")

try:
    fh = float(sh)
    fr = float(sr)
except:             # Incase someone enters TEN
    print("Error, please enter a numeric input")
    quit()

B = fh * fr
print("Total Bill:", B)