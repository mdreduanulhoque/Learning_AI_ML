"""
"r"    -    Read only (default)
"w"    -    Write only (creates file or overwrites existing content)
"a"    -    Append (adds data to the end of the file)
"x"    -    Create a new file (error if file exists)
"a+"   -    Append + Read
"r+"   -    Read + Write
"w+"   -    Write + Read
"b"    -    Binary mode
"""

f = open("D:/AAAAAAAAAAAAAAA/Learning_AI_ML/python_part_5/sample.txt", "a")
f.writelines("\nAdded new lines\nby write functionality")
f.close()
