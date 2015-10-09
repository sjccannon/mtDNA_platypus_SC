#import the relevant modules
import subprocess #this will be used to get the operating system (Linux Scientific) to execute a command (as opposed to python doing it)

#assign the following variables:
#path to the platypus variant caller
platypus_path  = "usr/share/platypus/Platypus_0.8.1/" 

#path to the reference sequence
build_37_ref  = "/mnt/Data1/resources/human_glk_u37.fasta" 

#path to bam files without specific sample
path_to_bam = "/mnt/Data4/targeted_sequencing/"

#interval file for the m.3243A>G mutation with 25bp either side 
#because only looking at a single region there is no need to create an interval list
interval_mtDNA = "chrM:3209-3249"

#base path to where the script is being run from and the files are being saved/output
base_path = "/mnt/Data4/working_directory/stuart/python-2-7-10/scripts/platypus"

#create a dictionary of sample = bam file of the 671 samples required to be tested
#Initially using the manually created subset of samples just from the MODY panel

#Constructiong a dictionary of sample number as key and the path to appropriate bam file as the value
for line in MODY_subset_infile:
	line.split()
	use regular expression to infer the location of the bam file based on the column 1 if it contails a 'P' 
	# if it c is part of the old version numbers. 
		if column 0 has a 'p' in it:
			assign column 0 to variable 'p_sample_number'
			extract the numerical sample number values by taking the last three digits, turn to an integer and assign to 'p_numeric_sample_number'
			if P_numeric_sample_number is between 1 and 48:
				additional path = 'P5_001-048/assembly/'
				bam_file_name = 'P5_001-48_' + str(p_numeric_sample_number) + '.realigned.sorted.bam'
				dictionary key == 'p_sample number', dictionary value == path_to_bam + additional path + bam_file_name 
			elif sample number is  49 and 96:
					sdditional_path = 
					bam_file_name = 
					dictionary_key == 
				dictionary key = sample number, dictionary valus = this path to bam file
			elif sample number is between 97 and 132
		elif column 0 has a 'v5' in it:
			
# for 	

#loop through each dictionary entry and initiate Platypus calls on it

#as the infile:
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

command  = "python platypus_path callVariants --bamfiles=path_to_bam_ files #include here all the relevant arguments required for platypus to work see platypus docs

subprocess.call(command)


