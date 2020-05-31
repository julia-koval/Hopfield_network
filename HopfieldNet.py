with open('text.txt', 'r') as f:
    l = [line.strip() for line in f]

for i in range(len(l)):
    l[i]=l[i].split()
    for j in range(len(l[i])):
        l[i][j]=int(l[i][j])

import math
from math import sqrt
for i in range(len(l)):
    try:
        int(sqrt(len(l[i])))
    except ValueError:
        print('Матрица № ',i+1,' не квадратная. Измените текстовый документ')

n = int(sqrt(len(l[0]))) 
z=l[len(l)-1]
l=l[:len(l)-1]

for i,val in enumerate(l):
    globals()['x'+str(i)]=val

## Creating a weight matrix.

W = [[0 for x in range(n*n)] for y in range(n*n)]    
    
for i in range(len(l)):
    x=globals()['x'+str(i)]
    f = lambda x, n=n: [x[j:j+n] for j in range(0, len(x), n)]
    print('x',i,' = ',f(x))
    a=f(x)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]==1:
                a[i][j]='*'
            elif a[i][j]==-1:
                a[i][j]=''
        print(a[i])
    for h in range(n):
        for g in range(n):
            for c in range(n):
                if g==c:
                    W[g][c]=0
                else:
                    W[g][c]+=f(x)[h][g]*f(x)[h][c]
print('W = ',W)

s = lambda z, n=n: [z[j:j+n] for j in range(0, len(z), n)]
print('z = ',s(z))
Y=[]
for a in range(n):
    for i in range(n):
        summ=0
        for j in range(n):
            summ+=W[a][j]*s(z)[j][i]
        if summ>=0:
            Y.append(1)
        else:
            Y.append(-1)

count=0
y = lambda Y, n=n: [Y[j:j+n] for j in range(0, len(Y), n)]
while y(Y)!=s(z):
    for a in range(n):
        for i in range(n):
            summ=0
            for j in range(n):
                summ+=W[a][j]*y(Y)[j][i]
            if summ>=0:
                y(Y)[a][i]=1
            else:
                y(Y)[a][i]=-1
            count+=1
    if count==10000:
        print('За 10000 итераций совпадения не выявлено')
        break
        
print('Y = ',y(Y))
b=y(Y)
for i in range(len(b)):
    for j in range(len(b[i])):
        if b[i][j]==1:
            b[i][j]='*'
        elif b[i][j]==-1:
            b[i][j]=''
    print(b[i])