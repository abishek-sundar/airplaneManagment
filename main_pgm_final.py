#DISPLAYING OF TICKET DETAILS (ADMIN FLIGHT MENU) TO BE CLEANED
#TO CHANGE THE ADMIN MANAGER PASSWORD, PLEASE OPEN 'Admin Manager Password.ak' FROM THE ROOT FOLDER AND TYPE IN THE REQUIRED PASSWORD (ONLY NUMBERS)
#TRY MAKING PAYMENTS TOGETHER INSTEAD OF PER PASSENGER
#DO CTRL + F AND SEARCH FOR "#" TO VIEW THE COMMENT LINES IN THE CODE

'''FINAL PROGRAM'''

from pickle import *
from os import *
from random import *

'''FLIGHT CLASS'''

class flight():  

    def __init__(self):     #ADMIN MEMBER FUNCTIONS
        
        self.f_id = None
        self.f_seats_first = None
        self.f_seats_business = None
        self.f_seats_eco = None
        self.f_origin = None
        self.f_dest = None
        self.f_date = None
        self.f_base_fare = None
        self.f_time = None
        self.f_total_seats = None
        self.f_seats_first_avail = None
        self.f_seats_business_avail = None
        self.f_seats_eco_avail = None

    def input_flight_data(self):

        while True:     #ID
            
            self.f_id = raw_input ('Enter ID of flight ')
            print

            break

        while True:     #SEATS

            try:    # ALL THE BELOW "TRY" LOOPS ARE TO HANDLE EVENTS WHERE NO INPUT IS ENTERED
                
                self.f_seats_first = input ('Enter number of seats in First class (multiples of 2) ')
                print
                
                if self.f_seats_first % 2 != 0:
                    print 'Please enter valid input!'
                    print
                    continue

                self.f_seats_first_avail = self.f_seats_first
                
            except SyntaxError:

                print 'Please enter a valid input!'
                print
                continue

            try:

                self.f_seats_business = input ('Enter number of seats in Business class (multiples of 4) ')
                print

                if self.f_seats_business % 4 != 0:
                    print 'Please enter valid input!'
                    print
                    continue

                self.f_seats_business_avail = self.f_seats_business
                
            except SyntaxError:

                print 'Please enter a valid input!'
                print
                continue

            try:
                
                self.f_seats_eco = input ('Enter number of seats in Economy class (multiples of 6) ')
                print

                if self.f_seats_eco % 6 != 0:
                    print 'Please enter valid input!'
                    print
                    continue

                self.f_seats_eco_avail = self.f_seats_eco
                
            except SyntaxError:

                print 'Please enter a valid input!'
                print
                continue

            break

        
        while True:     #ORIGIN + DEST
            
            self.f_origin = raw_input ('Enter port of origin ')
            print

            if self.f_origin.isalpha() != True:
                print 'Port of origin must contain only alphabets!'
                print
                
                continue

            self.f_dest = raw_input ('Enter port of destination ')
            print

            if self.f_dest.isalpha() != True:
                print 'Port of destination must contain only alphabets!'
                print
                
                continue

            if self.f_origin == self.f_dest:
                print 'Port of origin and port of destination cannot be the same!'
                print

                continue

            else:
                break

        while True:     #DATE

            self.f_date = raw_input ('Enter date of departure(In this format ---> DD/MM/YY) ')
            print

            #CHECKING FORMAT OF DATE (begin)
            
            if self.f_date[0:2] <= '31' and self.f_date[2:3] == '/' and self.f_date[3:5] <= '12' and self.f_date[5:6] == '/' and len(self.f_date) == 8:
        
                break

            #CHECKING FORMAT OF DATE (end)
            
            else:

                print 'Please enter a valid date!'
                print

        while True:     #BASE FARE
            
            try:
                
                self.f_base_fare = input ('Enter base fare for one person ')
                print

            except SyntaxError:

                print 'Please enter a valid input!'
                print
                continue

            break
                
        while True:     #TIME
            
            self.f_time = raw_input ('Enter time of flight (In 24 hour format & HH:MM) ')
            print

            if self.f_time[0:2] <= '23' and self.f_time[3:5] <= '60' and self.f_time[2:3] == ':': #CHECKING IF TIME IS APPROPRIATE

                break

            else:
                print 'Please enter a valid time!'
                print
                

        self.calc_total_seats()     #FN. TO CALCULATE NO. OF SEATS
        
    def calc_total_seats(self):

        self.f_total_seats = self.f_seats_first + self.f_seats_business + self.f_seats_eco

    def display_flight_data(self):  #DISPLAY ALL FLIGHT DETAILS

        print self.f_id, '\t\t', self.f_origin, '\t\t', self.f_dest, '\t\t', self.f_base_fare, '\t\t', self.f_date, '\t\t', self.f_time, '\t\t', self.f_total_seats

        
'''ADMIN CLASS'''

class admin:

    def __init__(self):     #ADMIN MEMEBER FUNCTIONS

        self.a_id = None
        self.pword = None
        self.name = None

    def input_admin_data(self):     #TRY LOOPS ARE FOR SITUATIONS WHERE NO INPUT IS PROVIDED

        while True:     #ID

            try:
            
                self.a_id = raw_input ('Enter ID of new admin (This wil be your USER ID) ')
                print

            except SyntaxError:
                print 'Please enter a valid input!'
                print
                continue

            break

        while True:     #PASSWORD

            self.pword = raw_input ('Enter password (Minimum 5 characters) ')
            print

            if len(self.pword) < 5:
                print 'Password too short!'
                print
                
                continue

            else:
                break
            
        while True:     #NAME
            
            self.name = raw_input ('Enter name of admin (Format : FIRSTNAME LASTNAME) ')
            print
            
            break

        print

    def display_admin_data(self):   #DISPLAY ADMIN DETAILS

        print self.a_id, '\t\t', self.name, '\t\t', self.pword


'''BOOKING CLASS'''

class booking:

    def __init__(self):

        self.b_ref = int(str(randint(10000, 99999)) + str(randint(10000, 99999)))  #EXTENDED RANGE TO MINIMIZE CHANCES OF REPEATS
        self.b_flight = ''
        self.b_class = ''
        self.b_seat = ''
        self.b_time = ''
        self.b_from = ''
        self.b_to = ''
        self.b_date = ''
        self.b_name = ''
        self.b_total_cost = 0
        self.b_price = 0
        

    def display_ticket_details_admin(self):

        print self.b_ref, '\t ', self.b_name, '\t ', self.b_flight, '\t ', self.b_class, '\t ', self.b_from, '\t ', self.b_to, '\t ', self.b_date, '\t ', self.b_time
        print

    def display_ticket_details_user(self):

        print '-------------- PRINTING TICKET --------------'
        print
        print '='*32 , 'TICKET', '='*32
        print '      Flight Name : AK AIRLINES                        Date :', self.b_date 
        print '      Booking Reference :',self.b_ref
        print '      Flight ID :', self.b_flight   
        print '      Time of Departure :', self.b_time 
        print '      Name of passenger :', self.b_name
        print '      From :', self.b_from                                                                                                     
        print '      To :', self.b_to
        print '      Seat :', self.b_seat
        print '      Class :', self.b_class
        print '='*72
        print

'''SEAT CLASSES'''

class first_seating():

    def __init__(self):

        self.s_id = None
        self.s_first = None
        self.s_matrix_first = []

    def init_seat_data_first(self):

        self.s_matrix_first = [['-' for j in range(2)] for i in range(self.s_first/2)]

    def show_seat_data_first(self):

        l = self.s_matrix_first

        print ' \tA B'

        for i in range(self.s_first/2):

            print i+1, '\t',
            
            for j in range(2):

                print l[i][j], 

            print

