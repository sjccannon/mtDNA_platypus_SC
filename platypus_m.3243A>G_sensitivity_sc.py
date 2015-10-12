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
format_p = re.compile(single character. the letter 5. under score. 5. underscore. three letter number)
format_v = re.compile()

#Constructiong a dictionary of sample number as key and the path to appropriate bam file as the value
for line in MODY_subset_infile:
	line.split()
	use regular expression to infer the location of the bam file based on the column 0. must meet format of "P5_5_211" because P5's above 500 are stroed in data 4 
	#if sample corresponds with old version numbers. 
	if format_p(column 0) == True: #is in foramt P5_5_221
		sample_ID = column(0)
		p_numeric_sample_ID = int(sample_ID[-3:])#uses reverse indicies extract the numerical sample number values by taking the last three digits, turn to an integer and assign to 'p_numeric_sample_ID'
		bam_end = '.realigned.sorted.bam'

		if p_numeric_sample_ID >= 1 and <= 48:
			additional_ path = 'P5_001-048/assembly/'
			bam_file_name = 'P5_001-48_' + str(p_numeric_sample_ID) + bam_end
			#append dictionary to include sample_ID as key and string of path to bam file
			my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_fie_name

		elif p_numeric_sample_ID >=  49 and <= 96:
			additional_path = 'P5_049_096/assembly/' 
			bam_file_name = 'P5_049-096_' + str(p_numeric_sample_ID) + bam_end
			my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name 

		elif p_numeric_sample_ID >= 97 and <= 144:
			additional_path = 'P5_097-144/assembly/'
			bam_file_name = 'P5_049-144_' + str(p_numeric_sample_ID) + bam_end
			my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name
		
		elif p_numeric_sample_ID >= 145 and <= 216:
			additional_path = 'P5_145-216/assembly/'
			bam_file_name = 'P5_145-216_' + str(p_numeric_sample_ID) + bam_end
			my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

		elif p_numeric_sample_ID >= 217 and <= 240:
			additional_path = 'P5_217-240/assembly/'
			bam_file_name = 'P5_217-240_' + str(p_numeric_sample_ID) + bam_end
			my_dict[sample_ID] = path_to_P5_bam +additional_path + bam_file_name

		elif p_numeric_sample_ID >= 241 and <= 336:
			additional_path = 'P5_241-336/assembly/'
			bam_file_name = 'P5_241-336_' + str(p_numeric_sample_ID) + bam_end
			my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

		elif p_numeric_sample_ID >= 337 and <= 384:
			additional_path = 'P5_337-384/assembly/'
			bam_file_name = 'P5_337-384_' + str(p_numeric_sample_ID) + bam_end
			my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

		elif p_numeric_sample_ID >= 385 and 432: 
			additional_path = 'P5_385-432_run2/assembly/'
			bam_file_name = 'P5_385-432_' + str(p_numeric_sample_ID) + 'realigned.sorted.merged.bam'
			my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

		elif p_numeric_sample_ID >= 433 and <= 480:
			additional_path = 'P5_433-480/assembly/'
			bam_file_name = 'P5_433-480_ + str(p_numeric_sample_ID) + bam_end
			my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name
			

		elif p_numeric_sample_ID >= 481 and <= 504:
			additonal_path = 'P5_481-504/assembly/'
			bam_file_name = 'P5_481-504_' + str(p_numeric_sample_ID) + bam_end
			my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name
	
	elif column 0 meets the regular expression in the format of P5_505 or has a v5 in it:
		sample_ID = str(column0 last three digits) 
		take column 1 and turn into a string
		take last 8 digits and assign as int(batch_number)
		if batch_number  >= 1501266:
			formatted_column_1 = replace full stops '.' with dashes '-' in column 1
			additional_path = formatted_column_1 + '/assembly/'
			for file_name in glob.glob(path_to_v5_bam + additional_path + sample_ID + '*realigned.bam')
				dictionary key == sample_ID, dictionary value == file_name
		else 	 		
			
		
		 
		if the last 8 digits (batch number) == 140383
		additional_path = take column 1, turn into a string
		
	else:
		print 'error with input file'

#loop through each dictionary entry and initiate Platypus calls on it

#create a vcf output file path consisting of: 
vcf_output = base_path + "/variants/" + sample_id + "platypus_m.3243A>G.vcf"

#to use platypus I am going to get the operating system to excecute a concatenated string of cammands and pathways on the Linux command line.
#include here the command to initiate playpus calling on each 
command = "python" + platypus_path + "callVariants --bamfiles=" + path_to_bam_files + " --refFile=" + build_37_ref + " --output=" + vcf_output + " --regions=" + interval_mtDNA
