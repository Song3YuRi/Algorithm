# solution.py 보다 더 나은 효율성을 보여줌. 
def solution(id_list, report, k):
    answer = []

    # 신고 횟수 중복 제거
    report = set(report)
    
    # 신고 한 ID 리스트
    people = {}
    # 메일을 받은 숫자
    mail_count = {}

    for i in id_list:
        people[i] = []
        mail_count[i] = 0

    for i in report:
        person = i.split(' ')[1]
        report_person = i.split(' ')[0]
        people[person].append(report_person)

    for i in people:
        if len(people[i]) >= k:
            for j in people[i]:
                mail_count[j] += 1
    
    for i in mail_count:
        answer.append(mail_count[i])

    return answer
