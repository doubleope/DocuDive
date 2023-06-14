import gradio as gr
from DocuDive import getResult, loadModel

llm = loadModel()

with gr.Blocks() as demo:
    gr.Markdown("## Chat with Amazon SageMaker")
    with gr.Column():
        chatbot = gr.Chatbot()
        with gr.Row():
            with gr.Column():
                message = gr.Textbox(label="Chat Message Box", placeholder="Chat Message Box", show_label=False)
            with gr.Column():
                with gr.Row():
                    submit = gr.Button("Submit")
                    clear = gr.Button("Clear")

    def respond(message, chat_history):
        # convert chat history to prompt
        converted_chat_history = ""
        if len(chat_history) > 0:
          for c in chat_history:
            converted_chat_history += f"<|prompter|>{c[0]}<|endoftext|><|assistant|>{c[1]}<|endoftext|>"
        prompt = f"{converted_chat_history}<|prompter|>{message}<|endoftext|><|assistant|>"

        # send request to endpoint
        llm_response = getResult(prompt, llm)

        # remove prompt from response
        answer, documents = llm_response
        
        response = answer +"\n"
        for doc in documents:
            response += doc.metadata["source"]+":\n" + doc.page_content + "\n\n"
        chat_history.append((message, response))
        return "", chat_history

    submit.click(respond, [message, chatbot], [message, chatbot], queue=False)
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch(share=True)