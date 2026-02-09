def file_opener(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            data = file.read()
            print(f"RECOVERED DATA: \n{data}\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error oppening the file: {e}")
    finally:
        file.close()
        print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}\n")
    file_opener(filename)