
def verbing(s):
    if len(s) < 3 : return s
    if s[-3:] == 'ing' : return s + 'ly'
    else : return s + 'ing'


def not_bad(s):
	a = s.find('not')
	b = s.find('bad')
	if not a or not b : return s
	if a > b : return s
	return s.replace(s[a : (b + 3)], 'good')

def front_back(a, b):
	a_len = len(a)
	a_front = a[:(a_len / 2) + ((a_len %2) == 1)]
	a_back = a[(a_len / 2) + ((a_len %2) == 1):]
	b_len = len(b)
	b_front = b[:(b_len / 2) + ((b_len %2) == 1)]
	b_back = b[(b_len / 2) + ((b_len %2) == 1):]
	return a_front + b_front + a_back + b_back

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
