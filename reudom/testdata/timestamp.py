import time


class TimeStamp:
    @staticmethod
    def millisecond():
        """Get millisecond timestamp"""
        times = time.time()
        MilliSecond = int(times * 1000)
        return MilliSecond

    @staticmethod
    def seconds():
        """Get second time stamp"""
        times = time.time()
        Seconds = int(times * 1)
        return Seconds


if __name__ == '__main__':
    print(TimeStamp.seconds())
    print(TimeStamp.millisecond())
