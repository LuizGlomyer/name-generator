#  takes a list of names in .txt format separeted by a new line
#  outputs a new list without duplicates and with every name capitalized

filename = "en_surnames.txt"
file = open(f"generator/data/{filename}", 'r')
name_list = file.readlines()

names = []
for name in name_list:
    name = name.rstrip('\n').title()
    if name not in names:
        names.append(name)

names.sort()
processed_names = open(f"processed_{filename}", "w")
for name in names:
    processed_names.write(name + '\n')

file.close()
processed_names.close()
