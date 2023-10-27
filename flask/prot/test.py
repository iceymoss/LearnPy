from sqlalchemy import create_engine
from models import create_session, User

# 配置数据库连接字符串
database_url = 'mysql://root:123456789@127.0.0.1/coolmovie'

# 创建数据库引擎
engine = create_engine(database_url)

# 创建会话
session = create_session(engine)

# 使用 User 类执行数据库操作
users = session.query(User).all()

for user in users:
    print(user.id, user.nickname, user.login_name, user.login_pwd, user.login_salt, user.status, user.updated_time, user.created)
