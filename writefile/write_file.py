def to_do(input):
    with open("output.txt", "w") as file:
        for date, item in input:
            formatted = date.strftime("%A %d %B %Y")
            file.write(f"{formatted}: {item}\n")
            