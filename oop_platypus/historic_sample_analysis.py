'''the following code enables historic samples to be analysed. Samples are read into a 1D array although additional methods could be constructed for additional data. 



-------------------------------------------------------
#class name
class Sample(object):
'''
initialises sample ID as itself and inludes it as an array.
class variable as the sample array to be appended with output of methods
class variable as base path to the directory where the data wouold be stored
locate_bam_file find the sample bam file and adds it to the sample_array
platypus_output_path takes the bam_file_iput_path and creates an output path for platypus

'''

#class variables
sample_array = []
base_path = "/mnt/Data4/targeted_sequencing"

#initialise 
	def __init__(self, sample_ID)
	    self.sample_ID = sample_ID
	    self.sample_array = [sample_ID]

#class methods
	def locate_bam_file(self)
	    #bam_file_input_path appended to bam file array with sample_ID
	    #return sample_array

	def platypus_output_path(self)
	    #output_path ending in <sample_ID>_platypus.vcf appended to bam_file_array
	    #return bam_file array 

--------------------------------------------------------
#class_name
class input_data(object):
    #class_variables
	patient_ID_array = []

#initalise
	def __init__(self, sample_list_file):
	    self.sample_list_file = sample_list_file

#class_methods
	def patient_IDs_to_list(self)
	    #appends patient Ids from input file to patient_ID array
	    #return patient ID array

--------------------------------------------------------
#class name
class variant_calling(object):

#class variables
	build_37_reference_path = <path_to_reference>

#initialise
	def __init__(self, input_array)
		self.input_array = input_array
		
#class methods
	def use_platypus(self)
		path_to_platypus = 
		cmd = "python " + path_to_platypus + "callVariants --bamFiles=" + str(input_array[1]) + " --refFile" + build_37_ref + "--output=" + str(input_array[2])
		grace_q_executor(cmd)


--------------------------------------------------------
#wrapper_script
from bam_finder.py import *

for sample_ID in Input_data(input_file).patient_IDs_to_list():
	input = Sample(sample_ID).locate_bam_path
	output = Sample(input[1]).generate_output_path()
	variant_calling(output).use_platypus()






	
	
	