class business_seating():

    def __init__(self):

        self.s_id = None
        self.s_business = None
        self.s_matrix_business = []

    def init_seat_data_business(self):

        self.s_matrix_business = [['-' for j in range(4)] for i in range(self.s_business/4)]

    def show_seat_data_business(self):

        l = self.s_matrix_business

        print ' \tA B C D'

        for i in range(self.s_business/4):

            print i+1, '\t',
            
            for j in range(4):

                print l[i][j], 

            print

class eco_seating():

    def __init__(self):

        self.s_id = None
        self.s_eco = None
        self.s_matrix_eco = []

    def init_seat_data_eco(self):

        self.s_matrix_eco = [['-' for j in range(6)] for i in range(self.s_eco/6)]

    def show_seat_data_eco(self):

        l = self.s_matrix_eco

        print ' \tA B C D E F'

        for i in range(self.s_eco/6):

            print i+1, '\t',
            
            for j in range(6):

                print l[i][j], 

            print    
    
'''MAIN PROGRAM'''

def main_menu():

    print '-------------- MAIN MENU --------------'
    print
    print ' 1 ---> ADMIN MENU '
    print ' 2 ---> USER MENU '
    print ' 3 ---> PROGRAM SETTINGS (FOR ADMIN MANAGERS ONLY) '
    print
    print ' 4 ---> Exit '
    print

    try:            

        c = input ('Enter choice ')
        print
        
    except SyntaxError:

        print
        print 'Please enter a valid input!'
        print

        main_menu()
        
    if c == 1:

        admin_menu()

    elif c == 2 :

        user_flight_menu()

    elif c == 3 :

        pass_input = raw_input('Enter password of admin manager ')  #TO ENSURE SECURITY OF DATA 
        print
        
        if pass_input == admin_manager_pword:        
        
            settings_menu()

        else:

            print
            print 'Unauthorized access!'
            print

            main_menu()

    elif c == 4:
        exit()

    else:
        print
        print 'Please enter a valid input!'
        print

        main_menu()
        
def admin_menu():

    print
    print '-------------- ADMIN MENU --------------'
    print
    print ' 1 ---> CREATE NEW ADMIN (Admin Manager password required) '
    print ' 2 ---> ADMIN LOGIN (For existing Admins) '
    print ' 3 ---> DISPLAY ALL ADMINS (Admin Manager password required) '
    print ' 4 ---> DELETE ADMIN (Admin Manager password required) '
    print ' 5 ---> MODIFY ADMIN DETAILS (Admin Manager password required) '
    print
    print ' 6 ---> BACK TO MAIN MENU '   
    print ' 7 ---> Exit '
    print

    try:            

        c = input ('Enter choice ')
        print

    except SyntaxError:

        print
        print 'Please enter a valid input!'
        print

        admin_menu()

    if c == 1:

        new_admin() 

    elif c == 2 :

        admin_login()   
        
    elif c == 3 :

        display_admin()

    elif c == 4:

        del_admin()     

    elif c == 5 :
        
        modify_admin()
        
    elif c == 6 :
        main_menu()

    elif c == 7 :
        exit()

    else:
        print
        print 'Please enter a valid input!'
        print

        admin_menu()

def user_flight_menu():

    print
    print '-------------- USER MENU --------------'
    print
    print ' 1 ---> MAKE A BOOKING '
    print ' 2 ---> CANCEL A BOOKING '
    print ' 3 ---> VIEW TICKET '
    print 
    print ' 4 ---> MAIN MENU '
    print ' 5 ---> Exit '
    print

    try:
        c = input ('Enter choice ')
        print

    except SyntaxError:

        print
        print 'Please enter a valid input!'
        print

        user_flight_menu()

    if c == 1:

        book_flight_menu()

    elif c == 2 :

        cancel_booking()    
        
    elif c == 3 :

        view_ticket()

    elif c == 4 :
        main_menu()

    elif c == 5:
        exit()

    else:
        print
        print 'Please enter a valid input!'
        print

        user_flight_menu()

def book_flight_menu():

    print '-------------- BOOKING MENU --------------'
    print
    print ' 1 ---> DISPLAY ALL FLIGHTS '
    print ' 2 ---> SEARCH VIA PORT OF ORIGIN '
    print ' 3 ---> SEARCH VIA PORT OF DESTINATION '
    print ' 4 ---> SEARCH VIA PORTS ORIGIN AND DESTINATION '
    print
    print ' 5 ---> BACK TO MAIN MENU '
    print ' 6 ---> Exit '
    print

    c = input ('Enter choice ')
    print

    if c == 1:

        book_flight_display_flights()
        
    elif c == 2 :

        book_flight_search_origin()
        
    elif c == 3 :

        book_flight_search_dest()

    elif c == 4:

        book_flight_search_ori_dest()
        
    elif c == 5 :

        main_menu()
        
    elif c == 6 :
        exit()
        
def new_admin():

    print
    print '-------------- NEW ADMIN --------------'
    print
    
    f = file('Admin Details.ak', 'ab')

    while True:

        try:
        
            master_key = raw_input('Enter password of Admin Manager (Hit "ENTER" to go back to Main Menu) ')  #TO PREVENT ILLICIT CREATION OF ADMINS
            print

            if master_key == admin_manager_pword:   

                add_admin = admin()
                add_admin.input_admin_data()

                dump(add_admin, f)

                print 'ADMIN CREATED!'
                print
                print 'You will be redirected to the "ADMIN MENU" page. Please use the above ID and password to login.'
                print

                f.close()
                admin_menu()

            else:

                print 'Please enter valid password!'
                print
                print '-------------- RESTARTING --------------'

                f.close()
                new_admin()

        except SyntaxError:

            print
            main_menu()
        

def admin_login():

    print
    print '-------------- ADMIN LOGIN --------------'
    print

    f = file('Admin Details.ak', 'rb')
    status = 0
    
    admin_id = raw_input ('Enter ID of Admin ')
    admin_pword = raw_input ('Enter password of Admin ')

    print

    try:
        while True:
            l = load(f)

            if l.a_id == admin_id and l.pword == admin_pword:

                status = 1

                print
                print 'LOGIN SUCCESSFUL!'
                print
                
                admin_flight_menu()                

    except EOFError:
        f.close()

    if status == 0:
        print 'ID and Passwords do not match!'
        print

        admin_login()

def display_admin():

    print
    print '-------------- ADMIN MANAGER LOGIN --------------'
    print

    f = file('Admin Details.ak', 'rb')

    while True:

        try:
            
            master_key = raw_input ('Enter password of Admin Manager (Hit "ENTER" to go back to Main Menu) ')
            print

            if master_key == admin_manager_pword:

                print 'ID \t\t NAME \t\t PASSWORD \t\t'
                print
                
                try:
                    while True:
                            
                        admin_disp = load(f)
                        admin_disp.display_admin_data()

                except EOFError:
                    f.close()

                print
                print '-------------- DISPLAYED ADMINS --------------'
                print

                admin_menu()

            else:
                print 'Please enter valid password!'
                print

                display_admin()

        except SyntaxError:

            print
            main_menu()
                    
