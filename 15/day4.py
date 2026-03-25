import hashlib

with open("input4.txt", "r") as file:
    start = file.readline().rstrip()
    result = ""
    end = 0
    while result[:6] != "000000":
        end += 1
        hashable = f"{start}{end}"
        result = hashlib.md5(hashable.encode()).hexdigest()

print(end)
print(result)