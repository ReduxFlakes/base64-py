import base64

user_input = input("Enter the desire string to be converted: ")
encoded_str = base64.b64encode(user_input.encode())
print("Encoded string: ", encoded_str.decode())
