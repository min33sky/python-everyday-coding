'''
    이전 호출로부터 지난 시간 계산하기
'''

import time


def elapsed_since(data):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        # 첫번째 요소는 이전 요소가 없으므로 0이 출력되도록 처리
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield (delta, item)


if __name__ == '__main__':
    for t in elapsed_since('abce'):
        print(t)
        time.sleep(2)
