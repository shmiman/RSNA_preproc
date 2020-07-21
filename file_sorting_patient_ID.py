# Imports
import csv
import os

# List directories
SOURCE_ROOT = 'stage_2_train'
DEST_ROOT = 'train'

# Move files
with open('train_metadata.csv') as infile:
    next(infile)  # Skip the header row
    reader = csv.reader(infile)
    seen = set()
    for SOPInstanceUID, StudyInstanceUID in reader:
        # Create a new directory if needed
        if StudyInstanceUID not in seen:
            os.mkdir(os.path.join(DEST_ROOT, StudyInstanceUID))
            seen.add(StudyInstanceUID)

        src = os.path.join(SOURCE_ROOT, SOPInstanceUID + '.dcm')
        dest = os.path.join(DEST_ROOT, StudyInstanceUID, SOPInstanceUID + '.dcm')

        try:
            os.rename(src, dest)
        except WindowsError as e:
            print (e)