# k=(101,123,124,567)
# v=("shivani")
# d=dict.fromkeys(k,v)
# print(d)

# a={'course':'python','fess':1300,1:{'course':'javascript',2:3456}}
# a['course']='softewere'
# a[1]['fess']=45000
# print(a)

# for i in a:
#     if type(a[i]) is dict:
#         for k in a[i]:
#             print(k,'=',a[i][k])
#     else:
#         print(i,'=',a[i])        

l=[]
for i in range(6,8):
    for j in range(4,7):
        d=i*j
        l.append([d])
print(l)             