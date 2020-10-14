import re


def to_filter(database, query):
    ########################
    response = []
    split = query.split()
    args = len(split)
    #########################################
    action = split[0]
    column = ''
    if args > 1:
        column = split[1]
    pattern = ''
    ############################
    if args == 3:
        pattern = query.split()[2]
    ############################
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
