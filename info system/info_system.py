import sqlite3
# Предметная область тату салон 
# Я не знаю,уже часика 3 сижу, и думаю, ошибка в строчке 78 хелпи плиз , я не понимаю что не так!!!!!!! Мои лапки уже с катушек съехали и хотят побыстрее закончить это..
class DataBase:
    conn = sqlite3.connect('taty_database.db')
    cursor = conn.cursor()

    @classmethod
    def create_tables(cls):
        cls.cursor.execute('''
                           
                CREATE TABLE WIZARDS (
                ID_WIZARDS INT PRIMARY KEY IDENTITY(1,1),
                Post VARCHAR(25) NOT NULL,
                Surname VARCHAR(35) NOT NULL,
                FirstName VARCHAR(30) NOT NULL,
                Mail VARCHAR (50) NOT NULL,
                Numner int NOT NULL
                );
                GO
            )
        ''')
        cls.cursor.execute('''
                           
                CREATE TABLE ROOMS (
                ID_ROOMS INT PRIMARY KEY IDENTITY(1,1),
                Departament VARCHAR(40) NOT NULL,
                Rooms VARCHAR(35) NOT NULL
                );
                GO
            )
        ''')
        cls.cursor.execute('''
                           
                CREATE TABLE STAFFS(
                ID_STAFFS INT PRIMARY KEY IDENTITY(1,1),
                Post VARCHAR (35) NOT NULL,
                Pay int NOT NULL,
                Wizard VARCHAR (45) NOT NULL
                );
                GO
            )
        ''')

        cls.cursor.execute('''
                           
                CREATE TABLE TATTOOS(
                ID_TATTOOS INT PRIMARY KEY IDENTITY(1,1),
                Tattoo VARCHAR (60) NOT NULL,
                Wizard VARCHAR(45) NOT NULL
                );
                GO
            )
        ''')
        cls.conn.commit()


    @classmethod
    def add_wizards(cls, wizards):
        cls.cursor.execute('''
            INSERT INTO users (post, full_name,Surname,Firstname,Mail,numner)
            VALUES (?, ?, ?)
        ''', 
        (wizards.post, wizards.full_name,wizards.Surname,wizards.Firstname,wizards.Mail,wizards.Numner ))
        cls.conn.commit()

    @classmethod
    def add_rooms(cls, rooms):
        cls.cursor.execute('''
            INSERT INTO orders (Departament,Rooms)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', 
        (rooms.Deoartament,rooms.Rooms))
        cls.conn.commit()

    @classmethod
    def add_staffs(cls, staffs):
        cls.cursor.execute('''
            INSERT INTO tovars (Post,Pay,Wizard)
            VALUES (?, ?, ?, ?, ?) 
        ''',    
        (staffs.Post,staffs.Pay,staffs.Wizard)  
        cls.conn.commit()

    @classmethod
    def add_Tatoos(cls, Tattoos):
        cls.cursor.execute('''
            INSERT INTO orders (Tattoo,Wizard )
            VALUES (?, ?, ?, ?)
        ''', 
        (tatoos.tattoo,tatoos.wizard))
        cls.conn.commit()

    @classmethod
    def fetch_user(cls, password, role, full_name):
        cls.cursor.execute('''
            SELECT * FROM Users
            WHERE password = ? AND role = ? AND full_name = ?
        ''', (password, role, full_name))
        user_data = cls.cursor.fetchone()

        if user_data:
            user_id, password, role, full_name = user_data
            return User(user_id, password, role, full_name)
        else:
            return None

class Wizards:
    def __init__(self, user_id, Post,Surname,FirstName,Mail,Numner):
        self.id = user_id
        self.surname = surname
        self.FirstName = FirstName
        self.Mail = Mail
        self.Numner = Numner

class Rooms:
    def __init__(self, rooms_id,Departament,Rooms):
        self.id = patient_id
        self.Departament = Departament
        self.rooms = rooms


class Staffs:
    def __init__(self, staffs_id,Post,Pay,Wizard ):
        self.id = staffs_id
        self.Post = Post
        self.name = name
        self.Wizard = Wizard
 
class Tatoos :
    def __init__(self, Tattoos_id,Tatto,Wizard):
        self.id = Tattoos_id
        self.Tattoo = Tattoo
        self.Wizard = Wizard

class Interface:
    @staticmethod
    def registration():
        password = input("Введите ваш пароль: ")
        role = input("Выберите свою должность (User/ Wizard/ Staffs): ")
        full_name = input("Введите ваше имя: ")

        user = User(None, password, role, full_name)
        DataBase.add_user(user)
        print("Регистрация завершена.") 

    @staticmethod
    def login():
        password = input("Введите ваш пароль: ")
        role = input("Введите свою роль (User/ Wizard/ Staffs):")
        full_name = input("Введите ваше имя:")
        user = DataBase.fetch_user(password, role, full_name) 

        if user:
            return user
        else:
            print("Вы ввели некорректный пароль.Попробуйте снова!.")
            return None

    @classmethod
    def main(cls):
        pass

    @staticmethod
    def add_patients(cls, wizards):
        cls.cursor.execute('''
            INSERT INTO orders (wizards_id, Post,Surname,FirstName,Mail,Numner)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', 
        ((wizards.post, wizards.full_name,wizards.Surname,wizards.Firstname,wizards.Mail,wizards.Numner )))
        cls.conn.commit()
        
    @staticmethod
    def view_wizards():
        DataBase.cursor.execute("SELECT * FROM Wizards")
        peoples = DataBase.cursor.fetchall()
        if peoples:
            print("Таблица: ")
            for people in peoples:
               wizards_id, post,fullname,Surname,Firstname,mail = people,Number
                print(f"ID: {patient_id}, Должноть: {post}, Имя: {fullname}, Фамилия: {Surname}, Отчество: {Firstname}, Почта: {mail}, телефон: {Number} ")
        else
            print("Отказанно.")


    @classmethod
    def change_wizards(cls, wizards_id, update_wizards):
        cls.cursor.execute('''
                UPDATE Patients
                SET post = ?
                SET fullname = ?
                SET Surname = ?
                SET Firstname = ?
                SET Mail = ?                  
                SET Number = ?
                WHERE id = ?
            ''', 
            (update_wizards, wizards_id))
        cls.conn.commit()
 )
    @staticmethod
    def change_patients():
        patient_id = input("напишите ID, чего хотите изменить(жмякать ENT чтобы ниче не менять ): ")

        DataBase.cursor.execute("SELECT * FROM Patients WHERE id = ?", (wizards_id,))
        wizards = DataBase.cursor.fetchone()

        if wizards:
            wizards_id, post,fullname,Surname,Firstname,mail = people,Number
 
            new_post = input("должность :")
            new_fullname = input("имя :")
            new_Surname = input("фамилия :")
            new_Firstname = input("отчество :")
            new_mail = input("почта:")
            new_number = input("телефон : ")
            if new_name:
                patient = (new_post, new_Surname, new_fullname, new_Firstname, new_mail, new_number)
                DataBase.cursor.execute('''
                    UPDATE Patients
                    SET npost = ?, surname = ? Firstname = ?, number = ?, mail = ?, fullname = ?
                    WHERE id = ?
                ''', wizards)
                DataBase.conn.commit()

            print("Данные изменены.")
        else:
            print("Отказано.")

    @classmethod
    def delete_patients(patient_id):
        DataBase.cursor.execute('''
                      DELETE FROM Wizards
                      WHERE id = ?
                  ''', 
                  (wizards_id,))
        DataBase.conn.commit()

    @classmethod
    def delete_wiz(cls):
        wizards_id = input("Удолятор из БД: ")

        DataBase.cursor.execute("SELECT * FROM orders WHERE id = ?", (wizards_id,))
        patient = DataBase.cursor.fetchone()

        if patient:
            cls.delete_patient_by_id(wizards_id)
            print("Удолятор из БД выполнил свою работу.")
        else:
            print("Отказано.")
            return


    