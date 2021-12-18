import random

'''
  사전 순서로 정렬된 단어 리스트를 만들고 보여준 후 그 중에서 단어 맞추기
'''


def find_voca():
    words = ['chimchakman', 'ddahyoni', 'faker', 'gumayushi',
             'hanryang', 'sonyshow', 'sopoong', 'woojeong']

    print('[단어 목록]')

    for idx, word in enumerate(words):
        print(idx+1, word)

    # 정답 설정
    answer = random.randint(0, len(words) - 1)
    print('정답: ', answer)

    # 최대 3번 기회
    count = 3

    while count > 0:
        word = input(f'단어를 입력하세요...... [기회: {count}번]: ')

        # * 배열에서 해당 단어의 인덱스를 찾기
        try:
            index = words.index(word)
        except:
            print('해당 단어는 없습니다.')
            continue

        if index == answer:
            print('정답 !!!!')
            return
        elif index > answer:
            print('답보다 뒤쪽 단어입니다.')
        else:
            print('답보다 앞쪽 단어입니다.')

        count -= 1

    print('실 패!!!!')


if __name__ == '__main__':
    find_voca()
