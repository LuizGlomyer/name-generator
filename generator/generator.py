from random import randint, choice
import hashlib


def ddd():
    file = open("generator/data/DDDs.txt", "r")
    ddd_list = file.read().split(" ")
    ddd = "(" + str(choice(ddd_list)).rstrip('\n') + ")"
    file.close()
    return ddd


def br_phone_number(**kwargs):
    part1 = randint(2, 5)
    part2 = randint(0, 999)
    part3 = randint(0, 9999)
    number = f"{part1}{part2:03d}-{part3:04d}"

    if kwargs.get('cellphone'):
        number = f"9{number}"
    if kwargs.get('ddd'):
        number = f"{ddd()} {number}"

    return number


def fantasy_name():
    def choose_syllable():
        import random
        
        file = open("generator/data/syllables.txt", "r")
        syllables = file.read()
        syllables = syllables.split()

        file = open("generator/data/loose_syllables.txt", "r")
        loose_syllables = file.read()
        loose_syllables = loose_syllables.split()

        file = open("generator/data/uncommon_syllables.txt", "r")
        uncommon_syllables = file.read()
        uncommon_syllables = uncommon_syllables.split()

        file.close()

        value = random.random() * 100
        if value >= 80:
            return choice(uncommon_syllables)

        value = random.random() * 100
        if value >= 70:
            return choice(loose_syllables)

        return choice(syllables)

    name = ""
    size = randint(2, 5)  # total number of syllables
    for syllable in range(size):
        sil = choose_syllable()
        # first syllable can't start with those
        while syllable == 0 and sil in "lrsxmntydkz":
            sil = choose_syllable()
        name = name + sil
        name = name.capitalize()

    
    return name


def br_surname():
    file = open("generator/data/br_surnames.txt", 'r')
    surname_list = file.readlines()
    file.close()
    number_of_names = ''
    surname = ""
    if randint(1, 10) > 8:  # 20% chance of having 1 or 4 surnames
        number_of_names = choice([1, 4])
    else:
        number_of_names = randint(2, 3)  # 2 to 3 surnames

    for i in range(number_of_names):
        surname += choice(surname_list).rstrip('\n')
        # adds a whitespace on all but the last iteration
        surname += " " if i != number_of_names-1 else ""
    return surname


def br_male_name():
    file = open("generator/data/brazilian_male_names.txt", 'r')
    name_list = file.readlines()
    file.close()
    name = choice(name_list).rstrip('\n')

    return name


def br_complete_male_name():
    return br_male_name() + " " + br_surname()


def br_female_name():
    file = open("generator/data/brazilian_female_names.txt", 'r')
    name_list = file.readlines()
    file.close()
    name = choice(name_list).rstrip('\n')

    return name


def br_complete_female_name():
    return br_female_name() + " " + br_surname()


def en_surname():
    file = open("generator/data/en_surnames.txt", 'r')
    surname_list = file.readlines()
    file.close()
    number_of_names = ''
    surname = ""
    if randint(1, 10) > 8:  # 20% chance of having 1 or 4 surnames
        number_of_names = choice([1, 4])
    else:
        number_of_names = randint(2, 3)  # 2 to 3 surnames

    for i in range(number_of_names):
        surname += choice(surname_list).rstrip('\n')
        # adds a whitespace on all but the last iteration
        surname += " " if i != number_of_names-1 else ""
    return surname


def en_male_name():
    f = open("generator/data/en_male_names.txt", 'r')
    name_list = f.readlines()
    f.close()
    name = choice(name_list).rstrip('\n')

    return name


def en_complete_male_name():
    return en_male_name() + " " + en_surname()


def en_female_name():
    file = open("generator/data/en_female_names.txt", 'r')
    name_list = file.readlines()
    file.close()
    name = choice(name_list).rstrip('\n')

    return name


def en_complete_female_name():
    return en_female_name() + " " + en_surname()


def br_cpf():  # not necessarily a valid CPF
    part1 = randint(0, 999)
    part2 = randint(0, 999)
    part3 = randint(0, 999)
    part4 = randint(0, 99)

    return f"{part1:03d}.{part2:03d}.{part3:03d}-{part4:02d}"


def date(**kwargs):  # not necessarily a valid date
    day = randint(1, 31)
    month = randint(1, 12)
    year = randint(1900, 2020)

    if month == 2:
        day = randint(1, 29)

    if kwargs.get('twoDigits'):
        year = str(year)[2:]

    return f"{day:02d}/{month:02d}/{year}"


def time():
    segundos = randint(0, 59)
    minutos = randint(0, 59)
    horas = randint(0, 23)

    return f"{horas:02d}:{segundos:02d}:{minutos:02d}"


def hash(**kwargs):
    for a in hashlib.algorithms_available:
        print(a)
    if not kwargs.get('value'):
        return "Invalid value"

    if kwargs.get('algorithm') == 'md5':
        value = kwargs.get('value')
        return hashlib.md5((value).encode('utf-8')).hexdigest()

    if kwargs.get('algorithm') == 'sha256':
        value = kwargs.get('value')
        return hashlib.sha256((value).encode('utf-8')).hexdigest()

    if kwargs.get('algorithm') == 'sha512':
        value = kwargs.get('value')
        return hashlib.sha512((value).encode('utf-8')).hexdigest()

    return "Invalid algorithm"
