import urllib.request
import os

urls = ['https://stackoverflow.com/',
        'https://reactjs.org/']

print("Downloading sites...")
for i in range(0, urls.__len__()):
    dir_path = 'server_files'
    full_path = dir_path + '/' + str(i) + '.html'
    if not os.path.exists(full_path):
        html_res = urllib.request.urlopen(urls[i])
        html_content = html_res.read()
        file = open(full_path, 'w', encoding='utf-8')
        file.write(html_content.decode())
        file.close()
