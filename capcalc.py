from math import ceil

def input_all_mods():
    all_mods = []
    while True:
        inp = input("input mod '<name> <MC count> <grade point>' or 'stop' to end: ")
        if inp == 'stop':
            break
        else:
            name, mc, grade = inp.split(' ')[0], int(inp.split(' ')[1]), float(inp.split(' ')[2])
            all_mods.append({'name': name, 'mc': mc, 'gradepoint': grade})
    return all_mods

def calc_cap(all_mods):
    number_of_grades = len(all_mods)
    total = 0
    for mod in all_mods:
        total += mod['gradepoint']
    cap = total / number_of_grades if number_of_grades > 0 else 0
    cap = ceil(float(cap)*100)/100
    return cap

def su(all_mods):
    for index, mod in enumerate(all_mods):
        print("Index:", index, "    ", mod['name'], mod['mc'], mod['gradepoint'])
    while True:
        inp = input("input indices to s/u or 'stop' to end: ")
        if inp == 'stop':
            break
        else:
            index = int(inp)
            del all_mods[index]
    return all_mods

all_mods = input_all_mods()
print("your cap is", calc_cap(all_mods))
if input("do you want to s/u? y/n: ") == 'y':
    all_mods = su(all_mods)
    print("your new cap is", calc_cap(all_mods))
