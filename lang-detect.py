from langdetect import detect
from langdetect import detect_langs
from languages import all_languages_codes

userInput = input("Enter input in any language: ")

language_code = detect_langs(userInput)
lang_code = detect(userInput)

sentence = all_languages_codes.get(lang_code), language_code, userInput
print("The language is:", sentence)




