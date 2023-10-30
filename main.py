def menu():
    print("Menu")
    print("-"*10)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

#mahek encode function
def encode(password):
    #takes number and adds 3 to it
    new_password = ''
    for digit in password:
        num = (int(digit) + 3) % 10
        new_password += str(num) 
    return new_password

#matthew decode function
def decode(encoded_password):
    """Takes in the encoded password and returns the original password."""
    decoded_password = ""
    for number in encoded_password:
        number = int(number)
        # converts password by subtracting 3 if 3 <= value <= 6
        # redefines the number if its between 0 and 2
        if number == 0:
            number = 7
        elif number == 1:
            number = 8
        elif number == 2:
            number = 9
        else:
            number -= 3
        # concatenates each value together into a string
        decoded_number = str(number)
        decoded_password += decoded_number

    return decoded_password


def main():
	flag = True
	while flag:
		menu()
		user_option = input("Please enter an option: ")
		if user_option == '1':
			password = input("Please enter your password to encode: ")
			encoded_password = encode(password)
			print("Your password has been encoded and stored!")
		elif user_option == '2':
			decoded_password = decode(encoded_password)
			print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
		elif user_option == '3':
			flag = False

if __name__ == "__main__":
	main()

