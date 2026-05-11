import os

filepath = r'c:\Users\nitesh.kumar\astroupes.github.io\activities.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace src="assests/images/ with src="assests/images/cache/
content = content.replace('src="assests/images/', 'src="assests/images/cache/')

# Replace "assests/images/ with "assests/images/cache/ for JS arrays
# Be careful not to replace it if it's already cached.
# A simple way to do it for JS arrays is to target lines that are in JS.
# Actually, since we only replaced src=" above, we can just replace
# "assests/images/ with "assests/images/cache/ where it is preceded by space or bracket
# Let's just do:
content = content.replace('    "assests/images/', '    "assests/images/cache/')
content = content.replace('          src: "assests/images/', '          src: "assests/images/cache/')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated activities.md")
