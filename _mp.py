original_open = open

import sys
import traceback

# modes:
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# 'U'       universal newline mode (deprecated)

def open(file, mode='r', *args, **kwargs):
    if file.startswith("/tmp/") and any(c in mode for c in "wxa+"):
        print("opening", file, file=sys.stderr)
        sys.stderr.writelines(traceback.format_list(traceback.extract_stack()[:-1]))
    return original_open(file, mode, *args, **kwargs)


__builtins__['open'] = open
