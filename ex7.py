class MorseMsg:
    """
    A class representing a Morse code message.
    """

    MORSE_EN = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--.."
    }

    MORSE_RU = {
        "А": ".-", "Б": "-...", "В": ".--", "Г": "--.",
        "Д": "-..", "Е": ".", "Ж": "...-", "З": "--..",
        "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..",
        "М": "--", "Н": "-.", "О": "---", "П": ".--.",
        "Р": ".-.", "С": "...", "Т": "-", "У": "..-",
        "Ф": "..-.", "Х": "....", "Ц": "-.-.",
        "Ч": "---.", "Ш": "----", "Щ": "--.-",
        "Ъ": "--.--", "Ы": "-.--", "Ь": "-..-",
        "Э": "..-..", "Ю": "..--", "Я": ".-.-"
    }

    def __init__(self, code: str):
        """
        Initialize a Morse code message.
        """
        self.code = code

  
    def _decode(self, alphabet: dict) -> str:
        """
        Decode Morse code using the provided alphabet.
        """
      
        reverse = {v: k for k, v in alphabet.items()}
        return "".join(reverse[s] for s in self.code.split())

  
    def eng_decode(self) -> str:
        """
        Return decoded message in English.
        """
      
        return self._decode(self.MORSE_EN)

  
    def ru_decode(self) -> str:
        """
        Return decoded message in Russian.
        """
      
        return self._decode(self.MORSE_RU)

  
    def get_vowels(self, lang: str) -> list:
        """
        Return vowels from the decoded message.
        """
      
        if lang == "ru":
            text = self.ru_decode()
            vowels = set("АЕЁИОУЫЭЮЯ")
        else:
            text = self.eng_decode()
            vowels = set("AEIOUY")
        return [ch for ch in text if ch in vowels]

  
    def get_consonants(self, lang: str) -> list:
        """
        Return consonants from the decoded message.
        """
      
        if lang == "ru":
            text = self.ru_decode()
            vowels = set("АЕЁИОУЫЭЮЯ")
        else:
            text = self.eng_decode()
            vowels = set("AEIOUY")
        return [ch for ch in text if ch not in vowels]

  
    def __str__(self) -> str:
        """
        Return the Morse code string.
        """
      
        return self.code

  
    __repr__ = __str__
