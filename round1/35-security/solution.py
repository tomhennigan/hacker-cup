from itertools import izip_longest, permutations, islice

def read_file(input_file):
    with open(input_file, 'r') as fp:
        num_lines = int(fp.next())
        # print "num_lines: %d" % num_lines

        while True:
            try:
                m = int(fp.next().strip())
                k1 = str(fp.next().strip())
                k2 = str(fp.next().strip())
                yield (m, k1, k2)

            except StopIteration as e:
                return

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return map(lambda g: ''.join(g), izip_longest(*args, fillvalue=fillvalue))

def roll_string(s):
    for offset in xrange(0, len(s)):
        yield s[offset:] + s[0:offset]

def possible_match(k1, k2):
    for i in xrange(0, len(k1)):
        e1 = k1[i]
        e2 = k2[i]

        for idx, e1c in enumerate(e1):
            e2c = e2[idx]

            if e1c == '?' or e2c == '?':
                continue

            if e1c != e2c:
                return False

    return True

def solution(n, k1, k2):
    # print 'n=%r' % n
    # print 'k1=%r' % k1
    # print 'k2=%r' % k2

    lk1 = grouper(k1, n)
    # print 'lk1=%r' % lk1

    lk2 = map(lambda w: grouper(w, n), roll_string(k2))
    # print 'lk2=%r' % lk2

    for possible_k2 in lk2:
        # print '  - possible_k2=%r' % (list(possible_k2))
        if possible_match(lk1, possible_k2):
            # print 'possible_match=%r' % list(possible_k2)
            pk2 = ''.join(possible_k2)

            possible = [c for c in k1]
            for idx, c in enumerate(possible):
                if c == '?':
                    if k1[idx] == '?':
                        # print '  - possible[%d] = %r' % (idx, pk2[idx])
                        possible[idx] = pk2[idx]
                    elif pk2[idx] == '?':
                        # print '  - possible[%d] = %r' % (idx, k1[idx])
                        possible[idx] = k1[idx]

            # print 'possible=%r' % possible
            possible = ''.join(possible)
            yield possible.replace('?', 'a')

for case_num, (n, k1, k2) in enumerate(read_file('input.txt'), start=1):
    k = None
    for possible in solution(n, k1, k2):
        if k is None or possible < k:
            k = possible

    print 'Case #%d: %s' % (case_num, 'IMPOSSIBLE' if (not k) else k)
