#! python2
# -*- coding: UTF-8 -*-
'''

74.0.3729.108
If you are using Chrome version 75, please download ChromeDriver 75.0.3770.8


0. Версии браузера Хром и селениум-хром должны совпадать
1. java -jar selenium-server-standalone.jar -role hub
2. java -Dwebdriver.chrome.driver=chromedriver.exe -jar selenium-server-standalone.jar -role webdriver -hub http://localhost:4444/grid/register -port 5558 -browser browserName=chrome

try:
    file = open('config-selenium.ini', 'r')
except FileNotFoundError:
    file = open('config-selenium.ini', 'w')

'''



try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0



from selenium import webdriver
import pickle,os,time,codecs
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from lxml import html
from random import random, randrange, randint
import time


'''if not os.path.exists('config-selenium.ini'):
    os.mknod('config-selenium.ini')'''
try:
    file = open('config-selenium.ini', 'r')
except:
    file = open('config-selenium.ini', 'w')
    

config = ConfigParser()
# parse existing file
config.read('config-selenium.ini')

desired_cap = { 
  'javascriptEnabled': True,
  'os' : 'Windows',
  'os_version' : '8.1',
  'browser' : 'Chrome',
  'browser_version' : '78.0',
  'chromeOptions': {
            'args': ['disable-infobars']
        },
  'resolution' : '1280x1024',
  'browserstack.local' : 'false',
  'browserstack.console' : 'info',
  'browserstack.video' : 'false',
  'browserstack.selenium_version' : '3.14.0'
}

class SessionRemote(webdriver.Remote):
    def start_session(self, desired_capabilities, browser_profile=None):
        self.w3c = True  

options = webdriver.ChromeOptions() 
options.add_argument("disable-infobars");
# options.add_argument("user-data-dir=C:\\Users\\Uuuuuser\\AppData\\Local\Google\\Chrome\\User Data\\Profile 1")

options.add_argument("user-data-dir=c:\\Users\\pletnev\\AppData\\Local\\Google\\Chrome\\User Data\\")


# options.add_argument('user-data-dir=C:\\Users\\Uuuuuser\\AppData\\Local\Google\\Chrome\\User Data')
options.add_argument('profile-directory=Profile 1')
# options.add_argument('profile-directory="Profile 1"')

if 1==2:
    driver = webdriver.Remote(command_executor='http://127.0.0.1:5558/wd/hub',desired_capabilities=options.to_capabilities())
    # driver = webdriver.Remote(command_executor='http://192.168.43.47:5558/wd/hub',desired_capabilities=options.to_capabilities()) # http://192.168.43.47/
    driver.get("http://1s.tw1.ru/")
    # #driver.quit()
    print(driver.session_id)
    config.set('init', 'session_id_lost', driver.session_id)
    with open('config-selenium.ini', 'w') as configfile:
        config.write(configfile)
    # driver.quit() 
    # exit()

try:

    print('try:')
except Exception as e:
    # print(e)
    pass


class fromxpt(object):
    def init(self, color):
        self.color = color
    
    def frst(self,obxpt,whtrm=None):
        try:
            f = (lambda a: a[0] if (whtrm is None ) else obxpt[0].split(whtrm))
            oxp=''.join(f(obxpt))
        except Exception as e:
            print e
            oxp=''
        return oxp
        
    def frtag(self,obxpt,whtrm=None):
        try:
            f = (lambda a: a[0] if (len(a)==1 ) else a)
            oxp=f(obxpt).get(whtrm).encode('utf-8').decode('utf-8')
        except Exception as e:
            # print e
            oxp=''
        return oxp        
        
    def frgrptxt(self,obxpt):
        try:
            lspret=[]
            for i in range(len(obxpt)):
                nb=obxpt[i]
                pret=nb.text_content().encode('utf-8').decode('utf-8')
                lspret.append(pret)   
            ret= ','.join(lspret)
                        
        except Exception as e:
            # print e
            ret=''
        return ret
        
    def frtxnode(self,obxpt):
        try:
            pret=obxpt[0].text_content().encode('utf-8').decode('utf-8') 
            ret= (pret)          
        except Exception as e:
            # print e
            ret=''
        return ret
        
    def cn(self,strng):
        return strng.decode('UTF-8').encode('cp1251')
