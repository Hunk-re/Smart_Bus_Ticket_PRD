"""Menu 3 - Book a Ticket."""

import streamlit as st
from helpers import build_route_rows, find_route, make_booking_id, money


def page_book_ticket():
    st.header("Book a Ticket")
    st.caption("Routes you can book:")
    st.table(build_route_rows(False))

    with st.form("booking_form"):
        name = st.text_input("Passenger name")
        age_text = st.text_input("Passenger age")
        route_text = st.text_input("Route ID (for example R101)")
        seats_text = st.text_input("Number of seats")
        submitted = st.form_submit_button("Book Ticket")

    if not submitted:
        return

    # ----- Step 1: validate everything BEFORE changing any data -----
    name = name.strip()
    age_text = age_text.strip()
    seats_text = seats_text.strip()

    if name == "":
        st.error("Passenger name cannot be empty.")
    elif not age_text.isdecimal() or int(age_text) == 0:
        st.error("Age must be a whole number greater than zero.")
    else:
        route = find_route(route_text)
        if route is None:
            st.error("Route ID not found. Please check the table above.")
        elif not seats_text.isdecimal() or int(seats_text) == 0:
            st.error("Number of seats must be a whole number greater than zero.")
        elif int(seats_text) > route["available_seats"]:
            st.error("Only " + str(route["available_seats"])
                     + " seat(s) are available on " + route["route_id"] + ".")
        else:
            # ----- Step 2: everything is valid, so now create the booking -----
            seats = int(seats_text)
            total_fare = route["ticket_price"] * seats
            booking_id = make_booking_id()

            booking = {
                "booking_id": booking_id,
                "passenger_name": name,
                "passenger_age": int(age_text),
                "route_id": route["route_id"],
                "seats": seats,
                "total_fare": total_fare,
                "status": "Confirmed",
            }
            st.session_state["bookings"].append(booking)
            st.session_state["booking_ids"].add(booking_id)
            route["available_seats"] = route["available_seats"] - seats

            st.success("Booking confirmed!")
            st.write("**Booking ID:** " + booking_id)
            st.write("**Passenger:** " + name)
            st.write("**Route:** " + route["route_id"] + " ("
                     + route["departure_city"] + " -> "
                     + route["destination_city"] + ")")
            st.write("**Seats booked:** " + str(seats))
            st.write("**Fare per seat:** " + money(route["ticket_price"]))
            st.write("**Total fare:** " + money(total_fare))
            st.write("**Status:** Confirmed")
