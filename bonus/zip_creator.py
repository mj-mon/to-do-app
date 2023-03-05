import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    # Path(path to zip file that will be created(not to the directory),
# with zipfile.ZipFile(dest_dir + "/" + "compressed.zip", 'w') as archive:
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["bonus1.py", "bonus2.1.py"], dest_dir="dest")

