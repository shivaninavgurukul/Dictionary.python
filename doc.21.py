Sample_Data = [{"V":"S001"},
{"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII":"S005"}, 
{"V":"S009"},{"VIII":"S007"}]
d=[]
for i in Sample_Data:
    for j in i:
        # print(i[j])
        d.append(i[j])
# print(d)
d1=[]
for i in d:
    if i not in d1:
        d1.append(i)
print(d1)    