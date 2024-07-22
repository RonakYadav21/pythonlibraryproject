n=int(input("enter rows of the matrix"))
m=int(input("enter coloumns of matrix"))
mat1=[]
for i in range(n):
    a=[]
    for j in range(m):
      ele=int(input())
      a.append(ele)
    mat1.append(a)
print(mat1)
for i in range(n):
   for j in range(m):  
     print(mat1[i][j],end=" ")
   print()

a=int(input("enter rows of the matrix"))
b=int(input("enter coloumns of matrix"))
mat2=[]
for i in range(a):
   c=[]
   for j in range(b):
      c.append(int(input()))
   mat2.append(c)
print(mat2)
 
if n==a and m==b:
   res=[[0 for j in range(m)] for i in range(n)]
   for i in range(n):
      for j in range(m):
         res[i][j]=mat1[i][j]+mat2[i][j]
else:
   print("matrix dimension must be same")
print(res)
