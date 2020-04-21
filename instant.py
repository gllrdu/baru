"""Release Version V.1"""
#import module
import os
import ast
import requests
from time import sleep
from bs4 import BeautifulSoup

        ##  ALL Personal Function Here  ##
#Clear Screen Finctiom
def hapus():
  if os.name=='nt':
    os.system('cls')
  else:
    os.system('clear')
    
#Checking folder
if not os.path.exists('data/result'):
    os.makedirs('data/result')
    
def myformat(nama,nilai):
    return "{:<25}  {:>0}".format(nama,nilai)
def myformat1(nama,nilai):
    return "{:<20}  {:>0}".format(nama,nilai)

#To show response from target host
def result(parsed):
  component = {
    'Cache-Control',
    'Connection',
    'Content-Length',
    'Content-Type',
    'Location',
    'Server',
    'Transfer-Encoding',
    'Vary',
    'X-Android-Received-Millis',
    'X-Android-Sent-Millis',
    'X-Android-Response-Source',
    'X-Android-Selected-Protocol',
    'X-XSS-Protection'
  }
  for com in component:
    try:
      print(myformat('\033[33m'+com,' : \033[37m'+parsed[com]))
    except: ga_kepake=1
    
    
#Write result to file
def hasil(mode,parsed,url,status,proxy):
  if status==200:
    s200.write('________________________\n')
    if mode=='1':
      s200.write('  '+url+'\n')
    if mode=='2':
      s200.write('  '+url+'\n')
      s200.write('  '+proxy+'\n')
    s200.write('Status : '+str(status)+'\n')
    for j in parsed:
      s200.write(j+' : '+parsed[j]+'\n')
    s200.write('\n')
    
  if status >=300 and status<400:
    s30x.write('________________________\n')
    if mode=='1':
      s30x.write('  '+url+'\n')
    if mode=='2':
      s30x.write('  '+proxy)
    for j in parsed:
      s30x.write(j+' : '+parsed[j]+'\n')
    s30x.write('\n')
    
  if status >=400 and status<500 :
    s40x.write('________________________\n')
    if mode=='1':
      s40x.write('  '+url+'\n')
    if mode=='2':
      s40x.write('  '+url+'\n')
      s40x.write('  '+proxy+'\n')
    s40x.write('Status : '+str(status)+'\n')
    for j in parsed:
      s40x.write(j+' : '+parsed[j]+'\n')
    s40x.write('\n')
    
  if status >=500 and status<600 :
    s50x.write('________________________\n')
    if mode=='1':
      s50x.write('  '+url+'\n')
    if mode=='2':
      s50x.write('  '+url+'\n')
      s50x.write('  '+proxy+'\n')
    s50x.write('Status : '+str(status)+'\n')
    for j in parsed:
      s50x.write(j+' : '+parsed[j]+'\n')
    s50x.write('\n')
  

#Function Welcome (Biar gampang klo mau makek di script lain :v)
def welcome():
  def prints(p1, p2):
    return "{:<22}  {:>0}".format(p1, p2)
  print('\033[32m')
  print(prints('         _____','| INSTANT'))
  print(prints('        / //  \\','|    HOST'))
  print(prints('       / // /\\ \\','|      CHECKER'))
  print(prints('      / // /__\\_\\','| v.1'))
  print(prints('     / //_______ \\','|'))
  print(prints('    / //_/______\\ \\','| Created by.'))
  print(prints('   / //____________\\','|   Luthfi zXc'))
  print(prints('   \\_______________/','|'))
  print('\n\033[31m        Yt: \033[33mhttp://youtube.com/luthfizxc')

#open bug list
xzxx = open('data/bug.txt','a+')
bug_list  = open('data/bug.txt','r+')

#open proxy list
zxzz = open('data/proxy.txt',  'a+')
proxy_list = open('data/proxy.txt',  'r+')

