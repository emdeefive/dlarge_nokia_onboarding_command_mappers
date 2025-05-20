"""nornir dispatcher for Nokia SROS."""

from nornir_nautobot.plugins.tasks.dispatcher.default import NapalmDefault, NetmikoDefault


class NapalmNokiaSros(NapalmDefault):
    """Collection of Napalm Nornir Tasks specific to NokiaSROS devices."""


class NetmikoNokiaSros(NetmikoDefault):
    """Collection of Netmiko Nornir Tasks specific to NokiaSROS devices."""

    config_command = "admin display-config"
