s1 = {"a", "b", "c"}
s2 = {"A", "a", "c"}


s3 = {None, None, None, None, None, None, None, None,}

for i in s1:
    for j in s2:
        if i != j:
            s3.add(i)
            s3.add(j)

s3.remove(None)

print(s3)


