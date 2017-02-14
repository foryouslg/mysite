def triangles():
    L = [1]
    while len(L) < 10:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

t = triangles()
for i in t:
    print(i)

