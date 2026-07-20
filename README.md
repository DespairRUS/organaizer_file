<div align="center"> <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"> <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License MIT"> <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status">
📁 Organaizer File
Элегантный инструмент для автоматической сортировки файлов

Установка •
Быстрый старт •
Документация •
Вклад
</div>
📖 О проекте

Organaizer File — это умный Python-скрипт, который наводит порядок в ваших папках. Забудьте о хаосе в загрузках и рабочем столе! Программа анализирует файлы по расширениям и автоматически распределяет их по тематическим папкам.
🎯 Ключевые особенности
Возможность	Описание
🤖 Автоматизация	Полностью автоматический процесс сортировки
🎨 8+ категорий	Изображения, документы, видео, аудио, архивы и другие
🔄 Рекурсивная обработка	Сортировка файлов во всех вложенных папках
🛡️ Безопасный режим	Предварительный просмотр действий без перемещения
⚙️ Гибкая настройка	Создание собственных правил сортировки
📊 Детальное логирование	Полный отчет о всех действиях
🚀 Быстрый старт
Установка
bash

# Клонируем репозиторий
git clone https://github.com/DespairRUS/organaizer_file.git

# Переходим в папку проекта
cd organaizer_file

Первый запуск
bash

python organaizer_file.py ~/Downloads

Готово! Ваши файлы будут отсортированы за секунды. ✨
📚 Документация
Поддерживаемые категории
<details> <summary><b>🖼️ Изображения</b></summary>

.jpg, .jpeg, .png, .gif, .bmp, .svg, .tiff, .webp
</details><details> <summary><b>📄 Документы</b></summary>

.pdf, .docx, .doc, .txt, .xlsx, .xls, .pptx, .ppt, .odt
</details><details> <summary><b>📦 Архивы</b></summary>

.zip, .rar, .7z, .tar.gz, .tgz, .bz2
</details><details> <summary><b>🎵 Аудио</b></summary>

.mp3, .wav, .flac, .aac, .ogg, .wma
</details><details> <summary><b>🎬 Видео</b></summary>

.mp4, .avi, .mov, .mkv, .webm, .flv
</details><details> <summary><b>💻 Программирование</b></summary>

.py, .js, .html, .css, .cpp, .java, .go, .rs
</details>
Аргументы командной строки
bash

python organaizer_file.py [путь] [опции]

Аргумент	Сокращение	Описание
--recursive	-r	Обрабатывать все вложенные папки
--dry-run	-d	Показать план действий без перемещения
--config	-c	Использовать пользовательский конфиг
--verbose	-v	Подробный вывод процесса
--help	-h	Показать справку
💡 Примеры использования
Базовый пример
bash

python organaizer_file.py ~/Загрузки

Рекурсивная сортировка с подробным выводом
bash

python organaizer_file.py ~/Documents -r -v

Просмотр плана действий (безопасный режим)
bash

python organaizer_file.py ~/Desktop -d

Использование пользовательской конфигурации
bash

python organaizer_file.py ~/Projects -c custom_rules.yaml

🎨 Пользовательские правила

Создайте файл custom_rules.yaml для своих категорий:
yaml

categories:
  📚 Книги:
    - .fb2
    - .epub
    - .mobi
    - .azw3
  
  🎮 Игры:
    - .iso
    - .nes
    - .rom
  
  🖌️ Дизайн:
    - .psd
    - .ai
    - .sketch
    - .fig

🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта!

    Форкните репозиторий

    Создайте ветку (git checkout -b feature/AmazingFeature)

    Зафиксируйте изменения (git commit -m 'Add some AmazingFeature')

    Отправьте пулл-реквест

📄 Лицензия

Распространяется под лицензией MIT. Подробности в файле LICENSE.
📞 Контакты и поддержка

    Автор: DespairRUS

    Создать Issue: GitHub Issues

    Обсуждения: GitHub Discussions

<div align="center">
Если проект оказался полезным, поставьте ⭐️ звезду!

Сделано с ❤️ и Python

⬆ Наверх
</div>

Примечание: Для актуальной информации всегда обращайтесь к официальному репозиторию.
