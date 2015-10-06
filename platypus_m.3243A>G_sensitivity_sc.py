#import the relevant modules
import subprocess #this will be used to get the operating system (Linux Scientific) to execute a command (as opposed to python doing it)


#assign the following variables:
#path to the platypus variant caller
platypus_path  = "usr/share/platypus/Platypus_0.8.1/" 

#path to the reference sequence
build_37_ref  = "/mnt/Data1/resources/human_glk_u37.fasta" 

#interval file for the m.3243A>G mutation with 25bp either side 
#because only looking at a single region there is no need to create an interval list
interval_mtDNA = "chrM:3209-3249"

#base path to where the script is being run from and the files are being saved/output
base_path = "/mnt/Data4/working_directory/stuart/python-2-7-10/scripts/platypus"

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

command  = "python platypus_path callVariants --bamfiles=path_to_bam_ files #include here all the relevant arguments required for platypus to work see platypus docs

subprocess.call(command)


