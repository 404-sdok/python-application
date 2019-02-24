account = {
    'naver' : {
        'id' : 'kpjhg0124',
        'pw' : 'hello'
    },
    'facebook' : {
        'id' : 'me@ho9.me',
        'pw' : 'facebook_password'
    }
}

while(1): # 계속 반복
    print('naver, facebook?', end = '') # 질문
    result = input() # result 변수에 질문 답변 저장
    if result in ['naver', 'facebook']: # 만약 질문 답변이 naver이거나 facebook이라면
        print('{} 아이디: {}, 비밀번호 : {}'.format(result, account[result]['id'], account[result]['pw']))