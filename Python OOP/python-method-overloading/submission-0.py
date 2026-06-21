class TextProcessor:
    def format_text(self, text1:str, text2 = None) -> str:
        return text1.upper() if text2 is None else text1+text2


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
