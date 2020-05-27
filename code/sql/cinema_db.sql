CREATE DATABASE IF NOT EXISTS cinema_db;

USE cinema_db;

CREATE TABLE IF NOT EXISTS admins(
	ID_admin INT NOT NULL AUTO_INCREMENT,
    a_name VARCHAR(35) NOT NULL,
    a_lastname1 VARCHAR(35) NOT NULL,
    a_lastname2 VARCHAR(35),
    a_username VARCHAR(35) NOT NULL,
    a_email VARCHAR(35) NOT NULL,
    a_password VARCHAR(16) NOT NULL,
    UNIQUE(a_username),
    PRIMARY KEY(ID_admin)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS movies(
	ID_movie INT NOT NULL AUTO_INCREMENT,
    m_title VARCHAR(32) NOT NULL,
    m_gender VARCHAR(20) NOT NULL,
    m_clasification VARCHAR(4) NOT NULL,
    m_director VARCHAR(35) NOT NULL,
    m_actors VARCHAR(280) NOT NULL,
    m_synopsis VARCHAR(350) NOT NULL,
    m_release_date DATE NOT NULL,
    m_language VARCHAR(20) NOT NULL,
    m_subtitles VARCHAR(20),
    m_format ENUM('2D', '3D') NOT NULL,
    UNIQUE(m_title, m_language, m_format),
    PRIMARY KEY(ID_movie)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS halls(
	ID_hall INT NOT NULL,
    h_no_seats INT NOT NULL,
    h_format ENUM('Tradicional','Premium','VIP') NOT NULL,
    h_price FLOAT NOT NULL,
    PRIMARY KEY(ID_hall)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS schedule_cinema(
	ID_schedule INT NOT NULL AUTO_INCREMENT,
    sc_movie INT NOT NULL,
    sc_hall INT NOT NULL,
    sc_hour TIME NOT NULL,
    UNIQUE(sc_hall, sc_hour),
    PRIMARY KEY(ID_schedule),
    CONSTRAINT fkHall_Schcin FOREIGN KEY(sc_hall)
		REFERENCES  halls(ID_hall)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fkIDMovie_Schcin FOREIGN KEY(sc_movie)
		REFERENCES movies(ID_movie)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS seat(
	ID_seat VARCHAR(3) NOT NULL,
    s_hall INT NOT NULL,
    PRIMARY KEY(ID_Seat, s_hall),
    CONSTRAINT fkHall_Seat FOREIGN KEY(s_hall)
		REFERENCES halls(ID_hall)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS ticket(
	ID_ticket INT NOT NULL AUTO_INCREMENT,
    t_date DATE NOT NULL,
    t_schedule INT NOT NULL,
    t_seat VARCHAR(3) NOT NULL,
    PRIMARY KEY(ID_ticket),
    CONSTRAINT fkIDSch_ticket FOREIGN KEY(t_schedule)
		REFERENCES schedule_cinema(ID_schedule)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fkSeat_ticket FOREIGN KEY(t_seat)
		REFERENCES seat(ID_seat)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;
