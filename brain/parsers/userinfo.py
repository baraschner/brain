def parse_user_info(data):
    return {'userId': data['userId'],
            'username': data['username'], 'birthday': data['birthday'], 'gender': data['gender']}


parse_user_info.field = 'user'
