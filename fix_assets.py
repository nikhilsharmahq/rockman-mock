import os
import glob

# Walk the current directory except rockman-static
for root, dirs, files in os.walk('.'):
    if 'rockman-static' in root or 'node_modules' in root or '.git' in root:
        continue
    
    for filename in files:
        if '?' in filename:
            old_path = os.path.join(root, filename)
            # Find the '?' and strip everything after it
            new_filename = filename.split('?')[0]
            new_path = os.path.join(root, new_filename)
            
            # If the file already exists, we might just delete the query version or overwrite
            if os.path.exists(new_path):
                # Just remove the duplicate versioned file since the base one exists
                os.remove(old_path)
                print(f"Removed duplicate {old_path}")
            else:
                os.rename(old_path, new_path)
                print(f"Renamed {old_path} to {new_path}")
