from django.contrib.auth.models import User, get_hexdigest
from dnevniktools.dbutils import get_nextautoincrement

def construct_user(email, password):
    next_id = get_nextautoincrement(User)
    username = "user%05d" % next_id
    user = User(username = username, email = email)
    user.set_password(password)
    return user
