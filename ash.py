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
            kvs = kv[1].split('&&',1);
            if os.path.exists(kvs[0].strip(' ')) == True:
                os.chdir(kvs[0].strip(' '));
                os.system(kvs[1]);
            else:
                print('cd: 目录 %s 不存在'%kvs[0]);
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
        commer(comm);
    except Exception as e:
        print('Something Error happened...'+e);