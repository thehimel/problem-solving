from solution import roman
import msvcrt

if __name__ == "__main__":
    esc = b'\x1b'  # Byte string for 'Esc' button.

    while(True):
        user_input = input("Enter an integer: ")
        try:
            user_input = int(user_input)
            try:
                print(f'Roman number: {roman(user_input)}')
            except Exception as e:
                print(e)

            print("Press any key to continue. Press 'Esc' to exit.")
            # Capture the pressed key and check if that is Esc.
            if msvcrt.getch() == esc:
                break

        except ValueError:
            # If the input is not an int.
            print("Invalid input. ", end='')
