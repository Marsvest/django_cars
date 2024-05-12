Create Table Users
(
    id       integer primary key autoincrement,
    login    text,
    password text
);

Create Table Cars
(
    id       integer primary key autoincrement,
    name     text,
    number   text,
    owner_id integer references Users (id)
);

Create Table Service
(
    id integer primary key autoincrement,
    work text,
    car_id integer references Cars(id)
);