a=[1,2,3]

def add(x,y):
    return x+y


def reverse(str):
    revstr = str[::-1]
    return revstr

def f1():
    #global a 
    a[1] = 100
    print(a)

def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))

def foo1(*numbers):
    total = 0
    for number in numbers :
        total = total + number
    return total

tot = foo1(1,2,3,4,5,6)
print(tot)
foo(name="Anitha",age=42,like="god")

ans = add(4,5)
print(ans)
print(reverse("Anitha"))
f1()
print(a)