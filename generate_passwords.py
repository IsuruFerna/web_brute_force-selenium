from string import ascii_letters, digits, punctuation

def appended_to_password_file(passwords, filename="passwords.txt"):
    try:
        with open(filename, 'a+') as file:
            # if passwords is a single string
            if isinstance(passwords, str):
                file.write(passwords + '\n')
                print(f'Appended: {passwords}')

            # if passwrod is a list
            elif isinstance(passwords, list):
                for pwd in passwords:
                    file.write(pwd + '\n')
                    print(f"Appended: {pwd}")
            
            else:
                print("Error: Input must be a sring or a list of strings")

    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    for i in ascii_letters + digits + punctuation:
        for j in ascii_letters + digits + punctuation:
            for k in ascii_letters + digits + punctuation:
                for l in ascii_letters + digits + punctuation:
                    for m in ascii_letters + digits + punctuation:
                        for n in ascii_letters + digits + punctuation:
                            password = f"{i}{j}{k}{l}{m}{n}"
                            appended_to_password_file(password, filename="passwords.txt")

