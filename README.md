# bassmaker
Simple script for writing DPCM instrument data to Famitracker .ftis.

# Features
Currently, this tool only allows for writing DPCM sample index, sample pitch, and note data to an .fti file (without the samples). Mostly useful for setting up templates for melodic DPCM instruments, such as bass instruments (ala Sunsoft). This is in an attempt to make it more convenient to make the same kind of instrument multiple times using different audio samples, since Famitracker doesn't allow you to automatically replace all instances of one sample with another one in the DPCM instrument settings. 

# Todo
Will be implementing a system for reading an audio file and directly writing sample audio data to the .fti file so that you don't also have to import your samples in Famitracker before you can use the output instrument.

# How to Use

First, write the template for your DPCM instrument in the note_data.txt file. 

Every line in the .txt file has data for three numerical parameters (in this exact order): note, sample index, and sample pitch. Notes have values from 0 (C-0), to 95 (B-7). Sample indices correspond to the # section of the "Loaded samples" section of the instrument editor. Assuming no samples have been loaded in your module, if you import sampleA, sampleB, and sampleC in that order, the corresponding indices for them are 1, 2, and 3 respectively. Finally, pitch just describes the DPCM sample pitch. This value can range from 0 to 15. 

Make sure to assign your own indices for each sample you intend to use before writing anything, and make sure these indices are in order starting from 1. Every line must be written in ascending order relative to the note data. 

Run the bassmaker.py script and call main(). Once complete, you load Famitracker and (in a new project) import the samples in order of the indices you assigned to each into a blank instrument. Load the resulting .fti, and all the imported samples should automatically be mapped to the settings you outlined in note_data.txt. 

The default note_data.txt file houses the instrument settings for the standard bass instrument in various Sunsoft games (e.g. Gimmick!, Journey to Silius). You can test the program out by using 5 different melodic samples of your choosing tuned to D-3 (146 hz), C#3, C-3, B-2, A#2. Output the default .fti, load these 5 samples in their respective order (in a new project), and then load the .fti to get your own bass instrument using the same tunings.

# Bugs

- Famitracker doesn't seem to like the way the sample index 0 gets written to the .fti with this program. When 0 is used as a sample index in the .txt, the sample you assign to index 0 will simply not be mapped to any of the rows whose sample index is 0. Sample indices are supposed to be zero-indexed, which is why this is a bug. 
- A blank sample will get imported when you load the output .fti. Does nothing and can be easily removed. 
