from itertools import combinations

def read_file(input_file):
    with open(input_file, 'r') as fp:
        num_lines = int(fp.next())
        # print "num_lines: %d" % num_lines

        while True:
            try:
                N, K = map(int, fp.next().split())
                a = map(int, fp.next().split())

                yield N, K, a

            except StopIteration as e:
                return


def solution(N, K, a):
    # print 'N=%r, K=%r, a=%r' % (N, K, a)

    the_sum = 0
    for combination in combinations(a, K):
        the_sum += max(combination)
        the_sum %= 1000000007

    return the_sum

for case_num, (N, K, a) in enumerate(read_file('input.txt'), start=1):
    print 'Case #%d: %d' % (case_num, solution(N, K, a))
