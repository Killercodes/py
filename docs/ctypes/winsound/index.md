# winsound
The winsound module provides access to the basic sound-playing machinery provided by Windows platforms. It includes functions and several constants.

```py
import winsound

"""
The winsound module provides access to the basic sound-playing machinery provided by Windows platforms.
It includes functions and several constants.
"""

# Play Windows exit sound.
# 'SystemAsterisk','SystemExclamation','SystemExit','SystemHand','SystemQuestion'
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
winsound.PlaySound("*", winsound.SND_ALIAS)

# ply beep 5000Hz for 1 second
## winsound.Beep(frequency, duration)
winsound.Beep(5000, 1000)

# Play Messge beep
winsound.MessageBeep(type=winsound.MB_OK)
#or
winsound.MessageBeep(type=-1)

```
