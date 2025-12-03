# A function that returns the sum of two digits
#
#
# START
#
# def sum(num1, num2):
#   SET output = num1 + num2
#   PRINT output


# A function that takes a list of strings, and returns a string that is all those strings concatenated together
#
#
# START
# 
# def concantenate(list):   
#   SET my_str = ''
#   SET index = 1    
#   WHILE index <= len(list):   
#       SET my_str = my_str + list[index]
#       SET index += 1
#   PRINT(my_str)


# A function that takes a list of integers, and returns a new list with every other element 
# from the original list, starting with the first element.
#
#
# START
# 
# def every_other(list):
#   SET new_list = []
#   for i in range(0, len(list), 2):
#       new_list.append(list[i])
#   PRINT(new_list)


# A function that determines the index of the 3rd occurrence of a given character in a string.
# For instance, if the given character is 'x' and the string is 'axbxcdxex',
# The function should return 6 (the index of the 3rd 'x').
# If the given character does not occur at least 3 times, return None.
# 
#
# START
#
# def third_occurence(string, x)
#   SET counter = 0
#   WHILE counter < 3:
#       for i in string:    
#           IF string[i] == x:
#               SET counter += 1
#       PRINT(f'The index of the 3rd {x} is {i}')


# A function that takes two lists of numbers and returns the result of merging the lists. 
# The elements of the first list should become the elements at the even indexes of the returned list,
# While the elements of the second list should become the elements at the odd indexes. For instance:
#
#
# START
#
# SET list_1 = [1, 2, 3]
# SET list_2 = [4, 5, 6]
#
# def combine(lst1, lst2)
#   SET zipped_list = zip(lst1, lst2)
#   for lst1, lst2 in zipped_list:
#       PRINT(f'{lst1} {lst2}')

# OUTPUT = WRONG:
# 1 4
# 2 5
# 3 6
#
#
# TRY AGAIN
#
# 
# START
#
# SET list_1 = [1, 2, 3]
# SET list_2 = [4, 5, 6]
#
# def combine(lst1, lst2):
#   SET new_list = []
#   SET index = 1
#   for i in range(0, len(lst1)):
#       newlist.append(lst1[i])
#       while index < len(lst2):
#           newlist.append(lst2[index])
#           SET index += 1 
#           BREAK
#   PRINT(new_list)

