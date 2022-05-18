#### code by ishan oshada ####

## student manage small project  ##


import json,os,getpass,random,subprocess,sys,time,datetime
try:
  from texttable import  Texttable
except:
     print('wait for downlaod to texttable pip module ..... ')
     subprocess.getoutput('pip install texttale')
     os.system('clear')
     from texttable import  Texttable
from functools import  lru_cache

## file var ##
file = ''
size= 999999999
admin_login_file = 'admin/admin_login.json'
admin_login_error = 'admin/login_error.json'
student_come = ''
## end ##



## print and input colors ##
#@lru_cache(maxsize=size)
def print_des(dataprint): 
  end = '\x1b[0m'
  ran = '\x1b[32m'
  print(f"{ran} {dataprint} {end}")
  print("")

#@lru_cache(maxsize=size)
def input_des(entername):
  end = '\x1b[0m'
  ran = '\x1b[34m'
  ran1 = '\x1b[31m'
  userEnter = input(f"{ran} {entername} {end}{ran1}")
  print(f"{end}")
  return  userEnter

## end ## 

#@lru_cache(maxsize=size)
def slow_type(text):
     fore=['\x1b[91m','\x1b[34m','\x1b[36m','\x1b[93m','\x1b[32m','\x1b[35m','\x1b[31m','\x1b[94m','\x1b[96m','\x1b[92m','\x1b[33m','\x1b[95m','\x1b[5;30;45m']
     
     end = '\x1b[0m'
     for x in text:
          ran = random.choice(fore)
          print(ran+x+end,end="")
          sys.stdout.flush()
          time.sleep(0.03)

s_text = """
පිළිගන්නවා ##### සිසුන්ගේ තොරතුරු එක් රැස් කිරීමේ මුදුකාංගය     ( V: 1.5 )

"""
slow_type(s_text)       
#@lru_cache(maxsize=size)
def banner():
     fore=['\x1b[91m','\x1b[34m','\x1b[36m','\x1b[93m','\x1b[32m','\x1b[35m','\x1b[31m','\x1b[94m','\x1b[96m','\x1b[92m','\x1b[33m','\x1b[95m','\x1b[5;30;45m']
     ran = random.choice(fore)
     end = '\x1b[0m'
     ban = f"""{ran}
banner 
       {end}"""
     print("")
     print(ban)
     print("")
#@lru_cache(maxsize=size)
def check():
           #os.system('clear')
	      a = subprocess.getoutput("cd admin")
	      if 'No such file' in a:
	            print_des('admin mkdir ')
	            subprocess.getoutput("mkdir  admin")
	      b =  subprocess.getoutput("cd grade")
	      if 'No such file' in a:
	            print_des('grade mkdir ')
	            subprocess.getoutput("mkdir grade")
	      
	      k = subprocess.getoutput('cd come')
	      if 'No such file' in k:
 	          print_des('come mkdir') 
 	          subprocess.getoutput('mkdir come')

	     
check()
## end ##

### user json grade file name get

#@lru_cache(maxsize=size)
def filename_get():
     global student_come
     global file
     gardes = """
      
      1. grade 6
      2. grade 7
      3. grade 8
      4. grade 9
      5. grade 10
      6. garde 11
          
      """
     print_des(gardes)
     gra = input_des('Enter grade : ')
     if '1' in gra:
          file = 'grade/user6.json'
          student_come = '_user6.json'
     elif '2' in gra:
          file = 'grade/user7.json'
          student_come = '_user7.json'
     elif '3' in gra:
          file = 'grade/user8.json'
          student_come = '_user8.json'
     elif '4' in gra:
          file = 'grade/user9.json'
          student_come = '_user9.json'
     elif '5' in gra:
          file = 'grade/user10.json'
          student_come = '_user10.json'
     elif '6' in gra:
          file = 'grade/user11.json'
          student_come = '_user11.json'
     else:
        print_des('you Enter grade not found ! ')
        exit()
     try:
         open(file,'r').read()
     except FileNotFoundError:
          os.system(f"touch {file}")
filename_get()

## end ##


## data table dump ##
def table(dic):
     call = Texttable()
     call.add_row(dic)
     #call.header(['i','b','c'])
     print_des(call.draw())
## end ##

## normal data convert json data ##
#@lru_cache(maxsize=size)
def data_prin(filename):
     try:
        jdata = json.load(open(filename))
        return  jdata
     except json.decoder.JSONDecodeError as h:
         print(f'error : frist student join and  {str(h)} ')
         exit()
     # print('error'8
#      exit()
## end ##

## json data write ##
#@lru_cache(maxsize=size)
def data_writ(filename,data):
     with open(filename,'w') as f:
                json.dump(data,f,indent=4)
## end ##

