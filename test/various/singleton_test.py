from timer import Timer

class TestSingleton():
    def test_only_one_instance(self):
        timer_1 = Timer()
        timer_2 = Timer()
        assert timer_2 is timer_1
