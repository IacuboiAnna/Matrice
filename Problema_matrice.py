a=[[1,7,3,2,5],
[2,0,4,9,2],
[5,6,1,4,7],
[6,9,7,1,8],
[4,2,9,7,3]]
for i in range(0,len(a)):
    print(sum(a[i]))
suma=0
for indice in range(0,5):
    suma=0
    for rand in range(len(a)):
        suma+=a[rand][indice]
    print(suma)
d_prin=[]
d_sec=[]
for j in range(0,5):
    for i in range(len(a)):
        if (i==j):
            d_prin.append(a[i][j])
        if (i+j==4):
            d_sec.append(a[i][j])
print(d_prin)
print(d_sec)