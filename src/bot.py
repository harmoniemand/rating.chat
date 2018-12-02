from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)




def start(bot, update):

    keyboard = [[InlineKeyboardButton('Yay!', callback_data='yay'),
                 InlineKeyboardButton('Nay!', callback_data='nay')]]

    replay_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Please choose:", reply_markup=replay_markup)


def button(bot, update):
    query = update.callback_query

    menu_keyboard = [["/start"]]
    menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=False, resize_keyboard=True)

    bot.send_message(text="You chose: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          #message_id=query.message.message_id
                          reply_markup=menu_markup)


def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates"""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():

    updater = Updater(token='752297138:AAHMney-g1TktWC2LCdn3FMAdagRukRQ6ik')

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()