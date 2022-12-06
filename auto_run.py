import os

path_parent = os.path.dirname(os.getcwd()) #go up ONE DIRECTORY
os.chdir(path_parent)
os.system('mkdir workshop_tools')
workshop_path = os.getcwd() + '/workshop_tools'
os.chdir(workshop_path)
print("Install Path : ", workshop_path)

#Install resfinder

print('Starting Install Resfinder')
os.system('pip install resfinder')
os.system('mkdir resfinder_db_tools')
path_resfinder_db_tools = workshop_path+"/resfinder_db_tools"
os.chdir(path_resfinder_db_tools)
print("your path:",os.getcwd())

# Install kma tool
os.system('git clone https://bitbucket.org/genomicepidemiology/kma.git')
path_res_kma = os.getcwd() + "/kma"
os.chdir(path_res_kma)
os.system('make')
os.chdir(path_resfinder_db_tools)

# Install resfinder database
os.system('git clone https://bitbucket.org/genomicepidemiology/resfinder_db/')
path_res_db = os.getcwd() + "/resfinder_db"
os.chdir(path_res_db)
os.system('python3 INSTALL.py')
os.chdir(path_resfinder_db_tools)

# Install pointfinder database
os.system('git clone https://bitbucket.org/genomicepidemiology/pointfinder_db/')
path_res_point = os.getcwd() + "/pointfinder_db"
os.chdir(path_res_point)
os.system('python3 INSTALL.py')
os.chdir(path_resfinder_db_tools)

# Install disinfinder database
os.system('git clone https://bitbucket.org/genomicepidemiology/disinfinder_db/')
path_res_dis = os.getcwd() + "/disinfinder_db"
os.chdir(path_res_dis)
os.system('python3 INSTALL.py')
os.chdir(path_resfinder_db_tools)

# Install blastn
os.system('wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.13.0+-x64-linux.tar.gz')
os.system('tar -xvzf ncbi-blast-2.13.0+-x64-linux.tar.gz ')
print("Install Resfinder Finish")

#install stringMLST 
print('start install stringMLST')
os.chdir(workshop_path)
os.system('mkdir stringMLST')
os.system('pip install stringMLST')
path_stringmlst = workshop_path+'/stringMLST'
os.chdir(path_stringmlst)
print('This program will install only Salmonella enterica database')
os.system('stringMLST.py --getMLST -P salmonella/nmb --species Salmonella enterica')
print("Install stringMLST Finish")

#install Krocus 
print('Start install Krocus')
os.chdir(workshop_path)
os.system('mkdir krocus')
path_krocus = workshop_path + "/krocus"
os.chdir(path_krocus)
os.system('conda install krocus')
print('This program will install only Salmonella database')
os.system('krocus_database_downloader  --species "Salmonella enterica" --output_directory Salmonella_enterica')
print('Install Krocus finish')


#show path 
print("==========================================================================")
print("Please copies five lines after this, to use when open resfinder program")
print('export CGE_RESFINDER_RESGENE_DB="'+path_resfinder_db_tools+'/resfinder_db"')
os.system('export CGE_RESFINDER_RESGENE_DB="'+path_resfinder_db_tools+'/resfinder_db"')
print('export CGE_RESFINDER_RESPOINT_DB="'+path_resfinder_db_tools+'/pointfinder_db"')
os.system('export CGE_RESFINDER_RESPOINT_DB="'+path_resfinder_db_tools+'/pointfinder_db"')
print('export CGE_DISINFINDER_DB="'+path_resfinder_db_tools+'/disinfinder_db"')
os.system('export CGE_DISINFINDER_DB="'+path_resfinder_db_tools+'/disinfinder_db"')
print('export CGE_KMA="'+path_resfinder_db_tools+'/kma/kma"')
os.system('export CGE_KMA="'+path_resfinder_db_tools+'/kma/kma"')
print('export CGE_BLASTN="'+path_resfinder_db_tools+'/ncbi-blast-2.13.0+/bin/blastn"')
os.system('export CGE_BLASTN="'+path_resfinder_db_tools+'/ncbi-blast-2.13.0+/bin/blastn"')
print("==========================================================================")

#test
# get_test = 'wget https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR107/DRR107053/DRR107053_1.fastq.gz'
# get_test2 = 'wget https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR107/DRR107053/DRR107053_2.fastq.gz'
# get_test3 = 'wget https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR154/DRR154180/DRR154180_subreads.fastq.gz'
# os.system(get_test)
# os.system(get_test2)
# os.system(get_test3)
# Test command
print('Command for run Resfinder')
print('python -m resfinder -o result_resfinder -s "salmonella enterica" -l 0.6 -t 0.8 --acquired --point -ifq <file_name_input>')
print('if pair file')
print('python -m resfinder -o result_resfinder -s "salmonella enterica" -l 0.6 -t 0.8 --acquired --point -ifq file_input_*')
print('Command for run stringMLST')
print('stringMLST.py --predict -1 <single-end file> -s --prefix stringMLST_analysis/salmonella/nmb -o result_stringMLST.txt')
print('if pair file')
print('stringMLST.py --predict -1 <paired-end file 1> -2 <paired-end file 2> -p --prefix stringMLST_analysis/salmonella/nmb -o result_stringMLST.txt')
print('Command for run Krocus')
print('krocus allele_directory <input.fastq> -o result_krocus.txt')

