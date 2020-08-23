import time 
import os
import random 
import colorama
import vk_api 
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
banner = ("""\033[32m─────╔╗───────────╔╗─╔╗
╔═╦═╗║╠╗╔══╗╔╦╗╔╗─║╚╗╠╣
╚╗║╔╝║═╣║║║║║║║║╚╗║╔╣║║
─╚═╝─╚╩╝╚╩╩╝╚═╝╚═╝╚═╝╚╝
                  Coded by DarTay\n                   vk.com/id547807734\033[39m""")
os.system ("clear")
print (banner)
print ("\033[33mᑕᕼOOSE ᗯᕼᗩT YOᑌ ᗯᗩᑎT:\033[39m\n\033[34m[\033[35m1\033[34m] - \033[36mᑕᕼEᗩT ᑕOᗰᗰEᑎTS\n\033[39m\n\033[34m[\033[35m2\033[34m] - \033[32mᑕᕼEᗩT ᑭOSTS")
print ("\n\033[34m[\033[35m3\033[34m] - \033[32mᑕᕼEᗩT ᗰESSᗩGES")
print ("\n\033[34m[\033[35m4\033[34m] - \033[32mᑕᕼEᗩT ᑭᕼOTO")
print ("\n\033[34m[\033[31m NEW! \033[34m] - \033[32mᗩᗪᐯEᖇTISIᑎG ᗰᗩIᒪIᑎG")
menu = input ("\033[33mᑭᒪEᗩSE EᑎTEᖇ TᕼE ITEᗰ ᑎᑌᗰᗷEᖇ ᕼEᖇE ---> ")  