def del_admin():

    f_a = file('Admin Details.ak', 'rb')
    

    print
    print '-------------- ADMIN MANAGER LOGIN --------------'
    print

    try:
        while True:
            
            master_key = raw_input('Enter password of Admin Manager (Hit "ENTER" to go back to Main Menu) ')
            print

            if master_key == admin_manager_pword:

                f_t = file('New file.ak', 'wb')
                
                del_id = input ('Enter ID of admin to be deleted ')
                print
                
                status = 0


                try:
                    while True:
                        s = load(f_a)


                        if s.a_id != del_id:
                            dump(s, f_t)


                        else:
                            status = 1


                except EOFError:

                    f_a.close()
                    f_t.close()


                remove('Admin Details.ak')
                rename('New file.ak', 'Admin Details.ak')

                if status == 1:

                    print '-------------- ADMIN DELETED --------------'
                    print
                    
                else:
                    print 'ADMIN ID NOT FOUND!'

                admin_menu()

            else:

                print 'Please enter valid password!'
                print
                print '-------------- RESTARTING --------------'

                f_a.close()
                f_t.close()
                
                del_admin()

    except SyntaxError:

        print
        main_menu()

def modify_admin():

    print
    print '-------------- ADMIN MANAGER LOGIN --------------'
    print

    try:
        
        master_key = raw_input ('Enter password of Admin Manager (Hit "ENTER" key to return to Main Menu) ')
        print


        if master_key == admin_manager_pword:


            f_a = file('Admin Details.ak', 'rb')
            f_t = file ('Temp.ak', 'wb')


            m_id = raw_input('Enter ID to modify ')
            print
            
            a = admin()
            
            print
            status = 0


            try:
                while True:


                    adm = load(f_a)


                    if adm.a_id == m_id:


                        status = 1
                        adm.input_admin_data()


                    dump(adm, f_t)


            except EOFError:
                
                f_a.close()
                f_t.close()


            remove('Admin Details.ak')
            rename('Temp.ak', 'Admin Details.ak')
            
            if status == 1:
                print 'ADMIN MODIFIED!'


            else:
                print 'ADMIN ID NOT FOUND!'


    except SyntaxError:


        print
        main_menu()

    admin_menu()
        
def admin_flight_menu():

    print '-------------- ADMIN FLIGHT MENU --------------'
    print
    print ' 1 ---> CREATE FLIGHT '
    print ' 2 ---> MODIFY FLIGHT '
    print ' 3 ---> DELETE FLIGHT '
    print ' 4 ---> DISPLAY FLIGHTS '
    print ' 5 ---> VIEW BOOKED TICKETS '
    print
    print ' 6 ---> BACK TO ADMIN MENU '
    print ' 7 ---> BACK TO MAIN MENU '
    print ' 8 ---> Exit '
    print

    try:   
        c = input ('Enter choice ')
        print

    except SyntaxError:

        print
        print 'Please enter a valid input!'
        print

        admin_flight_menu()
        
    if c == 1 :

        create_flight()     

    elif c == 2 :

        modify_flight()    

    elif c == 3 :

        del_flight()
        
    elif c == 4 :

        display_flight()

    elif c == 5 :

        display_tickets()
        
    elif c == 6 :

        admin_menu()
        
    elif c == 7 :

        main_menu()
        
    elif c == 8 :
        exit()

    else:
        print
        print 'Please enter a valid input!'
        print

        admin_flight_menu()

def display_tickets():

    f_b = file('Ticket Details.ak', 'rb')

    print '-------------- PRINTING BOOKED TICKETS --------------'
    print

    print 'REF. NO\t  NAME OF PASSENGER\t FLIGHT\t  CLASS\t  FROM\t  TO\t  DATE\t  TIME OF DEPARTURE'
    print

    try:
        while True:

            f_b_l = load(f_b)

            f_b_l.display_ticket_details_admin()

    except EOFError:

        print '-------------- BOOKED TICKETS PRINTED --------------'
        print
        
        f_b.close()

    admin_flight_menu()
    
def create_flight():

    print
    print '-------------- NEW FLIGHT --------------'
    print
    
    f = file('Flight Details.ak', 'ab')
    
    add_flight = flight()
    add_flight.input_flight_data()

    dump(add_flight, f)

    print 'FLIGHT CREATED!'
    print

    f.close()
    admin_flight_menu()

def display_flight():   #PRINTING TO BE CLEANED UP A LITTLE

    f = file('Flight Details.ak', 'rb')

    print
    print 'ID \t ORIGIN \t DESTINATION \t BASE FARE \t DATE OF DEPARTURE \t TIME OF DEPARTURE \t TOTAL SEATS'
    print
                
    try:
        while True:
                            
            flight_disp = load(f)
            flight_disp.display_flight_data()

    except EOFError:
        f.close()

    print
    print '-------------- DISPLAYED FLIGHTS --------------'
    print

    admin_flight_menu()

def modify_flight():

    f_a = file('Flight Details.ak', 'rb')
    f_t = file ('Temp.ak', 'wb')


    m_id = raw_input('Enter ID to modify ')
    
    print
    status = 0


    try:
        while True:


            flt = load(f_a)


            if flt.f_id == m_id:

                print '-------------- MODIFYING FLIGHT --------------'
                print
    
                status = 1
                flt.input_flight_data()

                dump(flt, f_t)

                break

    except EOFError:
                
        f_a.close()
        f_t.close()

    f_a.close()
    f_t.close()
    
    remove('Flight Details.ak')
    rename('Temp.ak', 'Flight Details.ak')
            
    if status == 1:
        print '-------------- FLIGHT MODIFIED --------------'
        print


    else:
        print 'FLIGHT ID NOT FOUND!'
        print


    admin_flight_menu()
        
def del_flight():

    f_a = file('Flight Details.ak', 'rb')
    f_t = file ('Temp.ak', 'wb')


    m_id = raw_input('Enter Flight ID to be deleted ')
    
    print
    status = 0


    try:
        while True:


            flt = load(f_a)


            if flt.f_id != m_id:
                dump(flt, f_t)
                
            else:
                status = 1

    except EOFError:
                
        f_a.close()
        f_t.close()


    remove('Flight Details.ak')
    rename('Temp.ak', 'Flight Details.ak')
            
    if status == 1:
        
        print '-------------- FLIGHT DELETED --------------'
        print


    else:
        print 'FLIGHT ID NOT FOUND!'
        print


    admin_flight_menu()      
    
def settings_menu():    

    print '-------------- PROGRAM SETTINGS --------------'
    print
    print ' 1 ---> CLEAR ADMIN DATA '
    print ' 2 ---> CLEAR FLIGHT DATA '
    print ' 3 ---> CLEAR BOOKING DATA '
    print ' 4 ---> CLEAR FIRST CLASS SEATING DATA '
    print ' 5 ---> CLEAR BUSINESS CLASS SEATING DATA '
    print ' 6 ---> CLEAR ECONOMY CLASS SEATING DATA '
    print ' 7 ---> CLEAR ALL DATA '
    print ' 8 ---> DELETE ALL FILES '
    print
    print ' 9 ---> BACK TO MAIN MENU '
    print ' 10 ---> Exit '
    print

    try:
        c = input ('Enter choice ')
        print

    except SyntaxError:

        print
        print 'Please enter a valid input!'
        print

        settings_menu()

    if c == 1:

        clear_adm_data()    

    elif c == 2:

        clear_flt_data()   

    elif c == 3:

        clear_ticket_data()

    elif c == 4:

        clear_first_class_data()

    elif c == 5:

        clear_business_class_data()

    elif c == 6:

        clear_eco_class_data()
        
    elif c == 7 :

        clear_data()
        
    elif c == 8 :

        delete_files()
        
    elif c == 9 :
        main_menu()

    elif c == 10:
        exit() 

    else:
        print
        print 'Please enter a valid input!'
        print

        settings_menu()
        
