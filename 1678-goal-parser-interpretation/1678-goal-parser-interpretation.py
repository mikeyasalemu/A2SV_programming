class Solution:
    def interpret(self, command: str) -> str:
        size = len(command)
        result = ""
        x = 0
        while x < size:
            if command[x] == "(" and command[x + 1] == ")":
                result += "o"
                x += 2
            elif command[x] == "(" and command[x + 1] == "a":
                result += "al"
                x += 4
            else:
                result += "G"
                x += 1
        return result
                