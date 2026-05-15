import os
import glob
import re

css_files = glob.glob('**/*.css', recursive=True)
pattern = re.compile(r'(\?|%3F)(v|ver)=[^"\'\s>\)]*')

for filepath in css_files:
    if 'node_modules' in filepath or 'rockman-static' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    new_content = pattern.sub('', content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
