import os

def readfile(filename): # Превращаем инфу с файла в нужную нам
     with open(filename, 'r', encoding='utf-8') as txt:
          textname = os.path.basename(txt.name)
          linescount = 0
          for line in txt:
               linescount += 1
     with open(filename, 'r', encoding='utf-8') as txt:
          data = txt.read()
     return f'{textname}\n{linescount}\n{data}\n'

outtext = open('num2/out.txt', 'w', encoding='utf-8')

# Запишем в выходной файл нужный текст

outtext.write(readfile('num2/texts_for_2/1.txt'))
outtext.write(readfile('num2/texts_for_2/2.txt'))
outtext.write(readfile('num2/texts_for_2/3.txt'))

outtext.close # Фенит!