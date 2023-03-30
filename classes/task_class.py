class Animal:

    def __init__(self, specie):
        self.specie = specie

    def move(self, paws_count: int = None):
        if isinstance(paws_count, int):
            if paws_count == 0:
                return f"{self.specie}, плавает"
            if paws_count not in [0, 2, 4, 6, 8]:
                return "Не знаю таких животных"
            if paws_count == 2:
                return f"{self.specie}, ходит"
            if paws_count == 4:
                return f"{self.specie}, бегает"
            if paws_count == 6:
                return f"{self.specie}, ползает"
            if paws_count == 8:
                return f"{self.specie}, плетет паутину"
        else:
            print("Некорректный формат ввода данных, необходимо целое число")
            return "Некорректный формат ввода данных, необходимо целое число"

    def __repr__(self):
        return f"{self.specie}"


class Pet(Animal):
    def __init__(self, specie, name):
        Animal.__init__(self, specie)
        self.name = name

    def pet_move(self, paws_count):
        move = Animal.move(self, paws_count)
        return f"{self.name}, {move}"

    def __repr__(self):
        return f"{self.specie}, {self.name}"



if __name__ == "__main__":
    dog = Pet("собака", "Шарик")
    print(dog.move(4))
    print(dog.pet_move(4))

    ant = Pet("муравей", "Энтц")
    print(ant.move(6))
    print(ant.pet_move(6))

    print(Animal("собака"))
    print(Pet("собака", "Шарик"))
