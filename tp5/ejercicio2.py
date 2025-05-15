class StringIterable:
    def __init__(self, text):
        self.text = text

    def forward_iterator(self):
        return ForwardIterator(self.text)

    def reverse_iterator(self):
        return ReverseIterator(self.text)


class ForwardIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration


class ReverseIterator:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            char = self.text[self.index]
            self.index -= 1
            return char
        else:
            raise StopIteration



# ejemplo de uso
s = StringIterable("Hola Mundo")

print("Recorrido directo:")
for c in s.forward_iterator():
    print(c, end=' ')
    
print("\nRecorrido inverso:")
for c in s.reverse_iterator():
    print(c, end=' ')
