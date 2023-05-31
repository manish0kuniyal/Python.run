#LOOP


# for j in range(17,9,-1):
# j=17;j<9;j-=1
#     print(j)
#
# for j in range(11, 0, -2):
#         print(j)
#end='' to print in the same line


# *****
# ****
# ***
# **
# *

for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end='')
    print()


# *
# **
# ***
# ****
# *****

print("\n")

for i in range(1,6,+1):
    for j in range (i):
        print("*",end='')
    print("")


# *****
# -----
# *****
# -----
# *****

print("\n")
for i in range (5):
    for j in range (1,5,+1):
        if(i%2==0):
            print("*",end='')
        else:
            print("-",end='')
    print()


# *       *
#   *   *
#     *
#   *   *
# *       *

for i in range (6):
    for j in range (1,6,+1):
        if((i==j) | (i+j==6)):
            print("*",end='')
        else:
            print(" ",end='')
    print()


#------*------
#-----***-----
#----*****----
#---*******---
#--*********--

print("\n")
k=5
for i in range (k):
        for j in range(k-i):
            print(" ",end='')
        for l in range(2*i-1):
            print("*",end='')

        print()
