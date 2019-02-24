account = {
          'naver' : {
            'id': 'naver id',
            'pw' : 'naver pw'
          },
           'facebook' : {
           'id' : 'facebook id',
           'pw' : 'facebook pw'
           },
          'kakao' : {
          'id' : 'kakao id',
          'pw' : 'kakao pw'
          }
        }
       

wihle(1):
      print('naver,facebook,kakao?',end='')
     result = input()
     if result in ['naver','facebook','kakao']:
            print ('{} 아이디 : {}, 비밀번호 : {}'. format(result,account[result]['id'],account[result]['pw']))
