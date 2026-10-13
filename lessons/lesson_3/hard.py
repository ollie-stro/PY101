#def first():
#    return {
#        'prop1': "hi there",
#    }
#
#def second():
#    return
#    {
#        'prop1': "hi there",
#    }
#
#print(first())
#print(second())

#dictionary = {'first': [1]}
#num_list = dictionary['first']
#num_list.append(2)
#
#print(num_list)
#print(dictionary)

#def mess_with_vars(one, two, three):
#    one[0] = "two"
#    two[0] = "three"
#    three[0] = "one"
#
#one = ["one"]
#two = ["two"]
#three = ["three"]
#
#mess_with_vars(one, two, three)
#
#print(f"one is: {one}")
#print(f"two is: {two}")
#print(f"three is: {three}")

#def is_an_ip_number(string):
#    string = str(string)
#    if string.isdigit():
#        number = int(string)
#        return 0 <= number <= 255
#    return False
#
#def is_dot_separated_ip_address(input_string):
#    dot_separated_words = input_string.split(".")
#    if len(dot_separated_words) != 4:
#       return False
#
#    while len(dot_separated_words) > 0:
#        word = dot_separated_words.pop()
#        if not is_an_ip_number(word):
#            return False
#
#    return True
#
#print(is_dot_separated_ip_address('2.1.1a.1'))


