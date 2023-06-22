import glob
import os
import subprocess

# Get sorted list of jpg and png files
image_files = sorted(glob.glob('pics_to_upload/*.jpg') + glob.glob('pics_to_upload/*.png'))

# Check if there are any image files
if image_files:
    first_file = image_files[0]

    # Call the profile pic update script on the first file
    result = subprocess.run(['python3', 'update_profile_pic.py', first_file])

    # If the script was successful, rename the file
    if result.returncode == 0:
        new_name = first_file + '.__used'
        os.rename(first_file, new_name)
    else:
        print(f'Error in updating profile picture with file: {first_file}')
else:
    print('No jpg or png files found.')
