# библиотека для получения почты
import poplib
# библиотека для анализа текста
import email
import time


class MailHelper:

    # Конструктор, который сохраняет ссылку на основной обьект
    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        # так как почта приходим не сразу, делаем несколько попыток прочитать сообщение
        for i in range(15):
            # адрес сервера
            pop = poplib.POP3(self.app.config['james']['host'])
            # Имя и пароль пользователя, с которым нужно открыть сессию
            pop.user(username)
            pop.pass_(password)
            # определяем кол-во писем. Этот метод возвращает стат инфо о том, что имеется в почтовом ящике
            num = pop.stat()[0]
            # первый элемент возвращаемого кортежа (num)- это кол-во писем
            if num > 0:
                for n in range(num):
                    # получаем письмо. В качестве параметра указываем индекс (n+1). Текст письма на-ся во втором
                    # элементе этого картежа . msglines - это список строчек
                    msglines = pop.retr(n + 1)[1]
                    # строки склеиваем вместе и получаем текст. map(lambda x: x.decode('utf-8'), msglines) - поток
                    # байтов конвертируем в обычную строку
                    msgtext = "\n".join(map(lambda x: x.decode('utf-8'), msglines))
                    # анализируем текст письма. Получили сообщение
                    msg = email.message_from_string(msgtext)
                    # если тема письма = заданной, то...
                    if msg.get("Subject") == subject:
                        # письмо помечаем на удаление
                        pop.dele(n + 1)
                        # закрываем соединение. close - без сохранения, quit - с сохранением
                        pop.quit()
                        # ... возвращаем тело письма
                        return msg.get_payload()
            pop.close()
            time.sleep(3)
        raise Exception("Mail not found")