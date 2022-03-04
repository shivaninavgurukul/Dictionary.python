# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# # print(dic)
# dic["ball"]="red"
# dic["bat"]=4
# print(dic)


a=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
l=[]
for i in range(len(a)):
    for j in a[i]:
        if a[i][j] not in l:
            l.append(a[i][j])
print(l)            
