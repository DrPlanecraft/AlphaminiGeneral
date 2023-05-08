# Imports
import asyncio
import logging

import mini.mini_sdk as MiniSdk
from mini.dns.dns_browser import WiFiDevice

# Alphamini Initiate
MiniSdk.set_log_level(logging.INFO)
MiniSdk.set_robot_type(MiniSdk.RobotType.EDU)

# attribuites
SerialNum = "100893"