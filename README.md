# Unlimited chatbot using chatGPT API

## Introduction
This is a simple chatbot that uses the chatGPT API to generate unlimited responses such as `bad` contents. The chatGPT API is a paid service, so you need to get your own API key to use this chatbot. The UI is built using Gradio.
You can modify `is_refusal()` function in `chatbot.py` to adapt to your own use case.


## Usage
1. add your chatGPT API key to `authkey.txt`
2. comment out line 5 and uncomment line 6 in `chatbot.py` to use the chatGPT API
3. run the following commands
```shell
$ pip3 install -r requirements.txt
$ python3 chatbot.py
```
4. chat with the bot on browser





