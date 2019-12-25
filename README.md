# Bitly clicks summary

This program gives a bitly link for a url and the summary of clicks for a bitly link.

### How to install

First sign up on the the website [bitly.com](https://bitly.com/). Activate your email and create 
a [generic access token](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-find-my-OAuth-access-token-).

After you copied this repo locally you'll have to create a `.env` file inside the main directory with one line:
```
BITLY_TOKEN=<your_token>
```

Check that `python3` is already installed (or check the [instructions](https://realpython.com/installing-python/#macos-mac-os-x) to install it):
```
python3 --version
```
Then use `pip3` to install dependencies:
```
pip3 install -r requirements.txt
```

Now you can run the script with the following command:
```
python3 main.py --url <your_url>
```

### Examples
```console
$ python3 main.py --url https://dvmn.org/
Your bitly link: bit.ly/2MvkwaR
The total amount of clicks - 0
```

```console
$ python3 main.py --url bit.ly/2MvkwaR 
The total amount of clicks - 0
```

### Project Goals

This program was created as part of education on [dvmn.org](https://dvmn.org/).