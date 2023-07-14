import requests
import json


def get_profile_by_gt(gamertag, authorization):
  try:
    if not gamertag:
      return 'null'
    url = 'https://profile.xboxlive.com/users/gt(' + gamertag + ')/profile/settings?settings=Gamertag,Gamerscore,GameDisplayPicRaw,AccountTier,XboxOneRep,PreferredColor,RealName,Bio,Location,RealNameOverride,Watermarks,IsQuarantined,DisplayedLinkedAccounts'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken']
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    json_data = {}
    json_data['id'] = fetched['profileUsers'][0]['id']
    json_data['isSponsoredUser'] = fetched['profileUsers'][0][
        'isSponsoredUser']
    for settings in fetched['profileUsers'][0]['settings']:
      if settings['id'] != 'DisplayedLinkedAccounts':
        json_data[settings['id']] = settings['value']
      else:
        json_data[settings['id']] = json.loads(settings['value'])
    return json_data
  except:
    return 'null'


def get_profile_by_xuid(gamertag, authorization):
  try:
    if not gamertag:
      return 'null'
    url = 'https://profile.xboxlive.com/users/xuid(' + gamertag + ')/profile/settings?settings=Gamertag,Gamerscore,GameDisplayPicRaw,AccountTier,XboxOneRep,PreferredColor,RealName,Bio,Location,RealNameOverride,Watermarks,IsQuarantined,DisplayedLinkedAccounts'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken']
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    json_data = {}
    json_data['id'] = fetched['profileUsers'][0]['id']
    json_data['isSponsoredUser'] = fetched['profileUsers'][0][
        'isSponsoredUser']
    for settings in fetched['profileUsers'][0]['settings']:
      if settings['id'] != 'DisplayedLinkedAccounts':
        json_data[settings['id']] = settings['value']
      else:
        json_data[settings['id']] = json.loads(settings['value'])
    return json_data
  except:
    return 'null'


def get_own_profile(authorization):
  try:
    url = 'https://profile.xboxlive.com/users/me/profile/settings?settings=Gamertag,Gamerscore,GameDisplayPicRaw,AccountTier,XboxOneRep,PreferredColor,RealName,Bio,Location,RealNameOverride,Watermarks,IsQuarantined,DisplayedLinkedAccounts'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken']
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    json_data = {}
    json_data['id'] = fetched['profileUsers'][0]['id']
    json_data['isSponsoredUser'] = fetched['profileUsers'][0][
        'isSponsoredUser']
    for settings in fetched['profileUsers'][0]['settings']:
      if settings['id'] != 'DisplayedLinkedAccounts':
        json_data[settings['id']] = settings['value']
      else:
        json_data[settings['id']] = json.loads(settings['value'])
    return json_data
  except:
    return 'null'


def get_profile_xuid(gamertag, authorization):
  try:
    url = 'https://profile.xboxlive.com/users/gt(' + gamertag + ')/profile/settings'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken']
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched['profileUsers'][0]['id']
  except:
    return 'null'


def get_profile_game_clips(xuid, authorization):
  try:
    url = 'https://gameclipsmetadata.xboxlive.com/users/xuid(' + xuid + ')/clips'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken']
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched['gameClips']
  except:
    return 'null'


def get_own_game_clips(authorization):
  try:
    url = 'https://gameclipsmetadata.xboxlive.com/users/me/clips'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken']
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched['gameClips']
  except:
    return 'null'


def get_profile_screenshots(xuid, authorization):
  try:
    url = 'https://screenshotsmetadata.xboxlive.com/users/xuid(' + xuid + ')/clips?type=screenshots'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken']
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched['gameClips']
  except:
    return 'null'


def get_own_screenshots(authorization):
  try:
    url = 'https://screenshotsmetadata.xboxlive.com/users/me/clips?type=screenshots'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken']
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched['gameClips']
  except:
    return 'null'


def get_profile_recent_games(xuid, authorization):
  try:
    url = 'https://titlehub.xboxlive.com/users/xuid(' + xuid + ')/titles/titlehistory/decoration/achievement,image'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en-GB'
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched['titles']
  except:
    return 'null'


def get_own_recent_games(authorization):
  try:
    url = 'https://titlehub.xboxlive.com/users/me/titles/titlehistory/decoration/achievement,image'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en-GB'
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched['titles']
  except:
    return 'null'


