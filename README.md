# python_test
autotest
Создаем проект.
Устанавливаем в проект модуль Selenium.
Скачиваем драйвер Chrome по ссылке https://chromedriver.storage.googleapis.com/index.html, скачиваем версию такую же как и у браузера Chrome на вашем компьютере.
Создаем в проекте директорию 'chromedriver' и копируем драйвер Chrome туда.
Копируем в проект файл test.py.
Запускаем в консоли файл test.py.
Вводим стартовую ссылку https://ru.wikipedia.org/wiki/Samsung_Galaxy_S22
Вводим конечную ссылку https://ru.wikipedia.org/wiki/Pixel_6
Нажимем Enter.
Запускается программа и подключается к https://ru.wikipedia.org/wiki/Samsung_Galaxy_S22.
На этой странице находит ссылку https://ru.wikipedia.org/wiki/Android, сохраняет его и текст вокруг ссылки.
Далее переходит на него.
На этой странице находит ссылку https://ru.wikipedia.org/wiki/Android_13, сохраняет его и текст вокруг ссылки.
Далее переходит на него.
На этой странице находит ссылку https://ru.wikipedia.org/wiki/Pixel_6, сохраняет его и текст вокруг ссылки.
В файл logger будут сохраняться все URL-адреса, к которым было подключение.
В итоге от стартовой страницы перешли в конечную за 3 клика.
