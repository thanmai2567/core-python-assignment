
def get_available_seats(total_seats, booked_seats):
    available_seats = []
    for seat in range(1, total_seats + 1):
        if seat not in booked_seats:
            available_seats.append(seat)
    return available_seats
def booking_seat(total_seats,booked_seats,seat_to_book):
    if seat_to_book < 1 or seat_to_book > total_seats:
        return "No seats Available"
    if seat_to_book in booked_seats:
        return f"seat {seat_to_book} is already booked"
    booked_seats.append(seat_to_book)
    return f"seat {seat_to_book} successfully booked"

def cancle_seat(booked_seats,seat_to_cancle):
    if seat_to_cancle not in booked_seats:
        return f"seat {seat_to_cancle} is not currently booked"
    booked_seats.remove(seat_to_cancle)
    return f"seat {seat_to_cancle} succesfully cancled"
total_seats = int(input())
booked_seats = list(map(int, input().split()))
seat_to_book = int(input())
seat_to_cancel = int(input())


booking_seat(total_seats, booked_seats, seat_to_book)
cancle_seat(booked_seats, seat_to_cancel)


available_seats = get_available_seats(total_seats, booked_seats)
print("Available seats:", available_seats)


