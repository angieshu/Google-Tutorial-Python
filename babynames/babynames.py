#!/usr/bin/python

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename, 'rw')
  text = f.readlines()
  lst = []
  for line in text:
    match = re.findall('in\s*(\d\d\d\d)', line)
    if match:
        lst.append(match[0])
        break
  for line in text:
    match = re.findall('<td>(\d+)</td>', line)
    if match:
        names = re.findall('<td>(\w+)</td>', line)
        if names:
            lst.append(names[1] + ' ' + match[0])
            lst.append(names[2] + ' ' + match[0])
  lst_0 = []
  lst_0.append(lst.pop(0))
  lst = lst_0 + sorted(lst)
  text = ''
  i = len(lst) - 1
  for line in lst:
    text += line
    if i > 0:
        text += '\n'
        i -= 1
  f.close()
  # +++your code here+++
  return text

def write_into_file(filename):
    text = extract_names(filename)
    summaryfile = filename + '.summary'
    f = open(summaryfile, 'w+')
    f.write(text)
    f.close

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

   summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    for arg in args:
        if not summary: print extract_names(arg)
        else: write_into_file(arg)
  
if __name__ == '__main__':
  main()
