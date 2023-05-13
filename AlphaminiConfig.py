# Imports
import asyncio
import logging

import mini.mini_sdk as MiniSdk
from mini.dns.dns_browser import WiFiDevice

# attribuites
SerialNum = "100893"

async def setup(robotSerialNumber=SerialNum):
    # Alphamini Initiate
    MiniSdk.set_log_level(logging.INFO)
    MiniSdk.set_robot_type(MiniSdk.RobotType.EDU)
    device: WiFiDevice = await MiniSdk.get_device_by_name(robotSerialNumber, 10)
    return device