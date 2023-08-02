from flask import Flask, render_template
from flask import request, url_for, redirect

app = Flask(__name__)

image_urls = [
    {
        "image_url": "/static/logo_w.png",
        "text": "이미지 게시물 1의 내용입니다.",
        "category": "category1"  # 카테고리 정보 추가
    },
    {
        "image_url": "/static/logo_w.png",
        "text": "이미지 게시물 2의 내용입니다.",
        "category": "category2"  # 카테고리 정보 추가
    },
    {
        "image_url": "/static/logo_w.png",
        "text": "이미지 게시물 3의 내용입니다.",
        "category": "category3"  # 카테고리 정보 추가
    },
    # 추가적인 이미지 게시물들을 이곳에 추가할 수 있습니다.
]


@app.route('/')
def basic() :
    return 'empty space'



@app.route('/coji')
def index():

    return render_template('index.html', image_urls=image_urls)


# 지원 기관 페이지 라우트
@app.route('/support')
def support():
    # 여기에서 지원 기관 페이지에 필요한 데이터를 전달하는 작업을 추가합니다.
    return render_template('support.html')


# 소셜 벤처 페이지 라우트
@app.route('/social_venture')
def social_venture():
    # 여기에서 소셜 벤처 페이지에 필요한 데이터를 전달하는 작업을 추가합니다.
    return render_template('social_venture.html')


# 팀 소개 페이지 라우트
@app.route('/team')
def team():
    # 여기에서 팀 소개 페이지에 필요한 데이터를 전달하는 작업을 추가합니다.
    return render_template('team.html')


if __name__ == '__main__':
    app.run(debug=True)

