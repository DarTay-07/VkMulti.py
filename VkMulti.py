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
print ("\n\n\033[34m[\033[31m NEW! \033[34m] [\033[35m4\033[34m] - \033[32mᑕᕼEᗩT ᑭᕼOTO")
menu = input ("\033[33mᑭᒪEᗩSE EᑎTEᖇ TᕼE ITEᗰ ᑎᑌᗰᗷEᖇ ᕼEᖇE ---> ")  


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
   for i in range(int(count_mess)):
     vk.wall.createComment(owner_id = id_man, post_id = id_post, message = mess)
     print ("\033[32mSEᑎT!")
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
    print ("\033[32mSEᑎT!")
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
    print ("\033[32mSᑌᑕᑕESSᖴᑌᒪᒪY!")
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
if menu == "1" or menu != "2" or menu != "3" or menu != "4":
  print ("\033[31mᑎO Sᑌᑕᕼ ITEᗰ, TᖇY ᗩGᗩIᑎ !!!")
     
