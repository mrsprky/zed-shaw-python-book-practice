## Here in this practice I am writing code for a making a copy of file with python. First we take the name of the file that we will copy and the file name for the copied file. We take the names via argument variable through sys moudule's argv function
# We will also check the file name to see that the file exist or not from os.path moudules exists function

# importing modules that we are going to use
from sys import argv
from os.path import exists # this return True or False based on files existence



script, input_file , output_file = argv # unpacking the variable that we will be using as argument variable

 # Displaying user what we are going to copy to which file
print(f"Copying from {input_file} to {output_file   }")

# opeing the file in this code 
in_file = open(input_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long")

print(f"Does the output file exist? {exists(output_file)}")

# giving the user a chance to stop or continue
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(output_file, 'w')
out_file.write(in_data)

print("Alright, all done")


# closing the file to avoid further problems
out_file.close()
in_file.close()
