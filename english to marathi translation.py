import requests
import time

# Function to get Marathi translation using a free translation API
def translate_word(word, target_language='mr'):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": word,
        "langpair": f"en|{target_language}"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['responseData']['translatedText']

# List of sample English words
for a in range(1,11):
 words = [str(input('enter the paragraph for translation: '))]
 a+=1

# Dictionary to store words and their translations
 word_translations = {}

# Loop over words and get their Marathi translation
 for word in words:
     try:
         translated_word = translate_word(word)
         word_translations[word] = translated_word
     except Exception as e:
         print(f"Error translating {word}: {e}")
         time.sleep(1)  # To prevent hitting the API rate limit

# Print the word translations
 for word, translation in word_translations.items():
    print(f" {translation}")

