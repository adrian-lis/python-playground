import os

name = str(os.getenv("REQUIREMENT_NAME"))
count = int(os.getenv("NUMBER_OF_REQUIREMENT"))

EveryRequiremet = [f"{name}-REQ-{i}" for i in range(count)]

for req in EveryRequiremet:
    print(req)