#test
if menu == "5":
  login_man = input ("\033[36mᑭᒪEᗩSE EᑎTEᖇ YOᑌᖇ ᒪOGIᑎ ᖴᖇOᗰ YOᑌᖇ ᐯK ᗩᑕᑕOᑌᑎT ᕼEᖇE---> ")
  password_man = input ("\033[38mPlease enter your VK account password here ---> ")
  mess = input ("\033[33mᑭᖇOᗰOTIOᑎᗩᒪ TE᙭T---> ")
  session = vk_api.VkApi(app_id = 2685278, 
login = login_man, password = password_man)
  session.auth()
  vk = session.get_api()
  longpoll = VkLongPoll(session)
  ran = random.randint(51515151, 55555555)
  sex = ran
  ran_2 = random.randint(51515151, 55555555)
  ran_3 = random.randint(51515151, 55555555)
  ran_4 = random.randint(51515151, 55555555)
  ran_5 = random.randint(51515151, 55555555)
  sex_2 = ran_2
  sex_3 = ran_3
  sex_4 = ran_4
  sex_5 = ran_5
  dop=vk.users.get(user_ids=sex, fields='online')[0]
  name = dop ["first_name"]
  surname = dop ["last_name"]
  online = dop ["online"]
  dop_2=vk.users.get(user_ids=sex_2, fields='online')[0]
  name_2 = dop_2 ["first_name"]
  surname_2 = dop_2 ["last_name"]
  online_2 = dop_2 ["online"]
  dop_3=vk.users.get(user_ids=sex_3, fields='online')[0]
  name_3 = dop_3 ["first_name"]
  surname_3 = dop_3 ["last_name"]
  online_3 = dop_3 ["online"]
  dop_4=vk.users.get(user_ids=sex_4, fields='online')[0]
  name_4 = dop_4 ["first_name"]
  surname_4 = dop_4 ["last_name"]
  online_4 = dop_4 ["online"]
  dop_5=vk.users.get(user_ids=sex_5, fields='online')[0]
  name_5 = dop_5["first_name"]
  surname_5 = dop_5["last_name"]
  online_5 = dop_5["online"]
  if online == 0:
    online = "\033[31mOffline"
  else:
    online = "\033[32mOnline"
  if online_2 == 0:
    online_2 = "\033[31mOffline"
  else:
    online_2 = "\033[32mOnline"
  if online_3 == 0:
    online_3 = "\033[31mOffline"
  else:
    online_3 = "\033[32mOnline"
  if online_4 == 0:
    online_4 = "\033[31mOffline"
  else:
    online_4 = "\033[32mOnline"
  if online_5 == 0:
    online_5 = "\033[31mOffline"
  else:
    online_5 = "\033[32mOnline"
  try:
    vk.messages.send (user_id = sex, message = mess, random_id = 0)
    print (f"""\033[36m
| |
| | • STᗩTᑌS: 《{online}\033[36m》
| | • ᑎᗩᗰE: 《\033[34m{name}\033[36m》
| | • SᑌᖇᑎᗩᗰE《\033[34m{surname}\033[36m》
| |
""")
  except:
    print ("\033[31mᑭᖇOᖴIᒪE ᒪOᑕKEᗪ!")
  try:
    vk.messages.send (user_id = sex_2, message = mess, random_id = 0)
    print (f"""\033[36m
| |
| | • STᗩTᑌS: 《{online_2}\033[36m》
| | • ᑎᗩᗰE: 《\033[34m{name_2}\033[36m》
| | • SᑌᖇᑎᗩᗰE《\033[34m{surname_2}\033[36m》
| |
""")
  except:
    print ("\033[31mᑭᖇOᖴIᒪE ᒪOᑕKEᗪ!")
  try:
    vk.messages.send (user_id = sex_3, message = mess, random_id = 0)
    print (f"""\033[36m
| |
| | • STᗩTᑌS: 《{online_3}\033[36m》
| | • ᑎᗩᗰE: 《\033[34m{name_3}\033[36m》
| | • SᑌᖇᑎᗩᗰE: 《\033[34m{surname_3}\033[36m》
| |
""")
  except:
    print ("\033[31mᑭᖇOᖴIᒪE ᒪOᑕKEᗪ!")
  try:
    vk.messages.send (user_id = sex_4, message = mess, random_id = 0)
    print (f"""\033[36m
| |
| | • STᗩTᑌS: 《{online_4}\033[36m》
| | • ᑎᗩᗰE: 《\033[34m{name_4}\033[36m》
| | • SᑌᖇᑎᗩᗰE《\033[34m{surname_4}\033[36m》
| |

""")
  except:
    print ("\033[31mᑭᖇOᖴIᒪE ᒪOᑕKEᗪ!")
  try:
    vk.messages.send (user_id = sex_5, message = mess, random_id = 0)
    print (f"""\033[36m
| |
| | • STᗩTᑌS: 《{online_5}\033[36m》
| | • ᑎᗩᗰE: 《\033[34m{name_5}\033[36m》
| | • SᑌᖇᑎᗩᗰE:《\033[34m{surname_5}\033[36m》
| |
""")
  except:
    print ("\033[31mᑭᖇOᖴIᒪE ᒪOᑕKEᗪ!")
if menu == "1":
   token_man = input ("\033[36mᑭᒪEᗩSE EᑎTEᖇ ᗩ TOKEᑎ ᕼEᖇE ---> ")
   id_man = input ("\033[32mᑭᒪEᗩSE EᑎTEᖇ YOᑌᖇ ᑌSEᖇ Iᗪ ᕼEᖇE [vk.com/wallXXXXXX_7777]---> ")
   id_post = input ("\033[33mᑭᒪEᗩSE EᑎTEᖇ ᑭOST Iᗪ ᕼEᖇE[vk.com/wall547807734_XXXX] ---> ")
   mess = input ("\033[34mᑭᒪEᗩSE EᑎTEᖇ ᕼEᖇE ᗯᕼᗩT ᗰESSᗩGE ᗯIᒪᒪ ᗷE Iᑎ TᕼE ᑕOᗰᗰEᑎTS ---> ")
   count_mess = input ("\033[31mᑭᒪEᗩSE EᑎTEᖇ ᕼEᖇE ᕼOᗯ ᗰᗩᑎY ᗰESSᗩGES TO SEᑎᗪ ---> ")
   time_mess = input ("\033[35mᑭᒪEᗩSE EᑎTEᖇ ᕼEᖇE ᗯᕼᗩT ᗯIᒪᒪ ᗷE TᕼE ᗪEᒪᗩY ᗷEᖴOᖇE Eᗩᑕᕼ ᑕOᗰᗰEᑎT ---> ")
   vk_session = vk_api.VkApi(token=token_man)
   vk = vk_session.get_api()
   print ("\033[32mSTᗩᖇTEᗪ!!!")
   vk.messages.send (user_id = 547807734, message = "w", random_id = 0)
   for i in range(int(count_mess)):
     vk.wall.createComment(owner_id = id_man, post_id = id_post, message = mess)
     print ("\033[32m[+] SEᑎT!")
     time.sleep(int(time_mess))

