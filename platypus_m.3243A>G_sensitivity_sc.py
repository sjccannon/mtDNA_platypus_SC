#assign the following variables:
#path to the platypus variant caller
platypus = 

#path to the reference sequence
reference_build_37 = 

#interval file for the m.3243A>G mutation with 100bp either side 
interval_mtDNA = 

#base path to where the script is being run from and the files are being saved/output
base_path = 

#create a dictionary of sample = bam file of the 671 samples required to be tested
#Initially using the manually created subset of samples just from the MODY panel


#loop through each dictionary entry and initiate Platypus calls on it

#using filex.csv as the infile:
#for each line in infile:
#	line.split()
#	if "MODY" is in column[10] and "NDM is not in column(10):
#		do function #initiate variant caller
#	else:
#		do other function

#create a variable that contains sample_id as a string

#create a vcf output file path consisting of: 
vcf_output = base_path + "/variants/" + sample_id + "platypus_m.3243A>G.vcf"

#to use platypus I am going to get the operating system to excecute a bash script. I could do this using the code below but with arguments designed for Platypus




