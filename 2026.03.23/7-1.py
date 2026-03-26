# 7-1.py
#scores=[55,35,40,70,65,30]

scores=[]

for i in range(6):
    print(i+1,'번째의 성적을 입력하세요', end=' ')
    scores.append(int(input()))
   

total=0
undersubject=0

for score in scores:
    if score < 40 :
        undersubject+=1
    
    total+=score

print('40점 이만의 과목수:',undersubject)
average=total/len(scores)
#print('평균점수:',format(average,'1.2f'))
print(f'평균점수 : {average:.2f}')

if undersubject>0 or average<60:
    print('불합격')
else:
    print('합격')
