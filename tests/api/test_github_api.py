import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')

    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('zhukazhuk')

    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')

    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('abs_crazy_thing')

    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char(github_api):
    r = github_api.search_repo('s')

    assert r['total_count'] != 0

@pytest.mark.api
def test_emojis_response(github_api):
    r = github_api.get_emojis()
    print(r['+1'])
    assert r['zombie_woman'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f9df-2640.png'

