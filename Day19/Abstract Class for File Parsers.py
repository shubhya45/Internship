# Abstract Class for File Parsers

# Create an abstract class named FileParser with an abstract method parse(data).

# Create concrete classes:

# JSONParser that implements parse(data) method and prints: “Parsing JSON data...”

# XMLParser that implements parse(data) method and prints: “Parsing XML data...”

# Test both classes.
from abc import ABC, abstractmethod
class File_Persers(ABC):
    # @abstractmethod
    def parse(data):
        pass
class JSONParser(File_Persers):
    def parse(data):
        print("parsing JSON data............")
class XMLParser(JSONParser):
    def parse(data):
        print("parsing XML data.............")
js=JSONParser()
js.parse()
xm=XMLParser()
xm.parse()