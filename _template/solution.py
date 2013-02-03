def read_file(input_file):
    with open(input_file, 'r') as fp:
        num_lines = int(fp.next())
        # print "num_lines: %d" % num_lines

        while True:
            try:
                arg1, arg2 = fp.next().split()
                yield (arg1, arg2)

            except StopIteration as e:
                return

def solution(arg1, arg2):
    return None

for case_num, args in enumerate(read_file('input.txt'), start=1):
    print 'Case #%d: %r' % (case_num, solution(*args))
