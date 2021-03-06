Задачи
============
Задача 1
------------
Напишите решение функции, которая, учитывая целое число N, возвращает строку, состоящую из N строчных букв (a-z), так что каждая буква встречается нечетное число раз. Мы заботимся только о появлении букв, которые появляются хотя бы один раз в результате.

Примеры:
1. При `N = 4` функция может возвращать `code` (каждая из букв `c`, `o`,
`d` и `e` встречается один раз). Другие правильные ответы: `cate`, `uutu` или
`xxxy`.
2. При `N = 7` функция может возвращать `gwgtgww` (`g` и `w` встречаются по три раза каждый, а `t` встречается один раз).
3. При `N = 1` функция может возвращать `z`.

Напишите эффективный алгоритм для следующих условий:
- N - целое число в диапазоне [1...200 000]


Задача 2
------------
Напишите функцию:
`def solution(S)`, которая, принимает строку S, состоящую из N строчных букв, возвращает
минимальное количество букв, которые необходимо удалить, чтобы получить слово, в
котором каждая буква встречается уникальное число раз. Нас волнует только 
появлении букв, которые появляются хотя бы один раз в результате.
Примеры:
1. Дано `S = "aaaabbbb"`, функция должна возвращать 1. Мы можем удалить одно
вхождение a или одно вхождение b. Тогда одна буква будет встречаться четыре
раза, а другая - три раза.
2. Дано `S = "ccaaffddecee"`, функция должна возвращать 6. Например, мы
можно удалить все вхождения e и f и одно вхождение d, чтобы получить
слово "ccaadc". Обратите внимание, что и e, и f будут встречаться ноль раз в новом
слове, но это нормально, так как нас интересуют только буквы, которые появляются хотя бы
один раз.
3. Дано `S = "eeee"`, функция должна возвращать 0 (нет необходимости удалять
какие-либо символы).
4. Дано `S = "пример"`, функция должна возвращать 4.


Напишите эффективный алгоритм для следующих предположений:
- N - целое число в диапазоне [0...300 000];
- строка S состоит только из строчных букв (a-z).