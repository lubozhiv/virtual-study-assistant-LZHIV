"if __name__ == '__main__'"
subjects = {}

while True:
    subject = input("Enter subject name: ")
    if subject == "":
        break

    while True:
        minutes = input(f'Enter time allocated for {subject}:')
        if minutes == "":
            break
        if minutes.isdigit() and int(minutes) > 0:
            subjects[subject] = int(minutes)
            break
        else:
            print("Invalid input. Please enter a valid number.")


if subjects:
    sum_of_study_minutes = sum(subjects.values())
    number_of_breaks = sum_of_study_minutes // 45
    total_time_including_breaks = sum_of_study_minutes + (number_of_breaks * 15)

    print("Your study plan:")
    for subj in subjects:
        print(f'{subj.capitalize()}: {subjects[subj]} minutes')
    print(f'Total study time: {sum_of_study_minutes} minutes')
    print(f'Total time including breaks: {total_time_including_breaks} minutes')

    real_time_studied = int(input("Enter time spent studying: "))

    completeness = (real_time_studied / sum_of_study_minutes * 100)

    completeness = min(completeness, 100)

    print(f'You have completed {completeness:.2f}% of your planned study time.')


#  You can experiment here, it won’t be checked

