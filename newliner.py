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
string      = file.read()
file.close()

file = open(argv[2] if argc >= 3 else inputfile, 'w')
file.write(string.replace(';', '\n'))
file.close()
