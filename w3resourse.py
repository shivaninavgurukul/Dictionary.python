# d={0:10,1:20,3:10}
# d.update({2:40})
# print(d)

# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# dic4={}
# for i in dic1,dic2,dic3:
#     dic4.update(i)
# print(dic4)    


# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def check_key(x):
#     if x in d:
#         print("yes key is present")
#     else:
#         print("key not present")
# check_key(5)
# check_key(8)
# check_key(6)            



# d = {'x': 10, 'y': 20, 'z': 30} 
# for i in d:
#     print(i,"->",d[i])


# n=int(input("enter the number:-"))
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)    

# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d2.update(d1)
# print(d2)



# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for i in d:
#     print(i,"correspond",d[i])

"q10"
# my_dict = {'data1':100,'data2':-54,'data3':247}
# s=0
# for i in my_dict:
#     s+=my_dict[i]
# print(s)

"q11"
# my_dict = {'data1':100,'data2':-54,'data3':247}
# m=1
# for i in my_dict:
#     m*=my_dict[i]
# print(m)

"q12"
# myDict = {'a':1,'b':2,'c':3,'d':4}
# if "a" in myDict:
#     del myDict['a']
# print(myDict) 
   
"q13"
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
i=0
b=0
d=[]
while i<len(keys):
    s={keys[i]:values[b]}
    d.append(s)
    i+=1
    b+=1
print(d)


"q14"

# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}
# for i in sorted(color_dict):
#     print(i,color_dict[i])

"q15"

# my_dict = {'x':500, 'y':5874, 'z': 560}
# m=0
# for i in my_dict:
#     if my_dict[i]>m:
#        m=my_dict[i]
# print(m)       
# m1=my_dict[i]
# if my_dict[i]<m1:
#     m1=my_dict[i]
# print (m1) 
# m2=0
# for i in my_dict:
#    if my_dict[i]<m1:
#       m2=my_dict[i]
# print(m2)

# my_dict = {'x':500, 'y':5874, 'z': 560}
# key_min=min(my_dict.keys(),key=(lambda k: my_dict[k]))
# print("minimum value",my_dict[key_min])



# i=0
# m=0
# while i<6:
#     m=i**2
#     print(m)
#     i+=1
# print(i)  


"q16"

# class dictObj(object):
#      def __init__(s):
#          s.x = 'red'
#          s.y = 'Yellow'
#          s.z = 'Green'
#      def do_nothing(s):
#          pass
# test = dictObj()
# print(test.__dict__)


"q16"
# Student = {}
# for i in range(3):
#     k=input("enter the key:-")
#     v=input("enter the value:-")
#     Student.update({k:v})
# print(Student)  

"q17"
# student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#    'id2': 
#   {'name': ['David'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id3': 
#     {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id4': 
#    {'name': ['Surya'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
# }
# d=[]
# for i in student_data:
#     if i not in d:
#         d.append(i)
#         if student_data[i] not in d:
#             d.append(student_data[i])
# print(d) 


"q19"
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d={}
# for i in d1,d2:
#     d.update(i)
# for i in d:
#     if i in d2:
#         if i in d1:
#             d.update({i:d2[i]+d1[i]})
# print(d)                

"q23"
# Sample_data=[ 
# {'item': 'item1', 'amount': 400}, 
# {'item': 'item2', 'amount': 300}, 
# {'item': 'item1', 'amount': 750}]
# d={}
# for i in Sample_data:
#     if i['item'] not in d:
#         d.update({i['item']: i['amount']})
#     else:
#         d[i["item"]] += i["amount"] 
# print(d)           

"q26"
# student = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# print(sum(d['id'] for d in student))
# print(sum(d['success'] for d in student))
# s=0
# s1=0
# for i in student:
#     s+=i['id']
#     s1+=i['success']
# print(s)
# print(s1)    

"q27"
# num_list = [1, 2, 3, 4]
# d = dic = {}
# for i in num_list:
#     dic[i] = {}
#     dic = dic[i]
# print(d)

"q28"
# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# for i in num:
#     for j in range(len(num)-1):
#         if num[i][j]>num[j+1]:
#             s=num[i][j]
#             num[i][j]=num[j+1]
#             num[j+1]=s
# print(num) 



