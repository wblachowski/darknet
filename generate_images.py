import os

image_files = []
os.chdir(os.path.join("tweets_data", "images"))
for filename in os.listdir(os.getcwd()):
    if not filename.endswith(".txt"):
        image_files.append("tweets_data/images/" + filename)
os.chdir("..")
with open("images.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
