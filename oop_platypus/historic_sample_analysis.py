'''the following code enables historic samples to be analysed with platypus variant caller although additional functionality 
could be added to the clases'''

--------------------------------------------------------
'''
initialises sample ID as itself and inludes it as an array.
class variable as the sample array to be appended with output of methods
class variable as base path to the directory where the data wouold be stored
locate_bam_file find the sample bam file and adds it to the sample_array
platypus_output_path takes the bam_file_iput_path and creates an output path for platypus
'''


class Sample(object):
	bam_file_array = []
	base_path = "/mnt/Data4/targeted_sequencing"

	#initialise
        def __init__(self, sample_ID):
            self.sample_ID = sample_ID
            self.bam_file_array = [sample_ID]

	#class methods
        #bam_file_input_path appended to bam file array with sample_ID
	
	def sample_sorter(self):
            if self.bam_file_array[0].startswith('P'):
                self.bam_file_array.append('data1')	
	    elif self.bam_file_array[0].startswith('v'):
            	self.bam_file_array.append('data4')
	    else:
		self.bam_file_array.append('not_P_or_v')
            return self.bam_file_array

        def locate_bam_file(self):
	        if self.bam_file_array[1] == 'data1':
		    found_bam_array = []
		    sliced_id = self.sample_id[-1:-3]
		    sample_regex = "P5_*-*_%s*realigned*bam" %sliced_id
   	            cmd = "find /mnt/Data1/targeted_sequencing/ -name " + sample_regex + " -type f"
		    #use subprocess.Popen to capture stdout and pipe to found_bam_array
		    if len(found_bam_array) > 0:
                        print 'multiple bam files identified for patient_id' + self.sample_ID
			for idx, item in enumerate(found_bam_array):
				print str(idx) + " " + str(item)
			user_input_statemet = "Enter the index of the bam file you wish to analyse %s : " %self.sample_id
			user_input = raw_input(user_input_statement)
			self.bam_file_array.append(found_bam_array[int(raw_input)])
		    else:
			print 'appending %s to bam_file_array for sample %s' %(str(found_bam_array[0], self.sample_id)
			self.bam_file_array.append(found_bam_array[0]) 
		    return self.bam_file_array
		elif self.bam_file_array[1] == 'data4':
                    found_bam_array = []
	
	def multiple_bam_files(self, array)
		if len(array) > 0:
                    print 'multiple bam files identified for patient_id' + self.sample_ID
                    for idx, item in enumerate(found_bam_array):
                        print str(idx) + " " + str(item)
			user_input_statemet = "Enter the index of the bam file you wish to analyse %s : " %self.sample_id
                        user_input = raw_input(user_input_statement)
                        self.bam_file_array.append(found_bam_array[int(user_input)])
                    else:
                        print 'appending %s to bam_file_array for sample %s' %(str(found_bam_array[0], self.sample_id)
                        self.bam_file_array.append(found_bam_array[0])
                    return self.bam_file_array


	def located_bam_file data1(self, ):
        #find /mnt/Data4/targeted_sequencing/ -name 'P5_*-*_045*realigned*bam


        def generate_output_path(self)
            #output_path ending in <sample_ID>_platypus.vcf appended to bam_file_array
            #return bam_file array

-------------------------------------------------------
'''reads a tab separated input file and produces an array of sample IDs
samples are read into a 1D array although additional methods could be constructed
where more data fields are included in the input data'''

class Input_data(object):
	patient_id_array = []

	def __init__(self, samples_file):
	    self.samples_file = samples_file
	    self.patient_id_array = patient_id_to_list()

	#extract the first column of the data into a class variable array    
	def patient_id_to_list(self)
    	    #appends patient Ids from input file to patient_ID array
	    with open(self.samples_file, 'r') as patient_id_file:
		for line in patient_id_file:
		    columns = line.split()
	 	    patient_id = columns[0]
		    patient_id_array.append(patient_id)
	return patient_id_array

	def samples(self):
	    sample_insatnces = []
	    for item in self.patient_id_array:
		sample_instances.append(Samples(item))
	    return sample_instances
	
		    

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
	
	
