# sample of the list
sample_list = [10,2,3,4,7]

#function to show the content of the list
def my_list(list):
    print("the cotent of the list is:",list)

#funtion to find the max number of the list
def my_list_value(max_value):
    max = sample_list[0]
    for number in max_value:
        if number > max:
            max_value = number
    print("the max value in the list:",max)



# calling the functions
my_list(sample_list)
my_list_value(sample_list)