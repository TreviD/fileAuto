import json
import util
import os
import time
import shutil


def isDir(dirPath):
    return os.path.isdir(dirPath)


def isFile(filePath):
    return os.path.isfile(filePath)


# 自动整理文件
def autoFile(path):
    oldDir = os.path.join(path, "old")
    if (not os.path.exists(path)):
        os.mkdir(oldDir)
    for i in os.listdir(path):
        # print(filename)
        # print(os.path.isfile(os.path.join("/Users/mac/Downloads", i)))
        absPath = os.path.join(path, i)
        if (isFile(absPath) and time.time() - float(util.get_FileModifyTimeStamp(absPath)) > delay):
            # if (time.time() - float(util.get_FileModifyTimeStamp(absPath)) > data["oldFileTime"] * 24 * 60 * 60):
            #     shutil.move(absPath, oldDir)    # 超过指定时间 移动到old文件夹内
            #     continue

            type = util.get_FileType(absPath)  # 判断类型
            if (type == None):  # 类型为None 移动到Other文件夹内
                type = "Other"
            else:  # 类型不为None
                print(absPath + " " + type)

            # 判断是否存在对应类型的文件夹 若不存在则新建
            if (not os.path.exists(os.path.join(path, type))):
                os.mkdir(os.path.join(path, type))
            # 移动文件到对应分类的文件夹中
            shutil.move(absPath, os.path.join(path, type))


def autoFloder(path):
    oldDir = os.path.join(path, "old")
    floderPath = os.path.join(path, "floder")
    if (not os.path.exists(oldDir)):
        os.mkdir(oldDir)
    if (not os.path.exists(floderPath)):
        os.mkdir(floderPath)

    for floderName in os.listdir(path):
        absPath = os.path.join(path, floderName)
        if (floderName in data["type"]["types"] or floderName in data["exclude"]):
            continue

        # print(time.time() - float(util.get_FileModifyTime(absPath) > delay))
        if (isDir(absPath) and time.time() - float(util.get_FileModifyTimeStamp(absPath) > delay)):
            if (time.time() - float(util.get_FileModifyTimeStamp(absPath)) > data["oldFileTime"] * 24 * 60 * 60):
                # zipfle = os.path.join(path, str(floderName)+".zip")
                # util.zip_dir(absPath, zipfle)
                shutil.move(absPath, oldDir)
            else:
                shutil.move(absPath, floderPath)


fileConfig = open("./config.json", 'r', encoding='utf-8')
data = json.loads(fileConfig.read())

if (data["delay"] != None):
    delay = data["delay"] * 24 * 60 * 60
else:
    delay = 999999999999999

for path in data["path"]:
    print(os.path.isdir(path))
    autoFile(path)
    autoFloder(path)
