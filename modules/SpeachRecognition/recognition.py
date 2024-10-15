import asyncio
import json
import logging

import speech_recognition as sr
from Interfece.Liza.event import Event, EventTypes

logger = logging.getLogger(__name__)

async def recognize(event: Event):
    # file_name = event.value
    text = voice_listening()
    event.value = text
    return event


# file_path = 'commands.txt'
#
#
# def save_to_file(file_path, text):
#     with open(file_path, 'a', encoding='utf-8') as file:
#         file.write(text + '\n')
#
#
# def clear_file():
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.write('')
async def voice_listening(
        queue: asyncio.Queue = None,
        config: dict = None,
):
    send_text_event = config["send_text_event"]
    ext_only = config["ext_only"]
    trigger_name = config["trigger_name"]

    if ext_only:
        return

    names = []
    if trigger_name:
        names = [i for i in trigger_name.split("|")]

    logger.info("Запуск распознователя речи Speach Recognition вход в цикл")

    r = sr.Recognizer()
    while True:

        await asyncio.sleep(0)

        with sr.Microphone() as source:
            audio = r.listen(source)
            user_command = r.recognize_google(audio, language="ru-RU").lower()
            if user_command != "" and user_command is not None:
                logger.info(f"SpeachRecognition: '{user_command}'")
                if len(names):
                    for name in names:
                        if name not in user_command:
                            continue

                        logger.debug("Имя обнаружено!")
                        user_command = " ".join(user_command.split(name)[1:])
                        user_command = user_command.strip()
                        break

                    else:
                        logger.debug("Имя не найдено!")
                        continue

                    await queue.put(
                        Event(
                            event_type=EventTypes.user_command,
                            value=user_command
                        )
                    )
                    if send_text_event:
                        await queue.put(
                            Event(
                                event_type=EventTypes.text,
                                value=user_command
                            )
                        )

                    logger.info(f"SpeachRecognition - передано в очередь: '{user_command}'")


