import os

image_files = []
os.chdir(os.path.join("tweets_data", "empty"))
for filename in os.listdir(os.getcwd()):
    if not filename.endswith(".txt"):
        txt_name = '.'.join(filename.split('.')[:-1]) + '.txt'
        open(txt_name, "w+").close()
