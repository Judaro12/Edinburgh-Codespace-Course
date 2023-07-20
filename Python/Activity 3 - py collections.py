# Define the sample list
sample_list = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

# Maximun and min Values
max = sample_list[0]
min = sample_list[0]

#go through each element
for number in sample_list:
    #checking if the current number is greater than the current max
    if number > max:
        max = number

    #checking if the current value is less than the current min
    if number < min:
        min = number
# printing the result 
print("original list: ",sample_list)
print("Maximun value for the list above =",max)
print("Minimun value for the list above =",min)