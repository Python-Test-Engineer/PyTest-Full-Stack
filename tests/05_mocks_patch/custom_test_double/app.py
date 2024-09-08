"""Test"""


class AppClient:
    """Doc string"""

    def __init__(self, model: str) -> None:
        """doc string"""
        self.model = model

    def get_result(self, sentence: str) -> dict:
        """doc string"""
        print("\n")
        print("=======================")
        print("do complex work...")
        sentence = sentence.upper()
        print(sentence)
        print("=======================")
        return {"ents": sentence}

    def func_to_patch(self) -> int:
        """We will patch this function"""
        result: int = 2 * 10
        print(f"---> IN func_to_patch returns {result}")
        return result
