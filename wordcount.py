
import sys

def open_read(filename):
    f = open(filename, 'rU')
    text = f.read().lower().split()
    dict = {}
    for word in text:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    f.close()
    return dict

def last(s): return s[-1]

def print_words(filename):
    dict = open_read(filename)
    for key in dict:
        print key, dict[key]

def print_top(filename):
    dict = sorted(open_read(filename).items(), key=last, reverse=True)[:20]
    for elem in dict:
        print elem[0], elem[1]

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
