
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(mess,key):
    cipher_text=""
    for i in message:
        if i in alphabets:
            position = alphabets.index(i)
            new_position = (position + shift_key) % 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text+=' '
    print(f"Here's the encrypted result:{cipher_text}")


def decrypt(mess,key):
    plain_text=""
    for i in message:
        if i in alphabets:
            position = alphabets.index(i)
            new_position = (position - shift_key)
            plain_text += alphabets[new_position]
        else:
            plain_text +=' '

    print(f"Here's the encrypted result:{plain_text}")


wanna_end=False
while not wanna_end:
    user_input = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:")
    message = input("Type a message:\n")
    shift_key = int(input("enter the shift number:\n"))
    if user_input == 'encrypt' or user_input == 'ENCRYPT':
        encrypt(mess=message, key=shift_key)
    elif  user_input == 'decrypt':
        decrypt(mess=message, key=shift_key)
    user_choice = input("Type 'yes' if you want to go again. Otherwise type 'no': ")


    if user_choice=='no':
        wanna_end=True
        print("thankyou")







