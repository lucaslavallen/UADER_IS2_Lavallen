import os

# Programa memory.py  modificado

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    def __init__(self):
        self.history = []

    def save(self, writer):
        # Solo guarda los últimos 4 estados
        if len(self.history) >= 4:
            self.history.pop(0)  # Elimina el más antiguo
        self.history.append(writer.save())

    def undo(self, writer, index=0):
        if 0 <= index < len(self.history):
            writer.undo(self.history[-1 - index])
        else:
            print(f"No hay estado guardado en la posición {index}")


if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará versiones anteriores")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional II\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Material adicional III\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional IV (no se guarda para limitar a 4)")
    writer.write("Material adicional IV\n")
    print(writer.content + "\n")
    # Esta línea no guarda el estado, solo modifica el contenido actual

    # Ejemplo de recuperación de estados
    print("\nRecuperar estado más reciente (undo(0)):")
    caretaker.undo(writer, 0)
    print(writer.content + "\n")

    print("Recuperar estado anterior (undo(1)):")
    caretaker.undo(writer, 1)
    print(writer.content + "\n")

    print("Recuperar estado más antiguo disponible (undo(3)):")
    caretaker.undo(writer, 3)
    print(writer.content + "\n")

    print("Intentar recuperar un estado inexistente (undo(4)):")
    caretaker.undo(writer, 4)
