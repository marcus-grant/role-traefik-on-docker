General Notes on Configuring Traefik with Ansible
=================================================

> These are just general and probably unorganized notes, please move these to the notes directories/repositories or incorporate into an edited document.

General Notes
-------------

- What makes traefik special is that it's a dynamic proxy, unlike the previously very popular Nginx and HAProxy, which is statically defined in its routing rules
- **Frontends** are the public side of a network, like an internet domain, *i.e. app.mydomain.com*
- **Backends** are the deployed services, which can be a docker container, or ansible orchastrated, etc.
    - Static rules can be easily defined for those, and it's easier for docker than most other options because traefik can scan docker's socket for labels for backend-frontend relationships
    - They can also be dynamically discovered by observing docker, kubernetes, ansible, openshift, vagrant, etc.


References
----------

1. [CodeMentor: Traefik - Alternative Reverse Proxy for Dockerized Apps][01]

[01]: https://www.codementor.io/slavko/traefik-as-an-alternative-reverse-proxy-to-nginx-for-self-hosted-dockerized-applications-bm5tpcsmj "CodeMentor: Traefik - Alternative Reverse Proxy for Dockerized Apps"
