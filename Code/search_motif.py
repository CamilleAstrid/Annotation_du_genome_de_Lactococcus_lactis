#!/usr/bin/env python
import re
import datetime

def SourceVersion_GMH(input:str)->tuple[str,str]:
    """
    Extracts the source and version information from the input data using a regular expression.

    - Searches the input string for a pattern that matches a source name (24 characters),
      followed by an additional string, and then a version number (format: X.XXX).
    - If a match is found, it returns the source name and version, else returns empty strings
      for both source and version.

    Args:
        input (str): The input data to search for the source and version information.

    Returns:
        list: A list containing two elements:
            - The source name as a string.
            - The version number as a string.
    """
    motif_sourceversion = re.compile(r"(?P<source>.{24})(?P<other>.{10})(?P<version>\d{1,2}\.\d{1,3})")
    matchSourceversion = re.search(motif_sourceversion, input)

    if matchSourceversion is not None:
        source=matchSourceversion.group('source')
        version=matchSourceversion.group('version')
    else:
        source=""
        version=""

    return (source, version)

def Date_GMH(input:str)->str:
    """
    Extracts the date information from the input data using a regular expression.

    - Searches the input string for the pattern "Date: <date>", where the date is a 24-25 character long string.
    - If a match is found, it returns the extracted date, else returns an empty string.

    Args:
        input (str): The input data to search for the date information.

    Returns:
        str: The extracted date as a string, or an empty string if no date is found.
    """
    motif_date = re.compile(r"(Date:)(?P<date>.{24,25})")
    matchDate = re.search(motif_date, input)
    
    if matchDate is not None:
        date=matchDate.group('date')
    else:
        date=""
    
    return date

def Seqfilename_GMH(input:str)->str:
    """
    Extracts the sequence file name from the input data using a regular expression.

    - Searches the input string for a pattern matching "Sequence file name: <filename>.fna".
    - If a match is found, it returns the sequence file name, else returns an empty string.

    Args:
        input (str): The input data to search for the sequence file name.

    Returns:
        str: The extracted sequence file name as a string (e.g., "example.fna"), or an empty string if no match is found.
    """
    motif_Seqfilename = re.compile(r"(?P<Seqfilename>Sequence\sfile\sname:.{1,}\.fna)")
    matchSeqfilename = re.search(motif_Seqfilename, input)
    
    if matchSeqfilename is not None:
        Seqfilename=matchSeqfilename.group('Seqfilename')
    else:
        Seqfilename=""
    
    return Seqfilename

def Model_GMH(input:str)->str:
    """
    Extracts the model file name from the input data using a regular expression.

    - Searches the input string for a pattern matching "Model file name: <filename>".
    - If a match is found, it returns the model file name, else returns an empty string.

    Args:
        input (str): The input data to search for the model file name.

    Returns:
        str: The extracted model file name as a string, or an empty string if no match is found.
    """
    motif_Model = re.compile(r"(?P<Model>Model\sfile\sname:.{1,})")
    matchModel = re.search(motif_Model, input)
    
    if matchModel is not None:
        Model=matchModel.group('Model')
    else:
        Model=""
    
    return Model

def RBS_GMH(input:str)->str:
    """
    Extracts the RBS (Ribosome Binding Site) information from the input data using a regular expression.

    - Searches the input string for a pattern matching "RBS: <sequence>", where <sequence> is "true" or "false".
    - If a match is found, it returns true or false, else returns an empty string.

    Args:
        input (str): The input data to search for the RBS information.

    Returns:
        str: The extracted RBS information as a string, or an empty string if no match is found.
    """
    motif_RBS = re.compile(r"(?P<RBS>RBS:\s\w{4,5})")
    matchRBS = re.search(motif_RBS, input)
    
    if matchRBS is not None:
        RBS=matchRBS.group('RBS')
    else:
        RBS=""
    
    return RBS

