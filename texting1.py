from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
#important libraries

bot=ChatBot('sana')
bot.set_trainer(ListTrainer)
#defining name

for files in os.listdir('C:/Users/LAPPY/Desktop/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
        data=open('C:/Users/LAPPY/Desktop/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
        bot.train(data)

while True:
        message=input('sana:')
        if message.strip!='Bye'or message.strip!='bye':
                reply=bot.get_response(message)
                print('chatbot:',reply)
        if message.strip=='Bye' or message.strip=='bye':
                print('chatbot:It was nice talking to you.Bye')
                break
