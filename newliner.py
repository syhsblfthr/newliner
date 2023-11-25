import sys
import io
import os

def print_usage():
    script_full_name    = __file__
    rmost_delimiter     = script_full_name.rfind(os.sep)
    script_name         = script_full_name[((rmost_delimiter + 1) if rmost_delimiter else 0) : None]
    sys.exit(str.format("Usage\n\tpy {0} INPUT_FILE [OUTPUT_FILE]", script_name))

if __name__ == '__main__':
    argv            = sys.argv
    argc            = len(argv)
    string          = None
    string_input    = None
    file_handle     = None

    if argc <= 1:
        print_usage()

    flag = argv[1]
    if not flag.startswith('--'):
        flag = None

    input_file  = argv[2 if flag else 1]

    output_file = None
    if not flag and argc >= 3:
        output_file = argv[2]
    elif flag and argc >= 4:
        output_file = argv[3]

    if flag and flag.lstrip('--').lower() == 'f':
        file_handle = open(input_file, 'r')
        string      = file_handle.read().replace(';', '\n')

        file_handle.close()
    else:
        string = input_file.replace(';', '\n')

    if output_file:
        file_handle = open(output_file, 'w')

        file_handle.write(string)
        file_handle.close()
    else:
        print(string)
