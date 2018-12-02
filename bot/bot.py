from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging
from profile.profile import Profile
from event_base.util import create_event_list

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)




def start(bot, update):

    profile = Profile.create(update.message.chat.id)
    event_list = create_event_list(profile['basic']['chat_id'])
    profile['progress']['event_id'] = 'creation_user_name'
    profile['event_list'] = event_list
    Profile.save(profile, update.message.chat.id)

    custom_keyboard = [['/next']]

    reply_markup = ReplyKeyboardMarkup(custom_keyboard, )
    bot.send_message(chat_id=update.message.chat.id, text='go on',
                    reply_markup = reply_markup)

def button(bot, update):

    query = update.callback_query
    last_event_data = str(query.data)
    split_string = last_event_data.split(";", 1)
    event_id = split_string[0]
    chat_id = split_string[1]
    profile = Profile.load(chat_id)
    profile['progress']['event_id'] = event_id
    Profile.save(profile,chat_id)



def next(bot, update):

    chat_id = update.message.chat.id
    profile = Profile.load(chat_id)
    event_id = profile['progress']['event_id']
    event_class = profile['event_list']
    event_object = event_class[event_id]['class'](chat_id)

    button_list, text = event_object.create_virtual_keyboard()

    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=3))
    bot.send_message(chat_id=update.message.chat.id, text=text, reply_markup=reply_markup)



def error(bot, update, error):
    """Log Errors caused by Updates"""
    logger.warning('Update "%s" caused error "%s"', update, error)


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def main():

    updater = Updater(token='683702767:AAEK7xW4HTckEj2BurhayfvW2dRvJiwoqfE')

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('next', next))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


main()
    