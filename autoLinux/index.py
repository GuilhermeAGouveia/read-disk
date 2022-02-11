import os


class Autolinux:
    def __init__(self, os):
        self.os = os

    def processDirectory(self, path=""):
        print("Coletando dados...")
        result = os.popen("ls -p -a | grep /").read()
        result = result.split('\n')
        result.pop(0)
        result.pop(0)

        result.remove

        arrayResult = []

        for i in result:
            if i != '':
                tmp = os.popen(f"du -hsk {i}").read()
                tmp = tmp.split('\t')
                arrayResult.append({
                    "name": tmp[1].replace('\n', ''),
                    "size": int(tmp[0])
                })
        return arrayResult

    def listDirectorySpace(self):
        arrayResult = self.processDirectory()
        print("Processando informação...")
        arrayResult.sort(key=lambda s: s["size"])
        sum = 0
        for info in arrayResult:
            sum += info["size"]
        print(f"{round(sum / 1024, 2)} MB")
