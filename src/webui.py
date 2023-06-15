import gradio as gr
from jarvis import jarvis


message_history = []
request_history = []

def predict(input):
    # print input of user
    print(f'User: {input}')
    # tokenize the new input sentence
    message_history.append({"role": "user", "content": f"{input}"})
    
    reply_content = jarvis(input)

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

    chatbot = gr.Chatbot()

    # creates a new Row component, which is a container for other components.
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(
            container=False)
        
    txt.submit(predict, txt, chatbot)  # submit(function, input, output)

    txt.submit(None, None, txt,
               _js="() => {''}")  # No function, no input to that function, submit action to textbox is a js function that returns empty string, so it clears immediately.

demo.launch(auth=("badass", "eatshit"), share=True)

