import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("packages", [
    ('bsd-mailx'),
    ('sendmail'),
])
def test_mailx_is_installed(host, packages):
    p = host.package(packages)
    assert p.is_installed


def test_config_mailx(host):
    file = host.file('/root/.mailrc')
    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert oct(file.mode) == '0600'
    assert file.contains('set smtp-use-starttls')
    assert file.contains('set smtp-auth-user=secretuser')


def test_mail_link(host):
    file = host.file('/usr/bin/mail')
    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.is_symlink
    assert file.linked_to == '/usr/bin/s-nail'
    # ls -l /usr/bin/mail
    # lrwxrwxrwx 1 root root /usr/bin/mail -> /usr/bin/heirloom-mailx
    # But the module says it's linked to /usrs/bin/s-nail \(O_o)/
    # Nevertheless, s-nail has the same md5 as heirloom-mailx
