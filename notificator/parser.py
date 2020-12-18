import re


class NginxParser():

    def __init__(self, filename):
        self.parsedLog = {}
        self.filename = filename
        self.data = ""

    def _read_data(self):
        with open(self.filename, "r") as file:
            self.data = file.read()

    def _get_timestamp(self,string):
        regex = re.search(r'(\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2})', string)
        print(regex.group(0))
        return regex.group(0)

    def _get_ip(self, string):
        regex = re.search(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', string)
        return regex.group(0)

    def _get_http_request(self,string):
        regex = re.search(r'\]\s+"(GET|POST|HEAD|PUT|DELETE|PATCH|OPTIONS)', string)
        return regex.group(1)

    def _parse_log(self):
        tmpList = []
        tmpDict = {}
        self.parsedLog["logs"] = []
        for item in self.data.split("\n"):
            tmpDict["timestamp"] = self._get_timestamp(item)
            tmpDict["ip_address"] = self._get_ip(item)
            tmpDict["request"] = self._get_http_request(item)
            tmpList.append(tmpDict)
            tmpDict = {}
        self.parsedLog["logs"] = tmpList
        return self.parsedLog

    def getLog(self):
        self._read_data()
        return self._parse_log()
