TO-DO's
=======

In-Progress
-----------

- [ ] Verify traefik container is running
- [ ] Install the container with defaults
- [ ] Let the playbook/role calling this role determine `become` status
- [ ] Try to get this to work with docker-in-docker instead
- [ ] Handle traefik dashboard auth properties
- [ ] Handle ACME encryption

Planning
--------

- [ ] Re-order defaults
- [ ] Document vars
- [ ] Migrate to v2 of traefik and handle the removal of `[api]` fields in v2
    - [this](https://docs.traefik.io/operations/api/) might point to the right way to configure dashboard in v2
- [ ] Deal with `docker_container` network params deprecation warning
- [ ] Tweak defaults to be compatible with your playbook
- [ ] Tweak defaults to be more generally usable
- [ ] Handle endpoint definitions

Future
------

- [ ] Consider testing the templated config files for the crucial config definitions
- [ ] Consider adding a more generic list of dictionaries to handle endpoint specs
- [ ] Add arch testing and dependencies with documentation
- [ ] Add variable for enabling logs and verify it works in testing
- [ ] Variable admin username
- [ ] List of admin user definitions and their encrypted passwords

Complete
--------

- [x] Network for traefik routing, default to `web`
- [x] Basic traefik config
- [x] Basic ACME config
  - (gets populated by traefik only test later if problems found in prod)
- [x] Verify the `traefik_data_directory` is created
- [x] Verify docker is installed
- [x] Verify hello-world test container is working
