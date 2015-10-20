import os, os.path, itertools

vcf_location = "/mnt/Data4/working_directory/stuart/python-2-7-10/scripts/platypus/variants/"

with open("m.3243A>G_filtered", "a") as out_file:
	list_of_files = os.listdir(vcf_location)
	open_first = open(vcf_location + list_of_files[0], "r")
	with open_first as text_file:
		for line in itertools.islice(text_file, 47, 48):
			out_file.write("Sample_ID\t" + line)

for filename in os.listdir(vcf_location):
	with open(vcf_location + filename, "r") as file, open("m.3243A>G_filtered", "a") as out_file:
		sample_ID = filename.strip('platypus_m.3243A')
		for line in file:
			if line.startswith("MT"):
#				print line
				columns = line.split()
#				print columns[1]
				if int(columns[1]) == 3243:
					out_file.write(sample_ID + "\t" +line)
#					out_file.write(filename + " " +line)


#file.close()
#out_file.close()					

# and columns[3] == "A" and colums[4] == "G":
		
		
		 	
