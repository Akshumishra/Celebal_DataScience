# Celebal ( Data Science ) ----- Assignment 1 ( Print the triangle pattern )
# Create lower triangular, upper triangular and pyramid containing the "*" character.


###  Lower Triangle  ###
n = int(input("Enter value of rows :"))
for i in range(1,n+1):
  print('* '*i)


###  Upper Triangle  ###
n = int(input("Enter value of rows :"))
for i in range(n,0,-1):
  print('* '*i)


###  Pyramid  ###
n = int(input("Enter value of rows :"))
for i in range(1,n+1):
  print(' '*(n-i)+'* '*i)

