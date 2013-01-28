from collections import Counter
import re

input_file = open('beautiful_input.txt', 'r')

if not input_file:
    print 'unable to open input file'
    exit

# Check the number of lines.
m = int(input_file.next().strip('\n'))
assert(5 <= m and m <= 50)

for i, s in enumerate(input_file):
    s = s.strip('\n')
    assert(2 <= len(s) and len(s) <= 500)

    # Sanitize.
    s = s.lower()
    s = re.sub('[^a-z]', '', s)

    # Work out the maximum possible beauty.
    b = 0
    beauties = iter(range(26, 0, -1))
    c = Counter(s)
    for letter, count in c.most_common():
        b += (beauties.next() * count)

    print 'Case #%d: %d' % (i + 1, b)
