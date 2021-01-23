mkdir lotto<br>
cd lotto<br>
git clone https://github.com/nikitasellin/webpython02.git

docker build -t lotto .

Запуск игры:<br>
docker run -it lotto

Запуск тестов:<br>
docker run -e TEST=yes lotto
