def get_most_common_letter(text):
    counter = {}
    print(f"For Loop starts:...")
    for char in text:
        if char not in "!, ":
            print(f"Value of char before: {char}")
            counter[char] = counter.get(char, 0) + 1
            print(counter)
    letter = sorted(counter.items(), key=lambda item: item[1])[::-1]
    print(f"Last letter: {letter}")
    print("Counter items:")
    print(list(counter.items()))
    print(letter)
    return letter[0][0]


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")