import psutil
import time
from threading import Thread


# Index : number of bytes sent
__BYTES_SENT__ = 0
# Index : number of bytes received
__BYTES_RECV__ = 1

class Tracker:

    def __init__(self):
        self.__reset_bytes_recv_vars__()
        self.__reset_bytes_sent_vars__()
        self.init_total_sent = self.__get_bytes_sent_total__()
        self.init_total_recv = self.__get_bytes_recv_total__()

    def get_total_data_used(self):
        """ Returns the data used since the start...
        """
        return ((self.__get_bytes_sent_total__() - self.init_total_sent) +
                (self.__get_bytes_recv_total__() - self.init_total_recv))

    def get_current_upload_speed(self):
        """ Returns the current upload speed in bytes per seconds.
        """
        dtime = time.time() - self.last_bytes_sent_time
        dsent = self.__get_bytes_sent_total__() - self.last_bytes_sent_total
        self.__reset_bytes_sent_vars__()
        return dsent / dtime if dtime != 0 else 0
