class FlatIterator:

    def __init__(self, list_of_list_1):
        self.lst = list_of_list_1
        self.counter = 0

    def __iter__(self):
        self.elem = iter([])
        return self

    def __next__(self):
       try:
           item = next(self.elem)
       except StopIteration:
           if len(self.lst) == self.counter:
               raise StopIteration
           self.elem = iter(self.lst[self.counter])
           item = next(self.elem)
           self.counter += 1
       return item


class FlatIterator_inner:

    def __init__(self, list_of_list_2):
        self.lst = list_of_list_2

    def __iter__(self):
        return self

    def __next__(self):
        if self.lst:
            while self.lst:
                elem = self.lst.pop(0)
                if isinstance(elem, list):
                    while elem:
                        self.lst.insert(0, elem.pop())
                else:
                    return elem
        raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator_inner(list_of_lists_2),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']):
        assert flat_iterator_item == check_item

    assert list(FlatIterator_inner(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

if __name__ == '__main__':
    test_1()
    #test_3()