"q29"
# student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# d={}
# for i,j in student_list.items():
#     i = i.split()
#     d["".join(i)]=j
# print(d)    



"q30"

# it = {'item1': 45.50, 'item2':35, 
# 'item3': 41.30, 'item4':55, 'item5': 24}
# m=0
# d=[]
# for i in it.items():
#     if it[i]>m:
#         m=it[i]
# print(m)        
# m1=0
# for i in it.items():
#     if it[i]>m1:
#         if it[i]!=m:
#             m1=it[i]
# print(m1)
# m2=0
# for i in it.items():
#     if it[i]>m2:
#         if it[i]!=m and it[i]!=m1:
#             m2=it[i]
# print(m2)
# d=[m1,m2,m] 
# print(d) 
        
"q31"
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key    value   count")
# c=0
# for i in dict_num:
#     c+=1
#     print(i,"\t",dict_num[i],"\t",c)    

"q32"
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for a in students:
#     print(a)
#     for b in students[a]:
#         print (b,':',students[a][b])
		
"q33"
# student = {
#   'name': 'Alex',
#   'class': 'V',
#   'roll_id': '2'
# }
# for i in student:
#     if 'name'and'class' in student:
#         print(True)
#     if 'name'and 'Alex' in student:
#         print(False)
#     if 'roll_id' and 'name' in student:
#         print(True)        

"q35"
# x ={'Math':81, 'Physics':83, 'Chemistry':87}
# res =dict(reversed(list(x.items())))
# print(str(res))


"q36"
# class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# id_list = [1, 2, 2, 3]
# d={}
# for i in range(len(class_list)):
#     if class_list[i] not in d:
#         d.update({class_list[i]:id_list[i]})
# print(d)        

"q38"
# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}
# for i,j in y.items():
#     if x[i]==y[i]:
#         print(i,'.',j,"is present ")
"q41"

# dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
# dict1.pop("c3")
# print(dict1)

"q42"
# marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# for i in marks:
#     if marks[i]>=170:
#         print(i,marks[i])

"q43"

# student_id = ["S001", "S002", "S003", "S004"] 
# student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
# student_grade = [85, 98, 89, 92]
# d1=[]
# d2=[]
# for i in range(len(student_name)):
#     d={}
#     if student_name[i] not in d:
#         d.update({student_name[i]:student_grade[i]})
#         d1.append(d)
# for j in range(len(student_id)):
#     dic={}
#     dic=({student_id[j]:d1[j]})
#     d2.append(dic)
# print(d2)



"q44" 
# students = {'Cierra Vega': (6.2, 70), 
# 'Alden Cantrell': (5.9, 65), 
# 'Kierra Gentry': (6.0, 68), 
# 'Pierre Cox': (5.8, 66)}
# for i in students:
#     if students[i][0]>=6.0 and students[i][1]>=70:
#         print(i,students[i])


"q45"
# n=int(input("enter the number:-"))
# students = {'Cierra Vega': 12, 
#  'Alden Cantrell': 12,
#  'Kierra Gentry': 12,
#  'Pierre Cox': 12}
# for i in students.values():
#     if i==n:
#         print(True,n)
#     else:
#         print(False,n)
#     break        

"q46"
# colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d={}
# for i in colors:
#     if i[0] not in d:
#         d.update({i[0]:[i[1]]})
#     else:
#         d[i[0]].append(i[1])
# print(d)        


"q47"
# marks = {'Science': [88, 89, 62, 95], 
# 'Language': [77, 78, 84, 80]}
# d={}
# for i in marks:
#     for j in marks[i]:
#        d.update({i:marks[i][0]})
# print(d)

# d=[]
# a=marks["Science"]
# b=marks["Language"]
# for i in range(len(a)):
#     for j,k in marks.items():
#         b=({j:k[i]})
#         d.append(b)
# print(d)        

# a,b=marks.values()
# for i in range(len(a)):
#     for j,k in marks.items():
#         b=({j:k[i]})
#         d.append(b)
# print(d)



