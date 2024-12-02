
from camel_tools.tokenizers.word import WordTokenizer
from camel_tools.utils.dediacritizer import Dediacritizer
from camel_tools.utils import BCP47
from camel_tools.ner import NamedEntityRecognizer

# Example: Camel Tools can perform root extraction
tokenizer = WordTokenizer()
tokens = tokenizer.tokenize("مكتوب")

# The tokenizer outputs words and roots
print(tokens)