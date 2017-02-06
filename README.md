HAProxy ansible role.
=====================

This role sets up HAProxy load balancer. It supports creating stats interface.
Services are defined in user-friendly YAML list format (example in defaults/main.yml). 
Every service creates one file in /etc/haproxy/conf.d on remote host, later from
those files main haproxy.cfg is created.
