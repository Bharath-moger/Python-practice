# import datetime
# import math
# import random
# print("hello world 1");
# print("hello world 2");
# print("hello world 3");
# # # print("hello world",end="-");

# # #DataTypes
# String = "String";
# Integer = 123;
# Float = 209.98;

# # # print(type(Float))

# print(Float,String,Integer,sep="--");
# List = ["sudeep","srajan","manjesh","sindhu","bharath"]
# Tuple = (1,"srajan","manjesh","sindhu","bharath")
# Set = {1,2,3,4,"bharath"}
# print(Tuple[0])

# #DYNAMIC BINDING
# a=b=c=1;
# a,b,c = 1,2,3;
# print(a)
# print(b)
# print(c)

# #COMMENT 
# This is a single line comment
'''This is a 
multiline 
comment'''

# #USER INPUT
# input()
# Input = input("Enter your input ");
# #by default enterd input is string 
# print(type(Input));
# IntInput = int(input("enter your number "))
# print(type(IntInput));

# #Type Conversion
# sudeep = "200.89";
# bharath = 200;
# # print(StrType)
# print(float(sudeep)+bharath); #we made type casting here

# #operator
# a=2
# b=20
# name = "bharath"
# print(a+b)
# # print(a>0 and b<5)
# # print("B" in name)#membership operator
# # print("A" not in name) #membership operator
# # print(a | b)

# #conditional statements
# # if a > b :
# #     print(a," is largest")
# # elif b > a:
# #     print(b," is largest");
# # else:
# #     print(a," is equal to ",b)

# # nested if else
# # age = int(input("Enter your age .. "));
# # Gender = input("are you a Male or female ? ");
# # if Gender == "male":
# #     if age >= 18 and age < 100:
# #         print("You are major ",Gender)
# #     elif age >0 and  age < 18:
# #         print("You are minor ",Gender)
# # elif Gender == "female":
# #     if age >= 18 and age < 100:
# #         print("You are major ",Gender)
# #     elif age >0 and  age < 18:
# #         print("You are minor ",Gender)
# # else:
# #     print("you are not male or female")
    

# #Modules
# #Date
# # currentDate = datetime.datetime.now()
# # print(currentDate)

# #math
# # number = 300.299
# # print(math.floor(number))
# # print(math.ceil(number))

# #random
# list = ["bharat","sudeep","manjesh","srajan"];
# print(random.choice(list));

# print(help('modules'))

#LOOPS IN PYTHON
#While Loop
# for i in range(1,11):
#     print(i);

# i = 0;
# while i <= 5 :
#     print("i is ",i);
#     i=i+1


#STRING
# my-string = "Hello world"


#LIST
# trade_logs = [[100,"BTC",110.9,True],200,300]
# print(id(trade_logs[0]))
# print(trade_logs[0][0:2])

# TUPLE
# t2 = (1,"BTC",1.5,True)
# print(t2[0])
# t2[0]=100; #camnt able add value
# print(t2)

# t2 = (1,"BTC",1.5,True)
# t3 = (2,"ETH",2.5,False)
# print(t2+t3)


# OOP'S CONCEPT
# class myClass:
#     name = "bharath"
#     age = 21 

#     def education(self,edu):
#         print(f"{edu} Graduate")
        

# bharat = myClass()
# bharat.education("BCA")


# class myClass:
    #     def __init__(self,name,age):
    #         self.name = name
    #         self.age = age 

    #     def education(self,edu):
    #         print(f"{edu} Graduate")
            

    # bharat = myClass("bharath",21)
    # print(bharat.name)
    # print(bharat.age)
    # bharat.education("BCA")