'''
this is ftp 
'''
from ftplib import FTP

def Get():
    pass

def Put():
    pass

def Help():
    print('#'*80)
    print('Simple Ftp Client')
    print('cd(切换目录)| ls(查看目录文件)| get(下载)| put(上传)| help(获取帮助)')

server = input('请输入服务器地址:')
ftp = FTP(server)
ftp.login()
Help()

dic = {
      'ls':ftp.dir,
      'pwd':ftp.pwd,
      'get':Get,
      'put':Put,
      'help':Help
      }

while True:
    print('milo_ftp>')
    cmdsrt = input()
    cmd = cmdstr.split()
    print(cmd)
    if len(cmd) ==1:
        print('cmd[0]', cmd[0])
        if str.lower(cmd[0]) == 'quit':
            break
        else:
            dic[str.lower(cmd[0])](cmd[1])
    elif len(cmd) ==2:
        dic[str.lower(cmd[0])](cmd[1])
    else:
        Help()
ftp.quit()












