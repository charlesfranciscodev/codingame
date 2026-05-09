if __name__ == "__main__":
    max_value = 0
    max_loss = 0

    n = int(input())
    for v in input().split():
        value = int(v)
        if value > max_value:
            max_value = value
        elif value < max_value:
            loss = max_value - value
            if loss > max_loss:
                max_loss = loss

    print(-max_loss)
