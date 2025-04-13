def get_integer(prompt):
    n = int(input(prompt))
    return n

def exchange(amount):
    coin500 = amount // 500
    amount = amount % 500

    coin100 = amount // 100
    amount = amount % 100

    coin50 = amount // 50
    amount = amount % 50

    coin10 = amount // 10
    amount = amount % 10

    print("500원 동전의 개수: {}".format(coin500))
    print("100원 동전의 개수: {}".format(coin100))
    print("50원 동전의 개수: {}".format(coin50))
    print("10원 동전의 개수: {}".format(coin10))

# 실행 부분
amount = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(amount)
