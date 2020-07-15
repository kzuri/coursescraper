#import telebot
import logging

from telegram.ext import CommandHandler, CallbackQueryHandler, Updater, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram
from bs4 import BeautifulSoup
import requests
import re
import os
import urllib.request
#import request
#from bs4 import beautifulsoup
import sys

token = '1089830193:AAHe8q93LFPQF5tJzu7PMLff8MeyNCsUQCg'

PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
#############################################################################3
def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text='Hey there!\n'+'Welcome to course scrapper bot!\n\n'+"As name suggests, this bot would automatically scrap course website, so that your lazy ass don't have to manually crawl through material.\n\n"
                                                           +'Press /help for help, duh!')

def help(bot,update):
  keyboard = [[InlineKeyboardButton('Message the developer', url='telegram.me/demonking1206')]]
  reply_markup = InlineKeyboardMarkup(keyboard)

  bot.send_message(chat_id=update.message.chat_id,text=
       '1) To view all available courses press /courses.\n' +
       '2) Click on the course you are interested in.\n' +
       '3) You will receive option regarding type of material you want to download i.e lecture notes (if available) or problem sets.\n' +
       '4) Sit back and watch those sweet sweet pdfs rolling in', reply_markup= reply_markup
   )
'''
def error(bot, update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
'''

def courses_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text="Choose course",
                        reply_markup=courses_keyboard())
'''
def start_command(message):
   bot.send_message(
       message.chat.id,
       'Greetings! I can show you PrivatBank exchange rates.\n' +
       'To get the exchange rates press /exchange.\n' +
       'To get help press /help.'
   )


def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   
   bot.send_message(
       message.chat.id,
       '1) To receive a list of available currencies press /exchange.\n' +
       '2) Click on the currency you are interested in.\n' +
       '3) You will receive a message containing information regarding the source and the target currencies, ' +
       'buying rates and selling rates.\n' +
       '4) Click “Update” to receive the current information regarding the request. ' +
       'The bot will also show the difference between the previous and the current exchange rates.\n' +
       '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
       reply_markup=keyboard
   )
'''
###################################################################3

#def list_courses(bot,update):
    
def mth202(bot,update):
    chat_id = update.message.chat_id

    url="https://sites.google.com/site/mth202jan2020/problem-sets"
    response = urllib.request.urlopen(url).read()
    soup= BeautifulSoup(response, "html.parser")   
    links = soup.find_all('a', href=re.compile(r'(.pdf)'))


    # clean the pdf link names
    url_list = []
    for el in links:
      if (el['href'].startswith('http')):
        url_list.append(el['href'])  
      else:
        url_list.append("https://sites.google.com" + el['href'])
 

    # download the pdfs to a specified location
    for url in url_list:
       bot.sendDocument(chat_id, document=url)


################################  Test  ######################################
def menu(bot, update):
  #update.message.reply_text(main_menu_message(),
   #                         reply_markup=main_menu_keyboard())
  chat_id = update.message.chat_id
  bot.send_message(chat_id=chat_id, 
                 text=main_menu_message(),reply_markup=courses_keyboard() )
  
def main_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=courses_keyboard())

def first_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        reply_markup=first_keyboard())

def second_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        reply_markup=second_keyboard())

def third_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        reply_markup=third_keyboard())

def fourth_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        reply_markup=fourth_keyboard())

def first_lc(bot,update):
    query = update.callback_query
    chat_id = update.effective_chat.id
    query.answer()

    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING) 
    query.edit_message_text(text="Lecture Notes coming right up!")
    
    url="https://sites.google.com/site/mth202jan2020/reading-lecture-notes"
    response = urllib.request.urlopen(url).read()
    soup= BeautifulSoup(response, "html.parser")   
    links = soup.find_all('a', href=re.compile(r'(.pdf)'))


    # clean the pdf link names
    url_list = []
    for el in links:
      if (el['href'].startswith('http')):
        url_list.append(el['href'])  
      else:
        url_list.append("https://sites.google.com" + el['href'])
     
    
    # download the pdfs to a specified location
    for url in url_list:
       bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.UPLOAD_DOCUMENT) 
       bot.sendDocument(chat_id, document=url)
       
