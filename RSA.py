
prims=[0,0,0]
R=[]
Rs=[]
nVal=0


print("Ingrese tres números primos P, Q y N mayores de 23")

while nVal < 3:
    print("Ingrese el "+str(nVal+1)+"° #")
    num=int(input())

    if num >= 23:
        if ((2** (num - 1)) % num) == 1 or num == 2:
            prims[nVal]=num
            nVal=nVal+1
        else:
            print("El número no es primo")
    else:
        print("El númro debe ser mayor de 23")

p=prims[0]
q=prims[1]
n=prims[2]
        
fi=(p-1)*(q-1)
z=p*q

s=n+1
valid=False
while valid==False:
    if (n*s) % fi == 1:
        valid=True
    else:
        s=s+1


k=input("ingrese texto a encriptar:  ")
print("")

for i in range(len(k)):
    R.append([])
    R[i]=(ord(k[i])**n)%z


print("s: "+str(s)+" \n")
print("z: "+str(z)+" \n")
print("Al encriptar")
for i in range(len(k)):
    print(""+str(R[i]),end=" ")


for i in range(len(k)):
    Rs.append([])
    Rs[i]=(R[i]**s)%z

for i in range(len(Rs)):
    Rs[i]=chr(Rs[i])

print("")
print("Al desencriptar ")
for i in range(len(k)):
    print(""+str(Rs[i]),end=" ")