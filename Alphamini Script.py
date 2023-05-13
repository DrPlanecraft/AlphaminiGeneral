import asyncio
import logging
import AlphaminiConfig
import mini.mini_sdk as MiniSdk
from mini.apis.api_expression import PlayExpression # express_name (.execute())
from mini.apis.api_action import PlayAction # action_name (.execute())
from mini.apis.api_sound import StartPlayTTS # text (.execute())

# Base Code for Programming Mode
async def exit_programmingMode():
    await MiniSdk.quit_program()
    await MiniSdk.release()

async def enter_programmingMode():
    await MiniSdk.enter_program()

# Programmed Action Parts go here
TTS_say = StartPlayTTS(text="Hello There!")
Action_Yoga = PlayAction(action_name="024")
Expression_Sneeze = PlayExpression(express_name="codemao9")

###########################################################################################################################################

async def main():
    # Setup for Programming Mode.
    await MiniSdk.connect(AlphaminiConfig.setup())
    await enter_programmingMode()

    # Perform Programmed Actions
    await TTS_say.execute()
    await Expression_Sneeze.execute()
    await Action_Yoga.execute()

    # Exitting Programming Mode
    await exit_programmingMode()

###########################################################################################################################################

if __name__ == "__main__": 
    asyncio.run(main())