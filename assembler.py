import sys
from os import listdir
##define the opcode table
OPCODES = {
    "ADD": "00",
    "SUB": "10",
    "LDR": "01",
    "STR": "11"
}

#define register codes
REGISTERS = {
    "X0": "00",
    "X1": "01",
    "X2": "10",
    "X3": "11"
}

#function to put all instructions into a list
def getInstructionList(file):
    file = open(file) ##open assembly file 
    start = False ##boolean indicator for when the instructions have started to be read 
    instructions = [] ##list to store instructions 
    while True: ##read file line by line
        content=file.readline()
        if not content:
            break
        if content==".data\n": ##if we reach the end of the instructions, break out of loop
            break
        if start==True: ##if we are still reading instrcutions, append it to the list
            content = content.strip() ##clearing whitespace
            if(content!=""): ##if instruction line is non-empty, append to list
                instructions.append(content)
        if content=="_start:\n": ##if instructions have started to be read, mark boolean start to True
            start = True    
    file.close()
    return instructions

##function to retreive data elements and put into list
def getDataList(file):
    file = open(file)
    data = [] ##list to store data elements
    start = False ##boolean indicator for if data is being read or not
    while True: ##loop to read file
        content = file.readline()
        if not content:
            break
        if start == True: ##if data is being read, append to list
            content = content.strip() ##clear whitespace
            if(content!=""): ##if data is non-empty, append to the list
                data.append(content)
        if content == ".data\n": ##if data is starting to be read, mark boolean start to True
            start = True
    file.close()
    return data

##function to convert instructions to hex
def convertInstructions(file):
    instructions = getInstructionList(file) ##stores string instructions
    hexInstructions = [] ##list to store hex version of the instructions
    for instruction in instructions:
        ##split up the instruction by operation and registers
        operation = instruction.split()[0]
        reg1 = instruction.split()[1]
        reg2 = instruction.split()[2]
        reg3 = instruction.split()[3]
        
        ##retreive opcodes and concatenate to get instruction in binary
        opcode = OPCODES.get(operation)
        opcode += REGISTERS.get(reg1)
        opcode += REGISTERS.get(reg2)
        opcode += REGISTERS.get(reg3)
       
        ##convert binary instructiont to hex and add to list
        opcode = int(opcode,2)
        opcode =format(opcode, '02x')
        hexInstructions.append(opcode)
        
    ##add 00 instructions to list for any empty entries in the 16x16
    fill = "00000000"
    fill = int(fill,2)
    fill = format(fill, '02x')
    while len(hexInstructions) < 256:
         hexInstructions.append(fill)
    return hexInstructions
    
##function to convert data to hex values
def convertData(file):
    data = getDataList(file)
    dataHex = []
    for d in data:
        ##convert data element to hex and append to dataHex list
        d = int(d)
        d = format(d, '02x')
        dataHex.append(d)
    
    ##add 00 instructions to list for any empty entries in the 16x16
    fill = "00000000"
    fill = int(fill,2)
    fill = format(fill, '02x')
    while len(dataHex) < 256:
         dataHex.append(fill)
    return dataHex

##function to create an image file for instructions and data for logism
def create_image_file(instructions, output_file):
    count = 0 ##indicates which element of the row we are in so we know when to increment address and get 16 new values
    address = 0x00 ##starting memory address
    count2 = 0 ##used to help index the slicing
    left = 0 ##used to index the slicing
    
    with open(output_file, 'w') as outfile:
        outfile.write("v3.0 hex words addressed\n") ##image file header
        
        ##this loop takes 16 elements at a time and inserts into image file (it iterates 1 at a time so we use count to manipulate it)
        for instruction in instructions:
            count+=1 ##update row element count
            if count == 16: ##if we are on the last element in the row, reset the count and increment address
                count = 0
                address += 16  #increment address by 16
            if(count!=1): continue  ##if we are not at a new row (first element), skip this iteration
            
            ##slice instructions list to get 16 elements at a time to fill row by row
            count2 += 1 ##increment count if code reaches here (essentially indicates the current row)
            right = count2*16 ##calculate rightbound
            current = instructions[left:right] 
            left = right ##update leftbound
            
            ##convert 16 list elements into a string, seperated by a space
            string = ""
            for c in current:
                string += c
                string += " "
            
            #write the 16 values to the image file with the corresponding starting address 
            outfile.write(f"{address:02x}: {string}\n")



def findFile():
    # open the assembly file
    found = False
    file = ""
    for file_name in listdir():
        # check if the file is a '.lim' file
        if file_name[-4:] == ".lim":
            file = file_name
            found = True
    return found, file


def main():
    found, file = findFile()
    if found:
        instruction_file = "instructions"
        create_image_file(convertInstructions(file), instruction_file)
        print(f"Instruction image file saved as {instruction_file}.")

        data_file = "data"
        create_image_file(convertData(file), data_file)
        print(f"Data image file saved as {data_file}.")
        return 0  #normal termination
    else:
        print("Assembly file not found. Exiting program.")
        return 1  #error termination


if __name__ == "__main__":
    sys.exit(main())



