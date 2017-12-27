from math import ceil
input_ended = False
number_of_grades = 0
total = 0
while not input_ended:
    inp = input("Enter a grade point, or 'stop' to end: ")
    if inp == 'stop':
        input_ended = True
    else:
        total += float(inp) 
        number_of_grades += 1
cap = total / number_of_grades if number_of_grades > 0 else 0
cap = ceil(float(cap)*10)/10   
print("your cap is", cap)
