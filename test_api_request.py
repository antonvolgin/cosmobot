#!/usr/bin/python3

""""""

def send_request_sostav(sostav, sub_type, type):
    # sub_type = 'sub'
    attempts = 5
    while attempts > 0:
        """sub: {free, sub}; type: {styling, balsam, shampoo}"""
        url = f'https://cosmocode.site/api/{sub_type}/{type}'
        # json = {"ingredients": sostav}
        # token = 'Token jXxtbRXhk7z6G01AGimEKP1j7UGLC_bmecIZa3wgMv9s3QrBBSlkVtqLeafuaLYmuOO5PjgdX6kSkqNTX2jg5A'
        # headers = {"Authorization": token}
        # a = requests.post(url, json=json, headers=headers)

        a = {"a":url}

        if a:
            return a
        else:
            attempts -= 1
    return {'status': False}


res_1 = send_request_sostav("состав", "free_1", "balsam")

print(f"{res_1}")
