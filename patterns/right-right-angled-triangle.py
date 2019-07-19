#Program to print star pattern as per below 
#    *
#   **
#  ***
# ****
#*****
for i in range(1,6):
    for j in range (i,i,-1):
        print(" ",end="")
    for k in range (1,i,1):
        print("*",end="")
    print("")