# a=[50,20,40,59,10,7,]
# b=max(a)
# m=0
# for i in range(len(a)):
#     if a[i]>m and a[i]<b:
#             m=a[i]
# print(m)            

# list=[10,20,60,40,67,76]
# d=max(list)
# m=0
# for i in range(len(list)):
#     if list[i]>m and list[i]<d:
#         m=list[i]
# print(m)      

"q48"
# dic=[{'id': '#FF0000', 'color': 'Red'}, 
# {'id': '#800000', 'color': 'Maroon'},
#  {'id': '#FFFF00', 'color': 'Yellow'}, 
# {'id': '#808000', 'color': 'Olive'}]
# for i in range(1,len(dic)):
#     print(dic[i])


"q50"
# d={'C1': [10, 20, 30], 
# 'C2': [20, 30, 40], 
# 'C3': [12, 34]}
# for i in d:
#     d[i]=[]
# print(d)

"51"
# d1={'Math': [88, 89, 90],
#  'Physics': [92, 94, 89], 
# 'Chemistry': [90, 87, 93]}
# d=[]
# dic=[]
# dict={}
# print(d1['Math'])
# for i in d1['Math']:
#     d.append(i+1)
# print(d)
# for i in d1['Physics']:
#     dic.append(i-2)
# print(dic)
# dict.update({'Math':d})
# dict.update({'Physics':dic})
# dict.update({'Chemistry':d1['Chemistry']})
# print(dict)

"52"
# d1=[{'Math': 90, 'Science': 92}, 
# {'Math': 89, 'Science': 94},
# {'Math': 92, 'Science': 88}]
# d=[]
# for i in d1:
#     d.append(i['Science'])
# print(d)


# d2=[{'Math': 90, 'Science': 92}, 
# {'Math': 89, 'Science': 94}, 
# {'Math': 92, 'Science': 88}]
# l=[]
# for i in d2:
#     l.append(i['Math'])
# print(l)    

# n=234
# s=0
# m=1
# while(n>0):
#     m*=(n%10)
#     s+=(n%10)
#     n=n//10
# print(m-s)  



"53"
# color_dict = {1 : 'red', 2 : 'green', 
# 3 : 'black', 
# 4 : 'white', 
# 5 : 'black'}
# d={}
# for i in color_dict.values():
#     d[i]=len(i)
# print(d)    

"q55"
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# for i in num:
#     print(i)

"q56"
# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# d=[]
# for i,j in a.items():
#         d1=[i,j]
#         d.append(d1)
# print(d)

# b={'1': 'Austin Little', 
# '2': 'Natasha Howard',
#  '3': 'Alfred Mullins', 
# '4': 'Jamie Rowe'}
# d=[]
# for i,j in b.items():
#     l=[i,j]
#     d.append(l)
# print(d)

"q57"
# students = {'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]} 
# d={}
# for i,j in students.items():
#     d1=[]
#     for k in j:
#         if k%2==0:
#             d1.append(k)
#         d.update({i:d1})
# print(d)

# dic={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# d={}
# for i,j in dic.items():
#     lis=[]
#     for n in j:
#         if n%2==0:
#             lis.append(n)
#         d.update({i:lis})
# print(d)            
      
"q59"
# from helas

# n=int(input("enter the number:-"))
# a={'a': 5, 'b': 14, 'c': 32, 
# 'd': 35,'e': 24,
# 'f': 100, 'g': 57, 
# 'h': 8, 'i': 100}
# r=nlargest(n,a,key=a.get)
# print(r)

"60"
# dic= {'V': [10, 12], 'VI': [10], 
# 'VII': [10, 20, 30, 40], 'VIII': [20], 
# 'IX': [10, 30, 50, 70], 'X': [80]}
# m=min([len(dic[i]) for i in dic])
# d=[]
# for i in dic:
#     if len(dic[i])==m:
#         d.append(i)
# print(d) 
                  
"61"
# stu={'V': 10, 'VI': 10, 'VII': 40, 
# 'VIII': 20, 'IX': 70, 
# 'X': 80, 'XI': 40, 'XII': 20}
# d=[]
# for i in  stu.values():
#     c=[]
#     count=0
#     for j in stu.values():
#         if i==j:
#             count+=1
#     c.append(i)
#     c.append(count)
#     if count not in d:
#         d.append(c)
# print(dict(d))    

