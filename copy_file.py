from sys import argv
#from os.exists import exists

script, file_name, file_out = argv

infile = open(file_name)
print "Opening %s" % file_name

outfile = open(file_out, 'w')
print "Creating %s" % file_out

in_data = infile.read()
outfile.write(in_data)
print "Writing data..."

infile.close()
outfile.close()
print 'Done.'
