n = input('What is the number you want to test?')
list1 = [int(d) for d in str(n)]
list2 = list()
counter = 0
for x in list1:
    i= x**3
    list2.append(i)
f = sum(list2)


if int(n) == f:
    print('Yes it is an armstrong number')
else:
    print('No it isnt an armstrong number')

