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

while(1):
    print('naver, facebook?', end = '')
    result = input()
    if result in ['naver', 'facebook']:
        print('{} 아이디: {}, 비밀번호 : {}'.format(result, account[result]['id'], account[result]['pw']))