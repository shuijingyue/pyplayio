import csv
from lib import resolver
import json


class Class:

    def __init__(self, str):
        self.class_name = resolver.class_name(str)


class Funct(Class):

    def __init__(self, str):
        super().__init__(str)
        self.funct_name = resolver.funct_name(str)
        self.param_list = resolver.param_list(str)

    
    def __str__(self) -> str:
        return json.dumps({'class': self.class_name, 'funct': self.funct_name, 'params': self.param_list})


class Field(Class):

    def __init__(self, str):
        super().__init__(str)
        self.field_name = resolver.field_name(str)

    
    def __str__(self) -> str:
        return json.dumps({'class': self.class_name, 'field': self.field_name})


if __name__ == "__main__":
    
    api_csv = open('./api.csv', 'r')

    reader = csv.reader(api_csv)

    for api_line in reader:
        if (reader.line_num == 1):
            continue
        api = None
        if resolver.is_field(api_line[0]):
            api = Field(api_line[0])
        else:
            api = Funct(api_line[0])
        print(api)

