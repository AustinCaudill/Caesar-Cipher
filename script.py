message_en = []
def cCipher(message, shift):
    if isinstance(message,str):
        for item in list(message):
            new_ch = ord(item) + shift
            message_en.append(chr(new_ch))
            #print(message_en)
        final_message = "".join(message_en)
        print(final_message)
    else:
        print("Message is not a string!")


# Test Function
cCipher("Testing my Caesar Cipher function.",7)

