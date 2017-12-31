from math import ceil

def input_all_mods():
    all_mods = []
    inp = input("input mod '<name> <MC count> <grade point>' or 'stop' to end: ")
    while inp.lower() != 'stop':
        name, mc, grade = inp.split(' ')[0], int(inp.split(' ')[1]), float(inp.split(' ')[2])
        all_mods.append({'name': name, 'mc': mc, 'gradepoint': grade})
        inp = input("input mod '<name> <MC count> <grade point>' or 'stop' to end: ") 
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

all_mods = input_all_mods()
print("your cap is", calc_cap(all_mods))
if input("do you want to s/u? y/n: ") == 'y':
    all_mods = su(all_mods)
    print("your new cap is", calc_cap(all_mods))
