import dropbox # https://github.com/dropbox/dropbox-sdk-python
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError
import os

UPLOAD_FOLDER = "./upload/"
COMPLETED_FOLDER = "./completed/"
DB_UPLOAD_PATH = "/" # This can be set to the dropbox folder you want shit saved into

# usually this would be set as environment variables for security reasons but im lazy
ACCESS_TOKEN = "sl.BK9NeLKwDceglxXw-JXiMo0lyvHxgpdTP3vLZMV7o822WHJctRWklRv2vBwVY26AR8TdZ6HLMdW3IEq0eC6uik8bRxIYT3qR5uLnQtGh9KT0THwOn8rRPUr9yDIrDsnGo0q0d-E"

dbx = dropbox.Dropbox(ACCESS_TOKEN)

for filename in os.listdir(UPLOAD_FOLDER):
    location = UPLOAD_FOLDER + filename

    if os.path.isfile(location):
        f = open(location, 'rb') # Opens file in binary mode
        try:
            dbx.files_upload(f.read(), DB_UPLOAD_PATH + filename, mode=WriteMode('overwrite'))
            f.close()
        except Exception as e:
            print("Something went wrong! Skipping to next file. Error: " + e)
            continue
        
        os.replace(location, COMPLETED_FOLDER + filename) # Move file to completed folder