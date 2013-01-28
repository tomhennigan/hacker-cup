from itertools import permutations

s = 'abbccc'
beauty = 152
for a, b, c in permutations(xrange(1, 27), 3):
    if (a + (2 * b) + (3 * c)) == beauty:
        break

for e, d, i, h, k, m, o, p, s, r, u, t in permutations(range(1, 27), 12):

    if ((4 * a) + c + (6 * e) + d + i + h + k + (3 * m) + (2 * o) + p + (5 * s) + (2 * r) + u + (4 * t)) == 729:
        print {
            'a': a,
            'c': c,
            'e': e,
            'd': d,
            'i': i,
            'h': h,
            'k': k,
            'm': m,
            'o': o,
            'p': p,
            's': s,
            'r': r,
            'u': u,
            't': t,
        }
