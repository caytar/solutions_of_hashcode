import math


def calculate_area(values):
    R=values[0]
    A=values[1]
    B=values[2]
    if (R*A) // B == 0 :
        return R*R*(1 + A*A )
    else :
         return R*R*(1 + A*A ) + calculate_area([(R*A)//B , A , B])

Lines = int(input())
myarray = []

i=0
for i in range(0,Lines):
    myarray.append ( [int(num) for num in input().split()] )


i=0
for i in range(0,Lines):
    print("Case #%s: %.6f" % (i+1,calculate_area(myarray[i])*math.pi))
