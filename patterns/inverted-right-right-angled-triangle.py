#Program to print pattern star pattern
#* * * * *
#  * * * *  
#    * * *
#      * *
#        *
for i in range (1,6):
    for j in range (1,i,1):
        print(" ",end="")
    for k in range(i-1,5,1):
        print("*",end="")
    print("")