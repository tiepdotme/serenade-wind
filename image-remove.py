import glob

import os
import sys
import argparse

# Images will be added to a landing zone (folder): source_dir
# Read images from landing zone and compress acording to:
# 
#  xlarge: "1280px"
#  large: "1024px"
#  medium: "768px"
#  small: "320px"
# Save resized files to the correct folder.
# If no errors, delete the source file. 

# Configuration
dest_dir = "tmp"
# Map out images sizes and destination subdir names
sizes = {
	'small':320,
	'medium': 768,
	'large':1024,
	'xlarge': 1280
}
print(
	'''
Hi Baby 
         ,
        ()    /)
----.---'----(  )
     \        \)
     ()                   
      `
	'''
	)
operation = input("Please select an option\n\n(1) to rename\n(2) to remove\n\nYour selection: ")
if operation == 2:
	print " === FILE REMOVAL ==="
	source_filename = raw_input("Enter image filename: ")
	source_extension = raw_input("File Extension (default jpg): ")
	if not source_extension:
		source_extension = "jpg"
elif operation == 1:
	print " === FILE RENAME === "
	source_filename = raw_input("Enter image filename: ")
	source_extension = raw_input("File Extension (default jpg): ")
	if not source_extension:
		source_extension = "jpg"	
	new_filename = raw_input("Enter new image filename: ")
	new_extension = raw_input("New file extension (default jpg): ")	
	if not new_extension:
		source_extension = "jpg"	

# Iterate through image sizes for each break point
for size in sizes:
	reg_filename = dest_dir + "/" + size + "/" + source_filename + "." + source_extension
	# define retina image filename
	ret_filename = dest_dir + "/" + size + "/" + source_filename + "_2x" + "." + source_extension	
	#check if files exist
	if os.path.isfile(ret_filename):
		# for renaming
		if operation == 1:
			
		print "Removing: " + ret_filename
		os.remove(ret_filename)
	else:
		print "File " + ret_filename + " does not exist"

	if os.path.isfile(reg_filename):
		print "Removing: " + reg_filename
		os.remove(reg_filename)
	else:
		print "File " + reg_filename + " does not exist"