#!/usr/bin/env python
import sys

def pause():
    """
    Pauses the program execution and waits for user input to proceed or quit.
    - Displays a prompt asking the user to press Enter to continue or 'q' to quit.
    - Removes the prompt from the terminal after the user inputs a response.
    - If the user enters 'q' (case insensitive), the program terminates.
    - If the user presses any key, the program continues execution.

    Raises:
        SystemExit: If the user enters 'q', the program exits.
    """
    response = input("\nPress any key to continue or 'q' to quit: ")
    sys.stdout.write("\033[F\033[K") # \033[F : Déplace le curseur à la ligne précédente et \033[K : Efface la ligne.
    if response.lower() == 'q':
        quit()
    
def help():
    """
    Displays a paginated help message, pausing for user input between sections.
    
    Raises:
        SystemExit: at the end of the function, the program exits.
    """
    print(
    "="*40,
    "User Manual for 'convert_to_GFF.py'".center(10),
    "="*40,
    "\n\n",
    "-"*40,
    "Purpose".center(10),
    "-"*40,"\n",
    "The 'convert_to_GFF.py' script converts gene sequence data from three possible formats:\n\
        -GeneMark (GENM)\n\
        -GeneMarkHMM (GENMH)\n\
        -ScanForMatches (SFM)\n\
    into the standard GFF (General Feature Format) file format. This facilitates the integration of gene annotations into various bioinformatics tools.\n")
    
    pause()
    
    print(
    "-"*40,
    "Features".center(10),
    "-"*40,"\n",
    "Supported input types:\n\
        GENM : GeneMark format\n\
        GENMH: GeneMarkHMM format\n\
        SFM: ScanForMatches format with an optional category (e.g., 'RBS', 'PROM', 'TERM')\n\
    Automatic metadata extraction:\n\
        Extracts key details like source version, model information, sequence file name and date\n\
    Error Handling:\n\
        Validates input arguments and file formats with informative error messages.\n\
    Output Format:\n\
        Produces a well-structured GFF v2 file.\n")
    
    pause()
    
    print(
    "-"*40,
    "Usage".center(10),
    "-"*40,"\n",
    "python convert_to_GFF.py [file type: SFM, GENM, GENMH] [input file path] [category (only for SFM: RBS/PROM/TERM)] [output file name (optional)]\n")
    
    pause()
    
    print(
    "-"*40,
    "Arguments".center(10),
    "-"*40,"\n",
    "file type (Required):\n\
        Defines the type of the input file: 'SFM', 'GENM', or 'GENMH'.\n\
    input file path (Required):\n\
        Path to the input file containing the gene sequence data.\n\
    category (Optional; only for SFM):\n\
        Specifies the category for SFM files: 'RBS', 'PROM', or 'TERM'.\n\
    output file name (Optional):\n\
        Name of the output GFF file. If not provided, defaults to 'output.GFF'.\n")
    
    pause()
    
    print(
    "-"*40,
    "Examples".center(10),
    "-"*40,"\n",
    "Convert GeneMark file:\n\
        'python convert_to_GFF.py GENM input_file.lst output.GFF'\n\
    Convert GeneMarkHMM file:\n\
        'python convert_to_GFF.py GENMH input_file.lst output.GFF'\n\
    Convert ScanForMatches file with category:\n\
        'python convert_to_GFF.py SFM input_file.sfm RBS output.GFF'\n")
    
    pause()
    
    print(
    "-"*40,
    "Output".center(10),
    "-"*40,"\n",
    "The script generates a GFF v2 file containing:\n\
        Metadata:\n\
            GFF version\n\
            Source version and date\n\
            Sequence file name, model file name, and RBS status\n\
            Model information\n\
        Annotations:\n\
            Gene locations with features like start, end, strand, and type (CDS/ATG)\n\
            Notes for each gene\n")
    
    pause()
    
    print(
    "-"*40,
    "Error Messages".center(10),
    "-"*40,"\n",
    "Argument Errors:\n\
        If required arguments are missing or invalid:\n\
            'ERR_ARG ! Bad arguments given...\n\
            usage: convert_to_GFF.py [file type : SFM, GENM, GENMH] [file path] [only if SFM : RBS/PROM/TERM] [name output file (Default=output.GFF)]'\n\
    File Format Errors:\n\
        If the input file format is incorrect or unsupported:\n\
            'ERR_TYPE ! Wrong type given...\n\
            usage: convert_to_GFF.py [file type : SFM, GENM, GENMH] [file path] [only if SFM : RBS/PROM/TERM] [name output file (Default=output.GFF)]'\n")
    
    pause()
    
    print(
    "-"*40,
    "How It Works".center(10),
    "-"*40,"\n",
    "Initialization:\n\
        Parses and validates the command-line arguments.\n\
        Determines input and output file names and types.\n\
    File Reading:\n\
        Reads the input file content into memory.\n\
    Data Processing:\n\
        Extracts metadata and gene annotations using functions from 'search_data.py' and 'search_motif.py'.\n\
        Processes each input format separately to handle its specific structure.\n\
    Output Writing:\n\
        Converts processed data into GFF format and writes it to the specified output file.\n")
    
    pause()
    
    print(
    "-"*40,
    "Additional Modules".center(10),
    "-"*40,"\n",
    "'search_data.py':\n\
        Provides utilities for parsing GeneMark and ScanForMatches data.\n\
        Key functions: 'Seq_GMH', 'Seq_GM', 'Create_Tab_GMH', 'Create_Tab_GM', 'Create_Tab_SFM'.\n\
    'search_motif.py':\n\
        Extracts metadata like version, date, and model information.\n\
        Key functions: 'SourceVersion_GMH', 'Date_GMH', 'Model_GMH', 'RBS_GMH', 'ModelInformation_GMH'.\n")
    
    pause()
    
    print(
    "-"*40,
    "Contact".center(10),
    "-"*40,"\n",
    "For further inquiries or support, please contact the developer : RODRIGUES Camille-Astrid (camille-astrid.rodrigues@univ-tlse3.fr).\n")
    
    quit()
