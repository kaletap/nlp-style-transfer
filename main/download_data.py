import os
import requests
from clint.textui import progress
import shutil


def download_and_save_file(url: str, save_path: str, overwrite: bool = False) -> bool:
    if os.path.exists(save_path) and not overwrite:
        print("File {} already exists.".format(save_path))
        return False
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()
    print("Saved data in {}.".format(save_path))
    return True


def download_and_save_imdb_dataset():
    imdb_data_url = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
    save_tar_path = "data/imdb_tmp.tar.gz"
    print("Started downloading idbd_v1 dataset from {}.".format(imdb_data_url))
    download_and_save_file(imdb_data_url, save_tar_path)
    print("Unpacking {}.".format(save_tar_path))
    shutil.unpack_archive(save_tar_path, "data")
    os.remove(save_tar_path)
    print("Imdb data now available in data folder")


if __name__ == "__main__":
    # Download and save imdb dataset to data folder
    download_and_save_imdb_dataset()
