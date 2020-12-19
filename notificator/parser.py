import re


class NginxParser():

    def __init__(self, filename):
        self.parsedLog = {}
        self.filename = filename
        self.data = ""

    def _read_data(self, filename="/var/log/nginx/access.log"):
        with open(filename, "r") as file:
            self.data = file.read()

    def get_timestamp(self, string):
        if string != "":
            regex = re.search(r'(\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2})', string)
            return regex.group(0)
        return ""

    def get_ip(self, string):
        if string != "":
            regex = re.search(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', string)
            return regex.group(0)
        return ""

    def get_http_request(self, string):
        if string != "":
            regex = re.search(r'\]\s+"(GET|POST|HEAD|PUT|DELETE|PATCH|OPTIONS)', string)
            return regex.group(1)
        return ""

    def get_path(self, string):
        if string != "":
            regex = re.search(r'(GET|POST|HEAD|PUT|DELETE|PATCH|OPTIONS)\s+(\/.*) HTTP\/1\.1', string)
            return regex.group(2)
        return ""

    def _parse_log(self):
        tmplist = list()
        self.parsedLog["logs"] = []
        for item in self.data.split("\n"):
            tmpdict = dict()
            tmpdict["timestamp"] = self.get_timestamp(item)
            tmpdict["ip_address"] = self.get_ip(item)
            tmpdict["request"] = self.get_http_request(item)
            tmpdict["path"] = self.get_path(item)
            tmplist.append(tmpdict)
        self.parsedLog["logs"] = tmplist
        return self.parsedLog

    def get_parsed_log(self, read=True):
        if read:
            self._read_data(self.filename)
        return self._parse_log()

    def raw_log(self, read=False):
        if read:
            self._read_data(self.filename)
        return self.data.split("\n")

    def log_last_line(self, read=False):
        if read:
            self._read_data(self.filename)
        counter = -1
        listdata = self.data.split("\n")
        while True:
            if listdata[counter] != "":
                return self.data.split("\n")[counter]
            if -counter == len(listdata):
                return ""
            counter = counter - 1
