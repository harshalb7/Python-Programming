import string
fname = input('Enter file name: ')
fhand = open(fname)
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans(",", string.punctuation))
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)
