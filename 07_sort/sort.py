def bubblesort(lst):
    end = len(lst) - 1
    has_changes = True
    while has_changes:
        has_changes = False

        for i in range(end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                has_changes = True

        end = end - 1


numbers = [4, 6, 9, 2, 5, 2, 8, 3, 6, 6, 2, 1, 9]
bubblesort(numbers)  # Zahlen werden an Ort und Stelle sortiert
print(numbers)


def quicksort(lst):
    if len(lst) <= 1:
        return lst
    reference = lst[0]
    smaller = []
    equal = []
    greater = []

    for element in lst:
        if element < reference:
            smaller.append(element)
        elif element == reference:
            equal.append(element)
        else:
            greater.append(element)

    return quicksort(smaller) + equal + quicksort(greater)


numbers = [4, 6, 9, 2, 5, 2, 8, 3, 6, 6, 2, 1, 9]
numbers_sorted = quicksort(numbers)  # Generiert eine neue sortierte Liste
print(numbers_sorted)
