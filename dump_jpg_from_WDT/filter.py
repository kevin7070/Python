import glob
import shutil
import os

# change sourceFolderName
sourceFolderName = 'HuaweiSDTData'
# change sourceFolderName
outPutFolderName = 'WDT COMM Photo'

rootDir = 'C:\\Users\\Kevin\\Desktop\\test_folder\\' + sourceFolderName
os.chdir(rootDir)
print("Current working dir : %s" % os.getcwd())
site_folders = os.listdir()

for index in range(len(site_folders)):
    # processing folder name
    processing_folder = site_folders[index]
    print("Processing site folder: " + processing_folder)

    # make dir for new site_folder
    new_folder = 'C:\\Users\\Kevin\\Desktop\\test_folder\\' + \
        outPutFolderName + '\\' + site_folders[index]
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # move file with ext *.jpg to new folder
    for file in glob.glob(rootDir + '\\' + processing_folder + '\\' + '**\*.jpg', recursive=True):
        shutil.copy(file, new_folder)

    # report done
    print(processing_folder, "is done")
