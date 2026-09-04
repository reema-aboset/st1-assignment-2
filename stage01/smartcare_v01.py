appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    # Check for booking conflicts
    for appointment in appointments:
        if (appointment["practitioner"] == practitioner_name and
                appointment["time"] == appointment_time):
            raise ValueError("Practitioner already has an appointment at this time")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | "
            f"Practitioner: {appointment['practitioner']} | "
            f"Time: {appointment['time']}"
        )

print("Welcome to SmartCare: The Clinical Appointment Booking System!")

book_appointment('Alice Smith', 'Dr. Jane Roe', '2024-07-20 10:00 AM')

# This will now cause an error because Dr. Jane Roe is already booked
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 10:00 AM')

display_appointments()