#create and write scanned host
s200 = open('data/result/200OK.txt', 'a+')
s30x = open('data/result/30x.txt','a+')
s40x = open('data/result/40x.txt',   'a+')
s50x = open('data/result/50x.txt',   'a+')

#Checking if file content is empty
cek_proxy = os.stat('data/proxy.txt').st_size != 0
cek_bug = os.stat('data/bug.txt').st_size != 0

#Your variable here
to = 5  #timeout variable for requests module


#text format
def prints(p1,p2):
  return "{:<18}  {:>0}".format(p1,p2)

#Welcome & Menu screen
hapus()
welcome()
def menu():
  print('\033[35m   ___________________________________________')
  print('\033[35m ||                \033[31m>\033[32m>\033[33m> \033[92mMENU\033[33m <\033[32m<\033[31m<              \033[35m ||')
  print('\033[35m ||___________________________________________\033[35m||')
  print('\033[35m ||   \033[31m>\033[33m  1. Direct Host Checker              \033[35m ||')
  print('\033[35m ||   \033[31m>\033[33m  2. Check Host with Proxy            \033[35m ||')
  print('\033[35m ||                                          \033[35m ||')
  print('\033[35m ||   \033[34m>  0. Help                             \033[35m ||')
  print('\033[35m ||   \033[34m>  9. Exit                             \033[35m ||')
  print('\033[35m ||___________________________________________\033[35m||')
menu()


###       Yeahh...... main program...     ###
def main():
  mode = input('  Pilih Mode: ')
  global count
  count=0
    #checking mode from input
  if mode == '1':
    hapus()
    welcome()
    #reading bug list
    if cek_bug == True:
      for a in bug_list:
        count = count+1                   #counter
        print('\n\033[32m'+str(count))    #print counter
        bug = a.replace('\n','')          #delete newline text
        cek = None
        #getting server response
        if 'https' in bug:
          try:
            cek = requests.get(bug, timeout=to)
            #print(bug,cek.status_code)
          except:
            print('\033[31m'+bug,'No Response')
        else:
          try:
            cek = requests.get('https://'+bug, timeout=to)
            #print(bug,cek.status_code)
          except:
            print('\033[31m'+bug,'No Response')
        #print(cek)
        if cek != None:
          soup = BeautifulSoup(cek.text, "html.parser")
          status = cek.headers
          parsed = ast.literal_eval(str(status))
          print('\033[32m '+bug)
          print(myformat('\033[33mStatus',' : '+str(cek.status_code)))
          result(parsed)
          hasil(mode,parsed,bug,cek.status_code,0)
    if cek_bug == False:
      print('\033[31m\nList Bug Kosong!')
      print('\033[33mSilahkan isi file terlebih dahulu')
      print('Lokasi file :')
      print(os.getcwd() + '/data/bug_list.txt')
      input('Press enter to exit...')
      exit()
    exit()


