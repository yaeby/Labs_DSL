# Open the input file for reading
with open('input.txt', 'r') as input_file:
    # Read all lines from the input file
    line = input_file.readline()
    print(line = input_file.readline)
    lines = input_file.readlines()
    print(lines)
# Open the output file for writing
with open('output.txt', 'w') as output_file:
    # Write each line to the output file
    for line in lines:
        output_file.write(line)
