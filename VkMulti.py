import time 
import colorama
import vk_api 
from vk_api.longpoll import VkLongPoll, VkEventType
banner = ("""\033[32m─────╔╗───────────╔╗─╔╗
╔═╦═╗║╠╗╔══╗╔╦╗╔╗─║╚╗╠╣
╚╗║╔╝║═╣║║║║║║║║╚╗║╔╣║║
─╚═╝─╚╩╝╚╩╩╝╚═╝╚═╝╚═╝╚╝
                  Coded by DarTay\n                   vk.com/id547807734\033[39m""")
print (banner)
print ("\033[33mᑕᕼOOSE ᗯᕼᗩT YOᑌ ᗯᗩᑎT:\033[39m\n\033[34m[\033[35m1\033[34m] - \033[36mᑕᕼEᗩT ᑕOᗰᗰEᑎTS\n\033[39m\n\033[34m[\033[35m2\033[34m] - \033[32mᑕᕼEᗩT ᑭOSTS")
menu = input ("\033[33mᑭᒪEᗩSE EᑎTEᖇ TᕼE ITEᗰ ᑎᑌᗰᗷEᖇ ᕼEᖇE ---> ")  

if menu == "1":
   token_man = input ("\033[36mᑭᒪEᗩSE EᑎTEᖇ ᗩ TOKEᑎ ᕼEᖇE ---> ")
   id_man = input ("\033[32mᑭᒪEᗩSE EᑎTEᖇ YOᑌᖇ ᑌSEᖇ Iᗪ ᕼEᖇE ---> ")
   id_post = input ("\033[33mᑭᒪEᗩSE EᑎTEᖇ ᑭOST Iᗪ ᕼEᖇE ---> ")
   mess = input ("\033[34mᑭᒪEᗩSE EᑎTEᖇ ᕼEᖇE ᗯᕼᗩT ᗰESSᗩGE ᗯIᒪᒪ ᗷE Iᑎ TᕼE ᑕOᗰᗰEᑎTS ---> ")
   count_mess = input ("\033[31mᑭᒪEᗩSE EᑎTEᖇ ᕼEᖇE ᕼOᗯ ᗰᗩᑎY ᗰESSᗩGES TO SEᑎᗪ ---> ")
   time_mess = input ("\033[35mᑭᒪEᗩSE EᑎTEᖇ ᕼEᖇE ᗯᕼᗩT ᗯIᒪᒪ ᗷE TᕼE ᗪEᒪᗩY ᗷEᖴOᖇE Eᗩᑕᕼ ᑕOᗰᗰEᑎT ---> ")
   session = vk_api.VkApi(token = token_man)
   longpoll = VkLongPoll(session)
   vk = session.get_api()
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
  for i in range(int(count_post)):
    vk.wall.post (owner_id = id_man, message = mess)
    print ("\033[32mSEᑎT!")
    time.sleep(int(time.post))


if menu != "1" or menu != "2":
  print ("\033[31mᑎO Sᑌᑕᕼ ITEᗰ, TᖇY ᗩGᗩIᑎ !!!")
