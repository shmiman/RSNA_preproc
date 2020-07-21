This script intends to fix some issues with the RSNA ICH Kaggle dataset to be able to use the dataset for conversion from DICOM to NIfTI files for further work to be done in this format (e.g. 3D analysis of brain CT scans)
The script is written in R and python in 2 steps

The intention of the python script (file_sorting_patient_ID.py) is to sort the DICOM files into folders which represent the studyIDs of each DICOM scans allowing the proper conversion of the files.
This script uses the metadata file to sort out each indiviudual image.
Directories required to be changed for the use to direct it to the correct folder on your machine 

The intention of the R script (scriptr.txt) is to pass through the files in each sorted folder and sort them in order of their z-axis, as due to the scrubbing of the metadata for the challenge, some information in the DICOM header is not 'standard' as if the scan was obtained directly from the scanner.
This results in inconsistent results if the scans were passed through the conversion after such as first slice of the image being out of position.
Directories required to be changed for the use to direct it to the correct folder on your machine

Thanks to muschellij2 and neurolabusc on this thread https://github.com/rordenlab/dcm2niix/issues/341 for the information needed to solve this problem.
