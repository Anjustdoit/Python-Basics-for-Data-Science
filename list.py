names =["A","B","C"]
del names[0]
print(names)


a = [5,12,72,55,89]
a = a+[1]
a.append(7)
a = a+ ["ABCD"]
a = a+ list('qrst')
a = a+ list(str(123))
a = a + [[4,5,6]]
a.append([7,8])
print(a)
a.insert(2,5000)
a.insert(2,[7,8,9])
print(a)
a.remove(1)
print(a)