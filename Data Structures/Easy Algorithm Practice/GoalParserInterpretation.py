class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
      
          # .replace("x", "y") is Python's String replace method, and it replaces x with y in a given string. In this case, a string already exists with the name 'command'.
          # count is optional for .replace. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
