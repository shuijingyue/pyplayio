import csv
from lib import resolver
import json


class Class:

    def __init__(self, row: list[str]):
        self.class_name = resolver.class_name(row[0])
        self.row = row
        self.used = False


class Funct(Class):

    def __init__(self, row: list[str]):
        super().__init__(row)
        self.funct_name = resolver.funct_name(row[0])
        self.param_list = resolver.param_list(row[0])

    
    @classmethod
    def is_funct(cls, api):
        return isinstance(api, cls)

    
    def __str__(self) -> str:
        return json.dumps({
            'class': self.class_name, 
            'funct': self.funct_name, 
            'param': self.param_list,
            'row': self.row
            })


class Field(Class):

    def __init__(self, row: list[str]):
        super().__init__(row)
        self.field_name = resolver.field_name(row[0])


    @classmethod
    def is_funct(cls, api):
        return isinstance(api, cls)

    
    def __str__(self) -> str:
        return json.dumps({
            'class': self.class_name, 
            'field': self.field_name,
            'row': self.row
            })