def quick_sort(sort_list):
    if not sort_list:
        return []
    else:
        pivot = sort_list[0]
        less = [x for x in sort_list if x < pivot]
        more = [x for x in sort_list[1:] if x >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)


def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        j = i-1
        key = sort_list[i]
        while j >= 0 and sort_list[j] > key:
            sort_list[j+1] = sort_list[j]
            j -= 1
        sort_list[j+1] = key
    return sort_list


def selection_sort(sort_list):
    for i, e in enumerate(sort_list):
        mn = min(range(i, len(sort_list)), key=sort_list.__getitem__)
        sort_list[i], sort_list[mn] = sort_list[mn], e
    return sort_list


def main():
    pass


if __name__ == "__main__":
    main()
