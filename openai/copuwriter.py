from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import gradio as gr

# .env 를 환경변수로 설정
load_dotenv(find_dotenv())
client = OpenAI()


def ads_text(name, breand_name, strength, value, tone_manner, keyword):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "developer", "content": "당신은 최고의 카피라이터 입니다"},
            {
                "role": "user",
                "content": f"""
                아래 내용을 참고해서 1~2줄짜리 광고 문구 5개 작성해
                - 제품명 : {name}
                - 브랜드명 : {breand_name}
                - 브랜드 핵심 가치 : {strength}
                - 제품특징 : {value}
                - 톤앤매너 : {tone_manner}
                - 필수 포함 키워드 : {keyword}
                """,
            },
        ],
    )
    return response.output_text


demo = gr.Interface(
    fn=ads_text,
    inputs=[
        gr.Text(label="제품명"),
        gr.Text(label="브랜드명"),
        gr.Text(label="브랜드 핵심 가치"),
        gr.Text(label="제품특징"),
        gr.Text(label="톤앤매너"),
        gr.Text(label="필수 포함 키워드"),
    ],
    outputs=[gr.Markdown()],
    title="광고문구 프로그램 구현😊",
)
demo.launch()
