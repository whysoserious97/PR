# Splitting FName
def split_full_name(pers):
    pers['first_name'] = pers['full_name'].split()[0]
    pers['last_name'] = pers['full_name'].split()[1]
    pers.pop('full_name')


# Merge info
def merge(people):
    people_set = []
    skip = False
    for person1 in people:          # Compare 2 persons like in bubble-sort but from different lists
        for person2 in people_set:
            # second we need to get first name and last name but avoid full name(as database good practice)
            in_list_a = in_list_b = False
            if 'full_name' in person1 or 'full_name' in person2:
                if 'full_name' in person1:
                    split_full_name(person1)
                    in_list_a = True
                if 'full_name' in person2:
                    split_full_name(person2)
                    in_list_b = True
            if in_list_a and in_list_b:
                if person1['first_name'] == person2['first_name'] and person1['last_name'] == person2['last_name']:
                    person2.update(person1)
                    skip = True
                    continue
            if 'email' in person1 and 'email' in person2:  # Condition: if there is a possibility to check emails...
                if person1['email'] == person2['email']:
                    person2.update(person1)
                    skip = True
                    continue
        if not skip:
            people_set.append(person1)
        skip = False
    return people_set