def get_all_clubs(authorization):
  try:
    url = 'https://profile.xboxlive.com/users/me/profile/settings?settings=Gamertag,Gamerscore,GameDisplayPicRaw,AccountTier,XboxOneRep,PreferredColor,RealName,Bio,Location,RealNameOverride,Watermarks,IsQuarantined,DisplayedLinkedAccounts'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken']
    }
    response = requests.get(url, headers=headers)
    xuid = response.json()['profileUsers'][0]['id']
    url = 'https://clubhub.xboxlive.com/clubs/xuid(' + xuid + ')/decoration/detail,settings'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def get_club_by_id(id, authorization):
  try:
    url = 'https://clubhub.xboxlive.com/clubs/Ids(' + id + ')/decoration/clubpresence,detail,settings,roster'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def fetch_messages(xuid, authorization):
  try:
    url = 'https://msg.xboxlive.com/users/xuid(' + xuid + ')/inbox'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def delete_message(xuid, messageid, authorization):
  try:
    url = 'https://msg.xboxlive.com/users/xuid(' + xuid + ')/inbox/' + messageid
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    response = requests.delete(url, headers=headers)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def send_message(xuid, message, authorization):
  try:
    url = 'https://msg.xboxlive.com/users/xuid(' + xuid + ')/outbox'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    body = {"messageText": message}
    response = requests.post(url, headers=headers, json=body)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def make_auth_url(clientinfo):
  try:
    return f"https://login.live.com/oauth20_authorize.srf?client_id={clientinfo['client_id']}&redirect_uri={clientinfo['redirect_uri']}&response_type=code&scope=Xboxlive.signin+Xboxlive.offline_access"
  except:
    return 'null'


def get_token(code, clientinfo):
  try:
    fetched = {}
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': clientinfo['client_id'],
        'scope': 'Xboxlive.signin Xboxlive.offline_access',
        'redirect_uri': clientinfo['redirect_uri'],
        'client_secret': clientinfo['client_secret']
    }
    response = requests.post(
        'https://login.microsoftonline.com/consumers/oauth2/v2.0/token',
        data=data)
    microsoft_code = response.json()
    fetched['refresh_token'] = microsoft_code['refresh_token']
    data_two = {
        "RelyingParty": "http://auth.xboxlive.com",
        "TokenType": "JWT",
        "Properties": {
            "AuthMethod": "RPS",
            "SiteName": "user.auth.xboxlive.com",
            "RpsTicket": "d=" + microsoft_code['access_token'],
        },
    }
    response = requests.post(
        'https://user.auth.xboxlive.com/user/authenticate',
        json=data_two,
        headers={
            'x-xbl-contract-version': '0',
            'Content-Type': 'application/json'
        })
    xbox_pre_code = response.json()
    data_three = {
        "RelyingParty": "http://xboxlive.com",
        "TokenType": "JWT",
        "Properties": {
            "UserTokens": [xbox_pre_code['Token']],
            "SandboxId": "RETAIL"
        }
    }
    response = requests.post('https://xsts.auth.xboxlive.com/xsts/authorize',
                             json=data_three,
                             headers={
                                 'x-xbl-contract-version': '1',
                                 'Content-Type': 'application/json'
                             })
    xbox_token_final = response.json()
    fetched['token'] = xbox_token_final['Token']
    fetched['UserHash'] = xbox_token_final['DisplayClaims']['xui'][0]['uhs']
    fetched['xuid'] = xbox_token_final['DisplayClaims']['xui'][0]['xui']
    fetched['gamertag'] = xbox_token_final['DisplayClaims']['xui'][0]['gtg']
    return fetched
  except:
    return 'null'