# .//div[@class='match-list-item']/a/@href
tx=fromxpt()




import json,codecs


try:
    driver = SessionRemote(
      command_executor='http://127.0.0.1:5558/wd/hub'
      ,desired_capabilities=options.to_capabilities()
    )
    driver.session_id = config.get('init', 'session_id_lost')# 
    print('fine:',config.get('init', 'session_id_lost'))
except Exception as e:
    pass
    # print e
    driver = webdriver.Remote(command_executor='http://127.0.0.1:5558/wd/hub',desired_capabilities=options.to_capabilities())
    # driver = webdriver.Remote(command_executor='http://192.168.43.47:5558/wd/hub',desired_capabilities=options.to_capabilities()) # http://192.168.43.47/
    driver.get("http://1s.tw1.ru/")
    # #driver.quit()
    # print(driver.session_id)
    config.set('init', 'session_id_lost', driver.session_id)
    with open('config-selenium.ini', 'w') as configfile:
        config.write(configfile)
    print('ready:',config.get('init', 'session_id_lost'))
    # driver.quit()  
    try:
        driver = SessionRemote(
          command_executor='http://127.0.0.1:5558/wd/hub'
          ,desired_capabilities=options.to_capabilities()
        )
        driver.session_id = config.get('init', 'session_id_lost') 
        print('readyready:',config.get('init', 'session_id_lost'))
    except:
        pass
        exit()
    
    
    
    

    
    
try:
    print(driver)
    print('environ:',config.get('init', 'session_id_lost'))
    # print(config.get('init', 'session_id_lost'))
    try:
        driver.get("")
    # except WebDriverException as e:
    except Exception as e:    
        print(str(e))
        # if e.msg.strip().endswith("chrome not reachable"):
        if str(e).find('not reachable')>0 or str(e).find('already closed')>0:
            print('try...')
            driver = webdriver.Remote(command_executor='http://127.0.0.1:5558/wd/hub',desired_capabilities=options.to_capabilities())
            # driver = webdriver.Remote(command_executor='http://192.168.43.47:5558/wd/hub',desired_capabilities=options.to_capabilities()) # http://192.168.43.47/
            driver.get("http://www.google.com")
            driver.get("http://1s.tw1.ru/")
            driver.get("http://www.google.com")
            # #driver.quit()
            print(driver.session_id)

            config.set('init', 'session_id_lost', driver.session_id)
            with open('config-selenium.ini', 'w') as configfile:
                config.write(configfile)
        else:
            pass
            print('reachable))')
        
        
        
        
except Exception as e:
    print(e)
    pass


# exit()



# driver.get("http://www.google.com")
# driver.get("https://ru.stackoverflow.com/questions/1043697/%d0%9c%d1%83%d0%bb%d1%8c%d1%82%d0%b8%d1%8f%d0%b7%d1%8b%d1%87%d0%bd%d0%be%d1%81%d1%82%d1%8c-%d0%b2-bitrix")
time.sleep(randint(2,5))

mUrl="http://1s.tw1.ru/"

driver.get(mUrl)


if 1==1:    
    responsetext=driver.page_source
    parsed_body = html.fromstring(responsetext)



    xidprsn=parsed_body.xpath(".//a")
    print len(xidprsn)
    al=[]
    for i in range(len(xidprsn)):
        go=1    #get_codepage(str = None):
        nobj=xidprsn[i]
        # tagname=xidprsn[i].xpath(".//div/h2/div/@translate")
        tagname=tx.frtag(nobj,'href')
        # if len(tagname)>0 and tagname.startswith('/catalog'):  
        if len(tagname)>0 and tagname.endswith('html'):     
            al.append(tagname)
        # print(tagname)

print(al)

time.sleep(randint(3,8))

if len(al)>0:
    urlnext=al[randint(0, len(al))]
    driver.get(mUrl+''+urlnext)

# print(al)


