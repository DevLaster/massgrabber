import os
import re
import sys
import requests
import platform
from urllib.parse import urlparse


if sys.platform:
   purple = '\033[95m'
   blue = '\033[94m'
   cyan = '\033[96m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   end = '\033[0m'
   bold = '\033[1m'
   u = '\033[4m'
else:
   purple = ''
   blue = ''
   cyan = ''
   green = ''
   yellow = ''
   red = ''
   end = ''
   bold = ''
   u = ''

if sys.platform == 'win32':
   os.system('cls')
else:
   os.system('clear')

class Pausi:
   PHPSESSID = ''
   ZHE = ''
   Url = ''
   Python_Version = ''
   def __init__(self, PHPSESSID, ZHE):
      self.PHPSESSID = PHPSESSID
      self.ZHE = ZHE
      self.ResultFileName = ''
      self.Python_Version = platform.python_version()
   def save(self, name, isi, a='a'):
      try:
         op = open(name,a)
         op.write(isi)
         op.close()
      except:
         pass
   def input_phpsessid(self):
      print ('Input PHPSESSID')
      self.PHPSESSID = self.input('PHPSESSID=')
      if self.PHPSESSID:self.save('.PHPSESSID',self.PHPSESSID, 'w')
   def input_zhe(self):
      print ('Input ZHE')
      self.ZHE = self.input('ZHE=')
      if self.ZHE:self.save('.ZHE',self.ZHE, 'w')
   def get_urls(self, source):
      r = re.findall('''<td>(.+?)
							</td>''',source)
      return r # source
      #for x in r:
      #  url = urlparse('http://'+x).netloc
      #  print url
   def Grab(self):
    #for pg in range(50):
    if not self.ResultFileName:
      print ('Input Result File Name:')
      try:
        self.ResultFileName = self.input('[Ex:Result.txt]=> ')
        if not self.ResultFileName: self.ResultFileName = 'Results.txt'
        print ('Results will be stored in: %s\n\n>_Start.' % (self.ResultFileName))
      except:pass
    i = 1
    while i<=50:
     try:
      self.Url = self.SetUrl+'page='+str(i+0)
      cookies = {
         'PHPSESSID' : self.PHPSESSID,
         'ZHE'       : self.ZHE
      }
      req = requests.get(self.Url, cookies=cookies)
      if '''<input type="text" name="captcha"''' in req.text:
         print ('Captcha')
         self.input_zhe()
      if '''<html><body>-<script type="text/javascript"''' in req.text:
        print ('Maybe Error PHPSESSID && ZHE')
        self.input_phpsessid()
        self.input_zhe()
      else:
        so = self.get_urls(req.text)
        i +=1
        if so:
          print ('\n'+red+self.Url)
          for x in so:
             url = urlparse('http://'+x).netloc
             print (blue+url)
             self.save(self.ResultFileName, url+'\n')
        else:break
     except KeyboardInterrupt:
        print ('Ctrl + C detect!')
        exit()
     except ValueError as ve:
      print (ve) #pass
   def input(self, q):
      #input based on python version
      if int(self.Python_Version[0]) == 3:
           return input(str(q))
      elif int(self.Python_Version[0]) == 2:
           return input(str(q))
   def menu(self):
       print ('''%s


███╗░░░███╗░█████╗░░██████╗░██████╗░██████╗░██████╗░░█████╗░██████╗░██████╗░███████╗██████╗░
████╗░████║██╔══██╗██╔════╝██╔════╝██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██╔████╔██║███████║╚█████╗░╚█████╗░██║░░██╗░██████╔╝███████║██████╦╝██████╦╝█████╗░░██████╔╝
██║╚██╔╝██║██╔══██║░╚═══██╗░╚═══██╗██║░░╚██╗██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝░░██╔══██╗
██║░╚═╝░██║██║░░██║██████╔╝██████╔╝╚██████╔╝██║░░██║██║░░██║██████╦╝██████╦╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝

%s # --%s  Coder: Laster
%s # --%s  Discord: 357r
%s # --%s  Enjoy (:

%s1.%s Mass Grab notifier
%s2.%s single grab notifier
%s3.%s grab from Special Archive
%s4.%s grab from Archive
%s5.%s grab from onhold%s
''' % (red,red,green,red,green,red,green,red,blue,red,blue,red,blue,red,blue,red,blue,end))
       try:
        menu = int(self.input('choose~$ '))
        if menu == 1:
          list = self.input('List Nick-> ')
          if list and os.path.isfile(list):
            pausiGans = open(list, 'r').read().strip().split('\n')
            for u in pausiGans:
             try:
              if u:
                self.SetUrl = 'http://zone-h.org/archive/notifier='+u+'?'
                self.Grab()
             except:pass
          else:
            print ('your list is not found')
        elif menu == 2:
          self.notifier = self.input('Notifier=> ')
          if self.notifier:
             self.SetUrl = 'http://zone-h.org/archive/notifier='+self.notifier+'?'
             self.Grab()
          else: pass
        elif menu == 3:
          self.SetUrl = 'http://zone-h.org/archive/special=1/'
          self.Grab()
        elif menu == 4:
          self.SetUrl = 'http://zone-h.org/archive/'
          self.Grab()
        elif menu == 5:
         self.SetUrl = 'http://www.zone-h.org/archive/published=0/'
         self.Grab()
        else:
          print ('Error -> Exit.')
        print (end)
       except ValueError:
         print ('ValueError ~> Error ~> Exit.')
       except:pass



if __name__ == '__main__':
     if os.path.isfile('.PHPSESSID'): PHPSESSID = open('.PHPSESSID','r').read().strip()
     else:PHPSESSID = ''
     if os.path.isfile('.ZHE'): ZHE = open('.ZHE','r').read().strip()
     else:ZHE = ''
     pausi = Pausi(PHPSESSID, ZHE)
     pausi.menu()
