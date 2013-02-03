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

    # Initialise dead pixel locations.
    dead_pixels = set()
    prev_x, prev_y = X, Y
    dead_pixels.add((prev_x, prev_y))
    for i in xrange(1, N):
        x = (prev_x * a + prev_y * b + 1) % W
        y = (prev_x * c + prev_y * d + 1) % H
        dead_pixels.add((x, y))
        prev_x, prev_y = x, y

    # print 'dead_pixels=%r' % sorted(dead_pixels)

    # Valid screen offsets to place the image.
    offsets = set()
    for y_start in xrange(0, (H - Q) + 1):
        for x_start in xrange(0, (W - P) + 1):
            contains_dead_pixel = False
            for y in xrange(y_start, y_start + Q):
                for x in xrange(x_start, x_start + P):
                    if (x, y) in dead_pixels:
                        contains_dead_pixel = True
                        break

                if contains_dead_pixel:
                    break

            if not contains_dead_pixel:
                offset = (x_start, y_start)
                # print 'offset=%r' % (offset,)
                offsets.add(offset)

    # print 'offsets=%r' % sorted(offsets)
    positions = len(offsets)
    return positions

for case_num, args in enumerate(read_file('input.txt'), start=1):
    print 'Case #%d: %r' % (case_num, solution(*args))
