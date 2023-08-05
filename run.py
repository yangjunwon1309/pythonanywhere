from flask import Flask, render_template
from flask import request, url_for, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBs"


image_urls = [
    {
        "image_url": "/static/logo_w.png",
        "text": "이미지 게시물 1의 내용입니다.",
        "category": "category1"  # 카테고리 정보 추가
    },
    {
        "image_url": "/static/recruit_poster.png",
        "text": "2023 하반기 루키 카이스트 리쿠르팅",
        "category": "category2"  # 카테고리 정보 추가
    },
    {
        "image_url": "/static/logo_w.png",
        "text": "이미지 게시물 3의 내용입니다.",
        "category": "category3"  # 카테고리 정보 추가
    },
    # 추가적인 이미지 게시물들을 이곳에 추가할 수 있습니다.
]

sv_urls = [
    {
        "name":"돌봄드림",
        "corevalue":"스마트 조끼로 안정과 안전을 동시에, 발달장애 아동들을 위한 솔루션",
        "image_url": "https://dolbomdream.com/web/upload/slide/slide3.jpg",
        "image_text": "스마트 조끼 Huggy, 데이터 기반 정신건강 관리 솔루션 ",
        "text" : "핵심 기술 : ",
        "link":"https://dolbomdream.com/",
        "category": "social"
    },
    {
        "name": "베이띵스",
        "corevalue": "KnockKnock, 누구나 어디에서도 편한 여행을 할 수 있도록",
        "image_url": "/static/logo_w.png",
        "image_text": "장애인들을 위한 숙박업소 안내 플랫폼, 노크노크",
        "text": "노크노크 설명 노크노크 설명",
        "link": "https://baithings.co.kr/",
        "category": "social"
    },
    {
        "name": "숨케어",
        "corevalue": "숨케어 앱으로 언제 어디서나 숨쉬는데 고통받지 않도록",
        "image_url": "/static/logo_w.png",
        "image_text": "만성호흡기 질환자 관리지침서 어플, 숨케어",
        "text": "설명",
        "link": "https://baithings.co.kr/",
        "category": "social"
    },
    {
        "name": "잇마플",
        "corevalue": "삼시세끼 먹는 시간마다 항상 안심하고 먹을 수 있도록",
        "image_url": "/static/logo_w.png",
        "image_text": "콩팥병 환자들을 위한 맞춤 저염식 배송 서비스, 맛있저염",
        "text": "설명",
        "link": "https://baithings.co.kr/",
        "category": "social"
    },
    {
        "name": "애프터레인",
        "corevalue": "앞으로의 숲을 책임질 묘목들을 스마트 농법으로, 가장 건강하게",
        "image_url": "/static/logo_w.png",
        "image_text": "데이터 기반 스마트 묘목 농법, Seedling Station",
        "text": "설명",
        "link": "https://baithings.co.kr/",
        "category": "enviro"
    },
    {
        "name": "퀀텀캣",
        "corevalue": "더 낮은 에너지와 적은 환경오염을 만드는 촉매 원천 기술",
        "image_url": "/static/logo_w.png",
        "image_text": "퀀텀캣 금 촉매",
        "text": "설명",
        "link": "https://baithings.co.kr/",
        "category": "enviro"
    },
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
    return render_template('social_venture.html', sv_urls = sv_urls)


# 팀 소개 페이지 라우트
@app.route('/team')
def team():
    # 여기에서 팀 소개 페이지에 필요한 데이터를 전달하는 작업을 추가합니다.
    return render_template('team.html')


if __name__ == '__main__':
    app.run(debug=True)

