<p><img src="https://cdn.haproxy.com/site/img/events/haproxy.png" alt="haproxy logo" title="haproxy" align="right" height="60" /></p>

Ansible Role: haproxy
=====================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-haproxy.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-haproxy) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.haproxy-blue.svg)](https://galaxy.ansible.com/SoInteractive/haproxy/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-haproxy.svg)](https://github.com/SoInteractive/ansible-haproxy/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Set up HAProxy loadbalancer with stats interface and prometheus-enabled metrics.

# :warning: IMPORTANT NOTICE

THIS PROJECT IS ABANDONED. WE DO NOT ACCEPT ANY NEW ISSUES AND/OR PULL REQUESTS.

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
