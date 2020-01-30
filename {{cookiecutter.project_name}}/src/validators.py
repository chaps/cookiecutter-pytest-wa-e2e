
from pytest_wa_e2e_plugin.utils import wait_for_n_messages, send_expect_n_and_validate



def validate_test_1(post_wait_messages, test_run_instance):
    assert "TEST" == post_wait_messages[-2][-2].decode()
    assert "MESSAGE" == post_wait_messages[-1][-2].decode()
    

def validate_test_2(post_wait_messages, test_run_instance):
    assert "NEW" == post_wait_messages[-2][-2].decode()
    assert "MESSAGE" == post_wait_messages[-1][-2].decode()


