# Lesta HH
## Задание 1 

### 1) Первый код
- Плюсы:
Первый код является более понятным для людей, которые знакомы с простейшей математикой.
- Недостатки: 
Деление обычно медленнее побитовых операций, особенно для больших чисел или в высокопроизводительных сценариях 
### 2) Второй код
- Плюсы:
Побитовые операции выполняются быстрее деления
- Недостатки: 
Требует понимания битовых операций

## Задание 2

1) Первая реализация - использование списка
- Плюсы: 
Простота реализации и понимания. Можно легко отслеживать элементы 
- Недостатки:
При большом количестве операций вставки и извлечения, повторные вычисления индексов могут быть затратными
2) Вторая реализация - collections.deque
- Плюсы:
collections.deque автоматически управляет памятью
- Недостатки:
Встроенный лимит размера maxlen не вызывает ошибку при превышении, а просто отбрасывает старые элементы

## Задание 3
Для сортировки массива с максимальной эффективностью по времени исполнения - встроенная функция sorted() или метод sort() для списков. Функции реализованы на уровне C в виде Timsort, который сочетает "идеи" сортировки вставками и сортировки слиянием. 
Также можно использовать quicksort, но скорость выполнения может не измениться или наоборот ухудшиться, все зависит от набора данных.

