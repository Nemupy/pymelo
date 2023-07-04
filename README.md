# pymelo
Wrapper for [DiscordPomeloAPI](https://github.com/Lixqa/DiscordPomelo)

# Install
Python 3 or higher is required.    
```cmd
# Linux/OS X
$ python -m pip install -U pymelo

# Windows
> py -3 -m pip install -U pymelo
```    

# Example
Check if the username 'nemupy' is available.    
```py
import pymelo


check = pymelo.Check("nemupy")

if check.status == 2:
    print(f"The username '{check.username}' is available.")
elif check.status == 3:
    print(f"The username '{check.username}' is not available.")
else:
    print(f"An error occurred while checking the username '{check.username}' availability.")

# The username 'nemupy' is not available.
```

# Method
- `username` Your checked username.
- `status` See [DiscordPomeloAPI](https://github.com/Lixqa/DiscordPomelo/blob/main/README.md#Status).
- `attempt` How many attempts it took until a valid response was returned by discord.
