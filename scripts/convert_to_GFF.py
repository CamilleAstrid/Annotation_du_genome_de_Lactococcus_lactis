#!/usr/bin/env python
import sys
import search_motif
import search_data
import man

'''
ERREURS possibles
'''
def Error_arg():
    """
    Displays an error message for invalid or insufficient arguments and exits the program.

    Raises:
        SystemExit: The program exits immediately after displaying the error message.
    """
    quit("\nERR_ARG ! Bad arguments given...\nusage: convert_to_GFF.py [file type : SFM, GENM, GENMH] [file path] [only if SFM : RBS/PROM/TERM] [name output file (Default=output.GFF)]\n")
    
def Error_type():
    """
    Displays an error message for an invalid or unsupported file type and exits the program.

    Raises:
        SystemExit: The program exits immediately after displaying the error message.
    """
    quit("\nERR_TYPE ! Wrong type given...\nusage: convert_to_GFF.py [file type : SFM, GENM, GENMH] [file path] [only if SFM : RBS/PROM/TERM] [name output file (Default=output.GFF)]\n")
    
    
'''
INITIALISATION du programme
'''
def initialise()->list[str]:
    '''
    Initializes the script parameters by retrieving command-line arguments.
    
    - Displays the name of the script being executed.
    - Checks for the presence of a category (RBS, Prom, or Term), a type (GeneMark/GeneMarkHMM/ScanForMatches), an input file (required), 
      and an output file (optional).
    - Returns a list containing the categorie, the type, the input file and the output file.
    
    Expected usage:
        script.py [input_file] [output_file (optional)] [category (RBS/Prom/Term)] [type (GENM/GENMH/SFM)]
    
    If the output file is not specified, "output.GFF" is used as the default.
    If insufficient arguments are provided, an error message is displayed, and the program terminates.
    
    Returns:
        list: [filename, fileout, categorie, type]
    '''
    if len(sys.argv) > 1 and (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
        man.help()

    try :
        print(sys.argv[0],"is running...")  
        type = sys.argv[1]
        filename = sys.argv[2]        
        type = type.upper()
        
        if type=="SFM":
            try :
                categorie = sys.argv[3]
                categorie = categorie.upper()
                if categorie!="RBS" and categorie!="PROM" and categorie!="TERM":
                    Error_arg()
                try:
                    fileout = sys.argv[4]
                except:
                    fileout="output.GFF"
            except:
                Error_arg()
        else:
            categorie="None"
            try:
                fileout = sys.argv[3]
            except:
                fileout="output.GFF"
    except:
        Error_arg()
    
    return [filename, fileout, categorie, type]


'''
LECTURE du fichier input
'''
def lire(files:list[str])->str:
    """
    Reads the contents of a file.
    
    - Retrieves the file name from the first element of the input list.
    - Opens the file in read mode and reads its entire content.
    
    Args:
        files (list): A list where the first element is the name of the file to be read.
    
    Returns:
        str: The content of the file as a string.
    """
    filename = files[0]
    print("Reading file", filename)
    with open(filename, "r") as input_file:
        input = input_file.read()
    return input


'''
TYPE du fichier input
'''
def ScanForMatches(files:list[str], input:str):
    """
    Writes the processed data from ScanForMatches file into an output file in GFF format.
    """
    fileout=files[1]
    category = files[2]
    if category=="RBS":
        RBS=True
    else:
        RBS=False
    try:
        Date=search_motif.Date()
        Info = search_data.Create_Tab_SFM(input)
        taille = Info[0]
        DataFrame = Info[1]
    except:
        Error_type()
    
    with open(fileout, "w") as output_file:
        output_file.write("##gff-version 2\n##source-version ScanForMatches")
        output_file.write("\n##date: "+Date[0]+" "+Date[1]+" "+Date[2]+" "+Date[3]+":"+Date[4]+":"+Date[5]+" "+Date[6])
        output_file.write("\n# Sequence file name: -\n# Model file name: -")
        output_file.write("\n# RBS: "+str(RBS))
        output_file.write("\n# Model information: -\n\n")
        
        for index in range (taille):
            output_file.write(DataFrame[index][0]+"\tScanForMatches\t"+category+"\t"+DataFrame[index][1]+"\t"+DataFrame[index][2]+"\t.\t+\t.\tnote \" "+DataFrame[index][3]+"\"\n")
    
def GeneMark(files:list[str], input:str):
    """
    Writes the processed data from GeneMark file into an output file in GFF format.
    """
    fileout=files[1]   
    try:
        SourceVersion = search_motif.SourceVersion_GM(input)
        Date = search_motif.Date()
        Seqfilename = search_motif.Seqfilename_GM(input)
        ModelInformation = search_motif.ModelInformation_GM(input)
        Seq = search_data.Seq_GM(input)
        Info = search_data.Create_Tab_GM(input)
        taille = Info[0]
        DataFrame = Info[1]
    except:
        Error_type()
    
    with open(fileout, "w") as output_file:
        output_file.write("##gff-version 2\n##source-version GeneMark "+SourceVersion)
        output_file.write("\n##date: "+Date[0]+" "+Date[1]+" "+Date[2]+" "+Date[3]+":"+Date[4]+":"+Date[5]+" "+Date[6])
        output_file.write("\n# "+Seqfilename)
        output_file.write("\n# Model file name: -")
        output_file.write("\n# RBS: -")
        output_file.write("\n# Model information: "+ModelInformation+"\n\n")
        
        for index in range (taille):
            output_file.write(Seq+"\tGeneMark\t"+DataFrame[index][6]+"\t"+str(DataFrame[index][1])+"\t"+str(DataFrame[index][2])+"\t?\t"+DataFrame[index][0]+"\t.\t"+str(DataFrame[index][7])+"\n")
        output_file.write("\n")

def GeneMarkHMM(files:list[str], input:str):
    """
    Writes the processed data from GeneMarkHMM file into an output file in GFF format.
    """
    fileout=files[1]    
    try:
        SourceVersion = search_motif.SourceVersion_GMH(input)
        Date = search_motif.Date_GMH(input)
        Seqfilename = search_motif.Seqfilename_GMH(input)
        Model = search_motif.Model_GMH(input)
        RBS = search_motif.RBS_GMH(input)
        ModelInformation = search_motif.ModelInformation_GMH(input)
        Seq = search_data.Seq_GMH(input)
        Info = search_data.Create_Tab_GMH(input)
        taille = Info[0]
        DataFrame = Info[1]
    except:
        Error_type()
    
    with open(fileout, "w") as output_file:
        output_file.write("##gff-version 2\n##source-version "+SourceVersion[0]+" "+SourceVersion[1])
        output_file.write("\n##date:"+Date)
        output_file.write("\n# "+Seqfilename)
        output_file.write("\n# "+Model)
        output_file.write("\n# "+RBS)
        output_file.write("\n# "+ModelInformation+"\n\n")
        
        for index in range (taille):
            output_file.write(Seq+"_"+str((index+1))+"\tGeneMark.hmm\tCDS\t"+DataFrame[index][1]+"\t"+DataFrame[index][2]+"\t?\t"+DataFrame[index][0]+"\t.\tgene GMH_CDS_"+str((index+1))+"\n")
   

'''
ECRITURE du fichier output
'''
def ecrire(files:list[str], input:str):
    """
    Writes the processed data into an output file in GFF format.
    
    - Retrieves the output file name from the second element of the `files` list.
    - Extracts metadata and sequence data from the input using helper functions (module search_motif and search_data).
    - Formats the data according to the GFF version 2 specification.
    - Writes the formatted data to the specified output file.
    
    Args:
        files (list): A list containing file names, where the second element is the output file name
                    and the third element is the category.
        input (str): The content of the input file to be processed and written to the output.
    
    Raises:
        SystemExit: If an error occurs while extracting data, an error message is displayed,
                   and the program terminates.

    Output:
        The output file is written with the following structure:
        - Metadata: GFF version, source version, date, sequence file name, model information.
        - Sequence data in GFF format, including start and end positions, strand, and other details.
    """
    type=files[3]
    fileout=files[1]
    print("Writting", fileout)
    if type=="GENM":
        GeneMark(files, input)
    elif type=="GENMH":
        GeneMarkHMM(files, input)
    else:
        ScanForMatches(files, input)

    
if __name__ == "__main__":
    files=initialise()
    input=lire(files)
    ecrire(files, input)
    print("Work done !")
