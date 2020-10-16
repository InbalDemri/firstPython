import random2


def gen_random_num(num):
    rand = random2.random()
    if rand < 0.5:
        print("even")
    else:
        print("odd")


if __name__ == '__main__':
    gen_random_num(10)
