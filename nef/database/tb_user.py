import nef.database


class TB_User(object):

    def __init__(self):
        TB_User.__create_database_if_not_exists()
        self.create_table_if_not_exists()

    @staticmethod
    def __create_database_if_not_exists():
        db = nef.database.SQLManager()
        db.execute("create database if not exists NefVision")

    def create_table_if_not_exists(self):
        with nef.database.SQLManager("NefVision") as db:
            db.execute("create table if not exists t_user("
                       "id bigint(15) not null auto_increment,"
                       "user_id bigint(15) not null,"
                       "username varchar(64) not null,"
                       "nickname varchar(64) default null,"
                       "password varchar(64) not null,"
                       "gendar int(1) not null,"
                       "email varchar(64) default null,"
                       "phone_number varchar(64) default null,"
                       "register_time timestamp default current_timestamp,"
                       "update_time timestamp default current_timestamp on update current_timestamp,"
                       "primary key(user_id),"
                       "unique uk_u_id(id),"
                       "unique uk_u_username(username),"
                       "unique uk_u_email(email),"
                       "unique uk_u_phone_number(phone_number))")

    def insert(self, args=None):
        with nef.database.SQLManager("NefVision") as db:
            db.execute(
                "insert into t_user(user_id,username,nickname,password,gendar,email,phone_number) "
                "values(%s,%s,%s,%s,%s,%s,%s)", args)

    def execute(self, sql, args=None):
        with nef.database.SQLManager("NefVision") as db:
            db.execute(sql, args)

    def fetch_one(self, sql, args=None):
        with nef.database.SQLManager("NefVision") as db:
            return db.fetch_one(sql, args)

    def fetch_all(self, sql, args=None):
        with nef.database.SQLManager("NefVision") as db:
            return db.fetch_all(sql, args)
