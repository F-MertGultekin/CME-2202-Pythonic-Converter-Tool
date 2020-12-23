from CSVtoXML import CsvToXml
from XmlToCsv import XmlToCsv
from XMLtoJSON import XmlToJson
from JSONtoXML import JsonToXml
from CSVtoJSON import CsvToJson
from JSONtoCSV import JsonToCsv
from XMLValidation import xmlValidation
import sys


inputFile=sys.argv[1]
outputFile=sys.argv[2]
if sys.argv[3]=='1':
    CsvToXml(inputFile,outputFile)
if sys.argv[3]=='2':
    XmlToCsv(inputFile,outputFile)
if sys.argv[3]=='3':
    XmlToJson(inputFile,outputFile)
if sys.argv[3]=='4':#kullanılmayan bir şey var departmnet name
    JsonToXml(inputFile,outputFile)
if sys.argv[3]=='5':
    CsvToJson(inputFile,outputFile)
if sys.argv[3]=='6':
    JsonToCsv(inputFile,outputFile)
if sys.argv[3]=='7':
    xmlValidation(inputFile,outputFile)