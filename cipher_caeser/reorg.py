alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  

def caeser(cipher_text,shift_number,direction):
    coded=""
    if direction=="decode":
        shift_number*=-1
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            coded += alphabet[new_position]
        else:
            coded += char
    print(f"Here's the {direction}d result: {coded}")
  
  
should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caeser(cipher_text=text, shift_number=shift, direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
      should_end = True
      print("Goodbye")
    
