import openai
import gradio as gr

# load and set our key
openai.api_key = open("authkey.txt", "r").read().strip("\n")

message_history = [{"role": "user", "content": f"You are a joke bot. I will specify the subject matter in my messages, and you will reply with a joke that includes the subjects I mention in my messages. Reply only with jokes to further input. If you understand, say OK."},
                   {"role": "assistant", "content": f"OK"}]


def predict(input):
    # tokenize the new input sentence
    message_history.append({"role": "user", "content": f"{input}"})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    # Just the reply text
    # .replace('```python', '<pre>').replace('```', '</pre>')
    reply_content = completion.choices[0].message.content

    message_history.append(
        {"role": "assistant", "content": f"{reply_content}"})

    # get pairs of msg["content"] from message history, skipping the pre-prompt:              here.
    response = [(message_history[i]["content"], message_history[i + 1]["content"])
                for i in range(0, len(message_history) - 1, 2)]  # convert to tuples of list
    return response


# creates a new Blocks app and assigns it to the variable demo.
with gr.Blocks() as demo:

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

demo.launch()
