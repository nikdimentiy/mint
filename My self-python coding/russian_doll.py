# the function represents: classic recursion call (for example: in Russian doll - "Matrioshka")

def doll(n):
    if n == 1:
        print("Tiny doll")
    else:
        print("The upper of doll, n = ", n)
        doll(n - 1)
        print("The bottom of doll, n = ", n)
