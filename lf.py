import os
import glob
import sys


if (sys.argv[1].lower() == "--help") or (sys.argv[1].lower() == "--h"):
	print("""
		lf [List Files] tool.
			Python script to generate a text file that recursively lists all 
			folders and files in a directory.
		Usage example:
		python lf.py filename.txt
		""")
	sys.exit()	

filename = sys.argv[1]

directories = glob.glob(os.path.join(os.getcwd(), "*/"))

#for item in directory_list:
#    file_list = glob.glob(os.path.join(item, "*"))
#    print(*file_list, sep='\n')
    
with open( os.path.join(os.getcwd(), filename), "w") as f:   # Opens file and casts as f 
    for directory in directories:
        folder_name = directory.replace(os.getcwd(), "")
        f.write(folder_name + "\n")
        files = glob.glob(os.path.join(directory, "*"))
        for file in files:
            filename = os.path.basename(file)
            f.write("\t->" + filename + "\n")
