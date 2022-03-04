# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d={}
# for i in d1,d2:
#     d.update(i)
# for i in d:
#     if i in d2:
#         if i in d1:
#             d.update({i:d1[i]+d2[i]}) 
# print(d) 
a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}







d=[]
a=marks["Science"]
b=marks["Language"]
for i in range(len(a)):
    for j,k in marks.items():
        b=({j:k[i]})
        d.append(b)
print(d)                