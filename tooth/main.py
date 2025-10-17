import random

VOCABULARY = [
    "は", "ハ", "歯",
    "Tooth", "Teeth",
    "🦷"
]

class Tooth:
    def __init__(self, vocab: list[str] = VOCABULARY):
        self.vocab = vocab
        self.memory: list[str] = []

    @property
    def seed(self):
        return "".join(self.memory)

    # Generating text
    def generate(self, input: str) -> str:
        self.memory.append(input)

        random.seed(self.seed)
        
        input_length = len(input)
        result_length = random.randint(input_length // 2, input_length * 2)

        result_list = []

        for i in range(result_length):
            result_list.append(random.choice(self.vocab))
        
        result_text = "".join(result_list)
        self.memory.append(result_text)
        return result_text