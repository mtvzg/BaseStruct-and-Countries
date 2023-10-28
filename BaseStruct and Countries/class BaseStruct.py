class BaseStruct:
    def __init__(self):
        self._data = []

    @property
    def is_empty(self):
        return not len(self._data)

    @property
    def length(self):
        return len(self._data)

    @property
    def has_elements(self):
        return not self.is_empty

    def set(self, element):
        self._data.append(element)

    def has_element(self, element):
        return element in self._data


class Queue(BaseStruct):
    def get(self):
        if self.is_empty:
            raise RuntimeError('Очередь пуста.')
        return self._data.pop(0)


class Stack(BaseStruct):
    def get(self):
        if self.is_empty:
            raise RuntimeError('Стек пуст.')
        return self._data.pop()


if __name__ == '__main__':
    queue = Stack()
    print(queue.is_empty)
    queue.set(1)
    queue.set(2)
    queue.set(3)
    queue.set(4)
    queue.set(5)
    print(queue.length)
    print(queue.has_elements)
    print(queue.has_element(3))
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.length)
