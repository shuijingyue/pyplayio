import csv
from lib import resolver
from lib.grammar import Field, Funct


if __name__ == "__main__":
    
    api_csv = open('./api.csv', 'r', encoding='utf-8')

    reader = csv.reader(api_csv)

    for row in reader:
        if (reader.line_num == 1):
            continue
        if resolver.is_field(row[0]):
            api = Field(row)
        else:
            api = Funct(row)
        

