from generator import generator
import routes

from flask import Flask, request
app = Flask(__name__)

max = 100  # to prevent server abuse


def generate(item, number_of_items, **kwargs):
    if number_of_items:
        number_of_items = int(number_of_items)
        if number_of_items > max:
            number_of_items = max
        list = {i+1: item(**kwargs) for i in range(number_of_items)}
        return list
    else:
        return item(**kwargs)


@app.route('/')
@app.route('/help/')
def index(): return routes.route_list()


@app.route('/dev')
def dev(): return routes.dev()


@app.route('/fantasy-name/')
def fantasy_name():
    return generate(generator.fantasy_name, request.args.get('quantity'))


@app.route('/br-male/')
def br_male_name():
    return generate(generator.br_male_name, request.args.get('quantity'))


@app.route('/br-male-complete/')
def br_complete_male_name():
    return generate(generator.br_complete_male_name, request.args.get('quantity'))


@app.route('/br-female/')
def br_female_name():
    return generate(generator.br_female_name, request.args.get('quantity'))


@app.route('/br-female-complete/')
def br_complete_female_name():
    return generate(generator.br_complete_female_name, request.args.get('quantity'))


@app.route('/br-surname/')
def br_surname():
    return generate(generator.br_surname, request.args.get('quantity'))


@app.route('/br-cpf/')
def br_cpf():
    return generate(generator.br_cpf, request.args.get('quantity'))


@app.route('/br-number/')
def br_number():
    number = generate(generator.br_phone_number, request.args.get('quantity'),
                      ddd=request.args.get('ddd'), cellphone=request.args.get('cellphone'))
    return number


@app.route('/date/')
def date():
    date = generate(generator.date, request.args.get(
        'quantity'), twoDigits=request.args.get("twoDigits"))
    return date


@app.route('/time/')
def time():
    return generate(generator.time, request.args.get('quantity'))


@app.route('/hash/')
def hash():
    algorithm = request.args.get('algorithm')
    value = request.args.get('value')
    return generator.hash(algorithm=algorithm, value=value)