## json data user add ##
#@lru_cache(maxsize=size)
def add_user(ran):
     if open(file,'r').read() == '':
          dic_w = {} 
     else:
          dic_w = data_prin(file)
     end_id = ''
     for p in dic_w:
          end_id = p
     print_des('last user id : ' + end_id)
     for i in range(1,ran):
          number = input_des('Enter id : ')
          name = input_des("Enter you are name : ")
          phone = input_des('Enter phone: ')
          shcoole = input_des('Enter shcoole name : ')
          subject = input_des('Enter subject : ')
          dic_w[number]  = [name]
          dic_w[number].append(phone)
          dic_w[number].append(shcoole)
          dic_w[number].append(subject)
          print_des(f"{name} student . ")
     return  dic_w
     #data_u = add_user(2)
     #data_writ(file,data_u)
     
## end ##

## user data edit ##
#@lru_cache(maxsize=size)
def edit_user():
     if open(file,'r').read() == '':
          dic_w = {} 
     else:
          dic_w = data_prin(file)
     for i in dic_w:
          print_des(i+'. '+dic_w[i][0])
     while True:
      id = input_des('Enter user id : ')
      if id == '0':
           break
      else:
       try:
        o = dic_w[id]
       except KeyError as f:
           print_des(f"you enter id {f} not found")
           break
          
     ## tables print ##
       print('')
       table(['1.name',' 2.number','3.shcoole','4.subject'])
       table(o)
     ## end ##
       end = '\x1b[0m'
       ran = '\x1b[34m'
       ran1 = '\x1b[31m'
       password = getpass.getpass(f'{ran}Enter admin password : {end} {ran1} ');print(end)
       pa = data_prin('admin/admin.json')
       if password == pa['password']:
          
        cho = input_des('Enter field : ')
        if  cho == '1':
          e = input_des('Enter edit value : ')
          dic_w[id][0] = e
          table(dic_w[id])
        elif  cho == '2':
          e = input_des('Enter edit value : ')
          dic_w[id][1] = e
          table(dic_w[id])
        elif  cho == '3':
          e = input_des('Enter edit value : ')
          dic_w[id][2] = e
          table(dic_w[id])
        elif  cho == '4':
          e = input_des('Enter edit value : ')
          dic_w[id][3] = e
          table(dic_w[id])
        else:
          print_des('you Enter field number not found ')
        if '1' in cho or '2' in cho or '3' in cho or '4' in cho:
          os.system(f'rm -rf {file}')
          os.system(f"touch {file}")
          with open(file,'w') as f:
                json.dump(dic_w,f,indent=4)
          
          
        else:
          print_des('not found field id : ')
       else:
          print_des('password worng ')
          break
## end ##          #
 
## user all data view ## 
#@lru_cache(maxsize=size)
def user_data_all_view():
       if  open(file,'r').read() == '':
          dic_w = {} 
       else:
          dic_w = data_prin(file)
       student_indexs = 0
       for key in dic_w:
            student_indexs += 1
       student_names = []
       for key in dic_w:
            student_names.append(key)
       index = 1
       table(['index','name','phone','collage','subject'])
       print('')
       for i in dic_w:
            table([index]+dic_w[i])
            index += 1            
  
## end ##
#@lru_cache(maxsize=size)
def student_day():
       user_json = data_prin(file)
       user = """
     
     1. Marking attendance
     2. Assembling student attendance ( සිසුන්ගේ පැමිණීම එක්රැස් කර බැලීම  )
     
     """
       print_des(user)
       cho = input_des('Enter you are choice : ')
       if '1' in cho:
         try:
           app_json = data_prin('come/2020'+student_come)
       #    print(app_json)
         except:
          print_des('error')
          app_json = {}
         num = 0
         date = input_des('Enter today date (20/5/30) : ')
         for i in user_json:
          num += 1
          print_des(str(num)+'. '+user_json[i][0])
         while True:
           user_input = input_des('Enter user id : ')
           if user_input == '0':
                
                break
                
           else:
                try:
                     app_json[date]
                except:
                     app_json[date] = [date]
                     
                try:
                     app_json[date].append(user_json[user_input][0])
                except KeyError as d:
                     print_des(f"you enter not found {d}")
                
                
       
         data_writ('come/2020'+student_come,app_json)     
         print_des('student come list ready ')
           #with open(,'w') as f:
#                json.dump(app_json,f,indent=4)

       elif '2' in cho:
          app_json = data_prin('come/2020'+student_come)
          w = 0
          maths  = []
          for i in app_json:
               w +=  1
               print_des(str(w)+'. '+i)
               maths.append(i)
               
          date = int(input_des('Enter month : '))
          k = 0
          try:
           for p in app_json[maths[date-1]]: 
               k += 1
               print_des(str(k)+'. '+p)
          except KeyError as l:
               print_des(f"you enter not found {l}")
               
          
       else:
          print_des(f"you enter choice not found {cho} ")


