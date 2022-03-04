# new={'sonu':85,'Kartik':90,'Deepak':96,'Aman':76,'Somesh':60,'Umesh':85,'Amarpal':70,'Roshan':57,'Riyaz':98,'Shabid':56}
# for i in new:
#     print(i,new[i])


d=[]
for i in range(11):
    num=input("enter the name:-")
    marks=int(input("enter the number:-"))
    f=num,marks
    d.append(f)
print(dict(d))    

