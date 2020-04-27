import tinify
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
# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--apikey", "-a", help="set tinypng API Key")

# Read arguments from the command line
args = parser.parse_args()

# Check for --width
if args.apikey:
    tinify.key = args.apikey  # API Key
else:
	sys.exit("No API Key")

source_dir = "RawImages"
dest_dir = "images"
# Map out images sizes and destination subdir names
sizes = {
	'small':320,
	'medium': 768,
	'large':1024,
	'xlarge': 1280
}

# Create a list of images from source directory
# Include all popular/normal file types
source_files = glob.glob(source_dir + '/*.jpg')
source_files.extend(glob.glob(source_dir + '/*.png'))
source_files.extend(glob.glob(source_dir + '/*.jpeg'))

if not source_files:
	sys.exit("No Images Found")

# Iterate through the images
for img in source_files:
	source = tinify.from_file(img)
	# Capture the image file without a path
	img_file = os.path.basename(img)

	# Capture the filename without the extension
	img_filename = os.path.splitext(img_file)[0]

	# Capture the file extension
	img_extension = os.path.splitext(img_file)[1]

	print "Generating Images for: " + img_filename

	# Iterate through image sizes for each break point
	for size in sizes:
		# Resize images based on width (assumes landscape)
		try:		
			resized = source.resize(
	    		method="scale",
	    		width=sizes[size]
			)

			# For each of the sizes, resize for retina screens
			resized_retina = source.resize(
	    		method="scale",
	    		width=sizes[size] * 2
			)

			# Resize and save to the appropriate size-named subdirs
			resized.to_file(dest_dir + "/" + size + "/" + img_filename + img_extension)
			resized_retina.to_file(dest_dir + "/" + size + "/" + img_filename + "_2x" + img_extension)

			print "Images generated successfully"
			# Remove file from source folder
			os.remove(img)
			print "Original image removed ( "+ img_file + " )"
  			pass
		except tinify.AccountError, e:
  			print "The error message is: %s" % e.message
  			# Verify your API key and account limit.
		except tinify.ClientError, e:
  			# Check your source image and request options.
  			print "Client Error: %s" % e.message
  			pass
		except tinify.ServerError, e:
  			# Temporary issue with the Tinify API.
  			print "Server Error: %s" % e.message
  			pass
		except tinify.ConnectionError, e:
  			# A network connection error occurred.
  			print "Network Connection Error: %s" % e.message
  			pass
		except Exception, e:
  			# Something else went wrong, unrelated to the Tinify API.
  			print "Unknown Error: %s" % e.message
  			pass