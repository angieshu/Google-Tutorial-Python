
import random
import sys


def mimic_dict(filename):
    f = open(filename, 'rU')
    text = f.read().split()
    d = {}
    d[''] = []
    d[''].append(text[0])
    i = 0
    count = len(text) - 1
    while i < count:
        if text[i] not in d:
            d[text[i]] = []
        d[text[i]].append(text[i + 1])
        i += 1
    if text[i] not in d:
        d[text[i]] = []
    d[text[i]].append('')
     return d


def print_mimic(mimic_dict, word):
    i = 0
    while i < 200:
        print word,
        word = random.choice(mimic_dict[word])
        i += 1

def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
