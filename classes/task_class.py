class Animal:
    """Базовый класс"""

    def __init__(self, specie: str):
        """Инициализия видом класса"""
        self.specie = specie

    def move(self, paws_count: int = None) -> str:
        """Метод move в который необходимо передать данные о количестве лап"""
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
    """Класс наследник"""
    def __init__(self, specie: str, name: str):
        super().__init__(specie)
        self.name = name

    def pet_move(self, paws_count: int) -> str:
        """Метод класса наследника основанный на методе класса родителя"""
        move = super().move(paws_count)
        return f"{self.name}, {move}"

    def __repr__(self):
        return f"{self.specie}, {self.name} экземпляр класса Pet"



if __name__ == "__main__":
    dog = Pet("собака", "Шарик")
    print(dog.pet_move(4))

    ant = Pet("муравей", "Энтц")
    print(ant.pet_move(6))

    pet = Pet("собака", "Шарик")
    print(pet)
