photo_file = "C:/Users/SameeraTanveer/OneDrive - BILVANTIS TECHNOLOGIES PRIVATE LIMITED/Pictures/Screenshots/test.png"
copy_to = "C:/Users/SameeraTanveer/OneDrive - BILVANTIS TECHNOLOGIES PRIVATE LIMITED/Pictures/Screenshots/copy.png"
with open(photo_file, "rb") as source:
    with open(copy_to, "wb") as target:
        target.write(source.read())
