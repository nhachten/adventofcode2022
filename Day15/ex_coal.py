
def coalesce(list_of_ranges):
    index = 0
    while index < len(list_of_ranges) - 1:
        print(f"index: {index}")
        left = list_of_ranges[index]
        right = list_of_ranges[index + 1]
        print(f"left: {left}")
        print(f"right: {right}")
        if left.stop >= right.start:
            new_range = range(left.start, max(left.stop, right.stop))
            print(f"new_range: {new_range}")
            list_of_ranges[index] = new_range
            list_of_ranges = list_of_ranges[:index+1] + list_of_ranges[index+2:]
            print(f"list_of_ranges: {list_of_ranges}")
        else:
            index += 1

    return list_of_ranges

def add_range_to_list(list_of_ranges, r):
    i = 0
    while True:
        try:
            if list_of_ranges[i].start > r.start:
                break
        except:
            break
        i += 1

    list_of_ranges.insert(i, r)
    list_of_ranges = coalesce(list_of_ranges)
    return list_of_ranges