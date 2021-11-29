# UIUC_CS_545

Put test.py and update_library.py under the same directory.

Create a new folder called "source" to store all songs used to build the library. 
  - The program will automatically convert mp3 files to wav files.
  - To add new songs to the library, simply copy the files to "source" folder and rerun update_library.
  
 Create a new folder named "test" to store all test samples.
  - Here all the test samples must be WAV files (because I forgot to wrote the conversion functionalities)
  - After you run the test.py, it will prompt you to select the test mode.
    - "one" to get the prediction of a specific sample (The program will then prompt you to enter the path for that file).
    - "multi" to get the predictions of all test samples under a directory and calculate accuracy (The program will then prompt you to enter the directory, in our case, "test").
  - NOTICE: For the test program to work correctly, the name for each test sample MUST BE THE SAME as its corresponding file name in the library. If the library does not contain the test sample, simply name it "None.wav" or something that does not exist in the library.
  
 
    
