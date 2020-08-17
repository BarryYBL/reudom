class time:
    @staticmethod
    def millisecond():
        """Get millisecond timestamp"""
        times = time.time()
        milliSecond = int(times * 1000)
        return milliSecond

    @staticmethod
    def seconds():
        """Get second time stamp"""
        times = time.time()
        Seconds = int(times * 10000)
        return Seconds