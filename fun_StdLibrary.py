import unicodedata

print(unicodedata.lookup('LEFT CURLY BRACKET'))

print(unicodedata.name('/'))

print(unicodedata.decimal('9'))

#unicodedata.decimal('a')

print(unicodedata.category('A'))  # 'L'etter, 'u'ppercase

print(unicodedata.bidirectional('\u0660')) # 'A'rabic, 'N'umber


from codecs import StreamWriter



from datetime import timedelta

d = timedelta(hours = 1)
print((d.days,d.seconds,d.microseconds))
