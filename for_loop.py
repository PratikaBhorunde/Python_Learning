#for loop

#range(start, stop, step)
a = range(1,21,1)
for i in a:
    print(i)

#table of 5
for i in range(5,51,5):
    print(i)    

#any table by user input
n = int(input("Enter a number to print its table: "))
for i in range(n,(n*10)+1,n):
       print(i)    

#for loop for strings
a = "Pratika"
for i in range(7):
    print(a[i])       

#calculate length of string using for loop
a = "Pratika"
for i in range(len(a)):
    print(a[i])

