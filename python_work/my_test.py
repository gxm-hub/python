from test import Dog

class Elecar(Dog):
    def __init__(self,name,age):
#初始化属性name and age
        self.name = name
        self.age = age
        self.size = 70

    def sit(self):
        print(self.name.title()+"is sitting")



    def roll_over(self):
         print(self.name.title()+"rolled over")

# my_telsa = test.Elecar('wichar',8)
# print(my_telsa.sit())
# print(my_telsa.size)