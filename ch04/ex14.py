'''
    식당 주문 프로그램 만들기
'''


MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}


def takeAnOrder():

    print(MENU)
    total_price = 0

    while order := input('무엇을 주문하시겠어요? ').strip():
        if not order in MENU:
            print(f'Sorry, we are fresh out of {order} today')
            continue
        total_price += MENU[order]
        print(f'{order} costs {MENU[order]}, total is {total_price}')

    print(f'Your total is {total_price}')


if __name__ == '__main__':
    takeAnOrder()
