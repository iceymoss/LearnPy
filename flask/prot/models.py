# models.py

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()

# 在此添加自动生成的类
User = Base.classes.users # 示例表名称

def create_session(engine):
    session = Session(engine)
    return session
