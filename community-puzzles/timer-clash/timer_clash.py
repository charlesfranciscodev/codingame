class Time:
    SEPARATOR = ':'

    def __init__(self, timestamp):
        self.nb_opponents = 0  # number of players in the room
        self.set_time(timestamp)

    def set_time(self, timestamp):
        time = timestamp.split(self.SEPARATOR)
        self.total_time = int(time[0]) * 60 + int(time[1])  # in seconds

    def update_time(self, timer):
        self.nb_opponents += 1
        self.total_time = timer.total_time - int(256 / 2 ** (self.nb_opponents - 1))
        if self.total_time < 0:
            self.total_time = 0

    def __repr__(self):
        minutes = self.total_time // 60
        seconds = str(self.total_time % 60)
        return f"{minutes}{self.SEPARATOR}{seconds.zfill(2)}"


def play_clash():
    nb_opponents = int(input())
    if nb_opponents == 0:
        print("NO GAME")
    else:
        timer = Time("5:00")
        start_time = Time("0:00")
        for _ in range(nb_opponents):
            timestamp = input()
            timer.set_time(timestamp)
            if timer.total_time < start_time.total_time:
                print(start_time)
                return
            if start_time.nb_opponents == 6:
                print(timestamp)
                return
            start_time.update_time(timer)
        print(start_time)
        return


if __name__ == "__main__":
    play_clash()
