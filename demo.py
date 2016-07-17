__author__ = 'Aobo Jaing'
# -?- coding: utf-8 -?-
import re
import webbrowser
import time
import os

old_url = 'http://blog.csdn.net/github_35160620/article/details/'
total_page = 20

f = open('text.txt', 'r')
html = f.read()
f.close()

a = re.findall('<a href="http://blog.csdn.net/github_35160620/article/details/(.*?)" target', html, re.S)
print(a)

couter = 10

while(couter > 0):
    for i in range(len(a)):
        new_link = re.sub('details/(.*?)', 'details/%s'%a[i], old_url)
        webbrowser.open(new_link, new=1)
        print(new_link)

    time.sleep(60)
    os.system('taskkill /F /IM chrome.exe')
    couter = couter - 1


print(webbrowser.get())