def ModelInformation_GMH(input:str)->str:
    """
    Extracts the model information from the input data using a regular expression.

    - Searches the input string for a pattern matching "Model information: <information>".
    - If a match is found, it returns the model information, else returns an empty string.

    Args:
        input (str): The input data to search for the model information.

    Returns:
        str: The extracted model information as a string, or an empty string if no match is found.
    """
    motif_ModelInformation = re.compile(r"(?P<ModelInformation>Model\sinformation:.{1,})")
    matchModelInformation = re.search(motif_ModelInformation, input)
    
    if matchModelInformation is not None:
        ModelInformation=matchModelInformation.group('ModelInformation')
    else:
        ModelInformation=""
    
    return ModelInformation

def SourceVersion_GM(input:str)->str:
    """
    Extracts the source version information from the input data using a regular expression.

    - Searches the input string for a pattern matching "Training set derived by <text> <version>", where the version
      is in the format X.XXX.
    - If a match is found, it returns the extracted version number, else returns an empty string.

    Args:
        input (str): The input data to search for the source version information.

    Returns:
        str: The extracted version number as a string, or an empty string if no match is found.
    """
    motif_sourceversion = re.compile(r"Training\sset\sderived\sby.{1,}(?P<version>\d{1,2}\.\d{1,3})")
    matchSourceversion = re.search(motif_sourceversion, input)

    if matchSourceversion is not None:
        version=matchSourceversion.group('version')
    else:
        version=""
    
    return version

def Seqfilename_GM(input:str)->str:
    """
    Extracts the sequence file name from the input data using a regular expression.

    - Searches the input string for a pattern matching "Sequence file: <filename>.fna".
    - If a match is found, it returns the sequence file name, else returns an empty string.

    Args:
        input (str): The input data to search for the sequence file name.

    Returns:
        str: The extracted sequence file name as a string (e.g., "example.fna"), or an empty string if no match is found.
    """
    motif_Seqfilename = re.compile(r"(?P<Seqfilename>Sequence\sfile:.{1,}\.fna)")
    matchSeqfilename = re.search(motif_Seqfilename, input)
    
    if matchSeqfilename is not None:
        Seqfilename=matchSeqfilename.group('Seqfilename')
    else:
        Seqfilename=""
    
    return Seqfilename

def ModelInformation_GM(input:str)->str:
    """
    Extracts the model information from the input data using a regular expression.

    - Searches the input string for a pattern matching "Matrix: <model information>".
    - If a match is found, it returns the model information, else returns an empty string.

    Args:
        input : The input data to search for the model information.

    Returns:
        The extracted model information as a string, or an empty string if no match is found.
    """
    motif_ModelInformation = re.compile(r"Matrix:\s(?P<ModelInformation>.{1,})")
    matchModelInformation = re.search(motif_ModelInformation, input)
    
    if matchModelInformation is not None:
        ModelInformation=matchModelInformation.group('ModelInformation')
    else:
        ModelInformation=""
    
    return ModelInformation

def Date()->list[str]:
    """
    Retrieves the current date and time in a specific formatted structure.
    - Uses the current system date and time to generate a formatted string.
    - Returns the formatted date as a list in the order: [weekday, month, day, hour, minute, second, year].
    The weekday and month names are abbreviated (e.g., "Mon", "Jan").

    Returns:
        A list containing the formatted date and time as strings:
            - [weekday, month, day, hour, minute, second, year]
            For example: ["Mon", "Dec", "08", "15", "45", "30", "2024"]
    """
    date = datetime.datetime.today() #year, month, day, hour, min, sec
    wkday = date.isoweekday()
    semaine = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}
    annee = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
    date = str(date)
    y_m = date.split("-") # y=[0], m=[1]
    d = y_m[2].split(" ") # d=[0]
    h_mn = d[1].split(":") # h=[0], mn=[1]
    s = h_mn[2].split(".") # s=[0]

    LineDate = [semaine[int(wkday)], annee[int(y_m[1])], d[0], h_mn[0], h_mn[1], s[0], y_m[0]]
    return LineDate
