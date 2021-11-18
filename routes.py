def route_list():
    list = {
        '/': 'Help',
        '/help': 'Help',
        '/fantasy_name': 'Fantasy name',
        '/br_surname': 'Brazilian surname',
        '/br_male_name': 'Brazilian male name',
        '/br_complete_male_name': 'Complete Brazilian male name',
        '/br_female_name': 'Brazilian female name',
        '/br_complete_female_name': 'Complete Brazilian female name',
        '/br_cpf': 'Brazilian CPF',
        '/br_number': 'Brazilian telephone number',
        '/br_cellphone_number': 'Brazilian cellphone number',
        '/date': 'Random date',
        '/time': 'Random time',

        '/dev': 'Info about the developer'
    }

    return list


def dev():
    return {
        'dev': 'Luiz Glomyer',
        'e-mail': 'glomyerjunior@hotmail.com',
        'github': 'https://github.com/LuizGlomyer',
        'repository': 'https://github.com/LuizGlomyer/name-generator'
    }
