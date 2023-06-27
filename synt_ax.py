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



///FUNCTIONS///


# INDENTATION - spaces in the beginning of a statement
# no. of statement is up to you but atleast one
if(5>2):
         print('okokok')


def func():
    print('a funcn')
func()
func()

# parameter
def func2(par):
    print('a',par)
func2("okk")
func2(2)

def func3(par,val):
    print(par+val)
func3('o','k')
func3(2,3)

def func(no):
    for i in range(0,5,+1):
        print(i,end='')
ar=[1,2,3,4]
func(ar)


# RECURSION
def func(val):
    print(val)
    if(val<5):
     func(val+1)

func(2)

def fun2():
    for i in range(1,4,+1):
        print('hello',i)
def fun1():
    print("func1")
    fun2()

fun1()

