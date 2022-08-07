from contextlib import closing
import glob
import os
import sys
import time
import zipfile

# Did tests with lzma, bz2
# No considerable difference in output size
NUMBER_OF_FILES_IN_EACH_ZIP = 100
SCRIPT_DIR = os.path.dirname(__file__)


def compress_to_zip(files, target):
    with zipfile.ZipFile(target, 'w') as zipF:
        for file in files:
            zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)


def number_of_files_in_zip(file):
    if not os.path.isfile(file):
        return 0
    with closing(zipfile.ZipFile(file)) as zipF:
        count = len(zipF.infolist())
        return count


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


input_dir = os.path.join(SCRIPT_DIR, sys.argv[1])
output_dir = os.path.join(SCRIPT_DIR, sys.argv[2])

list_of_files = filter(os.path.isfile, glob.glob(input_dir + '/*'))
list_of_files = sorted(list_of_files, key=os.path.getmtime)

i = 0
for chunk_of_files in chunks(list_of_files, NUMBER_OF_FILES_IN_EACH_ZIP):
    output_file = os.path.join(output_dir, str(i) + ".zip")

    # Only replace if it's the last chunk
    if number_of_files_in_zip(output_file) != NUMBER_OF_FILES_IN_EACH_ZIP:
        compress_to_zip(
          chunk_of_files,
          output_file
        )

    print("Completed - " + output_file)
    i += 1
