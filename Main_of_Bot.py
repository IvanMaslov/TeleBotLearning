#import config
import telebot

bot = telebot.TeleBot("531759775:AAEnCrQq4NNhye4EnH7B1-H9Nlib140PEhg")

print("FUCKS")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    print("pooling")
    bot.polling(none_stop=True)
    
#from telebot import types
#markup = types.ReplyKeyboardMarkup()
#markup.row('a', 'v')
#markup.row('c', 'd', 'e')
#bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
