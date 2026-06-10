import subprocess
import time

tests = [
    ("HELLO", "n", "VALID"),
    ("HELLO", "y", "CORRUPTED"),
    ("WORLD", "n", "VALID"),
    ("WORLD", "y", "CORRUPTED"),
    ("PIZZA", "n", "VALID"),
    ("PIZZA", "y", "CORRUPTED"),
    ("UNICORN", "n", "VALID"),
    ("UNICORN", "y", "CORRUPTED"),
    ("ROCKET", "n", "VALID"),
    ("ROCKET", "y", "CORRUPTED"),
    ("BANANA", "n", "VALID"),
    ("BANANA", "y", "CORRUPTED"),
    ("SUSHI", "n", "VALID"),
    ("SUSHI", "y", "CORRUPTED"),
    ("PENGUIN", "n", "VALID"),
    ("PENGUIN", "y", "CORRUPTED"),
    ("LASER", "n", "VALID"),
    ("LASER", "y", "CORRUPTED"),
    ("MEME", "n", "VALID"),
    ("MEME", "y", "CORRUPTED"),
]

passed = 0

for i, (message, corrupt, expected) in enumerate(tests, start=1):
    print(f"\nRunning Test {i}...")

    server = subprocess.Popen(
        ["python3", "-m", "server.server"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    time.sleep(1)

    client = subprocess.Popen(
        ["python3", "-m", "client.client"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    client.communicate(f"{message}\n{corrupt}\n")

    server_output, _ = server.communicate()

    if expected in server_output:
        print("PASS")
        passed += 1
    else:
        print("FAIL")
        print("Expected:", expected)
        print(server_output)

print(f"\nPassed {passed}/{len(tests)} tests")