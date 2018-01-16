import time
import webbrowser
print('the program start at'+time.ctime())
break_total = 3
break_count = 0
while(break_count<break_total):
 time.sleep(3)
 webbrowser.open('http://music.163.com/#/song?id=28202029')
 break_count+=1