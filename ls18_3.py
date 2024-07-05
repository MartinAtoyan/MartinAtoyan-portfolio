s1 = {"a", "b", "c"}
s2 = {"A", "a", "c"}
s3 = s1.copy()
s4 = s2.copy()


for i in s1:
    for j in s2:
        if i == j:
            s3.remove(i)
            s4.remove(j)


print(s3)
print(s4)