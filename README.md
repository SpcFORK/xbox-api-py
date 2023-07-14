# xbox-api-py

A simple Xbox API wrapper for Python that allows you to interact with various Xbox API endpoints. If you want to request any additional endpoints, please submit a feature request on the original [GitHub](https://github.com/RomanMender/xbox-api), or at my [Py Recode](https://github.com/SpcFORK/xbox-api-py).

## Installation
```shell
$ pip install xbox-api-py
```

## Example

```python
import xbox_api

authorization = {
    "userHash": "11039641451625114727",
    "XSTSToken": "eyJlbmMiOiJBMTI4Q0JDK0hTMjU2IiwiYWxnIjoiUlNBLU9BRVAiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJ4NXQiOiIxZlVBejExYmtpWklFaE5KSVZnSDFTdTVzX2cifQ.EVUwstAv_Vr4S6JQS3eEKQTrdqivPYCAWUtLuWTsBajNCmaKNtAIMUdMhypmpALCuwZg9JmIH9Bj7JU83zSxaS6urk6N93iOccfTsHXIcyplfewyk6CtHxCxX6jghEoA5LZLnci_xe8kKM6te1EYA8rBiCPdI-sFTqBaolyDbQA.o5mvE37qC24UvSDEzkzTMA.Z9WCgzwTGlgUdPE7DvDG5aC3vB5-zylnfHGVdKShP_668leL3GIWYCUROlVLraETJwZhYzWWF8kZvPsbV8bHHfdrlMeXa4zFUqB69zc2Xo7t8mfY9HVIZ5kKecI_d22BoK_mI0WFhD1QtGcU9njz9BI3BS4alxCTdGYsjVajmLqDP-gXOkj67TIRmG8hbM9yIQfCQkLJbEsXSWDR8vts8AM0PcK5AkeB9k_HSc1UWOHEAN3F2L23l1eqAdaFkRYlUfMk24SgC5uADsduGQGDHu82TRR9rE6w7roaefSl2bCwjQEzfZ86a-MnXaHfeq_6Dmi2wHK9l_qiFdhTLygU7GqY1fB9Kzfeu8vVj0NLOuIe5NKmKqOqNjCsDxRcRoKh7m4IJ_JlB22xXKd6Vk5onjm-RpYWNe1wIWB7jUTTjPadNKrUSacfrS5H7CwB6Tp0mhq1l21f_V0_4YYa2DmsGGNTvxb8xbMHKqM7H1pKMzKERSwcrEitnnsH69eoB_uVWFvTIeddl4qx_O1oIMl8XDeDqrDPZMxZ1zes8VsNqULJlOlxWe8zmCLyuACtKvhKllLiaAuuz93BD7MpRRHxvkID8QAt9J3-BpBnT0gFmVMjzz3N5_3jQuK7kSDlfE7DyC8lCFGVYnUxzd21oNWa8oWTHUpHBNbX13IUfiNt_YrmICdDEDa0JMo6F-fcSCXpaK1RJAGIzEzz0Nwfn3l_JOZuGU8ATpar3yR3MahLrvVcO_XuMILGnvAv3HTfFJZMu-YBrv2WY8jAPZ2R1QEh96bHja_9lbWLN7T4mqiUdgVrhKJb_n4kO3IVDtP756Lud1Dsh6xcJkCoFUp0dzsx2Cd7iCyZeXSxuwbcibPobMGNUMslyN8gzE_NTNqIdMhe2Kbf-M9TC1OKkF6NkLAyDKeWxkSQxN4Wru4So9oJkBaqG3mz615LYR_KrInyN3L4Ya6UN9dHx6VVDLjLkFPcAY9bCOFiZbUXMP2c11qznxnCO6v4Lj-HiF7VAXdtVJbNi18Dpfw8uzIJC9AEAmHc84jdYjkwD3fLSnTM2_qPwfT8wy4bhuqFX7y6zEvlfFP4W5x_Bg-dPVx1UU0knQ0I49GiLhv9bfdp_VSdl9f0g59BUe6VhLPz8RZivk1kIokKyMZ7jl6svyDvBDwb4q43wUWop8zcXGOE1WBVfracRswsUWsh8c56u23fGjE--39Q-l35gC4uCeH_IwqF7pkeSi6ThhrZBdKgad1jgTeP5wd2MLfCUS3J_SrV0xsg-upAzzjamdMsJju6OYbzN5sAh8pw74lJkFHcA_C7nCXUNgDUtrLxuF5FRLfGsqjlsEk5yUNZAzMuJiIMXYjnTAX0w_w7WYVSSzvpAZdaYiFQetBghR70YUZtT3xi4q1WZUNj8cl8qHOgmtvcB_2M4qUEDQje2zkc7wolQpqOzYfluP_1QFmzHgSfXONWAmKFls12DBkJtnGi6gsm5ZU2S3CtmA.Ui1dbEardw_cL0ETJ6BZBxC5vbHTMFhR_qAK_O7mVYY"
}

result = xbox_api.get_profile_by_gt("RomanMender3164", authorization)
print(result)
```

## Documentation

### Accounts

| API Call  | Syntax  | Returns  |
| ------------ | ------------ | ------------ |
| Get Profile From Gamertag  | get_profile_by_gt(gamertag, authorization)  | JSON  |
| Get Profile From Xuid  | get_profile_by_xuid(xuid, authorization)  | JSON  |
| Get Own Profile  | get_own_profile

(authorization)  | JSON  |
| Get Xuid From Gamertag  | get_profile_xuid(gamertag, authorization)  | String  |
| Get Clips From Xuid  | get_profile_game_clips(xuid, authorization)  | JSON  |
| Get Own Clips  | get_own_game_clips(authorization)  | JSON  |
| Get Screenshots From Xuid  | get_profile_screenshots(xuid, authorization)  | JSON  |
| Get Own Screenshots  | get_own_screenshots(authorization)  | JSON  |
| Get Recent Games From Xuid  | get_profile_recent_games(xuid, authorization)  | JSON  |
| Get Own Recent Games  | get_own_recent_games(authorization)  | JSON  |

### Friends & Messaging

| API Call  | Syntax  | Returns  |
| ------------ | ------------ | ------------ |
| Get Friends From Xuid | get_friends_by_xuid(xuid, authorization)  | JSON  |
| Get Friends From Gamertag | get_friends_by_xuid(gamertag, authorization)  | JSON  |
| Get Own Friends | get_own_friends(authorization)  | JSON  |
| Get Messages* | fetch_messages(xuid, authorization)  | JSON  |
| Send a Message* | send_message(xuid, message, authorization)  | JSON  |
| Delete a Message* | delete_message(xuid, message_id, authorization)  | JSON  |

*Note: These endpoints may require Xbox Gold.

### Clubs

| API Call  | Syntax  | Returns  |
| ------------ | ------------ | ------------ |
| Get Current Clubs  | get_all_clubs(authorization)  | JSON  |
| Get Club by ID | get_club_by_id(club_id, authorization)  | JSON  |
| Ban User from Club | ban_user_from_club(club_id, xuid, authorization)  | JSON  |
| Unban User from Club | unban_user_from_club(club_id, xuid, authorization)  | JSON  |
| Add Club Moderator | add_club_moderator(club_id, xuid, authorization)  | JSON  |
| Remove Club Moderator | remove_club_moderator(club_id, xuid, authorization)  | JSON  |
| Remove User from Club | remove_user_from_club(club_id, xuid, authorization)  | JSON  |

# Xbox OAuth2

To use Xbox OAuth2, you need to create an application in the [Azure Portal](https://aka.ms/appregistrations). Obtain the **Application (client) ID** and add a redirect URL in the **Authentication** tab. Then, go to **Certificates & secrets** and create a **Client Secret**. With this information, you can make Xbox OAuth2 requests.

## Example

```python
from flask import Flask, redirect, request
import xbox_api

app = Flask(__name__)
app.run(port=3000)

client_info = {
   "client_id": "2295a725-0097-47eb-ba1d-c79dca4606e1",
   "redirect_uri": "http://localhost:3000/xbox/auth/callback",
   "client_secret": "p53ug8Us5eygCCB-pST.Ut-_42E3Em62zg"  # keep this secret
}

@app.route('/xbox')
def xbox_login():
    return redirect(xbox_api.make_auth_url(client_info))

@app.route('/xbox/auth/callback')
def xbox_auth_callback():
    code = request.args.get('code')
    result = xbox_api.get_token(code, client_info)
    return f"Hello, {result['gamertag']}"

```

| API Call  | Syntax  | Returns  |
| ------------ | ------------ | ------------ |
| Get Token from OAuth2  | get_token(code, client_info)  | JSON  |
| Get Token from OAuth2 refresh  | refresh_token(refresh, client_info)  | JSON  |
