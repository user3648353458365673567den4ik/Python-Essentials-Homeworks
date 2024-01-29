import re
import abc


class Filter(abc.ABC):
    @staticmethod
    def sql_identify(query: str) -> bool:
        """
        Method that tell you, is that sql query in condition of regular expression or no
        :param query: SQL query to identify
        :return: Bool
        """
        pattern = r"^(SELECT|UPDATE|DELETE|INSERT)\b"
        matched = re.match(pattern, query)
        return matched is not None

    @staticmethod
    def name_find(text: str, only_unique: bool = True) -> str or None:
        """
        Method that finds names in text
        :param text: init text
        :param only_unique: true - method will return no-repeated list, false - init found list without other operations
        :return: list of found words
        """
        pattern = r"[AА-ЯZЁ][aа-яzё]+"
        found_in_sentences = []
        found = []

        sentences = text.split('.')

        for sentence in sentences:
            data = re.findall(pattern, sentence)[1:-1]
            if data:
                found_in_sentences.append(data)

        for arr in found_in_sentences:
            for item in arr:
                found.append(item)

        if only_unique:
            return list(set(found))
        else:
            return found

    @staticmethod
    def check_password(password: str) -> tuple or bool:
        """
        Checking password for security level
        :param password: Password to check
        :return: True | tuple(bool, str)
        """
        password = password.strip()
        incorrects = []

        if len(password) < 8:
            incorrects.append("Password can't be less than 8 symbols")

        if not re.findall(r"[%!\"$'()*+,-.&:;<=?>]", password):
            incorrects.append("Password must contain one or more special symbols")

        if not re.findall(r"[A-Z]", password):
            incorrects.append("Password must contain one or more capital letters")

        if incorrects:
            return False, tuple(incorrects)

        return True


def main():
    assert Filter.sql_identify("INSERT INTO Users") == True
    assert Filter.sql_identify("ALTER ...") == False

    assert Filter.check_password("Password123!") == True
    assert Filter.check_password("password") is not True
    assert Filter.check_password("12345678") is not True
    assert Filter.check_password("Password") is not True


    print(Filter.name_find("""У Саши живёт пёс Джин. Мальчик взял Джина на дачу в село Гречанино. Однажды Джин погнался за кошкой Муськой и пропал. Через час Саша нашёл Джина на улице Лесной. (29)
    
    Отличница Вера Гришина сидит за партой рядом с Женей Щучаровым. А Оля Птичкина сидит рядом с Геной Чумаковым. С кем сидит Катя Чанина? С Витей Чакиным. (26)
    
    Мы часто ездим в город Касимов. Рядом с Касимовым лежит село Глебово. Через село протекает речка Красная. Она вытекает из озера Чувиль. В речку впадает ручей Щучий. (27)"""))

if __name__ == "__main__":
    main()
