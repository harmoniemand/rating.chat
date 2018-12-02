from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

import logging

from profile import Profile


def start(bot, update):
    print(update.message)
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def start_game(bot, update):
    profile = Profile.create(chat_id=update.message.chat_id)
    print(update.message)
    bot.send_message(chat_id=update.message.chat_id, text='New game started')
    Profile.save(profile=profile, chat_id=update.message.chat_id)


def echo(bot, update):
    profile = Profile.load(chat_id=update.message.chat_id)
    Profile.save(profile=profile, chat_id=update.message.chat_id)
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)


def main():

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    token = '541471711:AAFC46JebZN5qQO_znvjz6QRXIaCTcrNp0k'
    updater = Updater(token=token)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    caps_handler = CommandHandler('new_game', start_game)
    dispatcher.add_handler(caps_handler)

    inline_caps_handler = InlineQueryHandler(inline_caps)
    dispatcher.add_handler(inline_caps_handler)


if __name__ == '__main__':
    main()
