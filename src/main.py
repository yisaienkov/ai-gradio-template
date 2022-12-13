import gradio as gr
import torch


print("Model initialization starts")
model = torch.hub.load(
    "AK391/animegan2-pytorch:main", 
    "generator", 
    pretrained="face_paint_512_v2",
)
face2paint = torch.hub.load(
    'AK391/animegan2-pytorch:main', 
    'face2paint', 
    size=512, 
    side_by_side=False,
)
print("Model initialization ends")

def inference(img):
    out = face2paint(model, img)
    return out


demo = gr.Interface(
    fn=inference, 
    inputs=[
        gr.inputs.Image(type="pil"),
    ], 
    outputs=[
        gr.outputs.Image(type="pil"),
    ],
    allow_flagging="never",
    title="AnimeGAN template",
)

demo.launch(server_name="0.0.0.0")