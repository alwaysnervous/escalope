# Иерархическая файловая система
Каждый пользовательский поиск информации – определённый **логический запрос**.  

Пример – _"Фотографии из Кисловодска в 2013 г."_

Структура папок может быть выполнена так:
  
* Россия  
  * 2013  
    * Кисловодск
	  * Фотографии

Каждое название папки представляет собой определённое свойство искомого файла.

Прохождение в глубь древа файловой системы по папкам представляет собой запрос, использующий только операцию логического умножения («И»), что означает наличие у файла всех указанных в названиях пройденных папок свойств.

Ввиду этого возникает неопределённость в структуре иерархии в связи с возможностью файлов иметь схожие свойства, из-за чего информация файлов будет подлежать _дубликации_, и её дальнейшее редактирование будет затруднено из-за необходимости корректировки множества файлов.

Например, в случае, если мы ведём отдельную папку с фотографиями, нам придётся туда скопировать файл из папки нашей поездки.

На помощь решения этой проблемы должна прийти семантическая файловая система, главная цель которой – **облегчение поиска файлов**.  

Она призвана быть более "гибкой", позволяя пользователю осуществлять более сложные запросы с логической точкой зрения, и, соответственно, получать намного более релевантную информацию.

При этой системе важным вопросом для пользователя остаётся присваивание файлам свойств (**тегов**). Эту задачу за пользователя можно решить программным путём, используя, в том числе, метаданные файлов и технологии машинного обучения.

# Принцип работы семантической файловой системы
