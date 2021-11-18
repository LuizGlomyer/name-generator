from random import randint, choice


# returns a number in the format XXXX-XXXX. If the first parameter is True, then it returns a number in the DDD format - (XX) XXXX-XXXX
def br_number(has_ddd = False):
    part1 = str(randint(2, 5))
    if has_ddd:
        f = open("generator/DDDs.txt", "r")
        ddd_list = f.read().split(" ")
        part1 = "(" + str(choice(ddd_list)).rstrip('\n') + ") " + part1
        f.close()

    part2 = randint(0, 999)
    part3 = randint(0, 9999)

    return part1 + "{:03d}-{:04d}".format(part2, part3)


def br_cellphone_number(has_ddd = False):
    part1 = "9"
    if has_ddd:
        f = open("generator/DDDs.txt", "r")
        ddd_list = f.read().split(" ")
        part1 = "(" + str(choice(ddd_list)).rstrip('\n') + ") " + part1
        f.close()

    part2 = randint(0, 9999)
    part3 = randint(0, 9999)

    return part1 + "{:04d}-{:04d}".format(part2, part3)


def fantasy_name():
    file = open("generator/syllables.txt", "r")
    syllables = file.read()
    syllables = syllables.split()

    name = ""
    size = randint(2,5) # total number of syllables
    for syllable in range(size):
        sil = choice(syllables)
        while syllable == 0 and sil in "lrsxmn" or syllable == 0 and sil in ["rra", "rre", "rri", "rro", "rru", "ssa","sse", "ssi", "sso", "ssu"]: # first syllable can't start with those
            sil = choice(syllables)
        name = name + sil
        name = name.capitalize()

    file.close()
    return name
    

def br_surname():
    f = open("generator/br_surnames.txt", 'r')
    surname_list = f.readlines()
    f.close()
    number_of_names = ''
    surname = ""
    if randint(1, 10) > 8: # 20% chance of having 1 or 4 surnames
        number_of_names = choice([1, 4])
    else:
        number_of_names = randint(2, 3) # 2 to 3 surnames
    
    for i in range(number_of_names):
        surname += choice(surname_list).rstrip('\n')
        surname += " " if i != number_of_names-1 else "" # adds a whitespace on all but the last iteration
    return surname


def br_male_name():
    f = open("generator/brazillian_male_names.txt", 'r')
    name_list = f.readlines()
    f.close()
    name = choice(name_list).rstrip('\n')

    return name


def br_complete_male_name():
    return br_male_name() + " " + br_surname()


def br_female_name():
    f = open("generator/brazillian_female_names.txt", 'r')
    name_list = f.readlines()
    f.close()
    name = choice(name_list).rstrip('\n')

    return name

def br_complete_female_name():
    return br_female_name() + " " + br_surname()

def br_cpf(): # not necessarily a valid CPF
    part1 = randint(0,999)
    part2 = randint(0,999)
    part3 = randint(0,999)
    part4 = randint(0,99)

    return "{:03d}.{:03d}.{:03d}-{:02d}".format(part1, part2, part3, part4)

def date(two_digits = False): # not necessarily a valid date. True for years in the 2 characters format
    year = str(randint(1900, 2020))
    month = randint(1, 12)
    if month == 2:
        day = str(randint(1, 29))
        day = "0" + day if len(day) < 2 else day
        return "{}/{:02d}/{}".format(day, month, year if not two_digits else year[2:])
    else:
        day = str(randint(1, 31))
        day = "0" + day if len(day) < 2 else day
        return "{}/{:02d}/{}".format(day, month, year if not two_digits else year[2:])

def time():
    segundos = randint(0, 59)
    minutos = randint(0, 59)
    horas = randint(0, 23)

    return "{:02d}:{:02d}:{:02d}".format(horas, segundos, minutos)