def clear_data():

    print
    print '-------------- ALL FILES CLEARED --------------'
    print
        
    f_a = file('Admin Details.ak', 'wb')    #ERASES ALL CONTENT IN THE RESPECTIVE FILES
    f_f = file('Flight Details.ak', 'wb')
    f_s_first = file('First Class Seat Details.ak', 'wb')
    f_s_business = file('Business Class Seat Details.ak', 'wb')
    f_s_eco = file('Economy Class Seat Details.ak', 'wb')
    f_t = file('Ticket Details.ak', 'wb')

    f_a.close()
    f_f.close()
    f_s_first.close()
    f_s_business.close()
    f_s_eco.close()
    f_t.close()
    
    settings_menu()

def delete_files():

    print
    print '-------------- ALL FILES DELETED --------------'
    print

    remove('Admin Details.ak')
    remove('Flight Details.ak')
    remove('Ticket Details.ak')
    remove('First Class Seat Details.ak')
    remove('Business Class Seat Details.ak')
    remove('Economy Class Seat Details.ak')
           
    settings_menu()

def clear_flt_data():

    print
    print '-------------- FLIGHT DETAILS CLEARED --------------'
    print
    
    f_f = file('Flight Details.ak', 'wb')
    f_f.close()

    settings_menu()

def clear_adm_data():

    print
    print '-------------- ADMIN DETAILS CLEARED --------------'
    print
    
    f_a = file('Admin Details.ak', 'wb')
    f_a.close()

    settings_menu()

def clear_ticket_data():

    print
    print '-------------- BOOKING DETAILS CLEARED --------------'
    print
    
    f_b = file('Ticket Details.ak', 'wb')
    f_b.close()

    settings_menu()

def clear_first_class_data():

    print
    print '-------------- FIRST CLASS SEATING DETAILS CLEARED --------------'
    print
    
    f_s = file('First Class Seat Details.ak', 'wb')
    f_s.close()

    settings_menu()

def clear_business_class_data():

    print
    print '-------------- BUSINESS CLASS SEATING DETAILS CLEARED --------------'
    print
    
    f_s = file('Business Class Seat Details.ak', 'wb')
    f_s.close()

    settings_menu()

def clear_eco_class_data():

    print
    print '-------------- ECONOMY DETAILS CLEARED --------------'
    print
    
    f_s = file('Economy Class Seat Details.ak', 'wb')
    f_s.close()

    settings_menu()

def book_flight_search_origin():

    f_f = file('Flight Details.ak', 'rb')

    search_ori = raw_input('Enter port of origin. Enter "0" to go back to USER MENU ')
    
    if search_ori != "0":

        print
        print 'ID \t ORIGIN \t DESTINATION \t BASE FARE \t DATE OF DEPARTURE \t TIME OF DEPARTURE \t TOTAL SEATS'
        print
        
        status = 0

        try:
            while True:

                f_f_l = load(f_f)

                if f_f_l.f_origin == search_ori:

                    f_f_l.display_flight_data()
                    
                    status = 1

        except EOFError:

            f_f.close()

        if status == 0:
            
            print 'Flight does not exist!'
            print

            book_flight_search_origin()

        else:
            
            book_flight_select_flight()

    else:
        user_flight_menu()
    
def book_flight_search_dest():

    f_f = file('Flight Details.ak', 'rb')

    search_dest = raw_input('Enter port of destination. Enter "0" to go back to USER MENU ')

    print
    print 'ID \t ORIGIN \t DESTINATION \t BASE FARE \t DATE OF DEPARTURE \t TIME OF DEPARTURE \t TOTAL SEATS'
    print
    
    if search_dest != "0":

        print
        print 'ID \t ORIGIN \t DESTINATION \t BASE FARE \t DATE OF DEPARTURE \t TIME OF DEPARTURE \t TOTAL SEATS'
        print
        
        status = 0

        try:
            while True:

                f_f_l = load(f_f)

                if f_f_l.f_dest == search_dest:

                    f_f_l.display_flight_data()
                    
                    status = 1

        except EOFError:

            f_f.close()

        if status == 0:
            
            print 'Flight does not exist!'
            print

            book_flight_search_dest()

        else:
            
            book_flight_select_flight()

    else:
        user_flight_menu()

def book_flight_search_ori_dest():

    f_f = file('Flight Details.ak', 'rb')

    search_ori = raw_input('Enter port of destination. Enter "0" to go back to USER MENU ') 
    
    if search_ori != "0":

        search_dest = raw_input('Enter port of destination ')

        print
        print 'ID \t ORIGIN \t DESTINATION \t BASE FARE \t DATE OF DEPARTURE \t TIME OF DEPARTURE \t TOTAL SEATS'
        print
        
        status = 0

        try:
            while True:

                f_f_l = load(f_f)

                if f_f_l.f_origin == search_ori and f_f_l.f_dest == search_dest:

                    f_f_l.display_flight_data()
                    
                    status = 1

        except EOFError:

            f_f.close()

        if status == 0:
            
            print 'Flight does not exist!'
            print

            book_flight_search_ori_dest()

        else:
            
            book_flight_select_flight()

    else:
        user_flight_menu()

def book_flight_display_flights():
    
    print
    print '-------------- AVAILABLE FLIGHTS --------------'
    print 

    f_f = file('Flight Details.ak', 'rb')

    print
    print 'ID \t ORIGIN \t DESTINATION \t BASE FARE \t DATE OF DEPARTURE \t TIME OF DEPARTURE \t TOTAL SEATS'
    print
                
    try:
        while True:
                            
            f_f_l = load(f_f)
            f_f_l.display_flight_data()     #DISPLAYING ALL AVAILABLE FLIGHTS

    except EOFError:
        f_f.close()

    print

    book_flight_select_flight()

def book_flight_select_flight():

    print
    print '-------------- SELECT FLIGHT TO BOOK --------------'
    print 

    f_f = file('Flight Details.ak', 'rb')

    global flt_id
    
    flt_id = raw_input('Enter ID of flight to book. Enter "0" to go back to USER MENU ')   #THIS ID REMAINS CONSTANT FOR ONE RUN OF THE PROGRAM

    if flt_id != "0":
        
        status = 0

        try:
            while True:

                f_f_l = load(f_f)

                if f_f_l.f_id == flt_id:

                    status = 1
                    break

        except EOFError:

            f_f.close()

        if status == 0:
            print 'Flight ID does not exist!'
            print

            book_flight_display_flights()

        else:

            f_f.close()
            
            book_flight_choose_class_menu()  #CHOOSING CLASS OF SEATING

    else:
        user_flight_menu()

def book_flight_choose_class_menu():

    print
    print '-------------- SELECT CLASS OF SEATING --------------'
    print
    
    print ' 1 ---> FIRST CLASS '
    print ' 2 ---> BUSINESS CLASS '
    print ' 3 ---> ECONOMY CLASS '
    print
    print ' 4 ---> BACK TO USER MENU '
    print ' 5 ---> Exit '
    print

    try:
        c = input ('Enter choice ')
        print

    except SyntaxError:

        print
        print 'Please enter a valid input!'
        print

        book_flight_choose_class_menu()
        
    if c == 1:

        book_flight_first_class_qty()  

    elif c == 2 :

        book_flight_business_class_qty()   
        
    elif c == 3 :

        book_flight_eco_class_qty()    
        
    elif c == 4 :

        user_flight_menu()

    elif c == 5 :
        exit()

    else:
        print
        print 'Please enter a valid input!'
        print

        book_flight_choose_class_menu()

