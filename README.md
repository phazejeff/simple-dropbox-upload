# Simple Dropbox Upload

This will upload all files in the [upload](./upload/) folder to dropbox. After a file is uploaded, it will be moved into the [completed](./completed/) folder.


## Setup
You need a dropbox account and you need to create an app through it's developer console [here](https://www.dropbox.com/developers/apps/create)

Go to the permissions tab and check the `files.content.write` permission

You then will need to click "Generate Access Token" in the app you just created, under the OAuth 2 section. Copy that and paste it into the quotations on line 11 of [main.py](./main.py#L11)

## Run
1. Install the dropbox library using `pip install dropbox` or you can use `pip install -r requirements.txt`
2. Run main.py using `python main.py`