while True:
    y = input("input number:  ")
    y = y.lower().replace("illion", "o")
    x = input("input number:  ")
    x = x.lower().replace("illion", "o")
    
    print(f"centinoni{x}-decinoni{x}-noni{x}-centinoni{y}-decinoni{y}-noni{y}-")