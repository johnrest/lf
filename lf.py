import os
import glob
import sys


if (len(sys.argv) < 2) or (len(sys.argv) > 4) or (sys.argv[1].lower() == "--help"):
    print("""
         List Files (lf) tool.
             Python script that recursively lists all 
             subdirectories and files in a main directory.
             The representation is display in the console or written to a
             file
         Usage:
         python lf.py --help
         python lf.py dir [-f out_filename]
         """)
    sys.exit()    

target_dir = os.path.normpath(os.path.abspath(sys.argv[1]))

nodes = glob.glob(os.path.join(target_dir, "**"), recursive=True)

all_dirs = [target_dir]

folder_sym = "□ "

out = str()
out += folder_sym + target_dir + ":\n"

buffer_parent_dir = target_dir

for node in nodes[1:]:
    if os.path.isdir(node):
        parent_dir, child_dir = os.path.split(node)
        if len(buffer_parent_dir) < len(parent_dir):
            all_dirs.append(parent_dir)
            buffer_parent_dir = parent_dir
        
        indent_carry = all_dirs.index(parent_dir)+1           

        out += (indent_carry-1)*"\t" + "└" + 3*"-" + folder_sym + child_dir + "\n"

    if os.path.isfile(node):
        parent_dir, child_file = os.path.split(node)
        if len(buffer_parent_dir) < len(parent_dir):
            all_dirs.append(parent_dir)
            buffer_parent_dir = parent_dir

        indent_carry = all_dirs.index(parent_dir)+1
        out += (indent_carry-1)*"\t" + "└" + 3*"-" + child_file + "\n"

if (len(sys.argv) == 2):
    print(out)

if (len(sys.argv) > 2) and (sys.argv[2].lower() == "-f"):
    filename = sys.argv[3]
    with open( os.path.join(target_dir, filename), "w", encoding='utf-8') as f:
        f.write(out)
        print("Output to file: ", filename)
