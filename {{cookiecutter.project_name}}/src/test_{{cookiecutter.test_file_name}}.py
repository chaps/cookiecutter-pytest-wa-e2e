from .validators import  validate_test_1, validate_test_2
from pytest_wa_e2e_plugin.utils import wait_for_n_messages, send_expect_n_and_validate


@send_expect_n_and_validate(
    "RESTART KEYWORD", 2, validate_test_1
)
def exec_restart(test_run_instance):
    pass

@send_expect_n_and_validate(
    "INPUT TEXT", 
    2, 
    validate_test_2
)
def exec_misc(test_run_instance):
    pass


def test_restart_and_misc(test_run_instance):
    exec_restart(test_run_instance)
    exec_misc(test_run_instance)

