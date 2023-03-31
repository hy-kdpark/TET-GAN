import gradio as gr
import torch
import sys
sys.path.append('src')
from models import TETGAN
from utils import load_image, to_data, to_var, save_image

tetGAN = TETGAN()
tetGAN.load_state_dict(torch.load('save/tetgan-aaai.ckpt'))
tetGAN.cuda()
tetGAN.eval()

def tet_gan(_content):
    files = []
    for i in range(64):
        # print('--- load data ---')
        style = to_var(load_image('data/style/{}.jpg'.format(i+1)))
        content = to_var(load_image(_content, 1))
        # print('--- testing ---')
        result = tetGAN(content, style)
        result = to_data(result)
        # print('--- save ---')
        save_image(result[0], 'output/gradio/{}.png'.format(i+1))
        # print('{}.png saved'.format(i+1))
        files.append('output/gradio/{}.png'.format(i+1))
    return files

inputs = [
    gr.Image(label='input', type='filepath', tool='None'),
]

outputs = [
    gr.Gallery(label='output').style(grid=[4], height='auto'),
]

contents = [
    ['data/content/01.png'],
    ['data/content/02.png'],
    ['data/content/03.png'],
    ['data/content/04.png'],
    ['data/content/05.png'],
    ['data/content/06.png'],
    ['data/content/07.png'],
    ['data/content/08.png'],
]

css = '''
    .input_image_example { height:10rem; max-width: none; }
'''

demo = gr.Interface(
    fn=tet_gan,
    inputs=inputs,
    outputs=outputs,
    live=False,
    title='텍스트 효과 입히기',
    allow_flagging='never',
    theme='default',
    examples=contents,
    css=css,
)

demo.launch(
    server_name='0.0.0.0', 
    server_port=8000,
    debug=False,
    # enable_queue=True
)
