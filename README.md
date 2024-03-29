# api_yamdb Docker 
 
## Описание 
Проект выполнен в учебных целях в работе с API (DRF).  
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор. 
Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается средняя оценка произведения.  
 
## Этапы развертывания Docker контейнера 
1. Склонировать репозиторий 
2. В корневой директории проекта создать файл `/api_yatube/.env` с переменными: 
  * `DB_NAME`=... 
  * `DB_USER`=... 
  * `DB_PASSWORD`=... 
  * `DB_HOST`=... 
  * `DB_PORT`=... 
   
3. Выполнить команду `docker-compose up` 
 
##### Остальное за вас выполнит скрипт. 
 
Проект достуен по адресу http://127.0.0.1:8000/api/v1/ 
 
 
### Итоговый проект курса "Работа с внешними API"   
#### Выполнили: 
- [Олег Тараканов](https://github.com/nonameists) 
- [Максим Карпов](https://github.com/TurboKach)  
- [Иван Лундак](https://github.com/netshy) 
