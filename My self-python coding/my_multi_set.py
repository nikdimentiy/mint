#  my realization  of hash table (hash function)

setsize = 10
myset = [[] for _ in range(setsize)]

#  operation add element in set
def add(x):
    myset[x % setsize].append(x)

#  operation find element in set
def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
    return False

#  operation delete element in set
def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]
            xlist.pop()
            return
