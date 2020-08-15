#sep (중간에 넣을 문자) end(뒷 문장이 바로 나오게 함. 문장의 끝 문자)
print("Python", "Java", sep=" ")
#print("Python", "Java", file=sys.stdout) #표준 출력
#print("Python", "Java", file=sys.stderr) #에러처리

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1,21):
    print("대기번호 :" + str(num).zfill(3))#값이 없는 숫자에 0 채우기

#answer = input("아무 값이나 : ")
#print("입력하신 값은 " + answer + "입니다")

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) #>: 오른쪽 정렬/ 10: 총 공간, 10 앞에 플마 붙이면 표시됨
print("{0:_<10}".format(500)) #왼쪽정렬 + 빈칸은 _
print("{0:,}".format(100000)) 
print("{0:f}".format(5/3)) #1.66667
print("{0:.2f}".format(5/3)) #소수점 둘째 자리까지 반올림

score_file= open("score.txt", "w", encoding="utf8") #w는 쓰기용도 (덮어쓰기), a는 append
print("수학 : 0", file =score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file= open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file= open("score.txt", "r", encoding="utf8") #r=read
print(score_file.read()) #모두 읽어오기
score_file.close()

score_file= open("score.txt", "r", encoding="utf8") #r=read
print(score_file.readline()) # 줄 별로 읽고 커서는 다음 줄로 이동, 붙이려면 end= " "사용
score_file.close()

score_file= open("score.txt", "r", encoding="utf8")
while True: #파일이 총 몇 줄인지 모를 때 불러오는 방법
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines=score_file.readlines()
for line in lines:
    print(line, end="")
#pickle 프로그램에서 사용하는 데이터를 파일 형태로 저장
import pickle 
#profile_file = open("profile.pickle", "wb") #binary
#profile = {"이름": "박명수", "나이" : 30, "취미":["축구", "골프", "코딩"]}
#print(profile)
#pickle.dump(profile, profile_file)
#profile_file.close()
#dump=save,-->load

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding= "utf8") as report_file:
        report_file.write("- {0} 주차 중간보고 -".format(i)) 
        report_file.write("\n부서 : ") 
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")



