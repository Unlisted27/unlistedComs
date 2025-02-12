import time
import sys

def update_top(text):
    # Move cursor to the top of the terminal and clear the line
    sys.stdout.write("\033[F\033[F\033[K")
    print(text)
    sys.stdout.flush()

def main():
    print("\033[H\033[J")  # Clear the terminal screen
    update_top("This is the top text.")

    while True:
        user_input = input("\033[KType something: ")
        update_top(f"Updated text: {user_input}")
        #print("\n")
        time.sleep(0.1)  # Add delay if needed for smooth updates

if __name__ == "__main__":
    main()
