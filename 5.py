pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and
# more than 15 gold

def pirates_with_wooden_leg_and_more_than_15_golds(input):
    pirate_names = []
    for x in input:
        if x['has_wooden_leg'] == True and x['gold'] > 15:
            pirate_names.append(x['Name'])
    return pirate_names

print(pirates_with_wooden_leg_and_more_than_15_golds(pirates))
