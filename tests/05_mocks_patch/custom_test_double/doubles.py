"""Test"""


class AppTestDouble:
    """
    Test double for spaCy NLP model
    """

    def __init__(self, model):
        self.model = model

    def return_result(self, ents):
        """test"""
        return ents

    def __call__(self, sentence):
        ents = {"ents": sentence}
        return self.return_result(ents)

    def patch_method(self, attr, return_value):
        """Custom patch"""

        def patched():
            """patch return value"""
            return return_value

        setattr(self, attr, patched)
        return self