def book_flight_first_class_qty():

    f_f = file('Flight Details.ak', 'rb+')

    try:
        while True:

            f_f_l = load(f_f)

            if f_f_l.f_id == flt_id:

                global first_seats_avail
                first_seats_avail = f_f_l.f_seats_first_avail

                print
                print 'Available Seats : ', first_seats_avail
                print

                global seats_req
                seats_req = input('Enter number of tickets to book. Enter "0" to go back to USER MENU (Please note : Payment is done individually) ')

                print

                if seats_req > first_seats_avail:

                    print seats_req, 'seats not available!'
                    print

                    print '-------------- RESTARTING --------------'

                    f_f.close()
                    
                    book_flight_first_class_qty()

                else:                    
                    
                    for i in range (seats_req):

                        book_flight_first_class_details(first_seats_avail)                     

                    break
    except EOFError:

        f_f.close()
        
    first_seats_avail -= seats_req

    f_f.close()

    f_f_new = file('Flight Details.ak', 'rb')
    f_temp = file('Temp.ak', 'wb')
    
    try:
        while True:

            f_f_l = load(f_f_new)

            if f_f_l.f_id == flt_id:

                f_f_l.f_seats_first_avail = first_seats_avail

            dump(f_f_l, f_temp)
        
    except EOFError:
            
        f_f_new.close()
        f_temp.close()

    f_f_new.close()
    f_temp.close()
    
    remove('Flight Details.ak')
    rename('Temp.ak', 'Flight Details.ak')
        
    user_flight_menu()

def book_flight_first_class_details(first_seats_avail):

    f_b = file('Ticket Details.ak', 'ab+')
    f_f = file('Flight Details.ak', 'rb+')

    try:
        while True:

            f_f_l = load(f_f)

            if f_f_l.f_id == flt_id:

                ticket = booking()

                ticket.b_flight = flt_id
                ticket.b_class = 'FIRST CLASS'
                ticket.b_time = f_f_l.f_time
                ticket.b_from = f_f_l.f_origin
                ticket.b_to = f_f_l.f_dest
                ticket.b_date = f_f_l.f_date
                ticket.b_name = raw_input('Enter name of passenger : ').upper()
                print

                global book_ref
                book_ref = ticket.b_ref

                ticket.b_total_cost = f_f_l.f_base_fare * 4

                dump(ticket, f_b)

                book_flight_first_class_matrix_init()
                book_flight_first_class_pay(ticket.b_total_cost)                

                break
            
    except EOFError:
        f_f.close()                    

    f_f.close()
    f_b.close()
    
    book_flight_first_class_update_seat_number()

def book_flight_first_class_update_seat_number():

    f_b = file('Ticket Details.ak', 'rb')
    f_temp = file('Temp69.ak', 'wb')

    while True:
        f_b_l = load(f_b)

        if f_b_l.b_ref == book_ref:

            f_b_l.b_seat = first_seat_number

            dump(f_b_l, f_temp)

            break

        else:
            dump(f_b_l, f_temp)

    f_b.close()
    f_temp.close()

    remove('Ticket Details.ak')
    rename('Temp69.ak', 'Ticket Details.ak')
    
def book_flight_first_class_matrix_init():

    f_s = file('First Class Seat Details.ak', 'ab+')
    f_f = file('Flight Details.ak', 'rb')

    while True:
        f_f_l = load(f_f)

        if f_f_l.f_id == flt_id:

            seat = first_seating()
            seat.s_id = flt_id
            seat.s_first = f_f_l.f_seats_first

            seat.init_seat_data_first()

            dump(seat,f_s)

            break

    f_s.close()
    f_f.close()

    book_flight_first_class_seat_matrix_modify()

def book_flight_first_class_seat_matrix_modify():   #ERROR HANDLING TO BE DONE

    f_s = file('First Class Seat Details.ak', 'rb')
    f_temp = file('Temp69.ak', 'wb')

    global first_seat_number
    first_seat_number = ''

    print
    print " '-' ---> Available ; 'o' ---> Selected ; 'x' ---> Occupied "
    print
    
    while True:
        f_s_l = load(f_s)

        if f_s_l.s_id == flt_id:

            l = f_s_l.s_matrix_first

            print ' \tA B'

            for i in range(f_s_l.s_first/2):

                print i+1, '\t',
            
                for j in range(2):

                    print l[i][j], 

                print

            while True:
                
                print
                col = raw_input('Enter column letter ')
                row = input('Enter row number ')
                print
                    
                if col in 'Aa' and row < ((f_s_l.s_first/2) + 1) and l[row-1][0] != 'x':

                    l[row-1][0] = 'o'
                    break
                    
                elif col in 'bB' and row < ((f_s_l.s_first/2) + 1) and l[row-1][1] != 'x':

                    l[row-1][1] = 'o'
                    break

                else:
                    
                    print 'Seat occupied/does not exist! Please choose another seat!'
                    print

                    continue
                
            print
            print ' \tA B'

            for i in range(f_s_l.s_first/2):

                print i+1, '\t',
            
                for j in range(2):

                    print l[i][j], 

                print

            print
            c = raw_input('Confirm this seat? (Y/N) ')
            print

            if c in "Nn":
                pass

            else:
                print ' \tA B'
                
                if col in 'aA':

                    l[row-1][0] = 'x'

                    first_seat_number = first_seat_number + str(row) + 'A'
                    
                elif col in 'bB':

                    l[row-1][1] = 'x'

                    first_seat_number = first_seat_number + str(row) + 'B'
                    
            for i in range(f_s_l.s_first/2):

                print i+1, '\t',

                for j in range(2):

                    print l[i][j],

                print

            f_s_l.s_matrix_first = l

            dump(f_s_l, f_temp)

            break

        else:
            dump(f_s_l, f_temp)
            
    f_s.close()
    f_temp.close()

    remove('First Class Seat Details.ak')
    rename('Temp69.ak', 'First Class Seat Details.ak')
    
def book_flight_first_class_pay(total_cost):

    f_b = file('Ticket Details.ak', 'rb+')
    
    print '-------------- PAYMENT --------------'
    print

    print 'Amount to be paid : AED', total_cost
    print

    while True:
        
        card_no = raw_input('Enter 16 digit credit card number ')
        print

        if len(card_no) != 16:
                
            print 'Please enter a valid card number!'
            print

            continue

        else:

            try:
                while True:

                    f_b_l = load(f_b)

                    if f_b_l.b_ref == book_ref:

                        f_b_l.b_card_no = card_no

                        break

            except EOFError:
                f_b.close()
                break

    while True:
        
        cvv_no = raw_input('Enter 3 digit CVV number ')
        print

        if len(cvv_no) != 3:

            print 'Please enter a valid CVV number!'
            print

            continue

        else:

            print 'Booking ticket number (Please save this number for future use) : ', book_ref
                
            print
            print '-------------- TICKET BOOKED --------------'
            print

            break

