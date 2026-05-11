import os
path = r'c:\Users\nitesh.kumar\astroupes.github.io\gallery.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('href="assests/images/', 'href="assests/images/cache/')
text = text.replace('src="assests/images/', 'src="assests/images/cache/')
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print("done gallery")
