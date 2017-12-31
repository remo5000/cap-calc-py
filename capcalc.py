from math import ceil

INPUT_PROMPT = "input mod '<name> <MC count> <grade point>' or 'stop' to end: "
INDICES_PROMPT = "input indices to s/u or 'stop' to end: " 
SU_PROMPT = "do you want to s/u? y/n: "

def input_all_mods():
    all_mods = []
    inp = input(INPUT_PROMPT)
    while inp.lower() != 'stop':
        name, mc, grade = inp.split(' ')
        all_mods.append({'name': name, 'mc': int(mc), 'gradepoint': float(grade)})
        inp = input(INPUT_PROMPT)
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
        print("Index: {}\t{}\t{}MCs\tGrade: {}".format(
            index, mod['name'], mod['mc'], mod['gradepoint']
        ))
    inp = input(INDICES_PROMPT)
    while inp.lower() != 'stop':
        all_mods[int(index)] = None
        inp = input(INDICES_PROMPT)
    return list(filter(lambda x: x is not None, all_mods))

all_mods = input_all_mods()
print("your cap is", calc_cap(all_mods))
if input(SU_PROMPT) == 'y':
    all_mods = su(all_mods)
    print("your new cap is", calc_cap(all_mods))