## delect user ## 
#@lru_cache(maxsize=size)
def delect_user():
     try:
       filedata = data_prin(file)
     except json.decoder.JSONDecodeError:
         print_des('file data not found ')
     try:
          
      for i in filedata:
          print_des(i+'. '+filedata[i][0])
      username = input_des('Enter delect user id : ')
      if username == '':
          print('id not found ')
      else:
        try:
         del filedata[username]
        except KeyError as d:
             print_des(f"you enter id {d} is not found ")
             pass
        os.system(f'rm -rf {file}')
        os.system(f'touch {file}')
        with open(file,'w') as f:
            json.dump(filedata,f,indent=4)
     except UnboundLocalError as f:
          print_des('error : '+f)
## end ##

## admin login and admin error recode ##
#@lru_cache(maxsize=size)
def admin_infomation():
     os.system('clear')
     user = """
     
       1. admin login infomation
       2. admin login error login infomation
     
     """
     print_des(user)
     cho = input_des('Enter choice : ')
     if '1' in cho:
          datajson = data_prin(admin_login_file)
      #    print(datajson)
          for i in datajson:
               table(datajson[i])
     elif '2' in cho:
          datajson = data_prin(admin_login_error)
          for i in datajson:
               table(datajson[i])
     else:
          print_des('you enter choice not found ')
## end ##


## all function get one main funcrtion 

#@lru_cache(maxsize=size)
def main():
     banner()
     user = f"""     
     
        time : {datetime.datetime.now()}
           
        Preparation of student information -*_*-
     
     1. Registration of students
     
     2. Changing student information
     
     3. View all student information
     
     4. Deleting student information
     
     5. admin login infomation
     
     6. Marking student attendance
     
     """
     admin1 = 'admin/admin.json'
     try:
         datas =  data_prin(admin1)
     except:
          os.system('touch '+admin1)
          datas=   data_prin(admin1)
          passw = getpass.getpass('Enter admin password : ')
          if datas['password'] == passw:
               pass
          else:
               print_des('password worng ')
               exit()
     print_des(user)
     print('')
     choice = input_des("Enter admin you choice : ")
     if '1' in choice:
          ran = int(input_des('Enter student loop number : '))
          data_u = add_user(ran+1)
          with open(file, 'w') as f:
                json.dump(data_u, f, indent=4)
          
     elif '2' in choice:
          edit_user()
     elif '3' in choice:
          user_data_all_view()
     elif '4' in choice:
          delect_user()
     elif '5' in choice:
          admin_infomation()
     elif '6' in choice:
          student_day()
     else:
           print_des('you Enter choice not found ')
## end ##
 
 
## admin login ##         
#@lru_cache(maxsize=size)            
def admin_login():
    wh = 0
    er = {}
    login = {}
    while True:
      if wh == 3:
           exit()
      else:
       
       slow_type('admin login page ')
       print('')
       print("")
       admin_de = {}
       user_name = input_des('Enter admin user name : ')
       end = '\x1b[0m'
       ran = '\x1b[34m'
       ran1 = '\x1b[31m'
       user_password = getpass.getpass(f'{ran} Entet admin password : {end}')
       admin_de['username'] = user_name
       admin_de['password'] = user_password
       admin1 = 'admin/admin.json'
     
       try:
          get_data = data_prin(admin1)
           #print(get_data)
       except:
          # print(admin_de)
           os.system("touch "+admin1)
           with open('admin/admin.json','w') as f:
                json.dump(admin_de,f,indent=4)
           get_data = data_prin(admin1)
       if get_data['username'] == user_name and get_data['password'] == user_password:
          print_des('login sucess ')
          try:
           datajson = data_prin(admin_login_file)
          except:
               datajson = {}
          with open(admin_login_file,'w') as f:
                t = str(datetime.datetime.today())
                now= str(datetime.datetime.now())
                datajson[now]= [now]
                datajson[now].append('username : '+user_name)
                datajson[now].append('password : '+user_password)
                json.dump(datajson,f,indent=4)
          get_data = data_prin(admin1)
          os.system('clear')
          break
          
       else:
           try:
                datajson = data_prin(admin_login_error)
           except:
                datajson = {}
               
           with open(admin_login_error,'w') as f:
                t = str(datetime.datetime.today())
                now= str(datetime.datetime.now())
                datajson[user_name] = [now]
                datajson[user_name].append('password : '+user_password)
                datajson[user_name].append('username : '+user_name)
                json.dump(datajson,f,indent=4)
           #get_data = data_prin(admin1)
           print_des('login error ')
         # exit()
       wh += 1
## end ##
     

## if __name__ == __main__ run to program  

if '__main__' == __name__:
         #  check()
           os.system('clear')
           admin_login()
           while True:
            main()
            cho = input_des('Enter ->> ')
            print()
            slow_type('SYSTEM DEVELOP BY K.A.ISHAN OSHADA ')
            if cho == 'e':
                 exit()
            else:
                 pass
## end ##           
