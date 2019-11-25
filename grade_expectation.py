#시험점수 분석
#class로 다시 작성해보기!
#딕셔너리 이용해서 학번만 입력하면 결과 나오도록!

import numpy

scores = [24,24,16,28,24,9.5,20,14,19,17,18,7,22,9.5,4,23,26,17,26,29,23,25]
hwork = [10,6,8,6,7,10,8,8,10,10,7,10,9,7,8,7,6,8,6,7,3,4]

print('중간고사 평균 : ', numpy.mean(scores))
print('중간고사 중앙값 : ', numpy.median(scores))
print('100점만점 환산 평균 및 중앙값 :', numpy.mean(scores)/30*100, numpy.median(scores)/30*100)

myscore = 19
myscore_hwork = 6
print('내 시험점수 :', myscore)

#sorting

for i in range(len(scores)):
    for j in range(i+1):
        if scores[i]>scores[j]:
            k = scores[j]
            scores[j] = scores[i]
            scores[i] = k
        else:
            pass

print()
print('~15%는 A+, ~30%는 A, ~45%는 B+, ~60%는 B입니다.')
print()

for i in range(len(scores)):
    if scores[i]==myscore:
        print('당신의 시험점수는 %d명 중 앞에서 %d번째 입니다.' %(len(scores), i))
        print('당신은 상위 %f 퍼센트 입니다.' %(i/len(scores)*100))
        break
    else:
        pass
    
#sorting    
for m in range(len(hwork)):
    for n in range(m+1):
        if hwork[m]>hwork[n]:
            o = hwork[n]
            hwork[n] = hwork[m]
            hwork[m] = o
        else:
            pass
print(hwork)

print()
l=[]
for m in range(len(hwork)):
    if hwork[m]==myscore_hwork:
        for n in range(m,len(hwork)):
            if hwork[m]==hwork[n]:
                l.append(m)
                break
            else:
                pass
    else:
        pass

print()

print('당신의 과제점수는 %d명 중 앞에서 %d번째 입니다.' %(len(hwork), l[0]+1))
print('동점자는 %d명입니다.' % len(l))
print('동점자들은 상위 %f~%f퍼센트 범위에 있습니다.' %((l[0]+1)/len(hwork)*100,(l[-1]+1)/len(hwork)*100))