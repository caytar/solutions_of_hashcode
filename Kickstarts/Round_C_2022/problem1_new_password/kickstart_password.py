import re

min_length = 7
english_upper = re.compile(r'[A-Z]')
english_lower = re.compile(r'[a-z]')
numbers = re.compile(r'[0-9]')
special_chars = set(['#','@','*','&'])

def check_rule1(mypass):
    return len(mypass) >= min_length

def check_rule2(mypass):
    for mychar in mypass:
        if english_upper.match(mychar):
            return True
    return False

def check_rule3(mypass):
    for mychar in mypass:
        if english_lower.match(mychar):
            return True
    return False

def check_rule4(mypass):
    for mychar in mypass:
        if numbers.match(mychar):
            return True
    return False

def check_rule5(mypass):
    for mychar in mypass:
        if mychar in special_chars:
            return True
    return False

test_cases_count = int(input())
myarray = []

i=0
for i in range(0,test_cases_count):
    myarray.append ( [int(input()) ,input()] )
    if not check_rule5(myarray[i][1]):
        myarray[i][1] = myarray[i][1] + '@'
    if not check_rule4(myarray[i][1]):
        myarray[i][1] = myarray[i][1] + '1'
    if not check_rule3(myarray[i][1]):
        myarray[i][1] = myarray[i][1] + 'a'
    if not check_rule2(myarray[i][1]):
        myarray[i][1] = myarray[i][1] + 'A'
    if not check_rule1(myarray[i][1]):
        for j in range(len(myarray[i][1]),7):
            myarray[i][1] = myarray[i][1] + '0'



for i in range(0,test_cases_count):
    print("Case #%s: %s" % (i+1,myarray[i][1]))


'''

Lines = int(input())
myarray = []

i=0
for i in range(0,Lines):
    myarray.append ( [int(num) for num in input().split()] )


i=0
for i in range(0,Lines):
    print("Case #%s: %.6f" % (i+1,calculate_area(myarray[i])*math.pi))

'''