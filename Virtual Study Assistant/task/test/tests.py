import os.path

from hstest import StageTest, dynamic_test, WrongAnswer, TestPassed, TestedProgram

class VirtualStudyAssistantTest(StageTest):

    @dynamic_test
    def test_single_subject(self):
        # Launch the program
        program = TestedProgram()
        output = program.start()

        if "Enter subject name:" not in output:
            raise WrongAnswer("Your input function should include 'Enter subject name:' string")

        output = program.execute("Math")
        if "Enter time allocated for" not in output:
            raise WrongAnswer("Your input function should include 'Enter time allocated for {subject}:' string")

        if "Enter time allocated for Math" not in output:
            raise WrongAnswer("Your input function should include 'Enter time allocated for {subject}:' string")

        output = program.execute("90")
        if "Enter subject name:" not in output:
            raise WrongAnswer("Your input should ask about next subject")

        program.execute('')

        raise TestPassed('Congrats!')

    @dynamic_test
    def test_multiple_subjects(self):
        # Launch the program
        program = TestedProgram()
        output = program.start()

        if "Enter subject name:" not in output:
            raise WrongAnswer("Your input function should include 'Enter subject name:' string")

        output = program.execute("Math")
        if "Enter time allocated for Math" not in output:
            raise WrongAnswer("Your input function should include 'Enter time allocated for {subject}:' string")

        output = program.execute("90")
        if "Enter subject name:" not in output:
            raise WrongAnswer("Your input should ask about next subject")

        output = program.execute("Science")
        if "Enter time allocated for Science" not in output:
            raise WrongAnswer("Your input function should include 'Enter time allocated for {subject}:' string")

        output = program.execute("120")
        if "Enter subject name:" not in output:
            raise WrongAnswer("Your input should ask about next subject")

        program.execute('')

        raise TestPassed('Congrats!')

    @dynamic_test
    def test_empty_input(self):
        # Launch the program
        program = TestedProgram()
        output = program.start()

        if "Enter subject name:" not in output:
            raise WrongAnswer("Your input function should include 'Enter subject name:' string")

        output = program.execute("")
        if len(output):
            raise WrongAnswer("The program should output nothing for no input.")

        raise TestPassed('Congrats!')

    @dynamic_test
    def test_formatted_output(self):
        # Launch the program
        program = TestedProgram()
        output = program.start()

        program.execute("Math")
        program.execute("90")
        program.execute("Science")
        program.execute("120")
        output = program.execute('')

        if "Your study plan:" not in output:
            raise WrongAnswer("The program should include 'Your study plan:' in the output.")

        if "Math: 90 minutes" not in output:
            raise WrongAnswer("The program should display the subject and its allocated time in the format '{subject}: {time} minutes'.")

        if "Science: 120 minutes" not in output:
            raise WrongAnswer("The program should display the subject and its allocated time in the format '{subject}: {time} minutes'.")

        if "Total study time: 210 minutes" not in output:
            raise WrongAnswer("The program should calculate and display the total study time.")

        if "Total time including breaks: 270 minutes" not in output:
            raise WrongAnswer("The program should calculate and display the total time including breaks.")

        raise TestPassed('Congrats!')

    @dynamic_test
    def test_progress_tracking(self):
        # Launch the program
        program = TestedProgram()
        output = program.start()

        # Input subjects and times
        program.execute("Math")
        program.execute("90")
        program.execute("Science")
        program.execute("120")
        program.execute('')

        # Simulate input of actual study time
        output = program.execute("150")

        if "You have completed 71.43% of your planned study time." not in output:
            raise WrongAnswer("The program should calculate and display the correct progress percentage.")

        raise TestPassed('Congrats!')

    @dynamic_test
    def test_exact_progress(self):
        # Launch the program
        program = TestedProgram()
        output = program.start()

        # Input subjects and times
        program.execute("Math")
        program.execute("90")
        program.execute("Science")
        program.execute("120")
        program.execute('')

        # Simulate input of actual study time
        output = program.execute("210")

        if "You have completed 100.00% of your planned study time." not in output:
            raise WrongAnswer("The program should calculate and display the correct progress percentage for exact completion.")

        raise TestPassed('Congrats!')

    @dynamic_test
    def test_over_progress(self):
        # Launch the program
        program = TestedProgram()
        output = program.start()

        # Input subjects and times
        program.execute("Math")
        program.execute("90")
        program.execute("Science")
        program.execute("120")
        program.execute('')

        # Simulate input of actual study time
        output = program.execute("250")

        if "You have completed 100.00% of your planned study time." not in output:
            raise WrongAnswer("The program should calculate and display the correct progress percentage for over-completion.")

        raise TestPassed('Congrats!')

    @dynamic_test
    def test_pep8(self):
        from pylint.lint import Run

        program = TestedProgram()
        program.start()

        script_path = os.path.join(
            program.executor.runnable.folder,
            program.executor.runnable.file
        )

        try:
            results = Run([script_path], exit=False)

            print("Information:", results.linter.generate_reports(verbose=True))

            if results.linter.stats.global_note < 6:
                raise WrongAnswer(
                    f"The file needs improvement to meet PEP-8 standard.\n" 
                    f"Your score {results.linter.stats.global_note:.2f}.\n"
                    f"Minimum passing grade: 6/10"
                )
            else:
                raise TestPassed
        except Exception as e:
            print(f"Error processing the file: {e}")
            raise TestPassed