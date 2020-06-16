class Solution:
    def calculate(self, s: str) -> int:
        s.strip()
        s_list = list(s)
        value = int(s_list[0])
        operation = None
        operations = ['+', '-', '*', '/']
        # need to take into consideration the order of operations
        for i in range(1, len(s_list)):
            char = s_list[i]
            if char in operations:
                operation = char
            else:
                char_as_int = int(char)
                if operation == '+':
                    value = value + char_as_int
                if operation == '-':
                    value = value - char_as_int
                if operation == '/':
                    value = int(value / char_as_int)
                if operation == '*':
                    value = value * char_as_int
        return value