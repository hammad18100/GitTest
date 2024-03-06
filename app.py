import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo1 = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo1.launch()