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
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# i=0
# b=0
# d=[]
# while i<len(keys):
#     s=keys[i],values[b]
#     d.append(s)
#     i+=1
#     b+=1
# print(dict(d)) 


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
# print("y",m)       
# m1=my_dict[i]
# if my_dict[i]<m1:
#     m1=my_dict[i]
# print ("z",m1) 
# m2=0
# for i in my_dict:
#    if my_dict[i]<m1:
#       m2=my_dict[i]
# print("x",m)

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
