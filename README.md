## IMGHash v0.1.2  
 Automated Python Script to Sort Visually Similar Images  
 Build Date: 9 March 2021  

### How it works:
  This script is powered by the wonderful imagehash library, which generates
  a unique hash value for all .png and .jpg images in a specified directory.

  When prompted, enter the directory which you would like to sort (please note
  at this time IMGHash does not search recursively). IMGHash will then sort
  the images in the specified directory and place copies in the "Quarantine"
  subfolder, which users can manually go through and remove any duplicate
  copies

  The hashing algorithm isn't perfect, and does on occasion miss similar
  images. This will try to be remedied in future releases

### Future Updates:
  1. Implement an algorithm to check for hash values that are off by only
       a few characters
  2. Using TKinter develop a GUI to make sorting flagged images easier

### Changelog:  

#### 9 March 2021 v0.1.2:  

    - Cleaned some code so a Quarantine folder would not be generated if there
      were no similar images in the directory being scanned.  

    - Reformatted README with markdown

#### 6 March 2021 v0.1.0:  

    - Added new function allowing the user to scan the immediate subdirectories
      of the specified filepath.

    - Added new main() function which prompts the user to specify which mode
      they would like to run the program in --> Perhaps down the road it can
      be written to show the first 3 or so folders that would be run in a
      subdirectory scan

### Contact & Credits:  

IMGHash ©2021 Robert Sammataro  
robbysam@udel.edu  

imagehash library by Johannes Buchner
