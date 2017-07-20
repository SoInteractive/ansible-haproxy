from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/etc/haproxy",
        "/etc/haproxy/conf.d",
        "/var/lib/haproxy",
        "/run/haproxy",
        "/opt/haproxy_exporter"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/haproxy/haproxy.cfg",
        "/etc/haproxy/conf.d/00-haproxy",
        "etc/systemd/system/haproxy_exporter.service"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service):
    present = [
        "haproxy"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_enabled
            assert s.is_running


def test_packages(Package, SystemInfo):
    present = []
    if SystemInfo.distribution == 'ubuntu':
        present = [
            "haproxy",
            "vim-haproxy",
            "psmisc"
        ]
    elif SystemInfo.distribution == 'centos':
        present = [
            "haproxy",
            "libselinux-python",
            "libsemanage-python"
        ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed


def test_socket(Socket):
    present = [
        # "unix:///run/haproxy/admin.sock",
        "tcp://127.0.0.1:1936",
        "tcp://127.0.0.1:8080",
        "tcp://127.0.0.1:5672"
    ]
    for socket in present:
        s = Socket(socket)
        assert s.is_listening


def test_sysctl_vars(Sysctl):
    assert Sysctl("net.ipv4.ip_nonlocal_bind")
