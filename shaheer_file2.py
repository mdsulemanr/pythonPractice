first_name = 'Muhammad'
middle_name = 'Shaheer'
last_name = 'Suleman'

full_name = f'{first_name} {middle_name} {last_name}'

full_name_lower = full_name.lower()
full_name_case_fold = full_name.casefold()

def upper(str):
    result = str.upper()
    return result

print(upper(full_name))

def lower(str):
    result = str.lower()
    return result

print(lower(full_name))

def case_fold(str):
    result = str.casefold()
    return result

print(case_fold(full_name))
