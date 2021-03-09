#   IMGHash by Robert Sammataro
#   Built with the ImageHash library
#
#   Version 0.1.2
#   Build Date 9 March 2021
#
#   github.com/robertsammataro/IMGHash

from PIL import Image
import imagehash
import os
import shutil
import time

def run_hash_scan(filepath):
    
    ### Scans through all .jpg and .png files in the specified filepath. Duplicates will be stored in the
    ### same folder in the subdirectory filepath/Quarantine/~ . Status messages will be sent to the terminal.
    ###            
    ### str filepath: String value representing the filepath of the folder that will be scanned.
    
    path = filepath
    hashes = []
    paths = []
    flags = []
    
    if not path.endswith("\\"):
        path = path + "\\"
    
    quar_path = path+"Quarantine\\"


    #Populates the hashes[] and paths[] lists
    
    for file in os.listdir(path):
        if file.endswith(".png") or file.endswith(".jpg"):
            paths.append(path+file)
            hashes.append(str(imagehash.average_hash(Image.open(path+"\\"+file))))
            
        
    #Populates the flags[] list with duplicate hashes. Tacks on it's corresponding filepath
    
    count = 0
    for item in hashes:
        if(hashes.count(item) > 1):
            flags.append(hashes[count]+"|"+paths[count])
        count += 1

    for item in sorted(flags):
        print(item)
        
        if not os.path.exists(quar_path):
            os.makedirs(quar_path)
            
        if not os.path.exists(quar_path+item.split("|")[0]):
            os.makedirs(quar_path+item.split("|")[0])

        shutil.move(item.split("|")[-1], quar_path+item.split("|")[0]+"\\"+item.split("\\")[-1])

def single_dir_scan_boot():
    
    ### Receives filepath from user and calls the run_hash_scan() function on JUST the specified filepath
    
    print("\nFile Path")
    inp = input()
    
    if os.path.exists(inp):
        run_hash_scan(inp)
        
    else:
        print("The path specified could not be located. Check your spelling and try again.\n")
        single_dir_scan_boot()


def multi_dir_scan_boot():
    
    ### Receives filepath from user and calls the run_hash_scan() function on JUST THE IMMEDIATE SUBDIRECTORIES of the specified filepath.
    ###
    ### For example, if the user enters the desired filepath as C:\Users\USERPROFILE\Documents:
    ###        - C:\Users\USERPROFILE\Documents\Images                    WOULD be scanned
    ###        - C:\Users\USERPROFILE\Documents\Images\Images_Subfolder   WOULD NOT be scanned
    ###        - C:\Users\USERPROFILE\Documents                           WOULD NOT be scanned
    
    print("\nParent Directory Path:")
    inp = input()
    
    if not inp.endswith("\\"):
        inp += "\\"
    
    if(os.path.exists(inp) and os.path.isdir(inp)):
        
        for item in os.listdir(inp):
            
            if(os.path.isdir(inp+item)):
                
                run_hash_scan(inp+item)
                
        print("Successfully scanned for duplicates in the following subdirectories:",inp+"\\"+str(os.listdir(inp)))
                
    else:
        print("The path specified could not be located. Check your spelling and try again.\n")
        multi_dir_scan_boot()

def main():
    
    ### Prompts the user to select a mode and sends them to the appropriate setup function
    
    print("\nWhich mode would you like to run in?\n\nTo scan ONE specified subdirectory, enter 1\nTo scan THE IMMEDIATE SUBDIRECTORIES of a specified directory, enter 2")
    choice = input()
    
    if(choice == "1"):
        single_dir_scan_boot()
    
    elif(choice == "2"):
        multi_dir_scan_boot()
        
    else:
        print("Your Selection Is Invalid. Check Your Spelling and Try Again\n")
        main()


if __name__ == "__main__":
    
    ### Shows program version information and sends users to main function to determine which mode the scan should run in
    
    print("IMGHash: Visual Image Sorter\nPowered by ImageHash\nVersion 1\n©2021 Robert Sammataro\n\n")
    main()