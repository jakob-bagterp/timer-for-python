from timer import Timer


def test_only_one_instance_of_timer() -> None:
    timer_1 = Timer()
    timer_2 = Timer()
    assert timer_2 is timer_1


def test_only_one_instance_of_timer_with_decimals_1() -> None:
    timer_1 = Timer(decimals=5)
    timer_2 = Timer(decimals=5)
    assert timer_2 is timer_1


def test_only_one_instance_of_timer_with_decimals_2() -> None:
    timer_1 = Timer(decimals=3)
    timer_2 = Timer(decimals=5)
    assert timer_2 is timer_1


def test_only_one_instance_of_timer_with_decimals_3() -> None:
    timer_1 = Timer()
    timer_2 = Timer(decimals=5)
    assert timer_2 is timer_1
