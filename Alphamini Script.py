import asyncio
import logging
import AlphaminiConfig
import mini.mini_sdk as MiniSdk
from mini.dns.dns_browser import WiFiDevice

async def get_device_by_name():
    """根据机器人序列号后缀搜索设备

    搜索指定序列号(在机器人屁股后面)的机器人, 可以只输入序列号尾部字符即可,长度任意, 建议5个字符以上可以准确匹配, 10秒超时


    Returns:
        WiFiDevice: 包含机器人名称,ip,port等信息

    """
    result: WiFiDevice = await MiniSdk.get_device_by_name(AlphaminiConfig.SerialNum, 10)
    print(f"test_get_device_by_name result:{result}")
    return result

async def shutdown():
    """断开连接并释放资源

    断开当前连接的设备，并释放资源

    """
    await MiniSdk.quit_program()
    await MiniSdk.release()

async def test_start_run_program():
    """进入编程模式demo

    使机器人进入编程模式，等待回复结果，并延时6秒，让机器人播完"进入编程模式"

    Returns:
        None:

    """
    await MiniSdk.enter_program()

async def main():
    await AlphaminiConfig.setup()
    await get_device_by_name()
    await shutdown()

if __name__ == "__main__": asyncio.run(main())