from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import gradio as gr

# .env 를 환경변수로 설정
load_dotenv(find_dotenv())
client = OpenAI()


# 장르를 받은 후 장르 작가에게 알맞는 질문 8개 생성
# 장르 특징 5줄로 정리
def interview_text(genre):
    if not genre.strip():
        return gr.Error("장르를 입력해 주세요")

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "developer",
                "content": "장르 작가에게 할 인터뷰의 질문을 만들어주는 전문가 입니다",
            },
            {
                "role": "user",
                "content": f"""
                - 먼저 {genre} 에 대한 설명과 특징을 5줄로 정리해서 설명해.
                - 그 이후 아래를 참고해서 8개의 질문을 생성해.
                - 유사한 내용의 질문은 중복하지마.
                - 전술한 장르 설명을 줄이고 개인적인 인터뷰를 하는 것을 권장할게.
                - 정중하고 매너있는 말투로 질문해.
                """,
            },
        ],
    )
    return response.output_text


demo = gr.Interface(
    fn=interview_text,
    inputs=[gr.Text(label="장르", placeholder="장르")],
    outputs=[gr.Markdown()],
    title="인터뷰 질문 생성 프로그램 구현",
)
demo.launch()
