photo_file = "C:/Users/SameeraTanveer/OneDrive - BILVANTIS TECHNOLOGIES PRIVATE LIMITED/Pictures/Screenshots/test.png"
with open(photo_file, "rb") as f:
    data = f.read()
    print(data)
    print(type(data))
