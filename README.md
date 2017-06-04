<p><img src="https://cdn.haproxy.com/site/img/events/haproxy.png" alt="haproxy logo" title="haproxy" align="right" height="60" /></p>

Ansible Role: haproxy
=====================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/haproxy/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Fhaproxy/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18233.svg)](https://galaxy.ansible.com/SoInteractive/haproxy/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Set up HAProxy loadbalancer with stats interface and prometheus-enabled metrics.

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.haproxy
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO
----

- test if unix socket is open
