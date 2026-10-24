# Smart Bus Ticket Booking & Reservation System

A beginner-friendly bus reservation app built with **Python 3** and **Streamlit**.
It uses only Python fundamentals (lists, dictionaries, tuples, sets, loops,
conditions and functions). No classes, no lambdas, no database.

## Requirements
- Python 3.8 or newer
- Streamlit (`pip install streamlit`)

## How to run
```
streamlit run main.py
```
Your browser opens the app automatically.

## Project structure
```
smart_bus/
|-- main.py              Entry point: page setup, sidebar menu, sends user to a page
|-- config.py            Fixed values: CITIES tuple and MENU_OPTIONS list
|-- data.py              Starting routes, bookings list and booking-ID set
|-- helpers.py           Shared functions: money, seat_status, find_route,
|                        make_booking_id, build_route_rows, show_route_line
|-- views/               One file per menu option (page functions)
|   |-- view_routes.py
|   |-- search_route.py
|   |-- book_ticket.py
|   |-- view_bookings.py
|   |-- cancel_booking.py
|   |-- seat_availability.py
|   |-- report.py
|   |-- schedule.py
|   `-- exit_page.py
|-- README.md
`-- test_cases.txt
```
The folder is called `views` (not `pages`) on purpose: Streamlit treats a
folder named `pages` as a separate multipage app.

## Menu guide (sidebar)
1. **View Available Routes** - table of routes; tick the box to hide full routes.
2. **Search for a Route** - search by route ID (e.g. R101) or city (e.g. hyderabad).
3. **Book a Ticket** - enter name, age, route ID and seats. Everything is validated first.
4. **View My Bookings** - all bookings, including cancelled ones.
5. **Cancel a Booking** - cancel a Confirmed booking by ID (only once).
6. **View Seat Availability** - available vs total seats and status per route.
7. **Generate Booking Report** - counts, reserved seats, confirmed revenue, fully booked routes.
8. **Route Schedule** - routes grouped by departure city.
9. **Exit** - goodbye message.

## Sample workflow
1. Open *Book a Ticket*: Ahmed, age 24, route R101, 2 seats -> Booking B1001, Rs. 2,400.
2. Open *View Seat Availability*: R101 now shows 38/40.
3. Open *Cancel a Booking*: enter B1001 -> seats restored (40/40).
4. Cancel B1001 again -> rejected (already cancelled).
5. Open *Generate Booking Report*: 1 booking, 0 confirmed, 1 cancelled, Rs. 0 revenue.

## Storage limitation
All data is kept in memory (`st.session_state`). It survives button clicks and
page switches, but it is **lost** when the app is stopped, or when the browser
tab is refreshed or closed. This is by design (no database).

## Notes for students (where each concept is used)
- **Tuple**: `CITIES`
- **Set**: `booking_ids` (prevents duplicate booking IDs)
- **List of dictionaries**: routes and bookings
- **enumerate()**: route and booking tables
- **for-else**: route search (`views/search_route.py`) and cancel booking (`views/cancel_booking.py`)
- **break / continue**: unique ID search, available-only filters
- **Nested loops**: report (routes -> bookings) and schedule (cities -> routes)
- **while**: `make_booking_id` (`helpers.py`) keeps going until the ID is unused
- Streamlit re-runs the script on every click, which acts as the "menu loop";
  the sidebar radio replaces `input()` and the Exit page replaces `break`.
