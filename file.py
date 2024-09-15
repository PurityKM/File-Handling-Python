"""
This module demonstrates Python file handling operations, including:
- Creating and writing to a file
- Reading file contents
- Appending to a file
- Handling file-related exceptions
"""

def create_file():
    """Create a file and write initial content."""
    try:
        with open("my_file.txt", "w", encoding="utf-8") as file:
            file.write("Hello, how is it going?.\n")
            file.write("I hope your're doing great.\n")
            file.write("Welcome all to the world of tech.\n")
        print("Coding is going to be fun.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while creating or writing to file: {e}")

def read_file():
    """Read the content of the file and display it."""
    try:
        with open("my_file.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print("File content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while reading file: {e}")

def append_to_file():
    """Append additional content to the file."""
    try:
        with open("my_file.txt", "a", encoding="utf-8") as file:
            file.write("But this is going to be possible when,\n")
            file.write("You make sure that you have some time to code.\n")
            file.write("Plus keeping yourself updated with the technology.\n")
        print("Additional content appended to file.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while appending to file: {e}")

def main():
    """Main function to execute file handling tasks."""
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read file again to show the appended content

if __name__ == "__main__":
    main()
