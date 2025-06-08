# Celebal ( Data Science ) ----- Assignment 1 ( Print the triangle pattern )
# Create lower triangular, upper triangular and pyramid containing the "*" character.


###  Lower Triangle  ###
n=int(input("Enter value of rows :"))
for i in range(1,n+1):
  for j in range(1,i+1):
    print('*',end=' ')
  print()

###  Upper Triangle  ###
n=int(input("Enter value of rows :"))
for i in range(n):
  for j in range(n,i,-1):
    print('*',end=' ')
  print()

###  Pyramid  ###
n=int(input("Enter value of rows :"))
for i in range(1,n+1):
  for k in range(n-i):
    print(' ',end='')
  for j in range(i):
    print('*',end=' ')
  print()

