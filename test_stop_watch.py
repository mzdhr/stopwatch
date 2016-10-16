import unittest
from stop_watch import StopWatch
import time


class TestStopWatch(unittest.TestCase):
    def setUp(self):
        self.files_set = set()
        self.files_list = []
        self.files_count = 500000
        self.n = 35
        self.fib_cache = {}

    def test_as_context_manager01(self):
        eye = StopWatch()
        with eye:
            time.sleep(1)
            time.sleep(1)

    def test_as_context_manager02(self):
        with StopWatch('Context Manager') as eye:
            time.sleep(1)
            time.sleep(1)

    def test_sleep(self):
        eye = StopWatch()
        eye.start()
        time.sleep(1)
        time.sleep(2)
        time.sleep(1)
        eye.end()

    def test_adding_files_to_list(self):
        eye = StopWatch()
        eye.start()
        for i in range(self.files_count):
            self.files_list.append(i)
        eye.end()

    def test_adding_files_to_set(self):
        eye = StopWatch()
        eye.start()
        for i in range(self.files_count):
            self.files_set.add(i)
        eye.end()

    def test_bad_rabbit(self, n=0):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n > 2:
            return self.test_bad_rabbit(n-1) + self.test_bad_rabbit(n-2)

    def test_fib_for_bad_rabbit(self):
        eye = StopWatch('Bad Rabbit')
        eye.start()
        for n in range(self.n):
            temp = n, ':', self.test_bad_rabbit(n)
        eye.end()

    def test_good_rabbit(self, n=0):
        value = 0
        if n in self.fib_cache:
            return self.fib_cache[n]

        if n == 1:
            value = 1
        elif n == 2:
            value = 1
        elif n > 2:
            value = self.test_good_rabbit(n-1) + self.test_good_rabbit(n-2)

        self.fib_cache[n] = value
        return value

    def test_fib_for_good_rabbit(self):
        eye = StopWatch('Good Rabbit')
        eye.start()
        for n in range(self.n):
            temp = n, ':', self.test_good_rabbit(n)
        eye.end()



