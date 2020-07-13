def minerando(base, altura):
    return base ** 2 * altura


b, a = map(int, input().split())
print(minerando(b, a))