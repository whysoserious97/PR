import data_loader
import colector
import merger
import datafilter


def load_data():
    files = data_loader.get_data()
    print(files)
    return files


def get_database(query, files):
    people = colector.parse_data(files)
    database = merger.merge(people)
    response = datafilter.to_filter(database, query)
    return response
