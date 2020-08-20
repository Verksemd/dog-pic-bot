from telegram.ext import Updater, CommandHandler
import requests
import re
import os
PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1291793507:AAEFTLlDmmUnO2hta3pzH5Q4qHaOYxwSi0g'


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater('1291793507:AAEFTLlDmmUnO2hta3pzH5Q4qHaOYxwSi0g')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN)
    updater.bot.setWebhook('https://salty-tor-57263.herokuapp.com/' + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()



