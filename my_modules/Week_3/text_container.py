import string

class TextContainer:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        return len(self.text.split())

    def count_chars(self):
        return len(self.text.replace(" ", ""))

    def count_letters(self):
        count = 0
        for c in self.text:
            if c in string.ascii_letters:
                count+=1
        return count
    
    def remove_punct(self):


tc = TextContainer('a b c d e')
print("Words: " + str(tc.count_words()))
print("Chars: " + str(tc.count_chars()))
print(tc.count_letters())