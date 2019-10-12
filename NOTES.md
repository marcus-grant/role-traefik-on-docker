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

### entryPoints

...
  [entryPoints.http]
    address = ":80"
      [entryPoints.http.redirect]
        entryPoint = "https"
  [entryPoints.https]
    address = ":443"
      [entryPoints.https.tls]
...

- `defaultEntryPoints` defines the behavior of the designed-for actions traefik takes to route all HTTP & HTTPS traffic it's meant to manage.
    - Recently, as of version 2.0, [traefik supports TCP][02] as well as HTTP & HTTPS
    - look for an article on using Traefik to route SSH through TCP in the future

- `entryPoints.http` defines the http protocol behavior when it's an `entryPoint`
  - this defines the overall behavior for any service using the HTTP protocol
  - in the next step it will be `redirect`ed as an HTTPS request so that every HTTP one becomes HTTP**S**
  - this enforces every connection to the services behind traefik to use secure HTTP**S**

- `entryPoints.https` defines how all HTTPS traffic is handled
    - previously, all HTTP traffic was told to be redirected to this HTTPS definition, securing it
    - `.tls` specifies that TLS/SSL encryption should be enforced to secure the traffic

### ACME

- `email` is required by ACME to communicate with Let's Encrypt to manage certificates, which need them to be valid. Every certificate needs some point of contact to be considered valid.

- `storage` just tells the service where to store ACME configurations.

- `entryPoint` is just the same `https` entry point used before (port `443`) that Let's Encrypt should use to encrypt all traffic that passes through.

- `onHostRule` determines whether traefik should generate certifactes as hosts start up, in the case of docker, when containers startup
    - **TODO** need to investigate whether this counts towards the rate limiting of Let's Encrypt

- `acmeHTTPChallenge` 

### Docker

```
[docker]
domain = "a-domain.com"
watch = true
network = "web"
```

- `docker` is the section where docker backend proxying configurations are specified, there's a ton, here are the basics:

- `domain` domains can be different for docker specifically, but in most cases probably the same, just make it the expected domain of the server*(s)*.

- `watch` tells traefik's docker provider to watch docker for new containers with labels to proxy.

- `network` specifies the docker network to watch specific docker networks to route to and to watch out for new containers on.
```

References
----------

1. [CodeMentor: Traefik - Alternative Reverse Proxy for Dockerized Apps][01]
2. [Containous on Medium: Back to Traefik 2.0][02]

[01]: https://www.codementor.io/slavko/traefik-as-an-alternative-reverse-proxy-to-nginx-for-self-hosted-dockerized-applications-bm5tpcsmj "CodeMentor: Traefik - Alternative Reverse Proxy for Dockerized Apps"
[02]: https://blog.containo.us/back-to-traefik-2-0-2f9aa17be305 "[Containous on Medium: Back to Traefik 2.0"
