from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)

    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15

    def __init__(self, name):
        self.name = name

    # method attack
    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанес противнику урон, равный {value_attack}'

    # method protect
    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} ед. урона'

    # method special attack
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзский воин ближного боя.'
                             ' Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дального боя.'
                             ' Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_STAMINA + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель.'
                             ' Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_STAMINA + 30
    SPECIAL_SKILL = 'Защита'


def start_training(character):
    """
    Принимает обьект метод
    возвращает результат о цикле.
    """
    commands = {'attack': character.attack, 'defence': character.defence, 'special': character.special}

    cmd = None
    while cmd != 'skip':
        cmd = input('Введите команду: ')
        if cmd in commands:
            print(commands[cmd]())


def choice_char_class(char_name: str) -> Character:
    """
     Возвращает строку с выборами
     классом персонажа.
    """
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = None

    while approve_choice != 'y':
        select_class = input('Введи называние персонажа, '
                             'за которого хочешь играть: Воитель - warrior, '
                             'Маг - mage, Лекарь - healer: ')
        char_class: Character = game_classes[select_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы потдвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персожана ').lower()
        return char_class


warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())
