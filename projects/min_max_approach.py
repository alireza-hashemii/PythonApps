first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
numbers_list = []
numbers_list.append(first_number)
numbers_list.append(third_number)
numbers_list.append(second_number)
if first_number > second_number:
    max = first_number
else :
    max = second_number
if max < third_number:
    max = third_number
else:
    max = max * 1
x1= max
numbers_list.remove(max)
if numbers_list[0] > numbers_list[1]:
    x2 = numbers_list[0]
    x3 = numbers_list[1]
else:
    x2 = numbers_list[1]
    x3 = numbers_list[0]
print(x1,">",x2,">",x3)
print("\U0001F605")





    


