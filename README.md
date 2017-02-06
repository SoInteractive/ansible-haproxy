HAProxy ansible role.
=====================

This role sets up HAProxy load balancer. It supports creating stats interface and adds VIP address to /etc/hosts (probably should be moved to keepalived role). Servives are defined in user-friendly YAML list format (example in defaults/main.yml).