def book_flight_business_class_qty():

    f_f = file('Flight Details.ak',  'rb+')

    try:
        while True:

            f_f_l = load(f_f)

            if f_f_l.f_id == flt_id:

                global business_seats_avail
                business_seats_avail = f_f_l.f_seats_business_avail

                print
                print 'Available Seats : ', business_seats_avail
                print

                global seats_req
                seats_req = input('Enter number of tickets to book. Enter "0" to go back to USER MENU (Please note : Payment is done individually) ')

                print

                if seats_req > business_seats_avail:

                    print seats_req, 'seats not available!'
                    print

                    print '-------------- RESTARTING --------------'

                    f_f.close()
                    
                    book_flight_business_class_qty()

                else:                    
                    
                    for i in range (seats_req):

                        book_flight_business_class_details(business_seats_avail)                     

                    break
    except EOFError:

        f_f.close()
        
    business_seats_avail -= seats_req

    f_f.close()

    f_f_new = file('Flight Details.ak', 'rb')
    f_temp = file('Temp.ak', 'wb')
    
    try:
        while True:

            f_f_l = load(f_f_new)

            if f_f_l.f_id == flt_id:

                f_f_l.f_seats_business_avail = business_seats_avail

            dump(f_f_l, f_temp)
        
    except EOFError:
            
        f_f_new.close()
        f_temp.close()


            
    remove('Flight Details.ak')
    rename('Temp.ak', 'Flight Details.ak')
        
    user_flight_menu()

def book_flight_business_class_details(business_seats_avail):

    f_b = file('Ticket Details.ak', 'ab+')
    f_f = file('Flight Details.ak', 'rb+')

    try:
        while True:

            f_f_l = load(f_f)

            if f_f_l.f_id == flt_id:

                ticket = booking()

                ticket.b_flight = flt_id
                ticket.b_class = 'BUSINESS CLASS'
                ticket.b_time = f_f_l.f_time
                ticket.b_from = f_f_l.f_origin
                ticket.b_to = f_f_l.f_dest
                ticket.b_date = f_f_l.f_date
                ticket.b_name = raw_input('Enter name of passenger : ').upper()
                print

                global book_ref
                book_ref = ticket.b_ref

                ticket.b_total_cost = f_f_l.f_base_fare * 2

                dump(ticket, f_b)

                book_flight_business_class_matrix_init()
                book_flight_business_class_pay(ticket.b_total_cost)                

                break
            
    except EOFError:
        f_f.close()                    

    f_f.close()
    f_b.close()

    book_flight_business_class_update_seat_number()

def book_flight_business_class_update_seat_number():

    f_b = file('Ticket Details.ak', 'rb')
    f_temp = file('Temp69.ak', 'wb')

    while True:
        f_b_l = load(f_b)

        if f_b_l.b_ref == book_ref:

            f_b_l.b_seat = business_seat_number

            dump(f_b_l, f_temp)

            break

        else:
            dump(f_b_l, f_temp)

    f_b.close()
    f_temp.close()

    remove('Ticket Details.ak')
    rename('Temp69.ak', 'Ticket Details.ak')

def book_flight_business_class_matrix_init():

    f_s = file('Business Class Seat Details.ak', 'ab+')
    f_f = file('Flight Details.ak', 'rb')

    while True:
        f_f_l = load(f_f)

        if f_f_l.f_id == flt_id:

            seat = business_seating()
            seat.s_id = flt_id
            seat.s_business = f_f_l.f_seats_business

            seat.init_seat_data_business()

            dump(seat,f_s)

            break

    f_s.close()
    f_f.close()

    book_flight_business_class_seat_matrix_modify()

def book_flight_business_class_seat_matrix_modify():   #ERROR HANDLING TO BE DONE

    f_s = file('Business Class Seat Details.ak', 'rb')
    f_temp = file('Temp69.ak', 'wb')

    global business_seat_number
    business_seat_number = ''

    print
    print " '-' ---> Available ; 'o' ---> Selected ; 'x' ---> Occupied "
    print
    
    while True:
        f_s_l = load(f_s)

        if f_s_l.s_id == flt_id:

            l = f_s_l.s_matrix_business

            print ' \tA B C D'

            for i in range(f_s_l.s_business/4):

                print i+1, '\t',
            
                for j in range(4):

                    print l[i][j], 

                print

            while True:
                
                print
                col = raw_input('Enter column letter ')
                row = input('Enter row number ')
                print
                    
                if col in 'Aa' and row < ((f_s_l.s_business)/4 + 1) and l[row-1][0] != 'x':

                    l[row-1][0] = 'o'
                    break
                    
                elif col in 'bB' and row < ((f_s_l.s_business)/4 + 1) and l[row-1][1] != 'x':

                    l[row-1][1] = 'o'
                    break

                elif col in 'cC' and row < ((f_s_l.s_business/4) + 1) and l[row-1][2] != 'x':

                    l[row-1][2] = 'o'
                    break
                
                elif col in 'dD' and row < ((f_s_l.s_business/4) + 1) and l[row-1][3] != 'x':

                    l[row-1][3] = 'o'
                    break

                else:

                    print 'Seat occupied/does not exist! Please choose another seat!'
                    print

                    continue
            print
            print ' \tA B C D'

            for i in range(f_s_l.s_business/4):

                print i+1, '\t',
            
                for j in range(4):

                    print l[i][j], 

                print

            print
            c = raw_input('Confirm this seat? (Y/N) ')
            print

            if c in "Nn":
                pass

            else:
                print ' \tA B C D'
                
                if col in 'aA':

                    l[row-1][0] = 'x'

                    business_seat_number = business_seat_number + str(row) + 'A'
                    
                elif col in 'bB':

                    l[row-1][1] = 'x'

                    business_seat_number = business_seat_number + str(row) + 'B'

                elif col in 'cC':

                    l[row-1][2] = 'x'

                    business_seat_number = business_seat_number + str(row) + 'C'

                elif col in 'dD':

                    l[row-1][3] = 'x'

                    business_seat_number = business_seat_number + str(row) + 'D'
            
            for i in range(f_s_l.s_business/4):

                print i+1, '\t',

                for j in range(4):

                    print l[i][j],

                print

            f_s_l.s_matrix_business = l

            dump(f_s_l, f_temp)

            break

        else:
            dump(f_s_l, f_temp)
            
    f_s.close()
    f_temp.close()

    remove('Business Class Seat Details.ak')
    rename('Temp69.ak', 'Business Class Seat Details.ak')

def book_flight_business_class_pay(total_cost):

    f_b = file('Ticket Details.ak', 'rb+')
    
    print '-------------- PAYMENT --------------'
    print

    print 'Amount to be paid : AED', total_cost
    print

    while True:
        
        card_no = raw_input('Enter 16 digit credit card number ')
        print

        if len(card_no) != 16:
                
            print 'Please enter a valid card number!'
            print

            continue

        else:

            try:
                while True:

                    f_b_l = load(f_b)

                    if f_b_l.b_ref == book_ref:

                        f_b_l.b_card_no = card_no

                        break

            except EOFError:
                f_b.close()
                break

    while True:
        
        cvv_no = raw_input('Enter 3 digit CVV number ')
        print

        if len(cvv_no) != 3:

            print 'Please enter a valid CVV number!'
            print

            continue

        else:

            print 'Booking ticket number(Please save this number for future use) : ', book_ref
                
            print
            print '-------------- TICKET BOOKED --------------'
            print

            break
        
def book_flight_eco_class_qty():

    f_f = file('Flight Details.ak',  'rb+')

    try:
        while True:

            f_f_l = load(f_f)

            if f_f_l.f_id == flt_id:

                global eco_seats_avail
                eco_seats_avail = f_f_l.f_seats_eco_avail

                print
                print 'Available Seats : ', eco_seats_avail
                print

                global seats_req
                seats_req = input('Enter number of tickets to book. Enter "0" to go back to USER MENU (Please note : Payment is done individually) ')

                print

                if seats_req > eco_seats_avail:

                    print seats_req, 'seats not available!'
                    print

                    print '-------------- RESTARTING --------------'

                    f_f.close()
                    
                    book_flight_eco_class_qty()

                else:                    
                    
                    for i in range (seats_req):

                        book_flight_eco_class_details(eco_seats_avail)                     

                    break
    except EOFError:

        f_f.close()
        
    eco_seats_avail -= seats_req

    f_f.close()

    f_f_new = file('Flight Details.ak', 'rb')
    f_temp = file('Temp.ak', 'wb')
    
    try:
        while True:

            f_f_l = load(f_f_new)

            if f_f_l.f_id == flt_id:

                f_f_l.f_seats_eco_avail = eco_seats_avail

            dump(f_f_l, f_temp)
        
    except EOFError:
            
        f_f_new.close()
        f_temp.close()
            
    remove('Flight Details.ak')
    rename('Temp.ak', 'Flight Details.ak')
        
    user_flight_menu()

