
class Calculator:
    def __init__(self):
        self._memory = []
        self._inputs = {'+': lambda x, y: x + y,
                        '-': lambda x, y: x - y,
                        '*': lambda x, y: x * y,
                        ':': lambda x, y: x / y,
                        '=': '',
                        'clear': ''}

    def action(self, input_action: str):
        if not input_action.isdigit() and input_action not in self._inputs.keys():
            print('Invalid input')
            return 1

        if input_action == "=":
            for action in ['*', ':', '-', '+']:
                while action in self._memory:
                    index = self._memory.index(action)
                    previous_element = float(self._memory[index-1])
                    next_element = float(self._memory[index+1])
                    result = self._inputs[action](previous_element, next_element)
                    del self._memory[index-1:index+2]
                    self._memory.insert(index-1, str(result))

        elif input_action == "clear":
            self._memory = []

        else:
            self._memory.append(input_action)

        print(self._memory)


if __name__ == '__main__':
    my_calc = Calculator()
    while True:
        inp = input("Input action: ")
        my_calc.action(inp)
