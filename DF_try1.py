# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    plt.show()

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


print("Hello")
csv_path = "C:\\apps\\Books-List\\Training\\csv\\TopSellingAlbums.csv"
df = pd.read_csv(csv_path)
print(df.head())
x = df[['Artist','Album']]

print(df.head())
x = df.iloc[2:6,1]
print(x)

x = df.loc[2:5,'Album']
print(x)

a = np.array([0, 1, 2, 3, 4])
print(a.dtype)
a[1] = 1000
print(a)

select = [1,2,3]
d = a[select]
print(d)
print(d.size)
print(a.shape)

u = np.array([1, 0])

v = np.array([0, 1])
z = u + v
Plotvec1(u, z, v)

x = np.linspace(0,2*np.pi,num=100)
print(type(x))
y=np.sin(x)
plt.plot(x,y)
plt.show()
