#!/usr/bin/python -tt

# import module `sys` to take argument on terminal
import sys

# define threetimes() function
def threetimes(word, exclaim):
  words = word + ' ' + word + ' ' + word

  if exclaim == 'exclaim':
    words = words + '!!!'

  print words

# take argument from command line and assigned to variable
if len(sys.argv) == 2:
  word = sys.argv[1]
  exclaim = False

elif len(sys.argv) >= 3:
  word = sys.argv[1]
  exclaim = sys.argv[2]

else:
  word = 'helllo'
  exclaim = 'exclaim'

if __name__ == '__main__':
  threetimes(word, exclaim)