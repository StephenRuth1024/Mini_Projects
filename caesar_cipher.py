alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")



should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Application closed. Goodbye.")
    




#code before refactoring


'''def encrypt(text, shift):

    cipher_text = ""
    for i in range(len(text)):
        letter = text[i]
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")'''





'''def decrypt(cipher_text, shift):
    original_text = ""
    for i in range(len(cipher_text)):
        letter = cipher_text[i]
        position = alphabet.index(letter)
        alphabet_length = 26
        formatted_position = position + alphabet_length        
        new_position = formatted_position - shift
        new_letter = alphabet[new_position]
        original_text += new_letter
    print(f"The decoded text is: {original_text}")




if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)


direction2 = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text2 = input("Type your message:\n").lower()
shift2 = int(input("Type the shift number:\n"))

if direction2 == "encode":
    encrypt(text2, shift2)
else:
    decrypt(text2, shift2)

    '''