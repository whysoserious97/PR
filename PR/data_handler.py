import data_loader
import colector
import merger
import data_filter


def load_data():
    files = data_loader.get_data()
    print(files)
    return files


def get_database(query, files):
    people = colector.parse_data(files)
    database = merger.merge(people)
    response = data_filter.to_filter(database, query)
    return response
