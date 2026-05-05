def binary_search(list, item):
    low = 0 # В переменных low and hign храняться границы той чатси списка, в которой выполняется поиск
    high = len(list)-1 # тут тоже самое что и вверху

    while low <= high: # пока эта часть не сократится до одного элемента
        mid = (low + high)/2 # проверяем средний элемент
        guess = list[mid]
        if guess == item: # значение найдено
            return mid
        if guess > item: # много
            high = mid - 1
        else:            # мало
            low = mid + 1
    return None # значение не сущ.

