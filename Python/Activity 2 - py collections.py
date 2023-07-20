# example list
list = [20,30,25,35,-16,60,-100]

sum_of_list = 0
number_of_elements = len(list)

for x in list:
    sum_of_list += x

average = sum_of_list / number_of_elements

print("Average value of the list element is: ", average)