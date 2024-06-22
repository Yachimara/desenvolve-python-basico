import emoji
print("Emojis disponíveis:")
print(f"{emoji.emojize(":thumbs_up:")} - :thumbs_up:")
print(f"{emoji.emojize(":smiling_face:")} - :smiling_face:")
print(f"{emoji.emojize(":hot_face:")} - :hot_face:")
print(f"{emoji.emojize(":winking_face:")} - :winking_face:")
g=input("Digite uma frase: ")
e=input("Escolha um emoji: ")
print(g, emoji.emojize(e))