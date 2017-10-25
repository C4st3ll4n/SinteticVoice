## Foi criada uma pasta chama "py" na pasta de Documentos, onde existem arquivos de textos com dialogos para o boot treinar

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3 as pt


f = pt.init()
a = "C:/Users/Henrique/Documents/py"
cb = ChatBot('Castellan')
cb.set_trainer(ListTrainer)
f.setProperty('voice', b'brazil')
for arq in os.listdir(a):
    chats = open(a+"/" + arq, 'r').readlines()
    cb.train(chats)
while True :
    resq = input("Você: ")
    resp = cb.get_response(resq)
    if resp.confidence > 0.5:
        print("CastellanBoot: " + str(resp))
        f.say(resp)
    elif 0.3 <= resp.confidence < 0.5:
        print('CastellanBoot: QUE ?')
        f.say(resp)
    else:
        print("CastellanBoot: Não entendi")
        f.say(resp)
    f.runAndWait()
