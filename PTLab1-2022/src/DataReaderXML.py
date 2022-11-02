import xml.etree.ElementTree as ET
from DataReader import DataReader


class DataReaderXML(DataReader):
    def read(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        result = []
        for item in root:
            name = item[0].text
            score = {t[0].text: int(t[1].text) for t in item[1]}
            result.append({"name": name, "score": score})
        return result
