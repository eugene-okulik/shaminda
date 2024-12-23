my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 3, 4, 5],
    'dict': {
        'one_value': 'one',
        'two_value': 'two',
        'three_value': 'three',
        'four_value': 'four',
        'five_value': 'five'
    },
    'set': {1, 4, 6, 77, 99}
}

last_element = my_dict['tuple'][-1]
print(last_element)

my_dict['list'].append(6)
del my_dict['list'][1]

my_dict['dict']['i am a tuple'] = 'new value'
del my_dict['dict']['three_value']

my_dict['set'].add('ggg')
my_dict['set'].remove(77)

print(my_dict)

