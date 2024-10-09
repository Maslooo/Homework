calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(user_str):
    len_str = len(user_str)
    up_reg_str = user_str.upper()
    down_reg_str = user_str.lower()
    count_calls()
    return len_str, up_reg_str, down_reg_str
def is_contains(string, list_to_search):
    lower_str = string.lower()
    count_calls()
    for elem in list_to_search:
        lower_elem = elem.lower()
        if (lower_str == lower_elem):
            return True
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)