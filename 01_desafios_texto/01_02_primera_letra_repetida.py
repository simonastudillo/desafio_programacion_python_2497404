def firstLetterRepeted(text):
  readedCharacters = []
  text = text.lower()
  text = text.replace(" ", "")
  for character in text:
    if character in readedCharacters:
      return character
    else:
      readedCharacters.append(character)
  return None

print(firstLetterRepeted("Hello World!"))  # {'l': 3, 'o': 2}
print(firstLetterRepeted("Hola mundo!"))  # {'o': 2}
print(firstLetterRepeted("hola"))  # None