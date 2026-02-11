from collections.abc import Callable
from contextlib import nullcontext as does_not_raise_exception

import pytest

from .soft_error.decimals_1_test import (
    test_timer_decimals_above_accepted_value,
    test_timer_decimals_below_accepted_value,
)
from .soft_error.invalid_thread_type_start_test import (
    test_timer_start_invalid_thread_type_soft_error_with_context_manager,
    test_timer_start_invalid_thread_type_soft_error_without_context_manager,
)
from .soft_error.invalid_thread_type_stop_test import (
    test_timer_stop_invalid_thread_type_soft_error_with_context_manager,
    test_timer_stop_invalid_thread_type_soft_error_without_context_manager,
)
from .soft_error.start_test import (
    test_timer_start_default_thread_twice_soft_error_without_context_manager,
    test_timer_start_thread_name_collision_soft_error_with_context_manager,
    test_timer_start_thread_name_collision_soft_error_without_context_manager,
)
from .soft_error.stop_test import (
    test_timer_stop_default_thread_while_custom_thread_is_running_soft_error,
    test_timer_stop_not_started_thread_soft_error_without_start,
    test_timer_stop_not_started_thread_soft_error_without_start_and_with_custom_thread,
    test_timer_stop_unknown_thread_soft_error_with_default_and_custom_thread,
    test_timer_stop_unknown_thread_soft_error_with_multiple_custom_threads,
)


@pytest.mark.parametrize(
    "test_function",
    [
        test_timer_decimals_below_accepted_value,
        test_timer_decimals_above_accepted_value,
        test_timer_start_invalid_thread_type_soft_error_without_context_manager,
        test_timer_start_invalid_thread_type_soft_error_with_context_manager,
        test_timer_stop_invalid_thread_type_soft_error_without_context_manager,
        test_timer_stop_invalid_thread_type_soft_error_with_context_manager,
        test_timer_start_default_thread_twice_soft_error_without_context_manager,
        test_timer_start_thread_name_collision_soft_error_with_context_manager,
        test_timer_start_thread_name_collision_soft_error_without_context_manager,
        test_timer_stop_default_thread_while_custom_thread_is_running_soft_error,
        test_timer_stop_not_started_thread_soft_error_without_start,
        test_timer_stop_not_started_thread_soft_error_without_start_and_with_custom_thread,
        test_timer_stop_unknown_thread_soft_error_with_default_and_custom_thread,
        test_timer_stop_unknown_thread_soft_error_with_multiple_custom_threads,
    ],
)
def test_timer_does_not_raise_exceptions(test_function: Callable[..., None], capfd: object) -> None:
    with does_not_raise_exception():
        test_function(capfd)
