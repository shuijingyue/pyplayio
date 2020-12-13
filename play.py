import re
import os
import csv
from lib import resolver
from lib.grammar import Class, Field, Funct

path = 'D:\\workspace\\android\\PersonalAssistant\\app\\src\\main\\java\\com\\miui'
row = ['Landroid/accessibilityservice/AccessibilityServiceInfo;->setCapabilities(I)V']


def readdirs(path: str) -> None:
    print(path)

    if os.path.isdir(path):
        for file in os.listdir(path):
            readdirs(os.path.join(path, file))
    else:
        compare(path)


def compare(path):

    api_csv = open('./api.csv', 'r', encoding='utf-8')

    reader = csv.reader(api_csv)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        for row in reader:
            if (reader.line_num == 1):
                continue
            if resolver.is_field(row[0]):
                api = Field(row)
                if content.find(api.class_name) != -1 and content.find(api.field_name):
                    print(api.class_name, api.field_name, path)
            else:
                api = Funct(row)
                if content.find(api.class_name) != -1 and content.find(api.funct_name):
                    print(api.class_name, api.funct_name, path)


if __name__ == "__main__":
    
    readdirs(path)
