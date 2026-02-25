import sys


def streams_tester() -> None:
    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print()
    sys.stdout.write(f"[STANDARD] Archive status from {id}: {status}\n")
    sys.stdout.flush()
    data = "[ALERT] System diagnostic: Communication channels verified\n"
    sys.stderr.write(data)
    sys.stderr.flush()
    sys.stdout.write("[STANDARD] Data transmission complete\n\n")
    sys.stdout.flush()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    streams_tester()
