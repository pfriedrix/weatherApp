from googletrans import Translator 


def to_translate(text, lang):
	translator = Translator()
	translation = translator.translate(text, dest=lang)
	return translation.text