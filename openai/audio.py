from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import base64
from io import BytesIO
from PIL import Image
import gradio as gr
import tempfile

# .env 를 환경변수로 설정
load_dotenv(find_dotenv())

client = OpenAI()


def generate_voice(prompt):
    speech = client.audio.speech.create(
        model="gpt-4o-mini-tts", voice="ash", input=prompt
    )
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    tmp_path = tmp.name
    tmp.close

    with open(tmp_path, "wb") as f:
        f.write(speech.read())

    return tmp_path


demo = gr.Interface(
    fn=generate_voice,
    inputs=gr.Text(placeholder="예)안녕하세요", label="텍스트", lines=3),
    outputs=gr.Audio(type="filepath", autoplay=True),
)

demo.launch()