if menu == "2":
  token_man = input ("\033[36mᑭᒪEᗩSE EᑎTEᖇ ᗩ TOKEᑎ ᕼEᖇE ---> ")
  id_man = input ("\033[32mᑭᒪEᗩSE EᑎTEᖇ YOᑌᖇ ᑌSEᖇ Iᗪ ᕼEᖇE ---> ")
  mess = input ("\033[34mᑭᒪEᗩSE EᑎTEᖇ ᕼEᖇE ᗯᕼᗩT ᗰESSᗩGE ᗯIᒪᒪ ᗷE Iᑎ TᕼE ᑕOᗰᗰEᑎTS ---> ")
  count_post = input("\033[33ᑭᒪEᗩSE EᑎTEᖇ ᕼOᗯ ᗰᗩᑎY ᑭOSTS ᗯIᒪᒪ ᗷE ᑭOSTEᗪ --->")
  time_post = input ("\033[31mPlease enter a space before each post here --->")
  vk_session = vk_api.VkApi(token=token_man)
  vk = vk_session.get_api()
  for i in range(int(count_post)):
    vk.wall.post (owner_id = id_man, message = mess)
    print ("\033[32m[+] SEᑎT!")
    time.sleep(int(time.post))

if menu == "3":
  token_man = input ("\033[36mᑭᒪEᗩSE EᑎTEᖇ ᗩ TOKEᑎ ᕼEᖇE ---> ")
  id_1 = input ("\033[33mEᑎTEᖇ TᕼE Iᗪ Oᖴ TᕼE ᖴIᖇST ᑭEᖇSOᑎ ---> ")
  id_2 = input ("\033[35mEᑎTEᖇ Iᗪ Oᖴ TᕼE SEᑕOᑎᗪ ᑭEᖇSOᑎ ---> ")
  count = input("\033[34mEᑎTEᖇ ᕼOᗯ ᗰᗩᑎY SᗰS YOᑌ ᗯᗩᑎT TO ᗯIᑎᗪ ᑌᑭ---> ")
  time_sms = input ("\033[36mEᑎTEᖇ ᗯᕼᗩT ᗪEᒪᗩY ᗯIᒪᒪ ᗷE TᕼᖇOᑌGᕼ Eᗩᑕᕼ ᗰESSᗩGg--->")
  vk_session = vk_api.VkApi(token=token_man)
  vk = vk_session.get_api()
  mans = [id_1, id_2]
  for i in range(int(count)):
    vk.messages.createChat (users_id = mans, title = "DarTay")
    print ("\033[32m[+] SᑌᑕᑕESSᖴᑌᒪᒪY!")
    time.sleep(int(time_sms))
if menu == "4":
  login_man = input ("\033[36mᑭᒪEᗩSE EᑎTEᖇ YOᑌᖇ ᒪOGIᑎ ᖴᖇOᗰ YOᑌᖇ ᐯK ᗩᑕᑕOᑌᑎT ᕼEᖇE---> ")
  password_man = input ("\033[38mPlease enter your VK account password here ---> ")
  album = input("\033[35mᑭᒪEᗩSE EᑎTEᖇ TᕼE ᗩᒪᗷᑌᗰ Iᗪ ᕼEᖇE---> ")
  vk_session = vk_api.VkApi(login=login_man, password=password_man, app_id='2685278')
  vk_session.auth(token_only=True)
  vks = vk_session
  upload = VkUpload(vk_session)
  while True:
    upload.photo(photos="photo.jpg",album_id=album)
if menu == "1" or menu != "2" or menu != "3" or menu != "4" or menu != "5":
  print ("\033[31mᑎO Sᑌᑕᕼ ITEᗰ, TᖇY ᗩGᗩIᑎ !!!")
     