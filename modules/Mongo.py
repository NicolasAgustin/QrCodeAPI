from pymongo.mongo_client import MongoClient


class Mongo():

    def __init__(this, db_port: str, db_ip: str, db_name: str):
        this.string_connection = (
            f'mongodb://{db_ip}:{db_port}'
        )
        this.client = MongoClient(this.string_connection)
        this.db = this.client.get_database(db_name)

    def get_user_by_pass_email(this, passw: str, user: str) -> dict:
        """ Method for search a user in db by password and username

        Args:
            this (Mongo): This
            passw (str): Password
            user (str): Username

        Returns:
            dict: Document found
        """
        collection = this.db.get_collection('users')
        doc = collection.find_one({'user': user, 'password': passw})
        return doc