def first_tq(bot,update):
    query = update.callback_query
    chat_id = update.effective_chat.id
    query.answer()

    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING) 
    query.edit_message_text(text="Problem sets coming right up!")
    
    url="https://sites.google.com/site/mth202jan2020/problem-sets"
    response = urllib.request.urlopen(url).read()
    soup= BeautifulSoup(response, "html.parser")   
    links = soup.find_all('a', href=re.compile(r'(.pdf)'))


    # clean the pdf link names
    url_list = []
    for el in links:
      if (el['href'].startswith('http')):
        url_list.append(el['href'])  
      else:
        url_list.append("https://sites.google.com" + el['href'])
 

    # download the pdfs to a specified location
    for url in url_list:
       bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.UPLOAD_DOCUMENT)
       bot.sendDocument(chat_id, document=url)    

def button(update,context):
    query = bot.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text="Selected option: {}".format(query.data))


# and so on for every callback_data option
def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

############################ Keyboards #########################################
def courses_keyboard():
  keyboard = [[InlineKeyboardButton('MTH202', callback_data='mth')],
              [InlineKeyboardButton('CHM202', callback_data='chm')],
              [InlineKeyboardButton('PHY202', callback_data='phy')],
              [InlineKeyboardButton('BIO202', callback_data='bio')]]
  return InlineKeyboardMarkup(keyboard)

def first_keyboard():
  keyboard = [[InlineKeyboardButton('Lecture Notes', callback_data='first_lc')],
              [InlineKeyboardButton('Tutorials', callback_data='first_tq')],
              [InlineKeyboardButton('<<', callback_data='menu')]]
  return InlineKeyboardMarkup(keyboard)

def second_keyboard():
  keyboard = [[InlineKeyboardButton('Lecture Notes', callback_data='second_lc')],
              [InlineKeyboardButton('Tutorials', callback_data='second_tq')],
              [InlineKeyboardButton('<<', callback_data='menu')]]
  return InlineKeyboardMarkup(keyboard)

def third_keyboard():
  keyboard = [[InlineKeyboardButton('Lecture Notes', callback_data='third_lc')],
              [InlineKeyboardButton('Tutorials', callback_data='third_tq')],
              [InlineKeyboardButton('<<', callback_data='menu')]]
  return InlineKeyboardMarkup(keyboard)

def fourth_keyboard():
  keyboard = [[InlineKeyboardButton('Lecture Notes', callback_data='fourth_lc')],
              [InlineKeyboardButton('Tutorials', callback_data='fourth_tq')],
              [InlineKeyboardButton('<<', callback_data='menu')]]
  return InlineKeyboardMarkup(keyboard)


############################# Messages #########################################
def main_menu_message():
  return 'Choose the course:'

def first_menu_message():
  return 'Choose type of material:'

############################################################################
def main():
    
    updater = Updater(token)

    
    dp = updater.dispatcher

   
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    #dp.add_error_handler(error)

    
    #dp.add_handler(CallbackQueryHandler(courses_menu, pattern='main'))
    dp.add_handler(CommandHandler("courses", menu))

    dp.add_handler(CallbackQueryHandler(main_menu, pattern='menu'))
    #updater.dispatcher.add_handler(CallbackQueryHandler(button_pressed,pattern='first_lc'))
    dp.add_handler(CallbackQueryHandler(first_menu, pattern='mth'))
    dp.add_handler(CallbackQueryHandler(second_menu, pattern='chm'))
    dp.add_handler(CallbackQueryHandler(third_menu, pattern='phy'))
    dp.add_handler(CallbackQueryHandler(fourth_menu, pattern='bio'))
    
    
    dp.add_handler(CallbackQueryHandler(first_lc,pattern='first_lc'))
    dp.add_handler(CallbackQueryHandler(first_tq,pattern='first_tq'))
    '''
    dp.add_handler(CallbackQueryHandler(first_lc,pattern='first_lc'))
    dp.add_handler(CallbackQueryHandler(first_tq,pattern='first_tq'))

    dp.add_handler(CallbackQueryHandler(first_lc,pattern='first_lc'))
    dp.add_handler(CallbackQueryHandler(first_tq,pattern='first_tq'))

    dp.add_handler(CallbackQueryHandler(first_lc,pattern='first_lc'))
    dp.add_handler(CallbackQueryHandler(first_tq,pattern='first_tq'))
    '''

    #updater.start_polling()

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=token)
    updater.bot.setWebhook('https://coursescarper.herokuapp.com/' + token)
    
    updater.idle()
    
if __name__ == '__main__':


    main()

