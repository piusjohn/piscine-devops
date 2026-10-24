def to_do(input):
    with open("output.txt", "w") as f:
        for date, item in input:
            formatted = date.strftime("%A %d %B %Y")
            f.write(f"{formatted}: {item}\n")
            
