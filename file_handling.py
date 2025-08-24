# File Read & Write with Error Handling

def modify_text(text):
    """Example modification: make text uppercase"""
    return text.upper()

def main():
    try:
        # Ask user for filename
        filename = input("Enter the filename to read: ")

        # Try opening the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_text(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
