Role Name
=========

Ansible role to install traefik onto any host with a Docker host installed, as a container.

Requirements
------------

The only real dependency is that docker is installed and configured on the host system and that the user being managed by Ansible is either root or a user in the `docker` group.

Role Variables
--------------

### TODO
A description of the settable variables for this role should go here, including
any variables that are in defaults/main.yml, vars/main.yml, and any variables
that can/should be set via parameters to the role. Any variables that are read
from other roles and/or the global scope (ie. hostvars, group vars, etc.) should
be mentioned here as well.

Dependencies
------------

### TODO

The go-to role for installing docker tends to be [geerlingguy's docker role](https://github.com/geerlingguy/ansible-role-docker) so that is one tentative dependency, but arch-based users will be left out in the cold if that were a dependency, so when this role is more mature, and I have my own or someone else's good docker role for arch users I'll add some role dependencies.

Example Playbook
----------------

### TODO

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: traefik-on-docker, x: 42 }

License
-------

CC-BY

Author Information
------------------

Reach out to me on the github repository's [issues section](https://github.com/marcus-grant/role-traefik-on-docker/issues) to point out problems or suggestions:

