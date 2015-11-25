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




#default URL locations of required files

gatk_path = "/usr/share/gatk/GenomeAnalysisTK-3.3-0/GenomeAnalysisTK.jar"
reference_path = "/mnt/Data1/resources/human_g1k_v37.fasta"

#interval_file_name = "PAv3_ROI_for_CNV_plots.interval_list"
interval_file_name = "haplotype_caller_validation_extended_ROI.interval_list"
base_path = "/mnt/Data1/targeted_sequencing/validation/haplotype_caller/gatk_3-3-0"

# Hash of sample name (key) and URL of selected BAM (value)

samples = Hash.new
samples["PA_01"] = "/mnt/Data1/targeted_sequencing/P1_01-10/bwa-mem/P1_01-10.realigned.PA01.bam"
samples["PA_02"] = "/mnt/Data1/targeted_sequencing/P1_01-10/bwa-mem/P1_01-10.realigned.PA02.bam"
samples["PA_03"] = "/mnt/Data1/targeted_sequencing/P1_01-10/bwa-mem/P1_01-10.realigned.PA03.bam"
samples["PA_04"] = "/mnt/Data1/targeted_sequencing/P1_01-10/bwa-mem/P1_01-10.realigned.PA04.bam"
samples["PA_05"] = "/mnt/Data1/targeted_sequencing/P1_01-10/bwa-mem/P1_01-10.realigned.PA05.bam"
samples["PA_06"] = "/mnt/Data1/targeted_sequencing/P1_01-10/bwa-mem/P1_01-10.realigned.PA06.bam"
samples["PA_07"] = "/mnt/Data1/targeted_sequencing/P1_01-10/bwa-mem/P1_01-10.realigned.PA07.bam"
samples["PA_08"] = "/mnt/Data1/targeted_sequencing/P1_01-10/bwa-mem/P1_01-10.realigned.PA08.bam"
samples["PA_09"] = "/mnt/Data1/targeted_sequencing/P1_01-10/bwa-mem/P1_01-10.realigned.PA09.bam"
samples["PA_10"] = "/mnt/Data1/targeted_sequencing/P1_01-10/bwa-mem/P1_01-10.realigned.PA10.bam"

samples["P2_01"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_01.bam"
samples["P2_02"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_02.bam"
samples["P2_03"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_03.bam"
samples["P2_04"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_04.bam"
samples["P2_05"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_05.bam"
samples["P2_06"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_06.bam"
samples["P2_07"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_07.bam"
samples["P2_08"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_08.bam"
samples["P2_09"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_09.bam"
samples["P2_10"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_10.bam"
samples["P2_11"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_11.bam"
samples["P2_13"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_13.bam"
samples["P2_16"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_16.bam"
samples["P2_17"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_17.bam"
samples["P2_18"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_18.bam"
samples["P2_19"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_19.bam"
samples["P2_20"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_20.bam"
samples["P2_21"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_21.bam"
samples["P2_22"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_22.bam"
samples["P2_23"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_23.bam"
samples["P2_24"] = "/mnt/Data1/targeted_sequencing/P2_01-24/bwa-mem/P2_01-24.realigned.P2_24.bam"

samples["P2_31"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_31.bam"
samples["P2_32"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_32.bam"
samples["P2_33"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_33.bam"
samples["P2_34"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_34.bam"
samples["P2_35"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_35.bam"
samples["P2_36"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_36.bam"
samples["P2_37"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_37.bam"
samples["P2_38"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_38.bam"
samples["P2_39"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_39.bam"
samples["P2_40"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_40.bam"
samples["P2_41"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_41.bam"
samples["P2_42"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_42.bam"
samples["P2_43"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_43.bam"
samples["P2_46"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_46.bam"
samples["P2_47"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_47.bam"
samples["P2_48"] = "/mnt/Data1/targeted_sequencing/P2_25-48/bwa-mem/P2_25-48.realigned.P2_48.bam"

samples["P3_001"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_01.bam"
samples["P3_011"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_11.bam"
samples["P3_013"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_13.bam"
samples["P3_016"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_16.bam"
samples["P3_018"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_18.bam"
samples["P3_020"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_20.bam"
samples["P3_021"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_21.bam"
samples["P3_028"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_28.bam"
samples["P3_030"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_30.bam"
samples["P3_035"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_35.bam"
samples["P3_036"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_36.bam"
samples["P3_037"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_37.bam"
samples["P3_038"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_38.bam"
samples["P3_039"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_39.bam"
samples["P3_043"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_43.bam"
samples["P3_044"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_44.bam"
samples["P3_045"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_45.bam"
samples["P3_046"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_46.bam"
samples["P3_047"] = "/mnt/Data1/targeted_sequencing/P3_001-048/bwa-mem/P3_001-048.realigned.P3_47.bam"

samples["P3_001A"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_01.bam"
samples["P3_011A"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_11.bam"
samples["P3_050"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_50.bam"
samples["P3_052"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_52.bam"
samples["P3_054"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_54.bam"
samples["P3_057"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_57.bam"
samples["P3_064"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_64.bam"
samples["P3_066"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_66.bam"
samples["P3_080"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_80.bam"
samples["P3_086"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_86.bam"
samples["P3_087"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_87.bam"
samples["P3_090"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_90.bam"
samples["P3_095"] = "/mnt/Data1/targeted_sequencing/P3_01-12_50-96/bwa-mem/P3_01-12_50-96.realigned.P3_95.bam"

samples["PL_001"] = "/mnt/Data1/targeted_sequencing/P3_097-133/bwa-mem/P3_097-133.realigned.PL_01.bam"
samples["P3_099"] = "/mnt/Data1/targeted_sequencing/P3_097-133/bwa-mem/P3_097-133.realigned.P3_99.bam"
samples["P3_100"] = "/mnt/Data1/targeted_sequencing/P3_097-133/bwa-mem/P3_097-133.realigned.P3_100.bam"
samples["P3_104"] = "/mnt/Data1/targeted_sequencing/P3_097-133/bwa-mem/P3_097-133.realigned.P3_104.bam"
samples["P3_122"] = "/mnt/Data1/targeted_sequencing/P3_097-133/bwa-mem/P3_097-133.realigned.P3_122.bam"
samples["P3_125"] = "/mnt/Data1/targeted_sequencing/P3_097-133/bwa-mem/P3_097-133.realigned.P3_125.bam"

samples["P3_136"] = "/mnt/Data1/targeted_sequencing/P3_134-181/bwa-mem/P3_134-181.realigned.P3_136.bam"
samples["P3_140"] = "/mnt/Data1/targeted_sequencing/P3_134-181/bwa-mem/P3_134-181.realigned.P3_140.bam"
samples["P3_149"] = "/mnt/Data1/targeted_sequencing/P3_134-181/bwa-mem/P3_134-181.realigned.P3_149.bam"
samples["P3_150"] = "/mnt/Data1/targeted_sequencing/P3_134-181/bwa-mem/P3_134-181.realigned.P3_150.bam"
samples["P3_157"] = "/mnt/Data1/targeted_sequencing/P3_134-181/bwa-mem/P3_134-181.realigned.P3_157.bam"
samples["P3_160"] = "/mnt/Data1/targeted_sequencing/P3_134-181/bwa-mem/P3_134-181.realigned.P3_160.bam"
samples["P3_172"] = "/mnt/Data1/targeted_sequencing/P3_134-181/bwa-mem/P3_134-181.realigned.P3_172.bam"
samples["P3_173"] = "/mnt/Data1/targeted_sequencing/P3_134-181/bwa-mem/P3_134-181.realigned.P3_173.bam"
samples["P3_178"] = "/mnt/Data1/targeted_sequencing/P3_134-181/bwa-mem/P3_134-181.realigned.P3_178.bam"

samples["P3_185"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_185.bam"
samples["P3_187"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_187.bam"
samples["P3_195"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_195.bam"
samples["P3_198"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_198.bam"
samples["P3_206"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_206.bam"
samples["P3_207"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_207.bam"
samples["P3_213"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_213.bam"
samples["P3_216"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_216.bam"
samples["P3_226"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_226.bam"
samples["P3_228"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_228.bam"
samples["P3_229"] = "/mnt/Data1/targeted_sequencing/P3_182-229/bwa-mem/P3_182-229.realigned.P3_229.bam"

samples["P3_236"] = "/mnt/Data1/targeted_sequencing/P3_230-273/bwa-mem_bam_files/P3_230-273.realigned.P3_236.bam"
samples["P3_242"] = "/mnt/Data1/targeted_sequencing/P3_230-273/bwa-mem_bam_files/P3_230-273.realigned.P3_242.bam"
samples["P3_249"] = "/mnt/Data1/targeted_sequencing/P3_230-273/bwa-mem_bam_files/P3_230-273.realigned.P3_249.bam"
samples["P3_259"] = "/mnt/Data1/targeted_sequencing/P3_230-273/bwa-mem_bam_files/P3_230-273.realigned.P3_259.bam"

samples["P3_280"] = "/mnt/Data1/targeted_sequencing/P3_274-316/bwa-mem/P3_274-316.realigned.P3_280.bam"
samples["P3_281"] = "/mnt/Data1/targeted_sequencing/P3_274-316/bwa-mem/P3_274-316.realigned.P3_281.bam"
samples["P3_282"] = "/mnt/Data1/targeted_sequencing/P3_274-316/bwa-mem/P3_274-316.realigned.P3_282.bam"
samples["P3_283"] = "/mnt/Data1/targeted_sequencing/P3_274-316/bwa-mem/P3_274-316.realigned.P3_283.bam"
samples["P3_294"] = "/mnt/Data1/targeted_sequencing/P3_274-316/bwa-mem/P3_274-316.realigned.P3_294.bam"
samples["P3_298"] = "/mnt/Data1/targeted_sequencing/P3_274-316/bwa-mem/P3_274-316.realigned.P3_298.bam"
samples["P3_300"] = "/mnt/Data1/targeted_sequencing/P3_274-316/bwa-mem/P3_274-316.realigned.P3_300.bam"
samples["P3_312"] = "/mnt/Data1/targeted_sequencing/P3_274-316/bwa-mem/P3_274-316.realigned.P3_312.bam"
samples["P3_315"] = "/mnt/Data1/targeted_sequencing/P3_274-316/bwa-mem/P3_274-316.realigned.P3_315.bam"

samples["P3_324"] = "/mnt/Data1/targeted_sequencing/P3_317-371/assembly/P3_317-371.realigned.P3_324.bam"
samples["P3_334"] = "/mnt/Data1/targeted_sequencing/P3_317-371/assembly/P3_317-371.realigned.P3_334.bam"
samples["P3_348"] = "/mnt/Data1/targeted_sequencing/P3_317-371/assembly/P3_317-371.realigned.P3_348.bam"
samples["P3_349"] = "/mnt/Data1/targeted_sequencing/P3_317-371/assembly/P3_317-371.realigned.P3_349.bam"
samples["P3_350"] = "/mnt/Data1/targeted_sequencing/P3_317-371/assembly/P3_317-371.realigned.P3_350.bam"
samples["P3_358"] = "/mnt/Data1/targeted_sequencing/P3_317-371/assembly/P3_317-371.realigned.P3_358.bam"
samples["P3_359"] = "/mnt/Data1/targeted_sequencing/P3_317-371/assembly/P3_317-371.realigned.P3_359.bam"
samples["P3_368"] = "/mnt/Data1/targeted_sequencing/P3_317-371/assembly/P3_317-371.realigned.P3_368.bam"
samples["P3_371"] = "/mnt/Data1/targeted_sequencing/P3_317-371/assembly/P3_317-371.realigned.P3_371.bam"

samples["P3_372"] = "/mnt/Data1/targeted_sequencing/P3_372-418/assembly/P3_372-403.merge_run1-2.P3_372.bam"
samples["P3_374"] = "/mnt/Data1/targeted_sequencing/P3_372-418/assembly/P3_372-403.merge_run1-2.P3_374.bam"
samples["P3_375"] = "/mnt/Data1/targeted_sequencing/P3_372-418/assembly/P3_372-403.merge_run1-2.P3_375.bam"
samples["P3_382"] = "/mnt/Data1/targeted_sequencing/P3_372-418/assembly/P3_372-403.merge_run1-2.P3_382.bam"
samples["P3_383"] = "/mnt/Data1/targeted_sequencing/P3_372-418/assembly/P3_372-403.merge_run1-2.P3_383.bam"
samples["P3_384"] = "/mnt/Data1/targeted_sequencing/P3_372-418/assembly/P3_372-403.merge_run1-2.P3_384.bam"
samples["P3_393"] = "/mnt/Data1/targeted_sequencing/P3_372-418/assembly/P3_372-403.merge_run1-2.P3_393.bam"

samples["P3_423"] = "/mnt/Data1/targeted_sequencing/P3_420-467/assembly/P3_420-467_423.realigned.sorted.bam"
samples["P3_425"] = "/mnt/Data1/targeted_sequencing/P3_420-467/assembly/P3_420-467_425.realigned.sorted.bam"
samples["P3_426"] = "/mnt/Data1/targeted_sequencing/P3_420-467/assembly/P3_420-467_426.realigned.sorted.bam"

samples["P3_483"] = "/mnt/Data1/targeted_sequencing/P3_468-515/assembly/P3_468-515_483.realigned.sorted.bam"

samples["P3_518"] = "/mnt/Data1/targeted_sequencing/P3_516-560/assembly/P3_516-560_518.realigned.sorted.bam"

samples["P3_581"] = "/mnt/Data1/targeted_sequencing/P3_564-611/assembly/P3_564-611_581.realigned.sorted.bam"

samples["P4_020"] = "/mnt/Data1/targeted_sequencing/P4_17-34/P4_17-34.realigned.P4_20.bam"
samples["P4_021"] = "/mnt/Data1/targeted_sequencing/P4_17-34/P4_17-34.realigned.P4_21.bam"


#run through samples hash and execute the Haplotype Caller for each key-value pair
#load resulting VCF file and check against expected result

samples.each { |sample_id, url_path|
	
#code to parse the Bash shell command and execute it
#note that this runs the haplotype caller in series if you want to run
#the haplotype caller in parallel add '&' to the end of the command string

	vcf_file_path = base_path + "/variants/" + sample_id + ".hap_call.vcf"
	
	command = "java -Xmx4g -jar " + gatk_path + " -T HaplotypeCaller -R " + reference_path + " -rf BadCigar -stand_call_conf 50.0 -stand_emit_conf 30.0 -dcov 100000 \
-L " + base_path + "/" + interval_file_name + " -log " + base_path + "/logs/" + sample_id + "_haplotype_caller.log -I " + url_path + " -o " + vcf_file_path
 
	system(command)
	

}



