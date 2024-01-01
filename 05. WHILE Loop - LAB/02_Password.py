name = input()
password = input()

prompt = input()

while prompt != password:
    prompt = input()

print(f"Welcome {name}!")