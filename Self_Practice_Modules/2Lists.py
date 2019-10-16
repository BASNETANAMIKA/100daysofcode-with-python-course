# Can you write a simple list comprehension to convert these names to title case (brad pitt -> Brad Pitt). Or reverse the first and last name?
# Should print(values might change as random):
#
# Arnold teams up with Brad
# Alec teams up with Julian

import random
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

caps_name = [name.title() for name in NAMES]
print(caps_name)

def gen_pairs(names=NAMES):
    for _ in range(len(names)):
        a = random.randint(0, len(names)-1)
        first_name = names[a].split()[0]
        b = random.randint(0, len(names)-1)
        second_name = names[b].split()[0]
        final_string = first_name + " is with " + second_name
        yield final_string


pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))

