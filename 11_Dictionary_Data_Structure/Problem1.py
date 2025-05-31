# Count how many times each character repeated in the String
word = 'mississippi'

d = {}

for x in word:
    d[x] = d.get(x,0) + 1

for (k,v) in d.items():
    print(k, 'occurred', v , 'times')


"""
First loop: for x in word:
This loop iterates over each character in the string word. Here's the breakdown of each iteration and the state of d:

x = 'm' → 'm' not in d, so d['m'] = 0 + 1 → {'m': 1}

x = 'i' → 'i' not in d, so d['i'] = 0 + 1 → {'m': 1, 'i': 1}

x = 's' → 's' not in d, so d['s'] = 0 + 1 → {'m': 1, 'i': 1, 's': 1}

x = 's' → 's' in d, d['s'] = 1 + 1 → {'m': 1, 'i': 1, 's': 2}

x = 'i' → d['i'] = 1 + 1 → {'m': 1, 'i': 2, 's': 2}

x = 's' → d['s'] = 2 + 1 → {'m': 1, 'i': 2, 's': 3}

x = 's' → d['s'] = 3 + 1 → {'m': 1, 'i': 2, 's': 4}

x = 'i' → d['i'] = 2 + 1 → {'m': 1, 'i': 3, 's': 4}

x = 'p' → 'p' not in d, so d['p'] = 0 + 1 → {'m': 1, 'i': 3, 's': 4, 'p': 1}

x = 'p' → d['p'] = 1 + 1 → {'m': 1, 'i': 3, 's': 4, 'p': 2}

x = 'i' → d['i'] = 3 + 1 → {'m': 1, 'i': 4, 's': 4, 'p': 2}


Second loop: for (k, v) in d.items():
This iterates over each key-value pair in the dictionary d:

First: k = 'm', v = 1 → prints "m occurred 1 times"

Then: k = 'i', v = 4 → "i occurred 4 times"

Then: k = 's', v = 4 → "s occurred 4 times"

Then: k = 'p', v = 2 → "p occurred 2 times"
"""










