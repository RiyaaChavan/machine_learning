r=6
for i in range(1,r+1):
    for j in range(1,2*r):
        if i==r or i+j==r+1 or j-i==r-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()