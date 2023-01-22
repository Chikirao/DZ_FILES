import os

def readfile(filename):
     with open(filename, 'r', encoding='utf-8') as txt:
          textname = os.path.basename(txt.name)
          linescount = 0
          for line in txt:
               linescount += 1
     with open(filename, 'r', encoding='utf-8') as txt:
          data = txt.read()
     return f'{textname}\n{linescount}\n{data}\n'

outtext = open('texts_for_2/out.txt', 'a', encoding='utf-8')

outtext.write(readfile('texts_for_2/1.txt'))
outtext.write(readfile('texts_for_2/2.txt'))
outtext.write(readfile('texts_for_2/3.txt'))
