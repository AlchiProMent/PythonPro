DROP TABLE IF EXISTS o_students;
DROP TABLE IF EXISTS r_cities;
DROP TABLE IF EXISTS r_faculties;
DROP TABLE IF EXISTS r_campuses;
CREATE TABLE IF NOT EXISTS r_cities (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       Name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS r_faculties (
       id INTEGER  PRIMARY KEY AUTOINCREMENT,
       Name TEXT,
       ShortName TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS r_campuses (
       id INTEGER  PRIMARY KEY AUTOINCREMENT,
       Corps TEXT NOT NULL,
       Address TEXT
);
CREATE TABLE IF NOT EXISTS o_students (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       fio TEXT NOT NULL CHECK (fio != ''),
       CityID INTEGER NOT NULL,
       FacultyID INTEGER NOT NULL,
       CampusID INTEGER NOT NULL DEFAULT 1,
       FOREIGN KEY (CityID)  REFERENCES r_cities (id) ON DELETE RESTRICT,
       FOREIGN KEY (FacultyID)  REFERENCES r_faculties (id) ON DELETE RESTRICT,
       FOREIGN KEY (CampusID)  REFERENCES r_campuses (id) ON DELETE RESTRICT
);
INSERT INTO r_campuses (Corps, Address)
VALUES ('нет',''),
       ('Корпус 1','ул.Синеухова, 23'),
       ('Корпус 2','ул.Чипполино, 45'),
       ('Корпус A','ул.Синеухова, 32');
INSERT INTO r_faculties (Name,ShortName)
VALUES ('Биологический','ФБ'),
       ('Гуманитарных наук','ФГН'),
       ('Информационных технологий','ФИТ'),
       ('Прикладной арифметики','ФПА'),
       ('Промышленной механики','ФПМ'),
       ('Рекламных технологий','ФРТ'),
       ('Физический','ФФ');
INSERT INTO r_cities (Name)
VALUES ('Архангельск'),
       ('Барнаул'),
       ('Белгород'),
       ('Бийск'),
       ('Владикавказ'),
       ('Владимир'),
       ('Воронеж'),
       ('Грозный'),
       ('Иваново'),
       ('Ижевск'),
       ('Казань'),
       ('Кострома'),
       ('Красноярск'),
       ('Магас'),
       ('Майкоп'),
       ('Махачкала'),
       ('Москва'),
       ('Нижний Новгород'),
       ('Новороссийск'),
       ('Новосибирск'),
       ('Омск'),
       ('Оренбург'),
       ('Ростов'),
       ('Ростиов-на-Дону'),
       ('Рыбинск'),
       ('Рязань'),
       ('Санкт-Петербург'),
       ('Соликамск'),
       ('Сыктывкар'),
       ('Тамбов'),
       ('Томск'),
       ('Чита'),
       ('Элиста'),
       ('Якутск');
