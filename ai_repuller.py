from platform import system
from urllib import response
import os
import ollama
import getpass
import platform

def main(request):
    response = ollama.chat(
        model='qwen2.5-coder:3b',
        messages=[{'role': 'system', 'content': """Ты - ии ассистент, как джарвис. тебе будут давать задания(к примеру: открой браузер), а ты отвечаешь командой в консоли который выполнит задачу. помни - только команда для терминала без другого текста. Все команды выполняются в корневой системе."""},
                  {'role': 'system', 'content': f"Вот данные о системе, используй их для более корректной генерации команд: {getpass.getuser()} \n {platform.system()}"},
                  {'role': 'user', 'content': request}]
    )
    print("CODE: " + response['message']['content'])
    if os.system(response['message']['content'].encode('utf-8')) != 0:
        os.system(response['message']['content'].encode('utf-8'))
    else:
        pass

    print('ИТОГО:' + response['message']['content'])
    print('Успешно выполнено.')