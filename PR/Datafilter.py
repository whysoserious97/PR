import re
def filter(database,query):
    ########################
    response=[]
    splited=query.split()
    args=len(splited)
    #########################################
    action=splited[0]
    column = splited[1]
    patern=''
    ############################
    if args==3:
        patern=query.split()[2]
    ############################
    if action=='SelectColumn':
        for person in database:
            if column in person:
                response.append(person[column])

    elif action =='SelectFromColumn':
        for person in database:
            if column in person:
                regexp = re.compile(patern)
                if regexp.search(person[column]):
                    response.append(person[column])
    return response
