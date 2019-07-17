# def build_profile(first,last,**user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key,value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('albert','einstein',
#                             location = 'princeton',
#                             filed='physics')
# print(user_profile)                           

class Dog():
 
    def __init__(self,name,age):
    #初始化属性name and age
       self.name = name
       self.age = age


    def sit(self):
        print(self.name.title()+"is now sitting. ")


    def roll_over(self):
        print(self.name.title()+"rolled over")

# my_telsa = test.Elecar('wichar',8)
# print(my_telsa.sit())
# print(my_telsa.size)

