def encode(password):
    new_password = ''
    for digit in password:
        num = (int(digit) + 3) % 10
        new_password += str(num) 
    return new_password

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
	print(encode('12345555')

if __name__ == "__main__":
	main()

