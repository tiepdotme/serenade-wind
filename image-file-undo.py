import glob
import sys 
from termcolor import colored, cprint
import os
import sys
import argparse


# Configuration
dest_dir = "images"
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
	print "\n\n === FILE REMOVAL ===\n\n"
	source_filename = raw_input("Enter image filename: ")
	source_extension = raw_input("File Extension (default jpg): ")
	if not source_extension:
		source_extension = "jpg"
elif operation == 1:
	print "\n\n === FILE RENAME ===\n\n"
	source_filename = raw_input("Enter image filename: ")
	source_extension = raw_input("File Extension (default jpg): ")
	if not source_extension:
		source_extension = "jpg"	
	new_filename = raw_input("Enter new image filename: ")
	new_extension = raw_input("New file extension (default jpg): ")	
	if not new_extension:
		new_extension = "jpg"	

# Iterate through image sizes for each break point
for size in sizes:
	reg_filename = dest_dir + "/" + size + "/" + source_filename + "." + source_extension
	# define retina image filename
	ret_filename = dest_dir + "/" + size + "/" + source_filename + "_2x" + "." + source_extension	
	#check if files exist
	if os.path.isfile(ret_filename):
		# for renaming
		if operation == 1:
			rename_to = dest_dir + "/" + size + "/" + new_filename + "_2x" + "." + new_extension
			success = colored("\nRenaming:\n(from) :: " + ret_filename + "\n( to ) :: " + rename_to, "green")
			print(success)

			os.rename(ret_filename, rename_to)
		# for removing
		elif operation == 2:
			success = colored("\nRemoving: " + ret_filename, "green")
			print(success)
			os.remove(ret_filename)
	else:
		err_msg = colored("\nFile " + ret_filename + " does not exist", "red")
		print(err_msg)

	if os.path.isfile(reg_filename):
		# for renaming
		if operation == 1:
			rename_to = dest_dir + "/" + size + "/" + new_filename + "." + new_extension
			success = colored("\nRenaming:\n(from) :: " + reg_filename + "\n( to ) :: " + rename_to, "green")
			print(success)
			os.rename(reg_filename, rename_to)
		elif operation == 2:	
			success = colored("\nRemoving: " + reg_filename, "green")
			print(success)
			os.remove(reg_filename)
	else:
		err_msg = colored("\nFile " + ret_filename + " does not exist", "red")
		print(err_msg)
