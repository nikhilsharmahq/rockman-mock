import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
pattern = re.compile(r'(%3F|\?)(ver|v|ao_version|time|id)=[^"\'\s>]*')

count = 0
for filepath in html_files:
    if 'rockman-static' in filepath or 'node_modules' in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} HTML files.")
