# Ingreso del texto
text= input("Please enter your text: ").lower()

# Guardar las letras en una lista

letter_list = []
letter_list.append(input("Please enter your  first letter: ").lower())
letter_list.append(input("Please enter your  second letter: ").lower())
letter_list.append(input("Please enter your  third letter: ").lower())

# Requisite #1
print("\n")
print("Letters quantity")
print(f"The letter '{letter_list[0]}' appears {text.count(letter_list[0])} times ")
print(f"The letter '{letter_list[1]}' appears {text.count(letter_list[1])} times ")
print(f"The letter '{letter_list[2]}' appears {text.count(letter_list[2])} times ")

# Requisite #2
print("\n")
print("Words quantity")
print(f"In the text are {len(text.split())} words")

# Requisite #3
print("\n")
print("First letter, last letter")
print(f"The first letter is {text[0]} and the last is {text[-1]}")

# Requisite #4
print("\n")
print("Reversed text")
print(f"The reverse of your text is {' '.join(text.split().reverse())}")

# Requisite #5
print("\n")
print("Searching for 'python' ")
consult = "python" in text
dic = {True: "yes" , False: "no"}
print(f"The word 'python' is in the text : {dic[consult]}")
