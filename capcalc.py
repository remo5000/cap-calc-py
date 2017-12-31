from math import ceil

INPUT_PROMPT = "input mod '<name> <MC count> <grade point>' or 'stop' to end: "
INDICES_PROMPT = "input indices to s/u or 'stop' to end: " 
SU_PROMPT = "do you want to s/u? y/n: "

def input_all_mods():
    all_mods = []
<<<<<<< HEAD
    inp = input("input mod '<name> <MC count> <grade point>' or 'stop' to end: ")
    while inp.lower() != 'stop':
        name, mc, grade = inp.split(' ')[0], int(inp.split(' ')[1]), float(inp.split(' ')[2])
        all_mods.append({'name': name, 'mc': mc, 'gradepoint': grade})
        inp = input("input mod '<name> <MC count> <grade point>' or 'stop' to end: ") 
=======
    inp = input(INPUT_PROMPT)
    while inp.lower() != 'stop':
        name, mc, grade = inp.split(' ')
        all_mods.append({'name': name, 'mc': int(mc), 'gradepoint': float(grade)})
        inp = input(INPUT_PROMPT)
>>>>>>> 42b2096786153535428ed8581e6d4ea8ab80e8b1
    return all_mods

def calc_cap(all_mods):
    number_of_mcs = 0
    total = 0
    for mod in all_mods:
        total += mod['gradepoint'] * mod['mc']
        number_of_mcs += mod['mc']
    cap = total / number_of_mcs
    cap = ceil(float(cap)*100)/100
    return cap

def su(all_mods):
    for index, mod in enumerate(all_mods):
<<<<<<< HEAD
        i = str(index)
        name = mod['name']
        mc = str(mod['mc'])
        gp = str(mod['gradepoint'])
        print("Index: " + i + "\t" + name + "\t" + mc + " MCs" + "\t" + "Grade: " + gp)
    inp = input("input indices to s/u or 'stop' to end: ")
    while inp != 'stop':
        index = int(inp)
        del all_mods[index]    
        inp = input("input indices to s/u or 'stop' to end: ")
    return all_mods
=======
        print("Index: {}\t{}\t{}MCs\tGrade: {}".format(
            index, mod['name'], mod['mc'], mod['gradepoint']
        ))
    inp = input(INDICES_PROMPT)
    while inp.lower() != 'stop':
        all_mods[int(index)] = None
        inp = input(INDICES_PROMPT)
    return list(filter(lambda x: x is not None, all_mods))
>>>>>>> 42b2096786153535428ed8581e6d4ea8ab80e8b1

all_mods = input_all_mods()
print("your cap is", calc_cap(all_mods))
if input(SU_PROMPT) == 'y':
    all_mods = su(all_mods)
    print("your new cap is", calc_cap(all_mods))
