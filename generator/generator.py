from random import randint, choice
import hashlib


def ddd():
    f = open("generator/DDDs.txt", "r")
    ddd_list = f.read().split(" ")
    ddd = "(" + str(choice(ddd_list)).rstrip('\n') + ")"
    f.close()
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
    file = open("generator/syllables.txt", "r")
    syllables = file.read()
    syllables = syllables.split()

    name = ""
    size = randint(2, 5)  # total number of syllables
    for syllable in range(size):
        sil = choice(syllables)
        # first syllable can't start with those
        while syllable == 0 and sil in "lrsxmn" or syllable == 0 and sil in ["rra", "rre", "rri", "rro", "rru", "ssa", "sse", "ssi", "sso", "ssu"]:
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
    f = open("generator/brazilian_male_names.txt", 'r')
    name_list = f.readlines()
    f.close()
    name = choice(name_list).rstrip('\n')

    return name


def br_complete_male_name():
    return br_male_name() + " " + br_surname()


def br_female_name():
    f = open("generator/brazilian_female_names.txt", 'r')
    name_list = f.readlines()
    f.close()
    name = choice(name_list).rstrip('\n')

    return name


def br_complete_female_name():
    return br_female_name() + " " + br_surname()


def br_cpf():  # not necessarily a valid CPF
    part1 = randint(0, 999)
    part2 = randint(0, 999)
    part3 = randint(0, 999)
    part4 = randint(0, 99)

    return f"{part1:03d}.{part2:03d}.{part3:03d}-{part4:02d}"


def date(**kwargs):  # not necessarily a valid date. True for years in the 2 characters format
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
