import pytest


@pytest.fixture
def database_cred(request, tmpdir):
    def clean_up_login():
        print(tmpdir)
        pass
        # Call method to clean up from
        # file
    request.addfinalizer(clean_up_login)
    return 'login_info'


def test_insert(database_cred):
    pytest.skip('WIP')
    assert "abc" == "bcd"


def test_select(database_cred):
    assert 'abc' == 'abc'
