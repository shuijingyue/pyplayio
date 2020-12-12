import csv

api = open('./api.csv', 'r')

reader = csv.reader(api)

for item in reader:
    if reader.line_num == 1:
        continue
    cls, field = item[0].split(';', 1)
    print('class', cls[1:].replace('/', '.').replace('$', '.'))
    if field.find(':') != -1:
        print()
    else:
        field_name, params_and_return = field[2:].split('(', 1)
        params_str, return_type = params_and_return.split(')')
        params = params_str.split(';')
        for index, item in enumerate(params):
            if len(item) > 1:
                params[index] = item[1:].replace('/', '.').replace('$', '.')
        print('params', params)