# Бинарный поиск
def binary_search(lst: list, search_item) -> list:
    left = 0
    right = len(lst) - 1
    operations_count = 0
    is_found = False
 
    while left <= right and not is_found:
        center = (left + right) // 2
        current_item = lst[center]
        operations_count += 1
 
        if current_item == search_item:
            is_found = True
            break
        elif current_item < search_item:
            left = center + 1
        else:
            right = center - 1
        
    result = {
        'is_found': is_found,
        'operations_count': operations_count,
    }
    
    return result
 
lst = [i for i in range(296)]
result = binary_search(lst, 296)
 
for key, value in result.items():
    print(f'{key}: {value}')