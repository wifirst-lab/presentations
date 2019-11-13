import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nginx(host):
    nginx = host.package("nginx")
    assert nginx.is_installed


def test_content(host):
    content = host.ansible(
      "uri",
      "url=http://localhost/ return_content=yes",
      check=False)["content"]
    assert "Sysadmin Days" in content


def test_false_content(host):
    content = host.ansible(
      "uri",
      "url=http://localhost/ return_content=yes",
      check=False)["content"]
    assert "NodeConf" in content
