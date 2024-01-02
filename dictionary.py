from googletrans import LANGUAGES, Translator

def display_languages():
    print("Available Languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")

def multi_language_dictionary(word, src_lang, dest_lang):
    translator = Translator()

    # Translate the word into the specified source and destination languages
    translation = translator.translate(word, src=src_lang, dest=dest_lang)
    return translation.text

# Display available languages
display_languages()

# Get user input for source and destination languages
source_language = input("Enter the source language code: ")
destination_language = input("Enter the destination language code: ")

word_input = input("Enter a word: ")
translation_result = multi_language_dictionary(word_input, source_language, destination_language)
print(f"Translation of '{word_input}' from {LANGUAGES[source_language]} to {LANGUAGES[destination_language]}:")
print(translation_result)

