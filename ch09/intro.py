# 객체 지향 프로그래밍은 코드의 기능(함수)과 그 함수가 활용하는 데이터를 한꺼번에 정의해 활용한다.


# * 절차형 프로그래밍으로 평균 구하기
def average(numbers):
    return sum(numbers) / len(numbers)


scores = [85, 95, 989, 87, 80, 92]
print(f'The final score is {average(scores)}')


# * 객체지향형 프로그래밍으로 평균 구하기

class ScoreList():
    def __init__(self, scores) -> None:
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)


scores = ScoreList([85, 95, 989, 87, 80, 92])
print(f'The final score is {scores.average()}')
