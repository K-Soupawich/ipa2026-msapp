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
        "session_log": "netmiko_session.log",
        "disabled_algorithms": {"pubkeys": []},
    }

    with ConnectHandler(**device) as conn:
        result = conn.send_command("show ip int br", use_textfsm=True)
        conn.disconnect()

    return result
