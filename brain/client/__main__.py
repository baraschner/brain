import fire
from .client_api import upload_sample

if __name__ == '__main__':
    fire.Fire({"upload-sample": upload_sample})
