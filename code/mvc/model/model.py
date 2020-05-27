from mysql import connector

class Model:

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
    
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()
    
    def close_db(self):
        self.cnx.close()

    """Admins Methods"""

    def create_admin(self, name, lastname1, lastname2, username, email, password):
        try:
            sql = 'INSERT INTO admins (`a_name`, `a_lastname1`, `a_lastname2`, `a_username`, `a_email`, `a_password`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = (name, lastname1, lastname2, username, email, password)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_admin(self, ID_admin):
        try:
            sql = "SELECT * FROM admins WHERE ID_admin = %s"
            vals = (ID_admin,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_admins(self):
        try:
            sql = 'SELECT * FROM admins'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_username_password(self, username, password):
        try:
            sql = 'SELECT admins.a_username, admins.a_password FROM admins WHERE a_username = %s AND a_password = %s'
            vals = (username, password)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def update_admin(self, fields, vals):
        try:
            sql = 'UPDATE admins SET '+','.join(fields)+'WHERE ID_admin = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_admin(self, ID_admin):
        try:
            sql = 'DELETE FROM admins WHERE ID_admin = %s'
            vals = (ID_admin,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """Movies Methods"""

    def create_movie(self, title, gender, clasification, director, actors, synopsis, release, language, subtitles, m_format):
        try:
            sql = 'INSERT INTO movies (`m_title`, `m_gender`, `m_clasification`, `m_director`, `m_actors`, `m_synopsis`, `m_release_date`, `m_language`, `m_subtitles`, `m_format`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            vals = (title, gender, clasification, director, actors, synopsis, release, language, subtitles, m_format)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_movie(self, title):
        try:
            sql = "SELECT * FROM movies WHERE m_title = %s"
            vals = (title,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_movie_id(self, ID_movie):
        try:
            sql = "SELECT * FROM movies WHERE ID_movie = %s"
            vals = (ID_movie,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_movies(self):
        try:
            sql = 'SELECT * FROM movies'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
        
    def read_movies_language(self, language):
        try:
            sql = 'SELECT * FROM movies WHERE m_language = %s'
            vals = (language,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
        
    def read_movies_format(self, format):
        try:
            sql = 'SELECT * FROM movies WHERE m_format = %s'
            vals = (format,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movies_hour(self, hour):
        try:
            sql = 'SELECT movies.m_title, movies.m_clasification, schedule_cinema.* FROM movies JOIN schedule_cinema ON movies.ID_movie = schedule_cinema.sc_movie AND schedule_cinema.sc_hour = %s'
            vals = (hour,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movies_clasification(self, clasification):
        try:
            sql = 'SELECT * FROM movies WHERE m_clasification = %s'
            vals = (clasification,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_movie(self, fields, vals):
        try:
            sql = 'UPDATE movies SET '+','.join(fields)+'WHERE ID_movie = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_movie(self, ID_movie):
        try:
            sql = 'DELETE FROM movies WHERE ID_movie = %s'
            vals = (ID_movie,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """Schedule Methods"""

    def create_schedule(self, ID_movie, hall, hour):
        try:
            sql = 'INSERT INTO schedule_cinema (`sc_movie`, `sc_hall`, `sc_hour`) VALUES(%s, %s, %s)'
            vals = (ID_movie, hall, hour)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            return err
    
    def read_a_schedule(self, hour):
        try:
            sql = 'SELECT schedule_cinema.*, movies.m_title FROM schedule_cinema JOIN movies ON schedule_cinema.sc_movie = movies.ID_movie AND schedule_cinema.sc_hour = %s'
            vals = (hour,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_schedule_id(self, ID_schedule):
        try:
            sql = 'SELECT schedule_cinema.*, movies.m_title FROM schedule_cinema JOIN movies ON schedule_cinema.sc_movie = movies.ID_movie AND schedule_cinema.ID_schedule = %s'
            vals = (ID_schedule,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_schedules(self):
        try:
            sql = 'SELECT schedule_cinema.*, movies.m_title FROM schedule_cinema JOIN movies ON schedule_cinema.sc_movie = movies.ID_movie'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_schedule_hall(self, hall):
        try:
            sql = 'SELECT schedule_cinema.*, movies.m_title FROM schedule_cinema JOIN movies ON schedule_cinema.sc_movie = movies.ID_movie JOIN halls ON schedule_cinema.sc_hall = halls.ID_hall AND schedule_cinema.sc_hall = %s'
            vals = (hall,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_schedule_movie(self, title):
        try:
            sql = 'SELECT schedule_cinema.*, movies.m_title FROM schedule_cinema JOIN movies ON schedule_cinema.sc_movie = movies.ID_movie AND movies.m_title = %s'
            vals = (title,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_schedule(self, fields, vals):
        try:
            sql = 'UPDATE schedule_cinema SET '+','.join(fields)+'WHERE ID_schedule = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_schedule(self, ID_schedule):
        try:
            sql = 'DELETE FROM schedule_cinema WHERE ID_schedule = %s'
            vals = (ID_schedule,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """Halls Methods"""

    def read_a_hall(self, hall):
        try:
            sql = 'SELECT * FROM halls WHERE ID_hall = %s'
            vals = (hall,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_halls(self):
        try:
            sql = 'SELECT * FROM halls'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_halls_seats(self, NoSeats):
        try:
            sql = 'SELECT * FROM halls WHERE h_no_seats = %s'
            vals = (NoSeats,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_hall_format(self, format_h):
        try:
            sql = 'SELECT * FROM halls WHERE h_format = %s'
            vals = (format_h,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_hall(self, fields, vals):
        try:
            sql = 'UPDATE halls SET '+','.join(fields)+'WHERE ID_hall = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """Seat Methods"""

    def read_a_seat(self, ID_seat, hall):
        try:
            sql = 'SELECT * FROM seat WHERE ID_seat = %s AND s_hall = %s'
            vals = (ID_seat, hall)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_seats(self):
        try:
            sql = 'SELECT * FROM seat'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_seats_hall(self, hall):
        try:
            sql = 'SELECT * FROM seat WHERE s_hall = %s'
            vals = (hall,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_seats_taken(self, schedule, date):
        try:
            sql = 'SELECT ticket.t_seat FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_schedule AND ticket.t_schedule = %s AND ticket.t_date = %s JOIN halls ON halls.ID_hall = schedule_cinema.sc_hall JOIN movies ON movies.ID_movie = schedule_cinema.sc_movie'
            vals = (schedule, date)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
        
    def update_seat(self, fields, vals):
        try:
            sql = 'UPDATE seat SET '+','.join(fields)+'WHERE ID_seat = %s AND s_hall = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """Ticket Methods"""

    def create_ticket(self, date, ID_schedule, seat):
        try:
            sql = 'INSERT INTO ticket (`t_date`, `t_schedule`, `t_seat`) VALUES(%s, %s, %s)'
            vals = (date, ID_schedule, seat)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            return err

    def read_hall_from_schedule(self, schedule):
        try:
            sql = 'SELECT schedule_cinema.sc_hall FROM schedule_cinema WHERE schedule_cinema.ID_schedule = %s'
            vals = (schedule,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_a_ticket(self, ID_ticket):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_seat, ticket.t_date, schedule_cinema.sc_hall, schedule_cinema.sc_hour, halls.h_format, halls.h_price, movies.m_title, movies.m_clasification, movies.m_language, movies.m_subtitles, movies.m_format FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_schedule AND ticket.ID_ticket = %s JOIN halls ON halls.ID_hall = schedule_cinema.sc_hall JOIN movies ON movies.ID_movie = schedule_cinema.sc_movie'
            vals = (ID_ticket,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_ticket_ssd(self, schedule, seat, date):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_seat, ticket.t_date, schedule_cinema.sc_hall, schedule_cinema.sc_hour, halls.h_format, halls.h_price, movies.m_title, movies.m_clasification, movies.m_language, movies.m_subtitles, movies.m_format FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_schedule AND ticket.t_date = %s AND ticket.t_schedule = %s AND ticket.t_seat = %s  JOIN halls ON halls.ID_hall = schedule_cinema.sc_hall JOIN movies ON movies.ID_movie = schedule_cinema.sc_movie'
            vals = (schedule, seat, date)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_tickets(self):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_seat, ticket.t_date, schedule_cinema.sc_hall, schedule_cinema.sc_hour, halls.h_format, halls.h_price, movies.m_title, movies.m_clasification, movies.m_language, movies.m_subtitles, movies.m_format FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_schedule JOIN halls ON halls.ID_hall = schedule_cinema.sc_hall JOIN movies ON movies.ID_movie = schedule_cinema.sc_movie'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_tickets_schedule(self, ID_schedule):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_seat, ticket.t_date, schedule_cinema.sc_hall, schedule_cinema.sc_hour, halls.h_format, halls.h_price, movies.m_title, movies.m_clasification, movies.m_language, movies.m_subtitles, movies.m_format FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_schedule AND ticket.t_schedule = %s JOIN halls ON halls.ID_hall = schedule_cinema.sc_hall JOIN movies ON movies.ID_movie = schedule_cinema.sc_movie'
            vals = (ID_schedule,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_tickets_date(self, date):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_seat, ticket.t_date, schedule_cinema.sc_hall, schedule_cinema.sc_hour, halls.h_format, halls.h_price, movies.m_title, movies.m_clasification, movies.m_language, movies.m_subtitles, movies.m_format FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_schedule AND ticket.t_date = %s JOIN halls ON halls.ID_hall = schedule_cinema.sc_hall JOIN movies ON movies.ID_movie = schedule_cinema.sc_movie'
            vals = (date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    def read_tickets_movie(self, ID_movie):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_seat, ticket.t_date, schedule_cinema.sc_hall, schedule_cinema.sc_hour, halls.h_format, halls.h_price, movies.m_title, movies.m_clasification, movies.m_language, movies.m_subtitles, movies.m_format FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_schedule JOIN movies ON movies.ID_movie = schedule_cinema.sc_movie AND movies.ID_movie = %s JOIN halls ON halls.ID_hall = schedule_cinema.sc_hall'
            vals = (ID_movie,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_tickets_hall(self, hall):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_seat, ticket.t_date, schedule_cinema.sc_hall, schedule_cinema.sc_hour, halls.h_format, halls.h_price, movies.m_title, movies.m_clasification, movies.m_language, movies.m_subtitles, movies.m_format FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_schedule AND schedule_cinema.sc_hall = %s JOIN movies ON movies.ID_movie = schedule_cinema.sc_movie JOIN halls ON halls.ID_hall = schedule_cinema.sc_hall'
            vals = (hall,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_ticket(self, fields, vals):
        try:
            sql = 'UPDATE ticket SET '+','.join(fields)+'WHERE ID_ticket = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_ticket(self, ID_ticket):
        try:
            sql = 'DELETE FROM ticket WHERE ID_ticket = %s'
            vals = (ID_ticket,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    
    

    