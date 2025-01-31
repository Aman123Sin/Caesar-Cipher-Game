alphabate = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        position = alphabate.index(char)
        new_position = (position+shift_key)%26
        cipher_text += alphabate[new_position]
    print(f"Here's is the text after encryption: {cipher_text}")

def decryption(plain_text, shift_key):
    cipher_text2 = ""
    for char in plain_text:
        position = alphabate.index(char)
        new_position2 = (position-shift_key)%26
        cipher_text2 += alphabate[new_position2]
    print(f"Here's is the text after decryption: {cipher_text2}")
should_container = True
while should_container:
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Enter shift Key: \n"))
    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(plain_text = text, shift_key=shift)
    else:
        print("You insert wrong input. \nPlease insert correct input. ")
    loop = input("If continue again than tap 'Yes' otherwise tap 'No'.\n").lower()
    if loop == 'yes':
        should_container = True
    elif loop == 'no':
        should_container = False
        print("................Goodbye!................")