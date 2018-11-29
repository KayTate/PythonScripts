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