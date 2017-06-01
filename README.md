HAProxy ansible role.
=====================

This role sets up HAProxy load balancer. It supports creating stats interface.
Services are defined in user-friendly YAML list format (example in defaults/main.yml). 
Every service creates one file in /etc/haproxy/conf.d on remote host, later from
those files main haproxy.cfg is created.

Role Variables
--------------

Below are the roles variables with the respective default values. 
```yml
haproxy_metrics: true

haproxy_exporter_version: 0.7.1
haproxy_exporter_download_url: "https://github.com/prometheus/haproxy_exporter/releases/download/v{{ haproxy_exporter_version }}/haproxy_exporter-{{ haproxy_exporter_version }}.linux-amd64.tar.gz"
haproxy_scrape_uri: {{ haproxy_stats_socket }}
#haproxy_scrape_uri: "http://{{ haproxy_stats_user }}:{{ haproxy_stats_pass }}@{{ haproxy_stats_address }}:{{ haproxy_stats_port }}{{ haproxy_stats_uri }};csv"

haproxy_exporter_config_flags:
  'haproxy.scrape-uri': '{{ haproxy_scrape_uri }}'
```

Example Playbook
----------------

    - hosts: proxy
      roles:
         - haproxy

