import re
import argparse


#é horrível... mas funciona :)

def tableFormatter(data, lineWidth):
    #extracts "from" text
    pattern = '(FROM *\n*\[.*)'
    fromString = re.findall(pattern, data, flags = re.S)[0]

    data = data.replace("\n", "")
    data = data.replace(" ", "")

    #extracs fields
    pattern = '(.*(?=FROM))'
    data = re.findall(pattern, data, flags = re.S)[0]
    data = data.replace(' ', '')
    data = data.replace('\n', '')
    fields = data.split(',')

    #generates fields text
    for i, field in enumerate(fields):
        n = lineWidth - len(field)
        #if word is too big, defaults to word length
        if n < 0:
            n = 1
        for j in range(n):
            fields[i] = fields[i] + ' '
        fields[i] = fields[i] + F"as {field}"


    finalString = "LOAD\n"
    #inserts commas and spaces to fields except first
    for i in range(len(fields)-1):
        fields[i+1] = ",   " + fields[i+1]

    #inserts spaces only into first field
    fields[0] = "    " + fields[0]
    
    #generates final string
    for field in fields:
        finalString = finalString + field + "\n"

    finalstring = finalString + fromString

    
    return finalstring

def formatter(inputString, lineWidth):
    modifiedInput = inputString
    output = ""

    #inserts "LOAD" at the end so REGEX parces correctly
    modifiedInput = modifiedInput + "\nLOAD"

    #parces each table
    pattern = "(?<=LOAD).*?(?=LOAD)"
    tableList = re.findall(pattern, modifiedInput, flags = re.S)

    #formats each table
    for table in tableList:
        output = output + "\n" + tableFormatter(table, lineWidth)

    return output

def main():
    linewidth = 50
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--linewidth", help="Set line width. Default is 50.")
    args = parser.parse_args()

    if  args.linewidth:
        if  args.linewidth.isdigit():
            linewidth = int(args.linewidth)

    try:
        with open ("input.txt", "r") as f:
            inputString = f.read()
    except:
        print("Please create input.txt file")
        return
    
    try:
        output = formatter( inputString, linewidth)
    except:
        print("Input text could not be converted")
        return

    with open ("output.txt", "w") as f:
        f.write(output)

if __name__ == "__main__":
    main()