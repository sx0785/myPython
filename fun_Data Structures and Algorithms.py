p = (4,5)
x,y=p
print(x,y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year,month, day) = data
print(name, shares, price,day)

_, shares, price, _ = data
print(price)

s = 'Hello'
a, b, c, d, e = s
print(e)

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record

print(phone_numbers[0])



records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname,homedir,sh)



from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

#d = defaultdict(set)
print(d)


prices = { 'AAA' : 41.23, 'ZZZ': 45.23 }
low_price = prices[min(prices, key=lambda k: prices[k])]
print(low_price)


prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
print(min(zip(prices.values(), prices.keys())))

print(max(zip(prices.values(), prices.keys())))


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
    ]
from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes',

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)