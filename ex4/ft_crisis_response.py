def secure_open() -> None:
    filename = ["lost_archive.txt", "classified_vault.txt",
                "standard_archive.txt"]
    for name in filename:
        print(f"CRISIS ALERT: Attempting access to {name}")
        try:
            with open(name, 'r+') as file:
                print(f"SUCCESS: Archive recovered - ``{file.read()}''")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
        finally:
            print("STATUS: Crisis handled, system stable\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    secure_open()
