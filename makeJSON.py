# -*- coding: utf-8 -*-
import json
import datetime
import codecs
from collections import OrderedDict

# JSON (Javascript object Notation)
# 여러 시스템 간 데이터 교환을 위해 고안한 데이터형
# XML : 데이터를 정의하는 태그 때뭉네 파일 용량이 커짐
# CSV : XML 보다 용량은 작지만, 데이터의 의미 파악이 힘듦

# 자바스크립트의 객체 표기법을 차용해서 만듦
# 객체는 키, 값의 형식으로 작성
# XML과 CSV의 장점을 따서 만든것이라 폭발적인 지지를 받음

# 주의! 파이선에는 이것과 유사한 자료구조인
# dictionary 가 이미 있음
# JSON과 dictionary 자료구조는 서로 구분해야 할 필요가
# 있기 때문에 dictionary 자료구조로 정의된 객체는
# dumps, loads 명령으로 JSON 객체로 변환해서 처리

# 성적 데이터를 JSON 데이터로 생성한 뒤
# 파일에 그것을 저장하는 예제

today = datetime.datetime.now()
sungjuk = {
    'hakbun' : 'a12345',
    'name' : '혜교',
    'kor' : 99, 'eng' : 98, 'mat' : 99,
    'regdate' : str(today)
}
print(sungjuk)

# dict 자료구조를 JSON 형식으로 인코딩 - json.dumps
jsonstring = json.dumps(sungjuk)
print(jsonstring)
print(type(jsonstring))

# json 형식을 보기좋게 출력하려면? - indent 사용
jsonstring = json.dumps(sungjuk, indent=4)
print(jsonstring)

# json 형식을 python에서 처리할 수 있도록 디코딩 - loads
# 디코딩된 결과는 dictionary 형식으로 다룰 수 있음
sjDict = json.loads(jsonstring)
print('%s: %s' % (u'학번',sjDict['hakbun']))
print('%s: %s' % (u'국어',sjDict['kor']))

# JSON 형식을 파일에 쓰기
with codecs.open('sungjuk2.json','w','utf-8') as make_json:
    # json으로 변환된 객체를 파일에 기록
    make_json.write(jsonstring)
with codecs.open('sungjuk2.json', 'w', 'utf-8') as make_json:
    # 파일에 기록할 때 json으로 변환
    json.dump(sungjuk, make_json)

# JSON 형식 파일 읽기
with codecs.open('sungjuk2.json', 'r', 'utf-8') as read_json:
    #'sungjuk2.json' 내용을 json으로 변환해서 readjson에 저장
    readjson = json.load(read_json)

print(readjson)

# 파일에서 읽은 내용을 dictionary 형식으로 처리
print(readjson['mat'])
print(readjson['name'])

# uid = 'abc123'
# pwd = 'xyz987'
# member = { 'uid' : str(uid), 'pwd': str(pwd) }

# 학생 데이터를 JSON으로 다루기
stdCode = '201350050'
name = u'김태희'
addr = u'경기도 고양시'
age = '25'
birthDate = '1985.3.22'
dept = u'컴퓨터공학'
professor = '504'
itvTime = u'목 2교시'
student = { 'stdCode' : stdCode,
            'name' : name,
            'addr' : addr,
            'age' : age,
            'birthDate' : birthDate,
            'dept' : dept,
            'professor' : professor,
            'itvTime' : itvTime,
            'regDate' : str(datetime.datetime.now() )}

print(student)

stdjson = json.dumps(student, indent=4)

print(stdjson)

stdDict = json.loads(stdjson)
print(stdDict['name'])
print(stdDict['addr'])

with codecs.open('student.json', 'w', 'utf-8') as make_json:
    json.dump(student, make_json)

deptname = u'컴퓨터공학'
depttel = '123-4567-8901'
deptoff = u'E동 2층'
deptchf = '504'
deptdate = u'2007년'

profid = '504'
profname = u'이성계'
profdept = u'철학'

student2 = {
    'stdCode' : stdCode,
    'name' : name,
    'addr' : addr,
    'age' : age,
    'birthDate' : birthDate,
    'dept' : {
        'deptname' : deptname,
        'depttel' : depttel,
        'deptoff' : deptoff,
        'deptchf' : {
            'profid' : profid,
            'profname' : profname,
            'profdept' : profdept
        },
        'deptdate' : deptdate
    },
    'professor' : {
        'profid' : profid,
        'profname' : profname,
        'profdept' : profdept
    },
    'itvTime' : itvTime,
    'regDate' : str(datetime.datetime.now() )
}

print(student2)
std2json = json.dumps(student2)
print(std2json)

std2Dict = json.loads(std2json)
print(std2Dict['name'])

for key in std2Dict['dept']:
    print(key)
    print(std2Dict['dept'][key])

# print(std2Dict['dept.deptname'])
# print(std2Dict['professor.profname'])

print(std2Dict['dept']['deptname'])
print(std2Dict['professor']['profname'])


# OrderedDict를 이용한 JSON 간단예제
idol_group = OrderedDict()
albums = OrderedDict()
album = OrderedDict()

idol_group["name"] = u'소녀시대'
idol_group["members"] = [u'태연', u'써니', u'효연', u'유리', u'윤아',
                         u'제시카', u'티파니', u'수영', u'서현']

album['년도'] = 2007
album['앨범명'] = u'소녀시대'
albums['1집'] = album

idol_group["albums"] = albums

idolJson = json.dumps(idol_group)
print(idolJson)


# 또 다른 방법으로 학생 JSON 데이터 생성하기
student = OrderedDict()
prof = OrderedDict()
dept = OrderedDict()

prof['profCode'] = '504'
prof['name'] = u'이성계'
prof['major'] = u'철학'

dept['deptname'] = u'컴퓨터공학'
dept['telNum'] = '123-4567-8901'
dept['offcLocation'] = u'E동 2층'
dept['dean'] = prof
dept['apptDate'] = u'2007년'

student['stdCode'] = '201350050'
student['name'] = u'김태희'
student['addr'] = u'경기도 고양시'
student['age'] = '25'
student['birthDate'] = '1985.3.22'
student['dept'] = dept
student['prof'] = prof
student['intvTime'] = u'목 2교시'

stdjson = json.dumps(student)
print(stdjson)

