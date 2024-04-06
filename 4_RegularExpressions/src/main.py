from regex_class import Regex 

if __name__ == "__main__":

    #Create an regex object
    obj = Regex()

    #Read the regexes from in input.txt
    with open('input.txt', 'r') as input_file:
        regexes = input_file.readlines()

    #Write the generated strings in output.txt
    with open('output.txt', 'w') as output_file:
        for regex in regexes:
            output_file.write("\nGenerated strings for regex '" + regex.strip() + "' :\n") 
            for i in range(0, 5):
                output_file.write(obj.generate_string(regex) + '\n')

    #Step by step processing of a regex
    obj.process_regex(regex=regexes[8])