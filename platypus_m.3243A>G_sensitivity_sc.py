#import the relevant modules
import glob, re, subprocess

#assign the following variables:
#path to the platypus variant caller
path_to_platypus  = "usr/share/platypus/Platypus_0.8.1/" 

#path to the reference sequence
build_37_ref  = "/mnt/Data1/resources/human_glk_u37.fasta" 

#path to bam file directories
path_to_P5_bam = "/mnt/Data1/targeted_sequencing/"
path_to_V5_bam  = "/mnt/Data4/targeted_sequencing/" #this also includes the old notation in the format P5_xyz where xyz are itegers

# assigning variable to be called by the command line with platypus.  m.3243A>G mutation with 25bp either side 
#because only looking at a single region there is no need to create an interval list
interval_mtDNA = "chrM:3209-3249"

#base path to where the script is being run from and the files are being saved/output
base_path = "/mnt/Data4/working_directory/stuart/python-2-7-10/scripts/platypus"

#createing regexs for different combinations of bam filename
format_P5 = re.compile('P5_\d_\d{1,3}')#matches samples in format P5_n_nnn
format_PorV = re.IGNORECASE('[Pv]\d+_\d+}') #includes samples in format v5_nnn, v501_nnnn, P5_nnn

#creating a dictionary look up
my_dict = {}

#Constructiong a dictionary of sample number as key and the path to appropriate bam file as the value
with open("test.csv", 'r') as in_file:
#with open("mitochondrial_sensitivity_MODY.csv", "r") as in_file:
	for line in in_file:
		columns = line.split()
		if format_P5.match(columns[0]): 
			sample_ID = columns[0]
			print sample_ID	
			ID_num = int(sample_ID[-3:])
			print ID_num
			bam_end = '.realigned.sorted.bam'

			if ID_num >= 1 and ID_num <= 9:
				additional_path = 'P5_001-48/assembly/'
				bam_file_name = 'P5_001-048_' + '00' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name 

			elif ID_num >= 10 and ID_num <= 48:
				additional_path = 'P5_001-048/assembly/'
				bam_file_name = 'P5_001-48_' + '0' + str(ID_num) + bam_end
				#append dictionary to include sample_ID as key and string of path to bam file
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name	

			elif ID_num >=  49 and ID_num <= 96:
				additional_path = 'P5_049_096/assembly/' 
				bam_file_name = 'P5_049-096_' + '0' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name 

			elif ID_num >= 97 and ID_num <= 99:
				additional_path = 'P5_097-144/assembly/'
				bam_file_name = 'P5_049-144_' + '0' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_paht + bam_file_name

			elif ID_num >= 100 and ID_num <= 144:
				additional_path = 'P5_097-144/assembly/'
				bam_file_name = 'P5_049-144_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name
		
			elif ID_num >= 145 and ID_num <= 216:
				additional_path = 'P5_145-216/assembly/'
				bam_file_name = 'P5_145-216_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

			elif ID_num >= 217 and ID_num <= 240:
				additional_path = 'P5_217-240/assembly/'
				bam_file_name = 'P5_217-240_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam +additional_path + bam_file_name

			elif ID_num >= 241 and ID_num <= 336:
				additional_path = 'P5_241-336/assembly/'
				bam_file_name = 'P5_241-336_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

			elif ID_num >= 337 and ID_num <= 384:
				additional_path = 'P5_337-384/assembly/'
				bam_file_name = 'P5_337-384_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

			elif ID_num >= 385 and ID_num <= 432: 
				additional_path = 'P5_385-432_run2/assembly/'
				bam_file_name = 'P5_385-432_' + str(ID_num) + 'realigned.sorted.merged.bam'
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

			elif ID_num >= 433 and ID_num <= 480:
				additional_path = 'P5_433-480/assembly/'
				bam_file_name = 'P5_433-480_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name
				
			elif ID_num >= 481 and ID_num <= 504:
				extra_path = 'P5_481-504/assembly/'
				bam_file_name = 'P5_481-504_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + extra_path + bam_file_name

			else:
				print 'error'

#print my_dict

#maybe redundant
#ascertaining how many digits the sample number contains so we can later extract the numerics from sample number from the 
#ID_num_3 = re.compile('*_\d{3}') 
#ID_num_4 = re.compile('*_\d{4}') 

#if the sample_ID matches the later panels this code finds the file location in Data4 based on the batch number and sample number and the deduced naming ocnventions within those files 
		elif format_PorV.match(columns[0]):
			sample_ID = str(columns[0])
			date_and_batch = str(columns[1])
			#take last 8 digits and assign to batch number
			batch_number = int(date_and_batch[-8:])
			if batch_number >= 1501266:
				path_to_bam_directory = path_to_v5_bam + date_and_batch.replace('.', '-', 2) + '/assembly/'
				for file in os.listdir(path_to_bam_directory):
					bam_pattern = sample_ID + '*.realigned.bam'
					if fnmatch.fnmatch(file, bam_pattern):
						complete_path_to_bam = path_to_bam_directory + file
						my_dict[sample_ID] = complete_path_to_bam

# This part may be redundant now because I'm using batch number as opposed to the numeric ID to locate the file
#			if ID_num_4.match(sample_ID):
#				ID_num = int(sample_ID[-4:])
#			elif ID_num_3.match(sample_ID):
#				ID_num = int(sample_ID[-3:])
#			else:
#				print 'ID error' + str(columns[0)]


		
#create a path to the directory using os.listdir

	for file in os.listdir('path_to_directory'):
		if fnmatch.fnmatch(file, 'pattern'):
			complete_path_to_bam = path_to_P5__bam + additional_path + file			
			my_dict[sample_ID] = complete_path_to_bam	
			
#		sample_ID = str(column0 last three digits) 
#		take column 1 and turn into a string
#		take last 8 digits and assign as int(batch_number)
#		if batch_number  >= 1501266: #the naming convention changes here to include the male/female aspect of the data. therefore need to work out how to alter the path including the filename
#			formatted_column_1 = replace full stops '.' with dashes '-' in column 1
#			additional_path = formatted_column_1 + '/assembly/'
#			for file_name in glob.glob(path_to_v5_bam + additional_path + sample_ID + '*realigned.bam') #need to make sure there is MODY in the title of the direct to the file containiing the sample number and 'realigned.bam'
#				dictionary key == sample_ID, dictionary value == file_name
#		else 	 		
#			
#		
#		 
#		if the last 8 digits (batch number) == 140383
#		additional_path = take column 1, turn into a string
#		
#	else:
#		print 'error with input file'
#
#loop through each dictionary entry and initiate Platypus calls on it

#create a vcf output file path consisting of: 
#vcf_output = base_path + "/variants/" + sample_id + "platypus_m.3243A>G.vcf"

#to use platypus I am going to get the operating system to excecute a concatenated string of cammands and pathways on the Linux command line.
#include here the command to initiate playpus calling on each 
#command = "python" + platypus_path + "callVariants --bamfiles=" + path_to_bam_files + " --refFile=" + build_37_ref + " --output=" + vcf_output + " --regions=" + interval_mtDNA
