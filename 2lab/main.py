class StringTransform:
    def __init__(self, string):
        self.step = [string]
        self.string = string

    def caesar_cipher(self, shift):
        result = []
        shift = shift % 26  #сдвиг

        for i in self.string:
            if i.isalpha():
                base = ord('a') if i.islower() else ord('A')
                #сдвиг буквы и возвращение в диапазон алфавита
                shift_i = chr((ord(i) - base + shift) % 26 + base)
                result.append(shift_i)
            else:
                result.append(i)
        return ''.join(result)

    def reverse(self):
        return self.string[::-1]

    def apply_command(self, command):
        orig = self.string

        try:
            if command == 'r':
                self.string = self.reverse()
            elif command.startswith('c'):
                try:
                    shift = int(command[1:])  # Извлекаем число после 'c'
                    self.string = self.caesar_cipher(shift)
                except ValueError:
                    raise ValueError(f"Некорректный сдвиг в команде: {command}")
            else:
                raise ValueError(f"Неизвестная команда: {command}")

            #cохранение шага
            self.step.append(self.string)
            return True

        except Exception as e:
            self.string = orig
            print(f"Ошибка выполнения команды '{command}': {e}")
            return False

    def apply_commands(self, commands_str):
        commands = commands_str.split()

        for command in commands:
            success = self.apply_command(command)
            if not success:
                print(f"Прервано из-за ошибки в команде: {command}")
                break

        return self.string

    def get_steps(self):
        #этапы преобразований
        return self.step.copy()

    def print_steps(self):
        print("Этапы преобразований:")
        for i, s in enumerate(self.step):
            print(f"Шаг {i}: '{s}'")


def main():
    # Входные данные
    commands_input = "c1 r c-1 r"
    str_input = "abcd"

    transformer = StringTransform(str_input)

    result = transformer.apply_commands(commands_input)

    #результат
    print(f"Исходная строка: '{str_input}'")
    print(f"Команды: '{commands_input}'")
    print(f"Результат: '{result}'")
    print()

    #все этапы
    transformer.print_steps()

    #пример для буквы а
    print("\nПоэтапное изменение для буквы 'a':")
    for i in range(len(transformer.step) - 1):
        print(f"{transformer.step[i][0]}:{transformer.step[i + 1][0]}", end="")
        if i < len(transformer.step) - 2:
            print(" -> ", end="")


main()
