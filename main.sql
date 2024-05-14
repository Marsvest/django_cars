Create Table Clients
(
    id        integer primary key autoincrement,
    name      text,
    last_name text
);

Create Table Cars
(
    id       integer primary key autoincrement,
    name     text,
    number   text,
    owner_id integer references Clients (id)
);

Create Table Service
(
    id                       integer primary key autoincrement,
    start_timestamp          integer,
    end_timestamp            integer,
    oil_work                 boolean,
    fluids_work              boolean,
    filters_work             boolean,
    brake_system_work        boolean,
    suspension_steering_work boolean,
    exhaust_work             boolean,
    tires_work               boolean,
    lighting_work            boolean,
    car_id                   integer references Cars (id)
);