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

completeness = 0  # Initialize to a default value

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

    if completeness > 0:  # Only output if completeness is greater than 0
        print(f'You have completed {completeness:.2f}% of your planned study time.')

        from huggingface_hub import InferenceClient

        # Read the API key from the .env file
        with open('.env', 'r') as fp:
            HF_API_KEY = fp.read().strip()

        # Initialize the client with the API key
        client = InferenceClient(token=HF_API_KEY)

        # Define the input prompt
        prompt = """
               I have to prepare for my {subjects} exams. I've completed {completeness:.2f}% of my curriculum. My motivation should be:
               """.format(
            subjects=','.join(subjects.keys()),
            completeness=completeness
        )

        # Generate a response
        response = client.text_generation(
            prompt=prompt,
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            temperature=0.01,
            max_new_tokens=50,
            seed=42,
            return_full_text=True,
        )

        # Print the response
        print(response)