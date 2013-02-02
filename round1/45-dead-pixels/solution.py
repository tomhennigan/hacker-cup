def read_file(input_file):
    with open(input_file, 'r') as fp:
        num_lines = int(fp.next())
        # print "num_lines: %d" % num_lines

        while True:
            try:
                W, H, P, Q, N, X, Y, a, b, c, d = map(int, fp.next().split())

                # assert(1 <= T and T <= 20)
                assert(1 <= W and H <= 40000)
                assert(1 <= P and P <= W)
                assert(1 <= Q and Q<= H)
                assert(1 <= N and N <= min(1000000, W * H))
                assert(1 <= a and 1 <= b and 1 <= c and d <= 100)
                assert(0 <= X and X < W)
                assert(0 <= Y and Y < H)
                yield (W, H, P, Q, N, X, Y, a, b, c, d)

            except StopIteration as e:
                return

def solution(W, H, P, Q, N, X, Y, a, b, c, d):
    # print 'W=%r, H=%r, P=%r, Q=%r, N=%r, X=%r, Y=%r, a=%r, b=%r, c=%r, d=%r' % (W, H, P, Q, N, X, Y, a, b, c, d)

    # x[0] = X
    # y[0] = Y
    # x[i] = (x[i - 1] * a + y[i - 1] * b + 1) % W (for 0 < i < N)
    # y[i] = (x[i - 1] * c + y[i - 1] * d + 1) % H (for 0 < i < N)

    dead_pixels = set()

    # x = [None] * N
    # y = [None] * N
    # x[0] = X
    # y[0] = Y
    # dead_pixels.add((x[0], y[0]))
    # for i in xrange(1, N):
    #     x[i] = (x[i - 1] * a + y[i - 1] * b + 1) % W
    #     y[i] = (x[i - 1] * c + y[i - 1] * d + 1) % H
    #     dead_pixels.add((x[i], y[i]))

    prev_x = X
    prev_y = Y
    dead_pixels.add((prev_x, prev_y))
    for i in xrange(1, N):
        x = (prev_x * a + prev_y * b + 1) % W
        y = (prev_x * c + prev_y * d + 1) % H
        dead_pixels.add((x, y))
        prev_x, prev_y = x, y

    # print 'dead_pixels=%r' % sorted(dead_pixels)

    # Valid offsets
    offsets = set()

    for y_start in xrange(0, (H - Q) + 1):
        for x_start in xrange(0, (W - P) + 1):
            contains_dead_pixel = False
            for y in xrange(y_start, y_start + Q):
                for x in xrange(x_start, x_start + P):
                    if (x, y) in dead_pixels:
                        contains_dead_pixel = True
                        # print ' X %r' % ((x, y),)
                        break

                    # print ' - %r' % ((x, y),)

                if contains_dead_pixel:
                    break

            if not contains_dead_pixel:
                offset = (x_start, y_start)
                # print 'offset=%r' % (offset, )
                offsets.add(offset)

    # print the screen
    # print
    # import sys
    # for y in xrange(0, H):
    #     sys.stdout.write('    ')
    #     if y < 0xf:
    #         sys.stdout.write('%X ' % y)
    #     else:
    #         sys.stdout.write('  ')

    #     for x in xrange(0, W):
    #         pixel = (x, y)
    #         sys.stdout.write('|')
    #         if pixel in dead_pixels:
    #             sys.stdout.write('D')
    #         elif pixel in offsets:
    #             sys.stdout.write('o')
    #         else:
    #             sys.stdout.write(' ')

    #     sys.stdout.write('|\n')
    # print

    # print 'offsets=%r' % sorted(offsets)
    positions = len(offsets)
    return positions

for case_num, args in enumerate(read_file('input.txt'), start=1):
    print 'Case #%d: %r' % (case_num, solution(*args))
