a={"1":["a","b"],"2":["c","d"]}
my=list(a.values())
for i in my[0]:
    for j in my[1]:
        print(i+j)
        