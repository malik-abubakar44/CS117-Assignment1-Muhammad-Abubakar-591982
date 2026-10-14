# Logic Gates
A = int(input("Enter A: "))
B = int(input("Enter B: "))

if (A != 0 and A != 1) or (B != 0 and B != 1):
    print("Bits must be 0 or 1")
else:
    print("AND", A & B)
    print("OR", A | B)
    print("XOR =", A ^ B)
