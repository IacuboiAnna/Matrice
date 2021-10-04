#Elaboraţi	un	program	care	citeşte	de	la	tastatură	un	tablou	pătratic	cu	n	linii,	
#2	≤	n	≤	10,	şi	afişează	la	ecran	suma	componentelor	care	se	află:	
#a)	pe	diagonala	principală;	
#b)	pe	diagonala	secundară;	
#c)	mai	sus	de	diagonala	principală;	
#d)	mai	jos	de	diagonala	principală;	
#e)	mai	sus	de	diagonala	secundară;	
#f)	mai	jos	de	diagonala	secundară.	
#Se	consideră	că	componentele	tabloului	pătratic	sunt	numere	întregi,	care	se	citesc	de	la	tastatură
n=int(input('Dati numarul de randuri si coloane din matricea patratica:'))
matrice=[]
print('Dati elementele componente ale matricii:')
for i in range(n):
    elem=[]
    for j in range(n):
        elem.append(int(input()))
    matrice.append(elem)
print('Matricea patratica formata este:')
for i in range(n):
    for j in range(n):
        print(matrice[i][j], end=" ")
    print()
#Rezolvarea punctelor a si b:
d_prin=[]
d_sec=[]
for j in range(n):
    for i in range(len(matrice)):
        if (i==j):
            d_prin.append(matrice[i][j])
        if (i+j==n-1):
            d_sec.append(matrice[i][j])
print('Suma elementelor pe diagonala principala:', sum(d_prin))
print('Suma elementelor pe diagonala secundara:', sum(d_sec))
#Rezolvarea punctelor c si d:
d_prin_sus=[]
d_prin_jos=[]
for j in range(n):
    for i in range(len(matrice)):
        if (i-j<0):
            d_prin_sus.append(matrice[i][j])
        if (i-j>0):
            d_prin_jos.append(matrice[i][j])
print('Suma elementelor mai sus de diagonala principala:', sum(d_prin_sus))
print('Suma elementelor mai jos de diagonala principala:', sum(d_prin_jos))
#Rezolvarea punctelor e si f:
d_sec_sus=[]
d_sec_jos=[]
for j in range(n):
    for i in range(len(matrice)):
        if (i+j<n-1):
            d_sec_sus.append(matrice[i][j])
        if (i+j>n-1):
            d_sec_jos.append(matrice[i][j])
print('Suma elementelor mai sus de diagonala secundara:', sum(d_sec_sus))
print('Suma elementelor mai jos de diagonala secundara:', sum(d_sec_jos))