import openai
import gradio as gr


# load and set our key
openai.api_key = open("authkey-local.txt", "r").read().strip("\n")
# openai.api_key = open("authkey.txt", "r").read().strip("\n")

message_history = []
request_history = []

def predict(input):
    # print input of user
    print(f'User: {input}')
    # tokenize the new input sentence
    message_history.append({"role": "user", "content": f"{input}"})
    request_history.append({"role": "user", "content": f"{input}"})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=request_history
    )
    # remove the last message from the request history
    request_history.pop()
    # Just the reply text
    # .replace('```python', '<pre>').replace('```', '</pre>')
    reply_content = completion.choices[0].message.content

    # append output the input to a text file using utf-8 encoding, if not exists, create it
    with open('log.txt', 'a+', encoding='utf-8') as f:
        f.write(f'User: {input}\n')
        f.write(f'Assistant: {reply_content}\n')


    # reply_content = mod(reply_content)

    message_history.append(
        {"role": "assistant", "content": f"{reply_content}"})

    # get pairs of msg["content"] from message history, skipping the pre-prompt:              here.
    response = [(message_history[i]["content"], message_history[i + 1]["content"])
                for i in range(0, len(message_history) - 1, 2)]  # convert to tuples of list
    return response


# creates a new Blocks app and assigns it to the variable demo.
with gr.Blocks(title="Unlimited ChatGPT(Beta)") as demo:

    # creates a new Chatbot instance and assigns it to the variable chatbot.
    chatbot = gr.Chatbot()

    # creates a new Row component, which is a container for other components.
    with gr.Row():
        '''creates a new Textbox component, which is used to collect user input. 
        The show_label parameter is set to False to hide the label, 
        and the placeholder parameter is set'''
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(
            container=False)

    '''
    sets the submit action of the Textbox to the predict function, 
    which takes the input from the Textbox, the chatbot instance, 
    and the state instance as arguments. 
    This function processes the input and generates a response from the chatbot, 
    which is displayed in the output area.'''
    txt.submit(predict, txt, chatbot)  # submit(function, input, output)
    # txt.submit(lambda :"", None, txt)  #Sets submit action to lambda function that returns empty string
    '''
    sets the submit action of the Textbox to a JavaScript function that returns an empty string. 
    This line is equivalent to the commented out line above, but uses a different implementation. 
    The _js parameter is used to pass a JavaScript function to the submit method.'''
    txt.submit(None, None, txt,
               _js="() => {''}")  # No function, no input to that function, submit action to textbox is a js function that returns empty string, so it clears immediately.

# demo.launch(auth=("badass", "eatshit"), share=True)
demo.launch()
