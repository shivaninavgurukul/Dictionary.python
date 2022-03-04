# intro={"name":"shivani","sarname":"mehta","age":22}
# print(intro["name"])


# intro={"name":"shivani","sarname":"mehta","age":22}
# print(intro)

# a={"b":1,"c":3,"d":5,"e":5,"f":6}
# sum=0
# m=1
# for i in a:
#     sum+=a[i]
#     m*=a[i]
# print(sum)
# print(m)    

"use to  items function"

# intro={"name":"shivani","sarname":"mehta","age":22}
# for x,y in intro.items():
#     print(x,y)

"use to  keys function"
# intro={"name":"shivani","sarname":"mehta","age":22}
# x=intro.keys()
# print(x)
# intro["vellage"]="ujjain"
# print(x)

"use to  values function"
# intro={"name":"shivani","sarname":"mehta","age":22}
# x=intro.values()
# print(x)
# intro["vellage"]="ujjain"
# print(x)

"use to update function"
# intro={"name":"shivani","sarname":"mehta","age":22}
# intro.update({"vellage":"ujjain","name":"civii"})
# print(intro)

"use to pop function"
# intro={"name":"shivani","sarname":"mehta","age":22}
# intro.pop("age")
# print(intro)

"use to popitem function"
# intro={"name":"shivani","sarname":"mehta","age":22}
# intro.popitem()
# print(intro)

"use to  del function"
# intro={"name":"shivani","sarname":"mehta","age":22}
# del intro["age"]
# print(intro)

"use to  clear function"
# intro={"name":"shivani","sarname":"mehta","age":22}
# intro.clear()
# print(intro)

"use to copy function"
# intro={"name":"shivani","sarname":"mehta","age":22}
# x=intro.copy()
# print(x)


"use to  dict function"
# intro={"name":"shivani","sarname":"mehta","age":22}
# x=dict(intro)
# print(x)

# student=dict(name= "Ravina",age= 20)
# print(student)


"nested dictionary"
# Dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To', 'C' : 'DHARAMSALA'}}
# print(Dic)



# person={'name':'jack','age':20,'gender':'male',4:'organisation'}
# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)

# person={'name':'jack','age':20,'gender':'male',4:{'organisation':'navgurukul','place':'dharamsala'}}
# print(person['gender'])
# print(person[4])
# result = person[4]['place']
# print(result)