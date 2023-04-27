import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("python", 2) == 'noht_yp'
    assert encrypt_message("computacional", 3) == 'moc_lanoicatup'
    assert encrypt_message("algorítmo", 22) == 'omtírogla'

    invalid_message_error = 'tipo inválido para message'
    invalid_key_error = 'tipo inválido para key'

    with pytest.raises(TypeError, match=invalid_message_error):
        encrypt_message(3, 2)

    with pytest.raises(TypeError, match=invalid_key_error):
        encrypt_message('abracaba', 'dois')
