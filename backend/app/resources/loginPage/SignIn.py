from app.resources.Common.UsersCommon import UsersCommon
from flask import request, session


class SignIn(UsersCommon):

    def post(self):
        try:
            login = request.json['login']
            password_request = self.to_hash(request.json['password'])
            result = self.__check_login_password(login, password_request)
            if result != "ok":
                return {'message': result}
            return "ok"
        except Exception as e:
            print(e)
            return e

    def __check_login_password(self, login, password_request):
        sql = '''SELECT user_id, password FROM users
                         WHERE login = %s
                        ;'''
        record = (login,)
        user_data = self.base_get_one(sql, record)
        if not user_data:
            return "Login does not exist"
        if password_request != user_data['password']:
            return "Invalid Passport"
        session['login'] = login
        session['user_id'] = user_data['user_id']
        print('user_id sign in: ', session['user_id'])
        return "ok"

    # def create_token(self):
    #     access_token = create_access_token(identity=session['user_id'], expires_delta=False)
    #     result_obj = {
    #         'message': "ok",
    #         'access_token': access_token,
    #         'user_id': session['user_id']
    #     }
    #     return result_obj


