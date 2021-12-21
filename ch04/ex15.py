'''
    강수량 계산하기
'''


def get_rainfall():
    records = {}

    while True:
        city = input('도시 이름을 입력하세요: ')

        if not city:
            break

        rainfall = input('강수량 입력하세요: ')

        if not rainfall:
            break

        records[city] = records.get(city, 0) + int(rainfall)

    for city, rainfall in records.items():
        print(f'{city}: {rainfall}')


if __name__ == '__main__':
    get_rainfall()
