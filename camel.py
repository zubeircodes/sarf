
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from google.cloud import translate_v2 as translate
# import nltk
# nltk.download('popular') 

# from nltk.corpus import wordnet as wn


kitab = "كِتَاب"


letters = [chr(code) for code in range(0x0621, 0x064B)]
fatha = '\u064E'

word1 = letters[8]+letters[12] + letters[15]
print(word1)

reshaped_word = reshape(kitab)
adjusted = get_display(reshaped_word)
print(adjusted)

print(len(letters))

verb = '' + letters[32]+fatha + letters[24]+fatha + letters[35] + fatha
print(verb)
# verb = reshape(verb)
verb = get_display(verb)
print(verb)

def getTranslation(text):
    translate_client = translate.Client()
    result = translate_client.translate(text, source_language='ar', target_language='en')
    return result['translatedText']

print(getTranslation(kitab))



# synsets = wn.synsets(kitab, lang='arb')
# for synset in synsets:
#     print(f"Synset: {synset.name()}, Definition: {synset.definition()}")

