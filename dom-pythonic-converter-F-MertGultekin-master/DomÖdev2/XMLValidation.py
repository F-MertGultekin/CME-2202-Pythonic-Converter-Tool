from lxml import etree as ET

def xmlValidation(inputFile,outputFile):
    xml_file = ET.parse(inputFile)
    xml_validator = ET.XMLSchema(file=outputFile)

    is_valid = xml_validator.validate(xml_file)

    print(is_valid)

