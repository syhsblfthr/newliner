import sys
import io
import os

argv = sys.argv
argc = len(argv)
if (argc <= 1):
    script_full_name    = __file__
    rmost_delimiter     = script_full_name.rfind(os.sep)
    script_name         = script_full_name[((rmost_delimiter + 1) if rmost_delimiter else 0) : None]
    sys.exit(str.format("Usage\n\tpy {0} INPUT_FILE [OUTPUT_FILE]", script_name))

inputfile   = argv[1]
file        = open(inputfile, 'r')
output_file = open(inputfile if argc < 3 else argv[2], 'r+')
string      = file.read()
lastindex   = 0
stream      = io.StringIO()

file.close()

for index in range(0, len(string)):
    if (string[index] != ';'):
        continue

    stream.write(string[lastindex : index] + '\n')
    lastindex = index + 1
else:
    stream.write(string[lastindex:])

output_file.write(stream.getvalue())

output_file.close()
stream.close()
