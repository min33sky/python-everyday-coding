
def run_timing():
    count = 0
    sum = 0

    while True:
        runtime = input('Enter 10 km run time: ')

        if not runtime:
            break

        sum += float(runtime)
        count += 1

    # 소수점 둘째 자리
    print(F'Average of {sum / count:.2f}, over {count} runs')


if __name__ == '__main__':
    run_timing()
