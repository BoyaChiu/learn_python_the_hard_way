from sys import argv #import argv from system

script, input_file=argv #argv from input_file

def print_all(f): #print f.read()
    print f.read()

def rewind(f): #rewind f.seek()
    f.seek(0) #value=0

def print_a_line(line_count,f):
    print line_count,f.readline()

current_file=open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)
print "Let's print three lines: "

current_line=1
print_a_line(current_line,current_file) #run print_a_line

current_line=current_line+1 #run 2nd line
print_a_line(current_line,current_file)

current_line=current_line+1 #run 3rd line
print_a_line(current_line,current_file)
