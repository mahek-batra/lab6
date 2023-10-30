def encode(password):
    new_password = ''
    for digit in password:
        num = int(digit) + 3
        new_password += str(num)
    return new_password

def main():
	print(encode('12345555')

if __name__ == "__main__":
	main()

