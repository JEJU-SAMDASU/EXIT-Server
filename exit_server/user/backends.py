from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserBackend(BaseBackend):
    """
    settings.AUTH_USER_MODEL 셋팅에 의존한다.
    """

    def authenticate(self, credentials):
        uid = credentials["uid"]
        password = credentials["password"]
        if uid is None:
            uid = kwargs.get(UserModel.USERNAME_FIELD)
        try:  # uid에 매치되는 인스턴스 존재하는지 확인
            user = UserModel.objects.get(uid=uid)
        except UserModel.DoesNotExist:
            return
        if user.check_password(password) and self.user_can_authenticate(
            user
        ):  # password랑 맞는지 체크, is_active 인지 체크
            return user

    def user_can_authenticate(self, user):
        return user.is_active