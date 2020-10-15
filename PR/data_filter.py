import re


def to_filter(database, query):

    # Setup
    response = []
    split = query.split()
    args = len(split)
    column = pattern = ''
    action = split[0]
    if args > 1:
        column = split[1]
    if args > 2:
        pattern = split[2]

    # Filtering
    if action == 'SelectColumn':
        for person in database:
            if column in person:
                response.append(person[column])

    elif action == 'SelectFromColumn':
        for person in database:
            if column in person:
                regexp = re.compile(pattern)
                if regexp.search(person[column]):
                    response.append(person[column])

    else:
        response.append("Sorry I don't understand you")
    return response
