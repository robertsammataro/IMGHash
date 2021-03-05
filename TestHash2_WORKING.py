from PIL import Image
import imagehash
import os
import shutil
import time

def run_hash_scan(filepath):
    path = filepath
    
    if not path.endswith("\\"):
        path = path + "\\"
    
    quar_path = path+"Quarantine\\"

    hashes = []
    paths = []
    flags = []

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


    if not os.path.exists(quar_path):
        os.makedirs(quar_path)


    for item in sorted(flags):
        print(item)
            
        if not os.path.exists(quar_path+item.split("|")[0]):
            os.makedirs(quar_path+item.split("|")[0])

        shutil.move(item.split("|")[-1], quar_path+item.split("|")[0]+"\\"+item.split("\\")[-1])

def boot_into_scan():
    print("File Path\n>")
    inp = input()
    
    if os.path.exists(inp):
        run_hash_scan(inp)
        
    else:
        print("The path specified could not be located. Check your spelling and try again.")
        boot_into_scan()


if __name__ == "__main__":
    print("IMGHash: Visual Image Sorter\nPowered by ImageHash\nVersion 1\n©2021 Robert Sammataro\n\n")
    boot_into_scan()