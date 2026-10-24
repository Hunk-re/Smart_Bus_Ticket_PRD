import streamlit as st

from config import MENU_OPTIONS
from data import load_starting_data
from view_routes import page_view_routes
from search_route import page_search_route
from book_ticket import page_book_ticket
from view_bookings import page_view_bookings
from cancel_booking import page_cancel_booking
from seat_availability import page_seat_availability
from report import page_report
from schedule import page_schedule
from exit_page import page_exit


def main():
    st.set_page_config(page_title="Smart Bus Reservation", page_icon="🚌")
    load_starting_data()

    st.title("🚌 SMART BUS RESERVATION SYSTEM")

    st.sidebar.title("Main Menu")
    choice = st.sidebar.radio("Choose an option:", MENU_OPTIONS)
    st.sidebar.caption("Data is stored in memory only.")

    if choice == MENU_OPTIONS[0]:
        page_view_routes()
    elif choice == MENU_OPTIONS[1]:
        page_search_route()
    elif choice == MENU_OPTIONS[2]:
        page_book_ticket()
    elif choice == MENU_OPTIONS[3]:
        page_view_bookings()
    elif choice == MENU_OPTIONS[4]:
        page_cancel_booking()
    elif choice == MENU_OPTIONS[5]:
        page_seat_availability()
    elif choice == MENU_OPTIONS[6]:
        page_report()
    elif choice == MENU_OPTIONS[7]:
        page_schedule()
    elif choice == MENU_OPTIONS[8]:
        page_exit()
    else:
        st.error("Unsupported choice. Please pick an option from the menu.")


main()
