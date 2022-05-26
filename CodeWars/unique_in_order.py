def unique_in_order(iterable):
    listofargs = [x for x in (list(iterable))]
    uniqueList = []
    prevItem = None
    for item in listofargs:
        if item == prevItem:
            prevItem = item
            continue
        else:
            uniqueList.append(item)
            prevItem = item
    return uniqueList
