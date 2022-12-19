#coding=utf-8
import os;
import getpass;
import sys;
print('''Crillerium Agent Shell
(C) Crillerium LLC。保留所有权利。
''');
user = getpass.getuser();
cwd = os.getcwd();
ash = os.getenv('ashdir');

f = open(ash+"/.shortcut","r");
lines = f.readlines();
comms = {};
for line in lines:
    kv = line.split('@',1);
    comms[kv[0]] = kv[1];
f.close();

f = open(ash+"/.env","r");
lines = f.readlines();
for line in lines:
    kv = line.split('@',1);
    os.environ[kv[0]] = os.getenv(kv[0])+';'+kv[1];
f.close();

def commer(comm):
    if comm == 'exit':
        sys.exit();
    elif comm.find('cd ') == 0:
        kv = comm.split(' ',1);
        if os.path.exists(kv[1]):
            os.chdir(kv[1]);
        else:
            print('cd: 目录 %s 不存在'%kv[1]);
    elif comm in comms:
            os.system(comms[comm]);
    else:
            os.system(comm);

f = open(ash+"/.launch","r");
lines = f.readlines();
for comm in lines:
    commer(comm);
f.close();

print('当前用户：'+user);
print('当前目录：'+cwd);
while True:
    try:
        comm = input('>>> ');
        if comm.find('&&') > 0:
            eachs = comm.split('&&');
            for each in eachs:
                each = each.strip();
                commer(each);
        else:
            commer(comm);
    except Exception as e:
        print('Caught Error:'+e);