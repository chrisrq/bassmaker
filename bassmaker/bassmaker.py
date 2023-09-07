import struct

output_directory =  "output\\output.fti"

note_data_dir = "note_data.txt"

header = "FTI"
ver = "2.4"


def main():
    output = open(output_directory, "wb")
    input = open(note_data_dir, "r")
    setup_write(output)
    init_sequences(output)

    readwrite_input_data(input, output)
    
    output.close()

    print("Finished writing DPCM instrument.")

def setup_write(output):
    writebytes(output, header)
    writebytes(output, ver)
    writeint8(output, 1)
    writestring(output, "output")

# Part of initializing 2A03 instrument with DPCM,
# initialize all instrument sequences to be empty.

def init_sequences(output):
    writeint8(output, 5)
    writeint8(output, 0)
    writeint8(output, 0)
    writeint8(output, 0)
    writeint8(output, 0)
    writeint8(output, 0)

# Write one section of the "Assigned samples"
# portion of the DPCM instrument manager to the FTI.

def write_sm_data(output, note, sample, pitch, delta=0):
    writeint8(output, note)
    writeint8(output, sample + 1)
    writeint8(output, pitch)
    writeint8(output, delta)

# Takes in an input file with the DPCM configuration data,
# writes it to the output FTI file.
def readwrite_input_data(input, output):
    maxSampleIndex = 0
    allDataInFile = []
    note_count = 0
    while True:
        
        read = input.readline()
        
        if read == "\n":
            writeint32(output, note_count)

            for dataPiece in allDataInFile:
                print(dataPiece)
                write_sm_data(output, dataPiece[0], dataPiece[1], dataPiece[2])

            writeint32(output, maxSampleIndex + 1)
            break;
        
        parsedData = [int(s.rstrip('\n')) for s in read.split(" ")]
        allDataInFile += [parsedData]
        
        maxSampleIndex = max(parsedData[1], maxSampleIndex)
        note_count += 1
        
    input.close()
    return

def write_dpcminst_settings(output):
    # sample count
    writeint32(output, 41)
    return

# section: .fti write functions

def writestring(output, string):
    writeint32(output, len(string))
    writebytes(output, string)

def writeint32(output, value):
    output.write(structconvert(value))
    output.write(structconvert(value >> 8))
    output.write(structconvert(value >> 16))
    output.write(structconvert(value >> 24))

def writebytes(output, string):
    output.write(bytes(string, 'utf-8'))

def writeint8(output, value):
    output.write(structconvert(value))

# end section

def structconvert(value):
    return struct.pack("B", value)

#section: tests

test_complete = "Test completed."
test_directory = "output\\test.fti"
    
def write_sm_data_test():
    output = open(test_directory, "wb")
    setup_write(output)
    init_sequences(output)
    
    sample_index = 0
    delta = 0

    writeint32(output, 1) # sample count

    write_sm_data(output, 22, sample_index, 15)

    writeint32(output, 1) # write used count
    output.close()

    print(test_complete)

def open_read_test():
    test = open("readtest.txt", "r")
    print(test.readline())
    print(test.readline())

# end section

    
    

    
