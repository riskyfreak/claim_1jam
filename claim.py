import json,re,sys,os
import argparse
import time
import csv
from time import sleep
try:
  import colorama
  from colorama import Fore, Back, Style
  colorama.init(autoreset=True)
  hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
  res = Style.RESET_ALL
  abu2 = Style.DIM+Fore.WHITE
  ungu2 = Style.NORMAL+Fore.MAGENTA
  ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
  hijau2 = Style.NORMAL+Fore.GREEN
  yellow2 = Style.NORMAL+Fore.YELLOW
  yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
  red2 = Style.NORMAL+Fore.RED
  red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
except:
  print ("Hmm Sepertinya Modul Colorama Belum Terinstall\n\n\n")
  sys.exit()

try:
  import requests
  from bs4 import BeautifulSoup
except:
  print ("Hmm Sepertinya Modul Requests Dan BS4 Belum Terinstall\n\n\n")
  sys.exit()

from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError

if not os.path.exists("session"):
  os.makedirs("session")

c = requests.Session()
                
def tunggu(x):
  sys.stdout.write("\r")
  sys.stdout.write("                                                                   ")
  for remaining in range(x, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{}[{}|{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
    sys.stdout.flush()
    sleep(0.125)
    sys.stdout.write("\r")
    sys.stdout.write("{}[{}/{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
    sys.stdout.flush()
    sleep(0.125)
    sys.stdout.write("\r")
    sys.stdout.write("{}[{}-{}]{} {:2d}{} seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
    sys.stdout.flush()
    sleep(0.125)
    sys.stdout.write("\r")
    sys.stdout.write("{}[{}\{}]{} {:2d}{} seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
    sys.stdout.flush()
    sleep(0.125)
    sys.stdout.write("\r")
    sys.stdout.write("{}[{}|{}]{} {:2d}{} seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
    sys.stdout.flush()
    sleep(0.125)
    sys.stdout.write("\r")
    sys.stdout.write("{}[{}/{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
    sys.stdout.flush()
    sleep(0.125)
    sys.stdout.write("\r")
    sys.stdout.write("{}[{}-{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
    sys.stdout.flush()
    sleep(0.125)
    sys.stdout.write("\r")
    sys.stdout.write("{}[{}\{}]{} {:2d}{} seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
    sys.stdout.flush()
    sleep(0.125)

api_id = 1121524
api_hash = '634f4ddb3b28036c456f4d4ab0aee9f9'

nomer_hp = []
client = list()
myself = list()
text_kalimat1 = 'Mencoba Claim Bot TRON PAY CLAIM'
text_pesankirim1 = '🎁 Bonus'
text_pesanterima1 = 'You have successfully received'
channel_entity1 = list()
channel_username1 = '@TronPayClaimBot'

########################################################################################
with open('nomerhp.csv') as nomerhp_file:
  csv_reader = csv.reader(nomerhp_file, delimiter=",")
  for row in csv_reader:
    nomer_hp.append(row)

hitung=0
for banyaknomer in nomer_hp:
  sys.stdout.write('\r                                                        \r')
  sys.stdout.write('\r['+str(hitung)+']{}Sedang memuat nomer HP {}'.format(hijau2,yellow2)+str(banyaknomer[0]))
  hitung=hitung+1
  sleep(1)

clientno=0
for sessionnomer in nomer_hp:
  client.append(TelegramClient("session/"+sessionnomer[0], api_id, api_hash))
  client[clientno].connect()
  sys.stdout.write('\r                                                        \r')
  sys.stdout.write('\r['+str(clientno)+']{}Sedang memeriksa session {}'.format(hijau2,yellow2)+str(sessionnomer[0]))
  if not client[clientno].is_user_authorized():
    try:
      client[clientno].send_code_request(sessionnomer[0])
      me = client[clientno].sign_in(sessionnomer[0], input('\n\033[1;0mEnter Your Code : '))
    except SessionPasswordNeededError:
      passw = input("\033[1;0mYour 2fa Password : ")
      me = client[clientno].start(sessionnomer[0],passw)
  myself.append(client[clientno].get_me())
  clientno=clientno+1
  sleep(1)

channel_entityno=0
for x in nomer_hp:
  channel_entity1.append(client[channel_entityno].get_entity(channel_username1))
  sys.stdout.write('\r                                                        \r')
  sys.stdout.write('\r{}Harap Tunggu '.format(yellow2)+str(channel_entityno))
  channel_entityno=channel_entityno+1
  sleep(1)
sleep(3)
########################################################################################

os.system("clear")
sys.stdout.write('{}      *****    *****    *****   *******  *    *  *  *******\n'.format(yellow))
sys.stdout.write('{}      *    *  *     *  *     *     *     *   *   *     *\n'.format(yellow))
sys.stdout.write('{}      *    *  *     *  *     *     *     *  *    *     *\n'.format(yellow))
sys.stdout.write('{}      * ***   *     *  *     *     *     * *     *     *\n'.format(yellow))
sys.stdout.write('{}      *  *    *     *  *     *     *     *  *    *     *\n'.format(yellow))
sys.stdout.write('{}      *   *   *     *  *     *     *     *   *   *     *\n'.format(yellow))
sys.stdout.write('{}      *    *   *****    *****      *     *    *  *     *\n'.format(yellow))
sys.stdout.write('{}=================================================================\n'.format(hijau2))
sys.stdout.write('{}[#]{}SCRIPT   : {}Claim\n'.format(red,hijau,yellow))
sys.stdout.write('{}[#]{}AUTHOR   : {}rootkit\n'.format(red,hijau,yellow))
sys.stdout.write('{}[#]{}THANKS   : {}Jejaka Tutorial\n'.format(red,hijau,yellow))
sys.stdout.write('{}[#]{}DONATION : {}1LWUpgSZ4kRBhMRtcxymRAQd41NV3k5PSV (Bitcoin)\n'.format(red,hijau,yellow))
sys.stdout.write('{}=================================================================\n'.format(hijau2))
print (f"{hijau}Jumlah Nomer Telegram "+str(len(nomer_hp)))
print("-"*65)

def claim1(nomerhp1, klien1, entitychannel1, kalimat, pesankirim, findpesan):
    sys.stdout.write('\r                                                                 \r')
    sys.stdout.write(f"\r{abu2}[{yellow2}!{abu2}]{yellow} {kalimat}")
    sys.stdout.flush()
    klien1.send_message(entity=entitychannel1, message=pesankirim)
    sleep(5)
    posts1 = klien1(GetHistoryRequest(peer=entitychannel1, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0,hash=0))
    pesan0 = posts1.messages[0].message
    pesan1 = posts1.messages[1].message
    if posts1.messages[0].message.find(findpesan) != -1 or posts1.messages[1].message.find(findpesan) != -1:
      sleep(2)
      sekarang = time.time()
      infowaktu = time.localtime(sekarang)
      sys.stdout.write('\r                                                                 \r')
      sys.stdout.write('\r['+str(infowaktu[3])+":"+str(infowaktu[4])+']{}'.format(hijau2,yellow2)+pesan1[2:51]+' ('+nomerhp1+')\n')
    else:
      sekarang = time.time()
      infowaktu = time.localtime(sekarang)
      sys.stdout.write('\r                                                                 \r')
      sys.stdout.write('\r['+str(infowaktu[3])+":"+str(infowaktu[4])+']{}'.format(hijau2,yellow2)+pesan0[2:37]+' ('+nomerhp1+')\n')

jmlhclaim=1
for i in range(5000000):
    x=0
    sys.stdout.write('\r                                                                 \r')
    print (f"{yellow2}Claim to "+str(jmlhclaim))
    for nomor in nomer_hp:
      claim1(nomor[0], client[x], channel_entity1[x], text_kalimat1, text_pesankirim1, text_pesanterima1)
      sleep(2)
      sys.stdout.write('{}-----------------------------------------------------------------\n'.format(yellow2))
      x=x+1
    sys.stdout.write('\n')
    jmlhclaim+=1
    t = 3530
    tunggu(t)
