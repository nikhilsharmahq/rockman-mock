import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

# Find all files starting with 'index.html?p='
bad_files = glob.glob('index.html?p=*.html')
rename_map = {}

for old_name in bad_files:
    # Extract the number, e.g., '146' from 'index.html?p=146.html'
    match = re.search(r'p=(\d+)\.html', old_name)
    if match:
        num = match.group(1)
        new_name = f'page-{num}.html'
        os.rename(old_name, new_name)
        rename_map[old_name] = new_name
        # Also map the url-encoded version
        encoded_name = old_name.replace('?', '%3F')
        rename_map[encoded_name] = new_name

print(f"Renamed {len(rename_map)//2} files.")

# Update all references in all HTML files
for filepath in html_files:
    # Skip the old files if they are in the list, though they're renamed now
    if filepath in rename_map:
        filepath = rename_map[filepath]
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    modified = False
    for old_ref, new_ref in rename_map.items():
        if old_ref in content:
            content = content.replace(old_ref, new_ref)
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated links in HTML files.")
