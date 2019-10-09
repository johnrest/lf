import os
import glob
import sys


# if (sys.argv[1].lower() == "--help") or (sys.argv[1].lower() == "--h"):
#     print("""
#         lf [List Files] tool.
#             Python script to generate a text file that recursively lists all 
#             folders and files in a directory.
#         Usage example:
#         python lf.py filename.txt
#         """)
#     sys.exit()    

# filename = sys.argv[1]

filename = "list.txt"

target_dir = os.path.normpath(r"D:/Projects/lf/test/")

nodes = glob.glob(os.path.join(target_dir, "**"), recursive=True)
# for node in nodes[1:]:
#     # print(node)
#     # print(os.path.isdir(node), os.path.isfile(node))
#     print(os.path.split(node))

all_dirs = [target_dir]

with open( os.path.join(target_dir, filename), "w", encoding='utf-8') as f:
    f.write(target_dir + ":\n")
    buffer_parent_dir = target_dir
    for node in nodes[1:]:
        if os.path.isdir(node):
            parent_dir, child_dir = os.path.split(node)
            print(parent_dir, child_dir)
            if len(buffer_parent_dir) < len(parent_dir):
                all_dirs.append(parent_dir)
                buffer_parent_dir = parent_dir
            
            indent_carry = all_dirs.index(parent_dir)+1           

            f.write("└" + indent_carry*4*"-" + child_dir + "\n")

        if os.path.isfile(node):
            parent_dir, child_file = os.path.split(node)
            if len(buffer_parent_dir) < len(parent_dir):
                all_dirs.append(parent_dir)
                buffer_parent_dir = parent_dir

            indent_carry = all_dirs.index(parent_dir)+1
            f.write((indent_carry*4+1)*"-" + child_file + "\n")

