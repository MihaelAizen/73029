# Бот для вк
# Для работы требуется группа в вк и взятый из нее API ключ/token

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

# API ключ группы вк
token = "-"

# Авторизация бота
vk = vk_api.VkApi(token=token)

# Работа с сообщениями (обработка и ответ)
longpoll = VkLongPoll(vk)

# Основа
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку/упоминание для бота
        if event.to_me:
        
            # Сообщение пользователя
            request = event.text
            
            # Ответ
            if request == 'привет':
                write_msg(event.user_id, 'Здравствуйте')
            elif request == 'как дела?':
                write_msg(event.user_id, 'Не очень, мне не хватает функций помимо ответов на ваши вопросы.')
            elif request == 'info':
                write_msg(event.user_id, 'ЧатБот для Вконтакте')
            elif request == 'как тебя зовут?':
                write_msg(event.user_id, 'Анатолий')
            elif request == 'чем ты занимаешься?':
                write_msg(event.user_id, 'Веду высокоинтеллектуальную беседу с вами.')
            elif request == 'смешно':
                write_msg(event.user_id, 'Немного')
            elif request == 'загадай загадку':
                    write_msg(event.user_id, 'Антону позавчера было семнадцать лет, а в следующем году ему исполнится двадцать. Возможно ли это?')
                if request == 'да':
                    write_msg(event.user_id, 'Ты угадал!')
                elif request == 'нет':
                    write_msg(event.user_id, 'Ты проиграл! Такое возможно, если такую фразу произнести 1 января, с учетом того, что Миша родился 31 декабря. Следовательно, 30 декабря ему было еще 17, а 31-го числа исполнилось 18. В наступившем году ему будет 19, ну а в следующем - 20.')
                elif request == 'хорошая загадка':
                    write_msg(event.user_id, 'Ага')
                else:
                    write_msg(event.user_id, 'Ответ еще не добавлен')
            elif request == 'пока':
                write_msg(event.user_id, 'До свидания')
            else:
                write_msg(event.user_id, 'Ответ еще не добавлен')