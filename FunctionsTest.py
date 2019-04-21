def distance_from_zero(n):
    if type(n)==int or type(n)==float:
        return abs(n)
    else:
        return "Nope"
n=float(raw_input("type a number:"))
print distance_from_zero(n)
