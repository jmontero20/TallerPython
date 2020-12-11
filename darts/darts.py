def score(x, y):
    radio = ((x**2)+(y**2))**(1/2)
    if radio <= 1:
        return 10
    if radio <= 5:
        return 5
    if radio <= 10:
        return 1
    return 0
