ls1 = [1, 2, 3, 4]
ls2 = [1, 2, 3, 4]
size1 = len(ls1)
size2 = len(ls2)
flag = 0
if size1 == size2:
    for i in range(size1):
        if ls1[i] == ls2[i]:
            flag = True

if flag == True:
    print("They are same")
else:
    print("They aren't same")