"62"
# d=[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
# {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
# {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
# {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
# {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# l=[]
# for i in d:
#     for j in i:
#         l.append(i[j])
# print(l)

"63"  "64"
# students = [[1,'Jean Castro','V'],
# [2, 'Lula Powell', 'V'], 
# [3, 'Brian Howell', 'VI'],
# [4, 'Lynne Foster', 'VI'],
# [5, 'Zachary Simon', 'VII']]
# d={}
# d1={}
# for i in students:
#     for j in i:
#         d.update({i[0]:i[1:]})
#         d1.update({i[0]:[i[1]]})
# print(d)
# print(d1)

"65"
# color = {'#FF0000':'Red', '#800000':'Maroon', 
# '#FFFF00':'Yellow', '#808000':'Olive'}
# s=0
# for i in color.values():
#     d=len(i)
#     s+=d
# print(s)

              
"70"
# d={}
# for i in range(1,5):
#     d[i]=i**2
# print(d,end="")              

"table in list"
# n=int(input("enter the number:-"))
# d=[]
# for i in range(1,n+1):
#     d1=[]
#     for j in range(1,11):
#         m=i*j
#         d1.append(m)
#     d.append(d1)
# print(d)

"68"
# d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# d2 = {'x': 300, 'y': 'Red', 'z': 600}
# for i in d2:
#     if i in d1:
#         d2[i]=[d1[i],d2[i]]
#     else:
#         d2[i]=[d1[i],d2[i]]
# print(d2)


# for i in d1:
#     if i in d2:
#         d1[i]=[d1[i],d2[i]]
#     else:
#         d1[i]=[d1[i]]
# print(d1)

"69"
# def floor(n):
#     d={}
#     for i in n:
#         d.update({int(i):[i]})
#     return d
# n1=[7,23,3.2,3.3,8.4]
# print(floor(n1)) 

# def lens(n):
#     d={}
#     d1=[]
#     for i in n:
#         if len(i)==len(i):
#            d.update({len(i):[i]})
#         else:
#             d.update({len(i):[i]})   
#     return d 
# n1=['Red', 'Green', 'Black', 'White', 'Pink'] 
# print(lens(n1))       

"72"
# students = {
#   'Theodore': 10,
#   'Mathew': 11,
#   'Roxanne': 9,
# }
# d={}
# for i in students:
#     d.update({students[i]:i})
# print(d)

"73"
# dic=[{'name': 'Theodore', 'age': 18},
# {'name': 'Mathew', 'age': 22}, 
# {'name': 'Roxanne', 'age': 20}, 
# {'name': 'David', 'age': 18}]
# d=[]
# for i in dic:
#     d.append(i['age'])
# print(d)

"74"
# d={'Theodore':{'user': 'Theodore', 'age': 45}, 
# 'Roxanne':{'user': 'Roxanne', 'age': 15}, 
# 'Mathew':{'user': 'Mathew', 'age': 21}}
# di={}
# for i in d:
#     for j in d[i]:
#         di.update({i:d[i][j]})
# print(di)

"75"
# n=int(input("enter the number:-"))
# students = {
#   'Theodore': 19,
#   'Roxanne': 20,
#   'Mathew': 21,
#   'Betty': 20,'shivi':21
# }
# d=[]
# for i in students:
#     if students[i]==n:
#         d.append(i)
# print(d)    

"76"
# def add(a,b):
#     return dict(zip(a,b))
# a=['a', 'b', 'c', 'd', 'e', 'f']
# b=[1, 2, 3, 4, 5]
# print(add(a,b))

"77"
# color={'Red':1,'Green':3,'White':5, 
# 'Black': 2,'Pink': 4}
# d=[]
# for i in color.items():
#     d.append(i)
# print(d)

"80"
# last={'Theodore': 19,'Roxanne':22,
# 'Mathew': 21, 'Betty': 20}
# m=0
# for i in last:
#     if last[i]>m:
#         c=i
#         m=last[i]
# print(c)        
 




