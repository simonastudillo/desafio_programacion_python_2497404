def first_letter_repeted(text):
  readed_characters = []
  text = text.lower()
  text = text.replace(" ", "")
  for character in text:
    if character in readed_characters:
      return character
    else:
      readed_characters.append(character)
  return None

print(first_letter_repeted("Hello World!"))  # {'l': 3, 'o': 2}
print(first_letter_repeted("Hola mundo!"))  # {'o': 2}
print(first_letter_repeted("hola"))  # None