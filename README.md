# IMGHash
 Automated Python Script to Sort Visually Similar Images

How it works:
    This script is powered by the wonderful imagehash library, which generates
    a unique hash value for all .png and .jpg images in a specified directory.

    When prompted, enter the directory which you would like to sort (please note
    at this time IMGHash does not search recursively). IMGHash will then sort
    the images in the specified directory and place copies in the "Quarantine"
    subfolder, which users can manually go through and remove any duplicate
    copies

    The hashing algorithm isn't perfect, and does on occasion miss similar
    images. This will try to be remedied in future releases

Future Updates:
    1. Implement an algorithm to check for hash values that are off by only
       a few characters
    2. Using TKinter develop a GUI to make sorting flagged images easier

Contact & Credits:

    IMGHash ©2021 Robert Sammataro
          robbysam@udel.edu

    imagehash library by Johannes Buchner
