import os
import shutil



#the path of the dounload folder
Dounload_path = r"C:\Users\hp\Downloads"
#All popular image extensions
ImagesExensions = [".png",".jpeg",".jpg",".svg",".gif"]
#All popular sound extensions
SoundExtensions = [".mp3", ".wav"," .aac",".flac"]

#for every items in dounloads
for filename in os.listdir(Dounload_path):
    #Creates a variable named filepath that stores the path of files
    filepath = os.path.join(Dounload_path,filename)
    # if it leads to dir then its folder if not then its file
    # we just ingore folders by directly continuing if any folder is seen in the dounloads
    if os.path.isdir(filepath):
        continue
    #Splits the extension
    #Gets the extension part by using 1 index
    #lowers the part for accurate comparision
    fileExtension = os.path.splitext(filepath)[1].lower()

    #if its in ImagesExtemion
    if (fileExtension in ImagesExensions):
        destination = os.path.join(Dounload_path,"Images")
    #if its in SoundExtension
    elif (fileExtension in SoundExtensions):
        destination = os.path.join(Dounload_path,"Sounds")
    else:
        destination = os.path.join(Dounload_path, "Others")
    #Creating New Folders if it doesnt exists
    #if it exists then we dont make
    os.makedirs(destination,exist_ok = True)

    #The path to move the file to
    NewPath = os.path.join(destination,filename)
    #Moves the files 
    shutil.move(filepath,NewPath);