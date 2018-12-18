N=int(input("Enter a number: "))
a=[]
for i in range(1,N+1):
    print(i,sep=" ",end=" ")
    if(i<N):
        print("+",sep=" ",end=" ")
    a.append(i)
print("=",sum(a))
 
print()
