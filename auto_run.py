import os
path = os.getcwd()
print("old path:", path)

#Install resfinder
print('Starting Install Resfinder')
os.system('pip install resfinder')
os.system('mkdir resfinder_db_tools')
path_resfinder_db_tools = path+"/resfinder_db_tools"
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
os.chdir(path)
os.system('mkdir stringMLST')
os.system('pip install stringMLST')
path_stringmlst = path+'/stringMLST'
os.chdir(path_stringmlst)
print('This program will install only Salmonella enterica database')
os.system('stringMLST.py --getMLST -P salmonella/nmb --species Salmonella enterica')
print("Install stringMLST Finish")

#install Krocus 
print('Start install Krocus')
os.chdir(path)
os.system('mkdir krocus')
path_krocus = path + "/krocus"
os.chdir(path_krocus)
os.system('conda install krocus')
print('This program will install only Salmonella database')
os.system('krocus_database_downloader  --species "Salmonella enterica" --output_directory Salmonella_enterica')
print('Install Krocus finish')


#show path 
print("==========================================================================")
print("Please copies five lines after this, to use when open resfinder program")
print('export CGE_RESFINDER_RESGENE_DB="'+path_resfinder_db_tools+'/resfinder_db"')
print('export CGE_RESFINDER_RESPOINT_DB="'+path_resfinder_db_tools+'/pointfinder_db"')
print('export CGE_DISINFINDER_DB="'+path_resfinder_db_tools+'/disinfinder_db"')
print('export CGE_KMA="'+path_resfinder_db_tools+'/kma/kma"')
print('export CGE_BLASTN="'+path_resfinder_db_tools+'/ncbi-blast-2.13.0+/bin/blastn"')
print("==========================================================================")
