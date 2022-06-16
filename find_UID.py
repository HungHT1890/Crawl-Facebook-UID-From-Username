from importlib import import_module
from requests import session
ss = session()
from time import sleep
import os,threading,re
hits,false,error = 0,0,0
os.system('title FB ID - Hits: {} False: {} Error: {}'.format(hits,false,error))
def findUID(username):
    global hits,false,error
    api = f'https://m.facebook.com/{username}'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    uid = ss.get(api,headers=header)
    if uid.status_code == 200:
        try:
            id = re.findall(r'entity_id:(.*?)}',uid.text)[0]
            print(f'{username} ===> {id}')
            with open('ID.txt','a',encoding='utf-8') as saveHits:
                saveHits.write(id+'\n')
                hits +=1
        except:
            print(f"False: {username}")
            with open('False.txt','a',encoding='utf-8') as saveFalse:
                saveFalse.write(username+'\n')
                false +=1
    else:
        print('Error: {username}')
        error +=1
    os.system('title FB ID - Hits: {} False: {} Error: {}'.format(hits,false,error))
with open('data.txt','r',encoding='utf-8') as readFile:
    data = readFile.readlines()
print('hungsaki2003@gmail.com - t.me/hunght1890')
thread_count = int(input('Enter Thread: '))
os.system('cls')
def runTools(thread_step):
    for i in range(thread_step,len(data),thread_count):
        username = data[i].strip()
        findUID(username)
        sleep(0.5)
for x in range(thread_count):
    newThread = threading.Thread(target=runTools,args=(x,))
    newThread.start()