p1 = [3,1,9]
p2 = [2,1,2,1]

p3 = []


counter = -1
for i in p1:
    num = p1[counter] + p2[counter]
    p3.insert(0,num)
    counter -= 1
if len(p2) > len(p1):
    if len(p2) + counter == 0:
        p3.insert(0,p2[0])
    else:
        p3.insert(0,p2[0:counter+1])
print(p3)
