#!/usr/bin/env python
import re

'''
Allow to convert GeneMarkHMM LST file to GFF file
'''
def Seq_GMH(input:str)->str:
    """
    Extracts the sequence definition line from the input data using a regular expression.
    
    - Searches the input string for a line matching the pattern "FASTA definition line: <sequence>".
    - If a match is found, extracts and returns the sequence portion, else returns an empty string.
    
    Args:
        input (str): The input data to search for the sequence definition line.
    
    Returns:
        str: The extracted sequence definition line, or an empty string if no match is found.
    """
    motif_Seq = re.compile(r"(?P<Other>FASTA\sdefinition\sline:\s)(?P<Seq>.{1,})")
    matchSeq = re.search(motif_Seq, input)
    
    if matchSeq is not None:
        Seq=matchSeq.group('Seq')
    else:
        Seq=""
    
    return Seq

def Create_Tab_GMH(input:str)->list:
    """
    Parses input data to create a dictionary of sequence features with their strand, left, and right endpoints.

    - Iteratively searches the input for lines matching the pattern:
      "<number> <strand> <left-end> <right-end>".
    - Stores each match as a list in a dictionary, where keys are sequential indices (starting from 0).
    - Continues searching for matches until no further lines are found.

    Args:
        input (str): The input data to parse for sequence features.

    Returns:
        list: A list containing:
            - The total number of features found (int).
            - A dictionary (dict) with sequential indices as keys and feature details as values, 
              where each value is a list: [strand, left-end, right-end].
    """
    tab, n = {}, 1
    
    motifTab = re.compile(re.escape(str(n))+r"\s{1,}(?P<Strand>[+,-])\s{1,}(?P<LeftEnd><{0,1}\d{1,10})\s{1,}(?P<RightEnd>>{0,1}\d{1,10})")
    matchLine = re.search(motifTab, input)
    if matchLine is not None:
        Line = [matchLine.group("Strand"), matchLine.group("LeftEnd"), matchLine.group("RightEnd")]
    
    while matchLine is not None :
        tab[n-1]=Line
        n+=1
        motifTab = re.compile(re.escape(str(n))+r"\s{1,}(?P<Strand>[+,-])\s{1,}(?P<LeftEnd><{0,1}\d{1,10})\s{1,}(?P<RightEnd>>{0,1}\d{1,10})")
        matchLine = re.search(motifTab, input)
        if matchLine is not None:
            Line = [matchLine.group("Strand"), matchLine.group("LeftEnd"), matchLine.group("RightEnd")]
    
    return [n-1,tab]


'''
Allow to convert GeneMark file to GFF file
'''
def Seq_GM(input:str)->str:
    """
    Extracts the sequence information from the input data using a regular expression.

    - Searches the input string for a line matching the pattern "Sequence: <sequence>".
    - If a match is found, extracts and returns the sequence portion, else returns an empty string.

    Args:
        input (str): The input data to search for the sequence information.

    Returns:
        str: The extracted sequence, or an empty string if no match is found.
    """
    motif_Seq = re.compile(r"(?P<Other>Sequence:\s)(?P<Seq>.{1,})")
    matchSeq = re.search(motif_Seq, input)
    
    if matchSeq is not None:
        Seq=matchSeq.group('Seq')
    else:
        Seq=""
    
    return Seq

def Create_Tab_GM(input:str)->list:
    """
    Parses GeneMark input data to create a structured table of gene information.

    - Identifies features such as strand, left and right ends, probability, and sequence type (CDS/ATG).
    - Iteratively matches data lines using a regular expression and stores information in a dictionary.
    - Handles duplicate features, selecting the one with the highest probability and marking it as an "ATG".
    - Generates annotations for each feature, adding gene-specific details.
    - Creates a separate dictionary for features marked as "ATG".

    Args:
        input (str): The GeneMark output data to parse.

    Returns:
        list: A list containing:
            - The total number of valid features (`taille`) as an integer.
            - A dictionary (`tab`) with indices as keys and feature details as values. 
              Each value is a list with the following structure:
              [strand, left-end, right-end, CDS index, sub-index, probability, feature type (CDS/ATG), annotation].
    """
    tab, taille, index, i = [], 0, 0, 0
    Line = ["0-Strand", "1-LeftEnd", "2-RightEnd", "3-IndexCDS", "4-Index", "5-Proba", "6-CDS/ATG", "7-note"]
    motifTab = re.compile(r"\s{1,}(?P<LeftEnd><{0,1}\d{1,10})\s{1,}(?P<RightEnd>>{0,1}\d{1,10})\s{1,}(?P<Strand>\w{6,10})\s{1,}(?P<Other>fr\s\d\s{1,}\d.\d{2})\s{1,}(?P<Proba>.{4})")
    matchLine = re.finditer(motifTab, input)
    
    if matchLine is not None :
        for element in matchLine:
            if element.group("Strand")=="direct":
                strand="+"
            else:
                strand="-"
            if element.group("LeftEnd")!=Line[1] and element.group("RightEnd")!=Line[2]:
                index+=1
                i=0
            i+=1
            Line = [strand, element.group("LeftEnd"), element.group("RightEnd"), index, i, element.group("Proba"), "CDS", "."]
            if float(element.group("Proba"))<=1 or element.group("Proba")=="....":
                tab.append(Line)
                taille+=1
            
    proba, positionATG, position = 0, 0, 0
    while position<taille:
        try:
            if tab[position][3]==tab[position+1][3] :
                if float(tab[position][5])>proba:
                    proba=float(tab[position][5])
                    positionATG=position
            else:
                if float(tab[position][5])>proba:
                    positionATG=position
                tab[positionATG][6]="ATG"
                positionATG=position
                proba=0
        except:
            if float(tab[position][5])>proba:
                positionATG=position 
            tab[positionATG][6]="ATG"
        position+=1

    position=0
    while position<taille:
        if tab[position][6]=="ATG":
            new_line = tab[position].copy()
            tab.insert(position+1, new_line)
            tab[position+1][6]="CDS"
            taille+=1
            tab[position][7]="."
            tab[position][2]=int(tab[position][1])+2
        else:
            tab[position][7]="gene GM_CDS_"+str(tab[position][3])+"."+str(tab[position][4])
        position+=1
        
    return [taille,tab]


'''
Allow to convert ScanForMatches file to GFF file
'''
def Create_Tab_SFM(input:str)->list:
    """
    Parses Sequence Feature Model (ScanForMatches) data and creates a structured table of sequence features.

    - Uses a regular expression to match sequence features in the input data, extracting the sequence name,
      left and right endpoints, and associated notes. Stores each feature as a list.
    - Creates a dictionary where each key is a feature index, and each value is the corresponding feature details.

    Args:
        input (str): The Sequence Feature Model data to parse.

    Returns:
        list: A list containing:
            - The total number of features (`n`) as an integer.
            - A dictionary (`tab`) where each key is an index and each value is a list with the structure:
              [sequence name, left-end, right-end, note].
    """
    tab, n = {}, 0
    
    motifTab = re.compile(r">(?P<Seq>.{1,}):\[(?P<LeftEnd>\d{1,}),(?P<RightEnd>\d{1,})\]\n(?P<Note>[^>\n]{1,})")
    matchLine = re.finditer(motifTab, input)
    if matchLine is not None:
        for element in matchLine:
            tab[n] = [element.group("Seq"), element.group("LeftEnd"), element.group("RightEnd"), element.group("Note")]
            n+=1
    
    return [n,tab]
