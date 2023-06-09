<h2>Описание проекта</h2>
<p>Этот проект представляет собой скрипт, предназначенный для обработки POST-запросов, обработки PDF-файлов и отправки их в указанные группы в Telegram с использованием библиотеки aiogram.</p>
<h3>Предварительные требования</h3>
<ul>
<li>Python 3.x</li>
<li>Необходимые пакеты Python: aiogram, flask, aioflask, asgiref, PyPDF2</li>
</ul>
<h3>Установка</h3>
<ol>
<li>Клонировать репозиторий:</li>
<pre><code>git clone &lt;repository_url&gt;</code></pre>
<li>Перейти в директорию проекта:</li>
<pre><code>cd &lt;project_directory&gt;</code></pre>
<li>Установить необходимые пакеты:</li>
<pre><code>pip install -r requirements.txt</code></pre>
</ol>
<h3>Конфигурация</h3>
<ul>
<li>Получить API-токен Telegram Bot.</li>
<li>Открыть файл скрипта (main.py) и заменить 'YOUR_TOKEN' на ваш реальный API-токен в переменной API_TOKEN.</li>
</ul>
<h3>Использование</h3>
<p>Запустить скрипт:</p>
<pre><code>python new_upload.py</code></pre>
<p>Скрипт запускает сервер Flask, который прослушивает PUT и POST запросы по корневому URL (/).</p>
<p>При получении POST-запроса скрипт выполняет следующие шаги:</p>
<ol>
<li>Создает директорию output_pdf, если она не существует.</li>
<li>Извлекает аргумент group_id из запроса.</li>
<li>Записывает полученные данные в PDF-файл в директории output_pdf с именем Отчёт.pdf.</li>
<li>Удаляет лишние страницы из PDF-файла с помощью функции convert2.</li>
<li>Отправляет измененный PDF-файл в указанную группу в Telegram с использованием Telegram Bot API.</li>
<li>Если отправка не удалась, повторяет попытку до 5 раз с задержкой в 3 секунды между попытками.</li>
<li>Отправляет сообщение об успешной отправке или ошибке в предопределенную группу Telegram.</li>
<li>Скрипт продолжает работу и ожидает новых запросов.</li>
</ol>
<h3>Дополнительные замечания</h3>
<ul>
<li>Сервер Flask работает на <code>host='0.0.0.0'</code> и <code>port=8000</code>.</li>
<li>Скрипт использует модуль logging для базовой настройки логирования. Логи выводятся в консоль.</li>
<li>Функция convert2 удаляет лишние страницы из PDF-файла, оставляя только первые 5 страниц.</li>
<li>Для отправки сообщений в Telegram требуется активное интернет-соединение.</li>
<li>Сообщения об ошибках отправляются в группу Telegram.</li>
<li>Скрипт должен выполняться с использованием событийного цикла asyncio в Python.</li>
</ul>
<p><em>Примечание: Перед развертыванием скрипта в рабочей среде убедитесь в правильной конфигурации и обработке соображений безопасности.</em></p>
