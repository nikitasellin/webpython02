## Описание.

Игра "Лото".

Правила игры: https://gist.github.com/DanteOnline/038d59cb9c5b704d02238f4e11b95c97
<br>При запуске запрашивается количество и тип игроков:
```
0. Компьютер против компьютера
1. Компьютер против человека
2-10. Компьютер + несколько игроков (до 10)
```
Максимальное количество дополнительных игроков  
настраивается в файле конфигурации (config.py)


* Игроку предлагается зачеркнуть цифру на карточке ('y') или продолжить ('n').
Если игрок выбрал "зачеркнуть":
    * цифра есть на карточке - она зачеркивается (помечается на игровом поле символами ХХ)
      и игра продолжается. 
    * цифры на карточке нет - игрок проигрывает.
* Если игрок выбрал "продолжить":
    * цифра есть на карточке - игрок проигрывает.
	* цифры на карточке нет - игра продолжается.

Компьютер всегда делает правильный выбор.
Побеждает тот, кто первым зачеркнул все цифры на карточке. 

### Запуск (пример для Linux).
```
# mkdir lotto
# cd lotto
# git clone https://github.com/nikitasellin/webpython02.git .
# docker build -t lotto .
```

Запуск игры:
```
# docker run -it lotto
```

Запуск тестов:
```
# docker run -e TEST=yes lotto
```
