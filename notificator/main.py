from parser import NginxParser
import time

parserLog = NginxParser("/var/log/nginx/access.log")


def main():
    log = parserLog.raw_log(read=True)
    lastline = parserLog.log_last_line()
    result = []
    while True:
        log_diff = get_log_diff(lastline)
        lastline = get_last_line(log_diff)
        for line in log_diff:
            if parserLog.get_path(line) == "/app/kibana":
                result.append(line)
        show_output(result)
        result.clear()
        time.sleep(30)


def get_log_diff(lastline):
    log = parserLog.raw_log(read=True)
    lineposition = 0
    for line in range(len(log)-1,-1,-1):
        if log[line] == lastline:
            print("LastLine {}".format(lastline))
            print(len(log[line:]))
            lineposition = line
            break
    return log[lineposition:]


#TODO it almost full copy of method in class NginxParser
def get_last_line(log):
    counter = -1
    while True:
        if log == [] or -counter > len(log):
            return ""
        if log[counter] != "":
            return log[counter]
        counter = counter - 1


def show_output(result):
    print("Last kibana entries")
    for line in result:
        print(line)


if __name__ == '__main__':
    main()