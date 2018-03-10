import json

import filetype
import os
import time
import datetime
import fileType
import zipfile

def TimeStampToTime(timestamp):
        timeStruct = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

#获取文件大小
def get_FileSize(filePath):
        fsize = os.path.getsize(filePath)
        fsize = fsize/float(1024*1024)
        return round(fsize,2)

#获取文件修改时间
def get_FileModifyTime(filePath):
        t = os.path.getmtime(filePath)
        return TimeStampToTime(t)

#获取文件修改时间戳
def get_FileModifyTimeStamp(filePath):
        return os.path.getctime(filePath)
#获取文件创建时间
def get_FileCreateTime(filePath):
        t = os.path.getctime(filePath)
        return TimeStampToTime(t)

#获取文件访问时间
def get_FileAccessTime(filePath):
        t = os.path.getatime(filePath)
        return TimeStampToTime(t)


def get_FileType(filePath):
        configfile = open("./config.json",'r',encoding="utf-8")
        data = json.loads(configfile.read())

        tmp = str(os.path.basename(filePath)).split('.')
        type = None
        if (len(tmp) > 1):
                type_str = tmp[len(tmp) - 1]
                for i in data["type"]['types']:
                        if (type_str in data["type"][i]):
                                return i


        type = filetype.guess(filePath)
        if type is None:
                tmp = fileType.filetype(filePath)
                if (tmp != "unknown"):
                        return tmp
                else:
                        return None

        else:
                return str(type).split('.')[2]

def zip_dir(file_path, zfile_path):
        '''
        function:压缩
        params:
            file_path:要压缩的件路径,可以是文件夹
            zfile_path:解压缩路径
        description:可以在python2执行
        '''
        filelist = []
        if os.path.isfile(file_path):
                filelist.append(file_path)
        else:
                for root, dirs, files in os.walk(file_path):
                        for name in files:
                                filelist.append(os.path.join(root, name))
                                print('joined:', os.path.join(root, name), dirs)

        zf = zipfile.ZipFile(zfile_path, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
                arcname = tar[len(file_path):]
                print(arcname, tar)
                zf.write(tar, arcname)
        zf.close()

def unzip_file(zfile_path, unzip_dir):
        '''
        function:解压
        params:
            zfile_path:压缩文件路径
            unzip_dir:解压缩路径
        description:
        '''
        try:
                with zipfile.ZipFile(zfile_path) as zfile:
                        zfile.extractall(path=unzip_dir)
        except zipfile.BadZipFile as e:
                print(zfile_path + " is a bad zip file ,please check!")


# print(get_FileType('/Users/mac/Desktop/uzerme.dmg'))