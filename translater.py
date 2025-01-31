from translate import Translator


translator = Translator(to_lang='es')

text = "Hello world!"

translation = translator.translate(text)
print(translation)
