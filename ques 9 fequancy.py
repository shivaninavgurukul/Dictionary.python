a="MISSISSIPPI"
b=a
dic={}
for i in b:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)            


