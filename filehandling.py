def read_and_write_file():
    """
    Reads content from a file, modifies it, and writes it to a new file.
    Handles errors gracefully if the file does not exist or cannot be read.
    """
    try:
        # Ask the user for the filename
        input_filename = input("Enter the name of the file to read: ")

        # Attempt to open and read the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content (convert to uppercase in this example)
        modified_content = content.upper()

        # Write the modified content to a new file
        output_filename = input("Enter the name of the file to write the modified content to: ")
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{input_filename}' or write to the output file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
if __name__ == "__main__":
    read_and_write_file()
