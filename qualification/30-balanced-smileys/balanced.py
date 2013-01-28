import re
import collections
import functools

input_file = open('balanced_smileystxt.txt', 'r')
if not input_file:
    print 'unable to open input.txt'
    exit

# Check the number of lines.
t = int(input_file.next().strip('\n'))
assert(1 <= t and t <= 50)

# ---------------------------- EXTERNAL CODE ----------------------------

# Taken from http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

# --------------------------- END EXTERNAL CODE -------------------------

@memoized
def balanced(s, recursive=True):
    # print '- balanced(%r)' % s
    # An empty string ""
    if s == '':
        return True

    # One or more of the following characters: 'a' to 'z', ' ' (a space) or ':' (a colon)
    if re.match('^[a-z :]+$', s):
        # print 'alpha %r' % s
        return True

    # An open parenthesis '(', followed by a message with balanced parentheses, followed by a close parenthesis ')'.
    if s[0] == '(' and s[-1:] == ')':
        # print '(balanced)'
        if balanced(s[1:-1]):
            return True

    # A smiley face ":)" or a frowny face ":("
    if s in (':(', ':)'):
        # print 'emote %r' % s
        return True

    # A message with balanced parentheses followed by another message with balanced parentheses.
    if recursive:
        start = None
        l = len(s)
        for i in xrange(1, l):
            if not balanced(s[0:i], False):
                break
            else:
                start = s[0:i]

        if start is not None:
            # Now work back along the balanced start until we get a balanced string.
            while i > 0:
                start = s[0:i]
                end = s[i:]

                # print 'testing start:%r => %r end:%r => %r' % (start, balanced(start), end, balanced(end))
                if balanced(start) and balanced(end):
                    return True

                i -= 1

    return False

# import sys
# if len(sys.argv) == 2:
#     case_num = 0
#     s = sys.argv[1]
#     print 'Case #%d: %s' % (case_num, 'YES' if balanced(s) else 'NO')
# sys.exit(1)

for case_num, s in ((i + 1, line) for i, line in enumerate(input_file)):
    # if case_num != 4:
        # continue

    s = s.strip('\n')
    assert(1 <= len(s) and len(s) <= 100)

    # print '-- %r' % s
    print 'Case #%d: %s' % (case_num, 'YES' if balanced(s) else 'NO')
    # print
