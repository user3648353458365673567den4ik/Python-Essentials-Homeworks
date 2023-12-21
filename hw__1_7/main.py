import time
import re

TEXT = "诚如Y小姐所言，我们住在这个城市某座随处可见的公寓楼里，而这座公寓楼对面是另一座一模一样的公寓楼，诸如此类的公寓楼像多米诺骨牌一样足以绕地球50圈，也许这就是城市本来的风景。当然，大多数人并不关心这件事，他们只是回到房间里睡觉，第二天又赶最早的高铁去另一个城市上班，而我的女朋友是个足不出户、依赖想象力存活的人，在她心中，我们的丑猫不但穿着靴子，而且还能随时从高礼帽中变出彩带。"


def clear_text(text: str):  # обработка символов китайского
    """ Анализирует текст на наличие китайского """
    kka = re.findall('[\u4e00-\u9fff]+', text)
    return kka


def analyze_text(text: str) -> dict:
    """ Анализирует текст и возвращает словарь из кол-ва символов с пробелом и без, кол-ва слов и кол-ва предложений в тексте """

    if not isinstance(text, str):
        text = str(text)

    if len(text.split(' ')) > 1 and len(clear_text(text)) > 0:
        raise Exception('You can enter only in chinese or in Latin/Cyrillic symbols')


    if clear_text(text) != []:
        sentences = len(text.split('。'))
    else:
        sentences = len(text.split('.'))

    return {
        'symbols': len(text),  # кол-во символов
        'symbols_without_space': len(text.replace(' ', '')),  # кол-во символов без учета пробелов
        'words': len(text.split(' ')) if clear_text(text) == [] else len(clear_text(text)),  # кол-во слов
        'sentences': sentences  # кол-во предложений
    }


print('Start time:', start_time := time.time())
print(analyze_text(TEXT))
print('Time result:', time.time() - start_time)
