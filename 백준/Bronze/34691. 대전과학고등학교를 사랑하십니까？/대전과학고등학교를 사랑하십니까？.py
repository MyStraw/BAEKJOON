mapping = {
    "animal": "Panthera tigris",
    "tree": "Pinus densiflora",
    "flower": "Forsythia koreana"
}

while True:
    q = input().strip()
    if q == "end":
        break
    print(mapping[q])
