""" Tests the role using the default ubuntu scenario
"""
import os
import requests

import testinfra.utils.ansible_runner

# pylint: disable=invalid-name
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# These test that the testing environment was created properly ################
def test_hosts_file(host):
    """ Standard molecule env test """
    h_file = host.file('/etc/hosts')

    assert h_file.exists
    assert h_file.user == 'root'
    assert h_file.group == 'root'


def test_docker_host_running(host):
    """ Just check systemd for running dockerd """
    dockerd = host.service('docker')
    assert dockerd.is_running


def test_helloworld_container_running(host):
    """ Ensure helloworld container running & and responds to http request """
    hello_container = host.docker('hello-world')
    assert hello_container.is_running
    req_url = 'http://192.168.99.13:12345'
    resp = requests.get(req_url)
    assert resp.ok
    assert b'<title>HTTP Hello World</title>' in resp.content


# Here testing the actual traefik install begins ##############################
def test_traefik_data_directory(host):
    """ Ensure default traefik data/config directory in place """
    traefik_dir = host.file('/var/www/traefik')
    assert traefik_dir.exists
    assert traefik_dir.is_directory


def test_config_files(host):
    """ Tests the existence and some of the contents of the two config files:
        - /var/www/traefik/traefik.toml
        - /var/www/traefik/acme.json """
    acme_config = host.file('/var/www/traefik/acme.json')
    assert acme_config.exists
    assert acme_config.is_file
    assert acme_config.mode == 0o600
    traefik_config = host.file('/var/www/traefik/traefik.toml')
    assert traefik_config.exists
    assert traefik_config.is_file
    assert traefik_config.mode == 0o600


def test_docker_traefik_network(host):
    """ Tests that the right docker network exists """
    cmd = host.run('docker network inspect web')
    assert cmd.rc == 0



#  def test_traefik_container_running(host):
#      """ Tests whether the traefik container is actually running """
#      traefik_container = host.docker('traefik')
#      assert traefik_container.is_running
