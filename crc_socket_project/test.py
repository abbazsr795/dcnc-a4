import subprocess
import time

tests = [
    ("A", "n", "VALID"),
    ("A", "y", "CORRUPTED"),
    ("", "n", "VALID"),
    ("", "y", "CORRUPTED"),
    ("AAAAAAA", "n", "VALID"),
    ("AAAAAAA", "y", "CORRUPTED"),
    ("12345", "n", "VALID"),
    ("12345", "y", "CORRUPTED"),
    ("HI!", "n", "VALID"),
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

    time.sleep(0.1)

    client = subprocess.Popen(
        ["python3", "-m", "client.client"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    client.communicate(f"{message}\n{corrupt}\n")

    server_output, _ = server.communicate()

    # extract decoded message
    decoded = None
    for line in server_output.splitlines():
        if "Decoded message:" in line:
            decoded = line.split("Decoded message:")[-1].strip()

    test_passed = False

    if expected == "VALID":
        test_passed = (
            "CRC RESULT: VALID" in server_output
            and decoded == message
        )

    else:  # CORRUPTED
        test_passed = (
            "CRC RESULT: CORRUPTED" in server_output
        )

    if test_passed:
        print("PASS")
        passed += 1
    else:
        print("FAIL")
        print("Expected:", expected)
        print("Message:", message)
        print(server_output)

print(f"\nPassed {passed}/{len(tests)} tests")