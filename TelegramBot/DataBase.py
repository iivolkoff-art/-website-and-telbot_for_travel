import psycopg2
from TelegramBot.JSON import JSON

class DataBase:
    def __init__(self):
        self.host = "#"
        self.user = "#"
        self.password = "#"
        self.db_name = "#"

        self.json = JSON()

    def get_data(self):
        data = None
        try:
            connection = psycopg2.connect(user=self.user,
                                            password=self.password,
                                            host=self.host,
                                            database=self.db_name)
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM travel_travel")
                data = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            if connection:
                connection.close()
        return data

    def get_max_id_from_db(self):
        data = None
        try:
            connection = psycopg2.connect(user=self.user,
                                            password=self.password,
                                            host=self.host,
                                            database=self.db_name)
            with connection.cursor() as cursor:
                cursor.execute("SELECT MAX(id) FROM travel_travel")
                data = cursor.fetchall()
                data = data[0][0]
        except Exception as e:
            print(e)
        finally:
            if connection:
                connection.close()
        return data

    def get_data_from_last_id_to_max_id(self, last_id):
        data = None
        try:
            connection = psycopg2.connect(user=self.user,
                                            password=self.password,
                                            host=self.host,
                                            database=self.db_name)
            with connection.cursor() as cursor:
                # cursor.execute(f"SELECT * FROM travel_travel WHERE id > {last_id}")
                cursor.execute(f"SELECT name, mail, phone_number, place_of_chill FROM travel_travel WHERE id > {last_id}")
                self.json.set_last_id(self.get_max_id_from_db())
                data = cursor.fetchall()
                data = str(data).translate({ord(i): None for i in "[]('"})
                data = data.replace("),", "\n\n")
        except Exception as e:
            print(e)
        finally:
            if connection:
                connection.close()
        return data if data else "Новых клиентов нет"
