import time as t
f = open('diary.txt', 'a', encoding="utf8")
con=input('Please type the content of the dairy:')
f.write(con)
f.write('\n')
f.close
