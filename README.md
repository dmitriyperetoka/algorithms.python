# Примеры решения алгоритмических задач
 
## Поиск
* [Линейный поиск.](https://github.com/dmitriyperetoka/algorithms.python/blob/main/algorithms/Search/linear_search.py) Простой алгоритм поиска без ограничений для массива. Осуществляется простым сравнением очередного элемента массива с искомым элементом. В случае нахождения искомого элемента, возвращает индекс его первого вхождения в массиве. Временная сложность в худшем случае O(n), в лучшем случае O(1), в среднем O(n/2). Дополнительная память O(1).

* [Бинарный поиск.](https://github.com/dmitriyperetoka/algorithms.python/blob/main/algorithms/Search/binary_search.py) Подходит только для поиска в отсортированном массиве. Осуществляется сравнением серединного элемента массива с искомым элементом и сужением области поиска в зависимости от результатов сравнения. Действие повторяется до нахождения элемента, равного искомой величине. Порядок вхождения элементов не учитывается. Временная сложность в худшем случае O(log n), в лучшем случае O(1), в среднем O(log n). Дополнительная память O(1).

## Сортировки
* [Сортировка пузырьком.](https://github.com/dmitriyperetoka/algorithms.python/blob/main/algorithms/Sorting/bubble_sort.py) Состоит из повторяющихся проходов по массиву. За каждый проход все элементы неотсортированной части массива сравниваются попарно. Если порядок в паре элементов не правильный, то элементы меняются местами. На каждом повторении самое большое число из неотсортированной части масива становится на своё место, при этом область сортировки сужается на один элемент. Если за очередное повторение не происходит ни одного обмена, массив считается отсортированным, и алгоритм завершается. Временная сложность в худшем случае O(n<sup>2</sup>), в лучшем случае O(n), в среднем O(n<sup>2</sup>). Дополнительная память O(1).

* [Сортировка вставками.](https://github.com/dmitriyperetoka/algorithms.python/blob/main/algorithms/Sorting/insertion_sort.py) Элементы массива просматриваются по одному, и каждый следующий элемент перемещается в подходящее место среди ранее упорядоченных элементов. Временная сложность в худшем случае O(n<sup>2</sup>), в лучшем случае O(n), в среднем O(n<sup>2</sup>). Дополнительная память O(1).
