n=int(input("Enter the number of rows:"))
k=ord("A")
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print(chr(k),end=" ")
        else:
            print(int(k)-64,end=" ")
        k=k+1
    print()