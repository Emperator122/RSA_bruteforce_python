import time

DEBUG_OUTPUT = True


class Log:  # weird class. I have to use python standard logger
    tracked_time = time.time()

    @classmethod
    def log(cls, message):
        if not DEBUG_OUTPUT:
            pass
        print(message)

    @classmethod
    def log_timed(cls, message=''):
        if not DEBUG_OUTPUT:
            pass
        if message != '':
            print(message)
        print("ELAPSED: --- %s seconds ---" % (time.time() - cls.tracked_time))

    @classmethod
    def track_time(cls, message=''):
        Log.tracked_time = time.time()
        if message != '':
            cls.log(message)
