#!/usr/bin/python

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  f = urllib.urlopen(filename)
  text = f.read()
  lst = re.findall('GET\s(\S+/puzzle/\S+)', text)
  urls = []
  if not re.search('http://', filename):
    filename = 'http://' + filename
  for img_url in lst:
    urls.append(filename + img_url)
  return urls
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if not os.path.exists(dest_dir):
    (st, out) = commands.getstatusoutput('mkdir ' + dest_dir)
    if st:
        sys.stderr.write(out)
  i = 0
  for img in img_urls:
    urllib.urlretrieve(img, dest_dir + '/' + 'img' + str(i))
    i += 1


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
