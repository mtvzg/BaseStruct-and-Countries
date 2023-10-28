str_country = 'Россия:1234563:5435434534|США:3453466463:3553253435|Италия:99999:99999'


class RawStrValidator:
    def __init__(self, raw_str):
        if not raw_str:
            raise ValueError('Сырая строка не может быть пустой')
        if self.DELIMITER not in raw_str:
            raise ValueError(f'Строка должна содержать разделитель {self.DELIMITER}')


class Country(RawStrValidator):
    DELIMITER = ':'

    def __init__(self, raw_str):
        super().__init__(raw_str)
        temp_raw_data = raw_str.split(self.DELIMITER)
        self.name = temp_raw_data[0]
        self.square = int(temp_raw_data[1].replace(' ', ''))
        self.population = int(temp_raw_data[2].replace(' ', '') if len(temp_raw_data) > 2 else 0)

    @property
    def is_empty(self):
        return not bool(self.name)

    @property
    def info(self):
        return f'{self.name} (Площадь: {self.square} км2) [Численность: {self.population} человек.]'


class Countries(RawStrValidator):
    DELIMITER = '|'

    def __init__(self, raw_str):
        super().__init__(raw_str)
        self.__data = []
        self._prepare_raw_str(raw_str)

    def _prepare_raw_str(self, raw_str):
        for country_str in raw_str.split(self.DELIMITER):
            country = Country(country_str)
            if not country.is_empty:
                self.__data.append(country)

    def get(self, index):
        max_index = len(self.__data) - 1
        if index > max_index:
            raise ValueError(f'Нет страны с индексом {index}, максимальный индекс {max_index}')
        print(self.__data[index].info)

    def find(self, string):
        if not string:
            raise ValueError('Строка не может быть пустой!')
        for item in self.__data:
            if string in item.name:
                print(item.info)
            else:
                print('Элемент не найден.')

    def get_more_square(self, number):
        for item in self.__data:
            if item.square > number:
                print(item.info)

    def get_less_square(self, number):
        for item in self.__data:
            if item.square < number:
                print(item.info)

    def get_more_population(self, number):
        for item in self.__data:
            if item.population < number:
                print(item.info)

    def get_less_population(self, number):
        for item in self.__data:
            if item.population < number:
                print(item.info)


countries = Countries(str_country)
countries.get(2)  # Получить страну из списка по индексу
countries.find('Росс')  # Поиск стран по слову
countries.get_more_square(100000)  # Страны с площадью больше
countries.get_less_square(100000)  # Страны с площадью меньше
countries.get_more_population(100000)  # Страны с населением больше
countries.get_less_population(100000)  # Страны с населением меньше