def refresh_token(refresh, clientinfo):
  try:
    fetched = {}
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh,
        'client_id': clientinfo['client_id'],
        'scope': 'Xboxlive.signin Xboxlive.offline_access',
        'redirect_uri': clientinfo['redirect_uri'],
        'client_secret': clientinfo['client_secret']
    }
    response = requests.post(
        'https://login.microsoftonline.com/consumers/oauth2/v2.0/token',
        data=data)
    microsoft_code = response.json()
    fetched['refresh_token'] = microsoft_code['refresh_token']
    data_two = {
        "RelyingParty": "http://auth.xboxlive.com",
        "TokenType": "JWT",
        "Properties": {
            "AuthMethod": "RPS",
            "SiteName": "user.auth.xboxlive.com",
            "RpsTicket": "d=" + microsoft_code['access_token'],
        },
    }
    response = requests.post(
        'https://user.auth.xboxlive.com/user/authenticate',
        json=data_two,
        headers={
            'x-xbl-contract-version': '0',
            'Content-Type': 'application/json'
        })
    xbox_pre_code = response.json()
    data_three = {
        "RelyingParty": "http://xboxlive.com",
        "TokenType": "JWT",
        "Properties": {
            "UserTokens": [xbox_pre_code['Token']],
            "SandboxId": "RETAIL"
        }
    }
    response = requests.post('https://xsts.auth.xboxlive.com/xsts/authorize',
                             json=data_three,
                             headers={
                                 'x-xbl-contract-version': '1',
                                 'Content-Type': 'application/json'
                             })
    xbox_token_final = response.json()
    fetched['token'] = xbox_token_final['Token']
    fetched['UserHash'] = xbox_token_final['DisplayClaims']['xui'][0]['uhs']
    fetched['xuid'] = xbox_token_final['DisplayClaims']['xui'][0]['xui']
    fetched['gamertag'] = xbox_token_final['DisplayClaims']['xui'][0]['gtg']
    return fetched
  except:
    return 'null'


def get_friends_by_xuid(xuid, authorization):
  try:
    url = 'https://profile.xboxlive.com/users/xuid(' + xuid + ')/profile/people/people?settings=Gamertag,Gamerscore,GameDisplayPicRaw,AccountTier,XboxOneRep,PreferredColor,RealName,Bio,Location,RealNameOverride,Watermarks,IsQuarantined,DisplayedLinkedAccounts'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def get_friends_by_gt(gt, authorization):
  try:
    url = 'https://profile.xboxlive.com/users/gt(' + gt + ')/profile/people/people?settings=Gamertag,Gamerscore,GameDisplayPicRaw,AccountTier,XboxOneRep,PreferredColor,RealName,Bio,Location,RealNameOverride,Watermarks,IsQuarantined,DisplayedLinkedAccounts'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def get_own_friends(authorization):
  try:
    url = 'https://profile.xboxlive.com/users/me/profile/people/people?settings=Gamertag,Gamerscore,GameDisplayPicRaw,AccountTier,XboxOneRep,PreferredColor,RealName,Bio,Location,RealNameOverride,Watermarks,IsQuarantined,DisplayedLinkedAccounts'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    response = requests.get(url, headers=headers)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def ban_user_from_club(clubid, xuid, authorization):
  try:
    url = 'https://clubroster.xboxlive.com/clubs/' + clubid + '/users/xuid(' + xuid + ')/roles/'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    body = {"userID": xuid, "roles": [""]}
    response = requests.post(url, headers=headers, json=body)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def unban_user_from_club(clubid, xuid, authorization):
  try:
    url = 'https://clubroster.xboxlive.com/clubs/' + clubid + '/users/xuid(' + xuid + ')/roles/'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    body = {"userID": xuid, "roles": ["Members"]}
    response = requests.post(url, headers=headers, json=body)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def add_club_moderator(clubid, xuid, authorization):
  try:
    url = 'https://clubroster.xboxlive.com/clubs/' + clubid + '/users/xuid(' + xuid + ')/roles/'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    body = {"userID": xuid, "roles": ["Moderator"]}
    response = requests.post(url, headers=headers, json=body)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def remove_club_moderator(clubid, xuid, authorization):
  try:
    url = 'https://clubroster.xboxlive.com/clubs/' + clubid + '/users/xuid(' + xuid + ')/roles/'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    body = {"userID": xuid, "roles": ["Member"]}
    response = requests.post(url, headers=headers, json=body)
    fetched = response.json()
    return fetched
  except:
    return 'null'


def remove_user_from_club(clubid, xuid, authorization):
  try:
    url = 'https://clubroster.xboxlive.com/clubs/' + clubid + '/users/xuid(' + xuid + ')/'
    headers = {
        'x-xbl-contract-version':
        '2',
        'Authorization':
        'XBL3.0 x=' + authorization['userHash'] + ';' +
        authorization['XSTSToken'],
        'Accept-Language':
        'en_us'
    }
    response = requests.delete(url, headers=headers)
    fetched = response.json()
    return fetched
  except:
    return 'null'
