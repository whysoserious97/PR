import json
import re
import xml.etree.ElementTree as ET
import yaml
import csv


def parseData(paths):
    listpeople = []
    for path in paths:
        f=open(path, 'r')
        content = f.read()

        regexp = re.compile(r'\w+\.json')
        if (regexp.search(path)):
            if content[len(content)-3]==',':
                content=content[:len(content)-3]+content[len(content)-2:]
            group = json.loads(content)
            for person in group:
                if 'id' in person:
                    person.pop('id')
                listpeople.append(person)
        regexp = re.compile(r'\w+\.xml')
        if (regexp.search(path)):
            tree = ET.parse(path)
            root = tree.getroot()
            for record in root:
                person={}
                for child in record:
                    if child.tag == 'id':
                        key = child.text
                    else:
                        person[child.tag]=child.text
                listpeople.append(person)

        regexp=re.compile(r'\w+\.yml')
        if(regexp.search(path)):
            with open(path, 'r') as stream:
                try:
                    group=yaml.safe_load(stream)
                    for person in group:
                        person.pop('id')
                        listpeople.append(person)
                except:
                    pass
        regexp = re.compile(r'\w+\.csv')
        if (regexp.search(path)):
            with open(path,'r') as file:
                csv_file=csv.DictReader(file)
                for row in csv_file:
                    person=dict(row)
                    person.pop('id')
                    listpeople.append(person)
    return listpeople
