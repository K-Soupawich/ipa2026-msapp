from netmiko import ConnectHandler
import ntc_templates
import os


def get_interfaces(ip, username, password):
    os.environ["NET_TEXTFSM"] = os.path.join(
        os.path.dirname(ntc_templates.__file__), "templates"
    )

    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
        "ssh_config_file": "/root/.ssh/config",
    }

    with ConnectHandler(**device) as conn:
        result = conn.send_command("show ip int br", use_textfsm=True)
        conn.disconnect()

    return result
