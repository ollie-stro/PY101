#def art(string):
#    for _ in range(0, 11):
#        string = '-' + string
#        print(string)
#    
#    for padding in range(1, 11):
#        print(f'{"-" * padding}The Flintstones Rock!')
#       
#art('The Flintstones Rock!')

#def factors(number):
#    divisor = number
#    result = []
#    
#    while divisor != 0 and divisor > 0:
#        if number % divisor == 0:
#            result.append(number // divisor)
#        divisor -= 1
#    return result
#print(factors(-15))


#buffer = ['-------------------']
#
#def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
#    buffer.append(new_element)
#    if len(buffer) > max_buffer_size:
#        buffer.pop(0)
#    return buffer
#
#def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
#    buffer = buffer + [new_element]
#    if len(buffer) > max_buffer_size:
#        buffer.pop(0)
#    return buffer
#
#print(add_to_rolling_buffer1(buffer, 5 , 'gaga'))
#print(add_to_rolling_buffer2(buffer, 5 , 'gaga'))

#print(0.3 + 0.6)
#print(0.3 + 0.6 == 0.9)

#nan_value = float("nan")
#
#print(nan_value == float("nan"))

#answer = 42
#
#def mess_with_it(some_number):
#    return some_number + 8
#
#new_answer = mess_with_it(answer)
#
#print(answer - 8)

#munsters = {
#    "Herman": {"age": 32, "gender": "male"},
#    "Lily": {"age": 30, "gender": "female"},
#    "Grandpa": {"age": 402, "gender": "male"},
#    "Eddie": {"age": 10, "gender": "male"},
#    "Marilyn": {"age": 23, "gender": "female"},
#}
#
#def mess_with_demographics(demo_dict):
#    for key, value in demo_dict.items():
#        value["age"] += 42
#        value["gender"] = "other"
#       
#mess_with_demographics(munsters)
#print(munsters)

#def rps(fist1, fist2):
#    if fist1 == "rock":
#        return "paper" if fist2 == "paper" else "rock"
#    elif fist1 == "paper":
#        return "scissors" if fist2 == "scissors" else "paper"
#    else:
#        return "rock" if fist2 == "rock" else "scissors"
#    
#print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

#def foo(param="no"):
#    return "yes"
#
#def bar(param="no"):
#    return (param == "no") and (foo() or "no")
#
#print(bar(foo()))

#a = 25999
#b = 25999
#c = a
#
#print(id(a) == id(b) == id(c))
