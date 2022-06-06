import sys
sys.setrecursionlimit(5500)

test_cases_count = int(input())
myarray = []

y_list = []

def sum_series(n):
    return (n*(n+1))/2

def find_elements(y,n):
    if y>n :
        y_list.append(n)
        find_elements(y-n,n-1)
    else:
        y_list.append(y)



i=0
for i in range(0,test_cases_count):
    myarray.append ( [int(num) for num in input().split()] )

for i in range(0,test_cases_count):
    if sum_series(myarray[i][0]) % (myarray[i][1] + myarray[i][2]) == 0:
        print ("Case #%s: POSSIBLE" % (i+1))
        y = (sum_series(myarray[i][0]) / (myarray[i][1] + myarray[i][2])) * myarray[i][2] 
        y_list = []
        find_elements(y,myarray[i][0])
        print(myarray[i][0]-len(y_list))
        for j in range(1,myarray[i][0]+1):
            if j not in y_list:
                print(j , end=" ")
        print(end="\n")
    else:
        print ("Case #%s: IMPOSSIBLE" % (i+1))