def book_flight_eco_class_details(eco_seats_avail):

    f_b = file('Ticket Details.ak', 'ab+')
    f_f = file('Flight Details.ak', 'rb+')

    try:
        while True:

            f_f_l = load(f_f)

            if f_f_l.f_id == flt_id:

                ticket = booking()

                ticket.b_flight = flt_id
                ticket.b_class = 'ECONOMY CLASS'
                ticket.b_time = f_f_l.f_time
                ticket.b_from = f_f_l.f_origin
                ticket.b_to = f_f_l.f_dest
                ticket.b_date = f_f_l.f_date
                ticket.b_name = raw_input('Enter name of passenger : ').upper()
                print

                global book_ref
                book_ref = ticket.b_ref

                ticket.b_total_cost = f_f_l.f_base_fare

                dump(ticket, f_b)

                book_flight_eco_class_matrix_init()
                book_flight_eco_class_pay(ticket.b_total_cost)                

                break
            
    except EOFError:
        f_f.close()                    

    f_f.close()
    f_b.close()

    book_flight_eco_class_update_seat_number()

def book_flight_eco_class_update_seat_number():

    f_b = file('Ticket Details.ak', 'rb')
    f_temp = file('Temp69.ak', 'wb')

    while True:
        f_b_l = load(f_b)

        if f_b_l.b_ref == book_ref:

            f_b_l.b_seat = eco_seat_number

            dump(f_b_l, f_temp)

            break

        else:
            dump(f_b_l, f_temp)

    f_b.close()
    f_temp.close()

    remove('Ticket Details.ak')
    rename('Temp69.ak', 'Ticket Details.ak')
    
def book_flight_eco_class_matrix_init():

    f_s = file('Economy Class Seat Details.ak', 'ab+')
    f_f = file('Flight Details.ak', 'rb')

    print
    print " '-' ---> Available ; 'o' ---> Selected ; 'x' ---> Occupied "
    print

    while True:
        f_f_l = load(f_f)

        if f_f_l.f_id == flt_id:

            seat = eco_seating()
            seat.s_id = flt_id
            seat.s_eco = f_f_l.f_seats_eco

            seat.init_seat_data_eco()

            dump(seat,f_s)

            break

    f_s.close()
    f_f.close()

    book_flight_eco_class_seat_matrix_modify()

def book_flight_eco_class_seat_matrix_modify():   #ERROR HANDLING TO BE DONE

    f_s = file('Economy Class Seat Details.ak', 'rb')
    f_temp = file('Temp69.ak', 'wb')

    global eco_seat_number
    eco_seat_number = ''

    while True:
        f_s_l = load(f_s)

        if f_s_l.s_id == flt_id:

            l = f_s_l.s_matrix_eco

            print ' \tA B C D E F'

            for i in range(f_s_l.s_eco/6):

                print i+1, '\t',
            
                for j in range(6):

                    print l[i][j], 

                print

            while True:
                
                print
                col = raw_input('Enter column letter ')
                row = input('Enter row number ')
                print
                    
                if col in 'Aa' and row < ((f_s_l.s_eco/6) + 1) and l[row-1][0] != 'x':

                    l[row-1][0] = 'o'
                    break
                    
                elif col in 'bB' and row < ((f_s_l.s_eco/6) + 1) and l[row-1][1] != 'x':

                    l[row-1][1] = 'o'
                    break
                
                elif col in 'cC' and row < ((f_s_l.s_eco/6) + 1) and l[row-1][2] != 'x':

                    l[row-1][2] = 'o'
                    break
                
                elif col in 'dD' and row < ((f_s_l.s_eco/6) + 1) and l[row-1][3] != 'x':

                    l[row-1][3] = 'o'
                    break
                
                elif col in 'eE' and row < ((f_s_l.s_eco/6) + 1) and l[row-1][4] != 'x':

                    l[row-1][4] = 'o'
                    break
                
                elif col in 'fF' and row <= ((f_s_l.s_eco/6) + 1) and l[row-1][5] != 'x':

                    l[row-1][5] = 'o'
                    break

                else:

                    print 'Seat occupied/does not exist! Please choose another seat!'
                    print
                    
            print
            print ' \tA B C D E F'

            for i in range(f_s_l.s_eco/6):

                print i+1, '\t',
            
                for j in range(6):

                    print l[i][j], 

                print

            print
            c = raw_input('Confirm this seat? (Y/N) ')
            print

            if c in "Nn":
                pass

            else:
                print ' \tA B C D E F'
                
                if col in 'aA':

                    l[row-1][0] = 'x'

                    eco_seat_number = eco_seat_number + str(row) + 'A'
                    
                elif col in 'bB':

                    l[row-1][1] = 'x'

                    eco_seat_number = eco_seat_number + str(row) + 'B'

                elif col in 'cC':

                    l[row-1][2] = 'x'

                    eco_seat_number = eco_seat_number + str(row) + 'C'
                    
                elif col in 'dD':

                    l[row-1][3] = 'x'

                    eco_seat_number = eco_seat_number + str(row) + 'D'
                    
                elif col in 'eE':

                    l[row-1][4] = 'x'

                    eco_seat_number = eco_seat_number + str(row) + 'E'
                    
                elif col in 'fF':

                    l[row-1][5] = 'x'

                    eco_seat_number = eco_seat_number + str(row) + 'F'
                    
    
            for i in range(f_s_l.s_eco/6):

                print i+1, '\t',

                for j in range(6):

                    print l[i][j],

                print

            f_s_l.s_matrix_eco = l

            dump(f_s_l, f_temp)

            break

        else:
            dump(f_s_l, f_temp)
            
    f_s.close()
    f_temp.close()

    remove('Economy Class Seat Details.ak')
    rename('Temp69.ak', 'Economy Class Seat Details.ak')
    
def book_flight_eco_class_pay(total_cost):

    f_b = file('Ticket Details.ak', 'rb+')
    
    print '-------------- PAYMENT --------------'
    print

    print 'Amount to be paid : AED', total_cost
    print

    while True:
        
        card_no = raw_input('Enter 16 digit credit card number ')
        print

        if len(card_no) != 16:
                
            print 'Please enter a valid card number!'
            print

            continue

        else:

            try:
                while True:

                    f_b_l = load(f_b)

                    if f_b_l.b_ref == book_ref:

                        f_b_l.b_card_no = card_no

                        break

            except EOFError:
                f_b.close()
                break

    while True:
        
        cvv_no = raw_input('Enter 3 digit CVV number ')
        print

        if len(cvv_no) != 3:

            print 'Please enter a valid CVV number!'
            print

            continue

        else:

            print 'Booking ticket number(Please save this number for future use) : ', book_ref
                
            print
            print '-------------- TICKET BOOKED --------------'
            print

            break
        
