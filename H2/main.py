import re

a=input('Please enter a\n')
numbers_list = re.findall(r'\d+', a)
even_numbers = numbers_list[1::2]

even_number_str = ''.join(even_numbers)
reverse_str = a[::-1].upper()

print(even_number_str)
print(reverse_str)













# See PyCharm help at https://www.jetbrains.com/help/pycharm/
