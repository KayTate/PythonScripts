import datetime, helpers

#Catches same-account transfers
def is_same(origin, destin):
    if origin == destin:
        return True
    return False

#Catches invalid phone numbers
def is_phone(number):
    if len(number) != 10:
        print('This is not a valid 10-digit number.')
        return False
    for char in number:
        if char not in '1234567890':
            print('This is not a valid 10-digit number.')
            return False
    return True

#Age Validator
def is_adult(year):
    #Gets the current year
    now = datetime.datetime.now()
    cyear = now.year

    #Checks age
    age = cyear-year
    if age < 18:
        return False
    return True

#Account holder
def is_holder(holders):
    members = helpers.get_holders()

    aliases = []
    for name in holders:
        if name in members:
            name_alias = helpers.get_aliases(name)
            for alias in name_alias:
                aliases.append(alias)

    return aliases