import re

def halved(lst):
    return [i/2 for i in lst]

def only_positive(lst):
    return [i for i in lst if i > 0]

def sum(lst):
    return sum(lst)


def stripped_strings(lst):
    return [re.sub('[^0-9a-zA-Z]', '', i) for i in lst]

def find_special(lst):
    for word in range(len(lst)):
        if lst[word] == 'special': return word
    return -1

def valid_contacts(lst):
    return [i for i in lst if len(i.phoneNumber) == 10]
    
def contact_names(lst):
    return [i.name for i in lst]

print(find_special(['spec', 'misc', 'bats', 'special']))