input_file = open('find_the_min.txt', 'r')

T = int(input_file.next().strip('\n'))
# print 'T: %r' % T
assert(T <= 20)

def read_input_file(fd):
    while True:
        try:
            n, k = map(int, input_file.next().strip('\n').split())
            a, b, c, r = map(int, input_file.next().strip('\n').split())
            yield (n, k), (a, b, c, r)
        except StopIteration:
            break

def m_next(m):
    minimum = min(m)

    for i in xrange(0, minimum):
        if not i in m:
            return i

    while minimum in m:
        minimum += 1

    return minimum

def get_value(n, k, a, b, c, r):
    # print 'n=%r, k=%r' % (n, k)
    # print 'a=%r, b=%r, c=%r, r=%r' % (a, b, c, r)

    # Allocate an array of length.
    m = [None] * k
    m[0] = a
    for i in xrange(1, k): # 0 < i < k
        # assert(0 < i and i < k)
        m[i] = (b * m[i - 1] + c) % r

    lm = len(m)

    if n <= lm:
        # n is already known.
        return m[n - 1]

    for i in xrange(k, n):
        next = m_next(m)
        del m[0]
        m.append(next)

    # print 'm=%r' % m

    return m[k - 1]

# expected = {
#     1: 8,
#     2: 38,
#     3: 41,
#     4: 40,
#     5: 12,
# }

case_num = 0
for (n, k), (a, b, c, r) in read_input_file(input_file):
    case_num += 1

    mn = get_value(n, k, a, b, c, r)
    # print 'mn=%r, expected=%r' % (mn, expected[case_num])
    # assert(mn == expected[case_num])

    print 'Case #%d: %r' % (case_num, mn)
