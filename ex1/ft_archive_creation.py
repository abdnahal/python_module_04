def file_opener(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            data = file.read()
            print(data)
            print()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error oppening the file: {e}")


def file_writer(filename: str) -> None:
    try:
        with open(filename, "w") as file:
            print("Inscribing preservation data...")
            file.write("[ENTRY 001] New quantum algorithm discovered\n")
            file.write("[ENTRY 002] Efficiency increased by 347%\n")
            file.write("[ENTRY 003] Archived by Data Archivist trainee")
        file_opener(filename)
    except (FileExistsError) as e:
        print(f"Error creating {filename}: {e}")
    finally:
        print("Data inscription complete. Storage unit sealed.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    filename = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")
    print("Storage unit created successfully...\n")
    file_writer(filename)
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