#mode 2 , host check with proxy
  if mode=='2':
    hapus()
    welcome()
    cek = None
    print('menu :')
    print('1. Masukkan Proxy')
    print('2. Gunakan proxy dari proxy list')
    b = input('Pilih menu :')
    if int(b)==1:
      hapus()
      welcome()
      c = str(input('Masukan proxy mu (ip:port) : '))
      pxy = c
      for a in bug_list:
        bug = a.replace('\n', '')
        count = count + 1
        proxy = {
          'http': 'http://' + pxy,
          'https': 'https://' + pxy
        }

        if 'https' in bug:
          try:
            cek = requests.get(bug, proxies=proxy, timeout=to)
            print('\n\033[32m' + str(count))
            # print(bug,cek.status_code)
          except:
            print('\n\033[32m' + str(count) + '\033[31m No Response')
            print('URL    : ' + bug)
            print('Proxy  : ' + pxy)
        else:
          try:
            cek = requests.get('https://' + bug, proxies=proxy, timeout=to)
            print('\n\033[32m' + str(count))
            # print(bug,cek.status_code)
          except:
            print('\n\033[32m' + str(count) + '\033[31m No Response')
            print('URL    : ' + bug)
            print('Proxy  : ' + pxy)
        # print(cek)

        if cek != None:
          soup = BeautifulSoup(cek.text, "html.parser")
          status = cek.headers
          parsed = ast.literal_eval(str(status))
          print('\033[32mURL    : ' + bug)
          print('Proxy  : ' + pxy)
          print('\033[33mStatus :', str(cek.status_code))
          result(parsed)
          hasil(mode, parsed, bug, cek.status_code, pxy)

    if int(b)==2:
      if cek_proxy and cek_bug:
        for z in proxy_list:
          bug_list.seek(0,0)
          #print(proxy_list)
          for a in bug_list:
            bug = a.replace('\n','')
            count = count+1
            pxy = z.replace('\n', '')
            #print(pxy)
            proxy = {
              'http': 'http://' + pxy,
              'https': 'https://' + pxy
            }

            if 'https' in bug:
              try:
                cek = requests.get(bug, proxies=proxy, timeout=to)
                print('\n\033[32m' + str(count))
                # print(bug,cek.status_code)
              except:
                print('\n\033[32m' + str(count) + '\033[31m No Response')
                print('URL    : ' + bug)
                print('Proxy  : ' + pxy)
            else:
              try:
                cek = requests.get('https://' + bug, proxies=proxy, timeout=to)
                print('\n\033[32m' + str(count))
                # print(bug,cek.status_code)
              except:
                print('\n\033[32m' + str(count) + '\033[31m No Response')
                print('URL    : ' + bug)
                print('Proxy  : ' + pxy)
            # print(cek)

            if cek != None:
              soup = BeautifulSoup(cek.text, "html.parser")
              status = cek.headers
              parsed = ast.literal_eval(str(status))
              print('\033[32mURL    : ' + bug)
              print('Proxy  : ' + pxy)
              print('\033[33mStatus :', str(cek.status_code))
              result(parsed)
              hasil(mode,parsed,bug,cek.status_code,pxy)

      else:
        if cek_bug == False:
          print('\033[31m\nList Bug Kosong!')
          print('\033[33mSilahkan isi file terlebih dahulu')
          print('Lokasi file :')
          print(os.getcwd()+'/data/bug_list.txt')
          input('Press enter to exit...')
          exit()
        if cek_proxy == False:
          print('\033[31m\nList Proxy Kosong!')
          print('\033[33mSilahkan isi file atau pilih menu yang lain')
          print('Lokasi file :')
          print(os.getcwd()+'/data/proxy_list.txt')
          input('Press enter to return to menu...')
          welcome()
          menu()
          main()
    exit()

  #Help program
  if mode == '0':
    
    hapus()
    welcome()
    print('Subscribe YT : http://youtube.com/luthfizxc',
               '\n______________________________',
               '\n\033[32mPenjelasan menu dari script ini\033[33m',
         
                '\n1. Direct host checker',
                '\n        Cek respon dari bug dengan metode get secara direct',
                '\n2. Check Host with proxy',
                ' \n       Cek respon bug menggunakan dengang metode get menggunakan proxy',
                '\n\n\033[32mDi menu no. 2 ini ada pilihan lagi\033[33m',
                '\n1. Masukkan proxy',
                '\n        Ketik proxy yang akan digunakan untuk mengecek bug dengan formar ip:port',
                '\ncontoh :  103.25.20.30:8080',
                '\n2. Gunakan proxy dari proxy list',
                '\n        Mengecek bug menggunakan proxy list yang sudah diisi tadi'
                )
    input('Press enter to return to menu ')
    hapus()
    welcome()
    menu()
    main()
  if mode == '9':
    print('\033[31m Exit.....\033[37m')
    exit()
  else:
    print('\033[31mInvalid input\n  Please try again')
    sleep(2)
    hapus()
    welcome()
    menu()
    main()

main()
print('\033[37m')

    