def calculate_study_time(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return hours, remaining_minutes


def main():
    subject = input("Enter subject: ")
    minutes = int(input("Minutes studied: "))

    hours, remaining = calculate_study_time(minutes)

    print(f"\nSubject: {subject}")
    print(f"Study time: {hours} hours "
          f"and {remaining} minutes")


if __name__ == "__main__":
    main()