# When obtaining slices, you can specify a step

# Creating the list
my_list = [5, 7, 9, 1, 1, 2]

sub_list = my_list[0:-1:2]

print(sub_list)

# Output of the list items from the second (third) to the penultimate with a step of two
print(my_list[2:-2:2])
# Displays all the list items except the first one in reverse order
print(my_list[-1:0:-1])
