from parser import NginxParser

def main():
    parserLog = NginxParser("/home/user/workshop/docker_elastic/access.log")
    output = parserLog.getLog()
    print(output)


if __name__ == '__main__':
    main()