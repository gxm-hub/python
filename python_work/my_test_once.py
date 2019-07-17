# from test import Dog
# from my_test import Elecar


# my_bomei = Dog('dukki',3)
# print(my_bomei.sit())


# my_telsa = Elecar('rokki',2)
# print(my_telsa.roll_over())
file_path = '/home/ocean/python_work/text_files/pi_digits.txt'
fiel_name = 'pi_digits.txt'

try:

    with open(fiel_name)as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "sorry,the file"+fiel_name+"don't exit"
    print(msg)

else:
    #  计算文件包含单词数
    words = contents.split()
    num_words = len(words)
    print(str(num_words))