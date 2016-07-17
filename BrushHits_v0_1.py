# -?- coding: utf-8 -?-
import re
import webbrowser

old_url = 'http://blog.csdn.net/github_35160620/article/details/'
total_page = 20

f = open('text.txt', 'r')
html = f.read()
f.close()

a = re.findall('<a href="http://blog.csdn.net/github_35160620/article/details/(.*?)" target', html, re.S)
print(a)

for i in range(len(a)):
    new_link = re.sub('details/(.*?)', 'details/%s'%a[i], old_url)
    webbrowser.open(new_link, new=1)
    print(new_link)

print(webbrowser.get())
