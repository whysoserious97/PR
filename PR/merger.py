# Splitting FName
def split_full_name(pers):
    pers['first_name'] = pers['full_name'].split()[0]
    pers['last_name'] = pers['full_name'].split()[1]
    pers.pop('full_name')


# Merge info
def merge(people):
    people_set = []
    skip = False
    for person in people:
        for pers in people_set:
            # second we need to get first name and last name but avoid full name(as database good practice)
            in_list_a = False
            in_list_b = False
            if 'full_name' in person or 'full_name' in person:
                if 'full_name' in person:
                    split_full_name(person)
                    in_list_a = True
                if 'full_name' in pers:
                    split_full_name(pers)
                    in_list_b = True
            if in_list_a and in_list_b:
                if person['first_name'] == pers['first_name'] and person['last_name'] == pers['last_name']:
                    pers.update(person)
                    skip = True
                    continue
            if 'email' in person and 'email' in pers:  # Condition: if there is a possibility to check emails...
                if person['email'] == pers['email']:
                    pers.update(person)
                    skip = True
                    continue
        if not skip:
            people_set.append(person)
        skip = False
    return people_set