def view_ticket():

    f_b = file('Ticket Details.ak', 'rb')

    ref = input('Enter booking reference : ')
    print
    
    status = 0
    
    try:
        while True:

            f_b_l = load(f_b)

            if ref == int(f_b_l.b_ref):     

                status = 1
                
                f_b_l.display_ticket_details_user()
                
    except EOFError:
        f_b.close()
    
    if status == 0:

        print 'Reference number not found!'
        print

    user_flight_menu()
    
def cancel_booking():   

    f_b = file('Ticket Details.ak', 'rb')
    f_temp = file('Temp.ak', 'wb')
    
    ref = raw_input('Enter booking reference : ')
    print

    status = 0

    try:
        while True:

            f_b_l = load(f_b)

            if f_b_l.b_ref != int(ref):
                
                dump(f_b_l, f_temp)                

            else:                
                status = 1
                book_flight_inc_seats(ref)
                
    except EOFError:
        
        f_b.close()
        f_temp.close()

    f_b.close()
    f_temp.close()

    remove('Ticket Details.ak')
    rename('Temp.ak', 'Ticket Details.ak')
    
    if status == 0:
        
        print 'Reference number not found!'
        print

    elif status == 1:

        print 'Ticket deleted!'
        print

    user_flight_menu()

def book_flight_inc_seats(booking_ref):
    
    f_b = file('Ticket Details.ak', 'rb')
    f_f = file('Flight Details.ak', 'rb')
    f_temp2 = file('Temp2.ak', 'wb')

    while True:

        f_b_l = load(f_b)

        if f_b_l.b_ref == int(booking_ref):

                if f_b_l.b_class == 'FIRST CLASS':

                    while True:
                        f_f_l = load(f_f)

                        if f_f_l.f_id == f_b_l.b_flight:
                    
                            f_f_l.f_seats_first_avail += 1
                            seats_update_first_get_row_col(f_f_l.f_id, f_b_l.b_ref, f_b_l.b_seat)

                            dump(f_f_l, f_temp2)
                            
                            break
                        
                        else:

                            dump(f_f_l, f_temp2)
                    break

                elif f_b_l.b_class == 'BUSINESS CLASS':

                    while True:

                        f_f_l = load(f_f)

                        if f_f_l.f_id == f_b_l.b_flight:

                            f_f_l.f_seats_business_avail += 1
                            seats_update_business_get_row_col(f_b_l.b_flight, f_b_l.b_ref, f_b_l.b_seat)

                            dump(f_f_l, f_temp2)
                            
                            break

                        else:

                            dump(f_f_l, f_temp2)
                    break
                
                elif f_b_l.b_class == 'ECONOMY CLASS':

                    while True:

                        f_f_l = load(f_f)

                        if f_f_l.f_id == f_b_l.b_flight:

                            f_f_l.f_seats_eco_avail += 1
                            seats_update_eco_get_row_col(f_b_l.b_flight, f_b_l.b_ref, f_b_l.b_seat)

                            dump(f_f_l, f_temp2)

                            break

                        else:

                            dump(f_f_l, f_temp2)
                    break

    f_b.close()
    f_f.close()
    f_temp2.close()

    remove('Flight Details.ak')
    rename('Temp2.ak', 'Flight Details.ak')

def seats_update_first_get_row_col(flight_id, ref, seat_no):

    row = ''
    col = ''

    for ch in seat_no:

        if ch.isalpha() != True:

            row = row + ch

        else:

            col = col + ch

    seats_update_first(flight_id, ref, seat_no, row, col)

def seats_update_business_get_row_col(flight_id, ref, seat_no):

    row = ''
    col = ''

    for ch in seat_no:

        if ch.isalpha() != True:

            row = row + ch

        else:

            col = col + ch

    seats_update_business(flight_id, ref, seat_no, row, col)

def seats_update_eco_get_row_col(flight_id, ref, seat_no):

    row = ''
    col = ''

    for ch in seat_no:

        if ch.isalpha() != True:

            row = row + ch

        else:

            col = col + ch

    seats_update_eco(flight_id, ref, seat_no, row, col)
    
def seats_update_first(flight_id, ref, seat_no, row, col):
    
    f_temp = file('Temp69.ak', 'wb')
    f_seat_first = file('First Class Seat Details.ak', 'rb')
    
    while True:
        
        f_seat_first_l = load(f_seat_first)

        if f_seat_first_l.s_id == flight_id:

            if col == 'A':

                f_seat_first_l.s_matrix_first[int(row)-1][0] = '-'

            elif col == 'B':

                f_seat_first_l.s_matrix_first[int(row)-1][1] = '-'

            dump(f_seat_first_l, f_temp)                

        else:

            dump(f_seat_first_l, f_temp)

        break

    f_temp.close()
    f_seat_first.close()
    
    remove('First Class Seat Details.ak')
    rename('Temp69.ak', 'First Class Seat Details.ak')

def seats_update_business(flight_id, ref, seat_no, row, col):
    
    f_temp = file('Temp69.ak', 'wb')
    f_seat_business = file('Business Class Seat Details.ak', 'rb')
    
    while True:
        
        f_seat_business_l = load(f_seat_business)

        if f_seat_business_l.s_id == flight_id:

            if col == 'A':

                f_seat_business_l.s_matrix_business[int(row)-1][0] = '-'

            elif col == 'B':

                f_seat_business_l.s_matrix_business[int(row)-1][1] = '-'

            elif col == 'C':

                f_seat_business_l.s_matrix_business[int(row)-1][2] = '-'

            elif col == 'D':

                f_seat_business_l.s_matrix_business[int(row)-1][3] = '-'

            dump(f_seat_business_l, f_temp)                

        else:

            dump(f_seat_business_l, f_temp)

        break

    f_temp.close()
    f_seat_business.close()
    
    remove('Business Class Seat Details.ak')
    rename('Temp69.ak', 'Business Class Seat Details.ak')

def seats_update_eco(flight_id, ref, seat_no, row, col):
    
    f_temp = file('Temp69.ak', 'wb')
    f_seat_eco = file('Economy Class Seat Details.ak', 'rb')
    
    while True:
        
        f_seat_eco_l = load(f_seat_eco)

        if f_seat_eco_l.s_id == flight_id:

            if col == 'A':

                f_seat_eco_l.s_matrix_eco[int(row)-1][0] = '-'

            elif col == 'B':

                f_seat_eco_l.s_matrix_eco[int(row)-1][1] = '-'

            elif col == 'C':

                f_seat_eco_l.s_matrix_eco[int(row)-1][2] = '-'

            elif col == 'D':

                f_seat_eco_l.s_matrix_eco[int(row)-1][3] = '-'

            elif col == 'E':

                f_seat_eco_l.s_matrix_eco[int(row)-1][4] = '-'

            elif col == 'F':

                f_seat_eco_l.s_matrix_eco[int(row)-1][5] = '-'

            dump(f_seat_eco_l, f_temp)                

        else:

            dump(f_seat_eco_l, f_temp)

        break

    f_temp.close()
    f_seat_eco.close()
    
    remove('Economy Class Seat Details.ak')
    rename('Temp69.ak', 'Economy Class Seat Details.ak') 

def admin_manager_pass():

    f_admin_manager_pword = file('Admin Manager Password.ak', 'r')

    global admin_manager_pword
    admin_manager_pword = f_admin_manager_pword.read()

def welcome_screen():

    print
    print 'Welcome to AK AIRLINES FLIGHT MANAGEMENT SOFTWARE (Version 2.0)'
    print
    print 'Please note, all ID and PASSWORD inputs are CASE-SENSITIVE!'
    print
    
def main():

    welcome_screen()
    
    admin_manager_pass()
    
    main_menu()
    
    
main()
