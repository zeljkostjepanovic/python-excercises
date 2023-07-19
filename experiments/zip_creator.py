import zipfile
import pathlib

def archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'archive.zip')
    with zipfile.ZipFile(dest_path, 'w') as zf:
        for filepath in filepaths:
            zf.write(filepath)
            
            
if __name__ == '__main__':
    archive(filepaths=["webbrowser_test.py", "glob_test.py"], dest_dir="compressed")