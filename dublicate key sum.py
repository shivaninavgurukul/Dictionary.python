# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# d={}
# for i in dic1,dic2,dic3:
#     d.update(dic1)
#     d.update(dic2)
#     d.update(dic3)
# print(d)    


d1={1:10, 2:20}
d2={3:30,2:40}
d3={5:50,6:60}            
dic={}
for i in d1,d2,d3:
    dic.update(i)   
for i in dic:
    if i in d1:
        if i in d2:
                dic.update({i:d1[i]+d2[i]})
print(dic)



