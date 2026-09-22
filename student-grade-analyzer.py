# ============================================================
# STUDENT GRADE ANALYZER
# ============================================================

import csv
import math
import os
import statistics

import ipywidgets as widgets
import matplotlib.pyplot as plt

from IPython.display import clear_output, display


# ============================================================
# STEP 1 — CORE GRADE ANALYSIS
# ============================================================

def calculate_average(grades, coefficients):
    """Calculate the weighted average of grades."""

    if len(grades) != len(coefficients):
        raise ValueError("Grades and coefficients must have the same length.")

    if not grades:
        raise ValueError("No grades provided.")

    total = sum(
        grade * coefficient
        for grade, coefficient in zip(grades, coefficients)
    )

    return total / sum(coefficients)


def get_performance(average):
    """Return a performance level based on the average."""

    if average >= 16:
        return "Excellent"
    elif average >= 14:
        return "Very Good"
    elif average >= 12:
        return "Good"
    else:
        return "Needs Improvement"


def get_advice(grade):
    """Return personalized advice for a subject."""

    if grade >= 16:
        return "Excellent work! Keep it up."
    elif grade >= 14:
        return "Very good! Keep improving."
    elif grade >= 12:
        return "Good job! You can improve further."
    else:
        return "Practice more in this subject."


# ============================================================
# STEP 2 — CSV DATA STORAGE
# ============================================================

def save_to_csv(name, subjects, coefficients, grades, average):
    """Save student results to a CSV file."""

    filename = "student_grade_analyzer.csv"
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Student",
                "Subject",
                "Coefficient",
                "Grade",
                "Average"
            ])

        for subject, coefficient, grade in zip(
            subjects, coefficients, grades
        ):
            writer.writerow([
                name,
                subject,
                coefficient,
                grade,
                round(average, 2)
            ])

    return filename


# ============================================================
# STEP 3 — STATISTICS
# ============================================================

def calculate_statistics(grades):
    """Calculate basic statistics for the grades."""

    if not grades:
        raise ValueError("No grades provided.")

    return {
        "mean": statistics.mean(grades),
        "median": statistics.median(grades),
        "highest": max(grades),
        "lowest": min(grades)
    }


# ============================================================
# STEP 4 — GRADE VISUALIZATION
# ============================================================

def show_grade_chart(subjects, grades):
    """Display a bar chart of subject grades."""

    plt.figure(figsize=(8, 5))
    plt.bar(subjects, grades)
    plt.title("Student Grades")
    plt.xlabel("Subjects")
    plt.ylabel("Grade / 20")
    plt.ylim(0, 20)
    plt.tight_layout()
    plt.show()


# ============================================================
# STEP 5 — PROGRESS TRACKING
# ============================================================

def calculate_progress(previous_average, current_average):
    """Calculate the difference and percentage change."""

    difference = current_average - previous_average

    if previous_average != 0:
        percentage = (difference / previous_average) * 100
    else:
        percentage = 0

    return difference, percentage


# ============================================================
# STEP 6 — PROGRESS VISUALIZATION
# ============================================================

def show_progress_chart(previous_average, current_average):
    """Display previous vs current average."""

    tests = ["Previous", "Current"]
    averages = [previous_average, current_average]

    plt.figure(figsize=(7, 5))
    plt.plot(
        tests,
        averages,
        marker="o",
        linewidth=2
    )

    plt.title("Student Progress")
    plt.xlabel("Test")
    plt.ylabel("Average / 20")
    plt.ylim(0, 20)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


# ============================================================
# STEP 7 — GUI SETUP
# ============================================================

title = widgets.HTML(
    "<h3>STUDENT GRADE ANALYZER</h3>"
)

name_box = widgets.Text(
    description="Name:",
    placeholder="Enter your name"
)

subjects_box = widgets.IntText(
    description="Subjects:",
    value=2,
    min=1
)

previous_average_box = widgets.FloatText(
    description="Previous Avg:",
    value=0.0,
    min=0.0,
    max=20.0,
    step=0.1
)

start_button = widgets.Button(
    description="Start Analysis",
    button_style="success"
)

output = widgets.Output()
subject_container = widgets.VBox()
button_container = widgets.VBox()

main_box = widgets.VBox([
    title,
    name_box,
    subjects_box,
    previous_average_box,
    start_button,
    output,
    subject_container,
    button_container
])


# ============================================================
# STEP 8 — START ANALYSIS
# ============================================================

def start_analysis(button):
    """Create the subject input fields."""

    with output:
        clear_output()

        student_name = name_box.value.strip()
        number = subjects_box.value
        previous_average = previous_average_box.value

        if student_name == "":
            print("Please enter your name.")
            return

        if number < 1:
            print("Number of subjects must be at least 1.")
            return

        if not math.isfinite(previous_average):
            print("Previous average must be a valid number.")
            return

        if previous_average < 0 or previous_average > 20:
            print("Previous average must be between 0 and 20.")
            return

        print("===================================")
        print("       STUDENT GRADE ANALYZER")
        print("===================================")
        print()
        print(f"Welcome, {student_name}!")
        print()
        print(f"Number of subjects: {number}")
        print()

        subject_container.children = ()
        button_container.children = ()

        subject_inputs = []

        for i in range(number):
            subject_name = widgets.Text(
                description="Name:"
            )

            coefficient = widgets.FloatText(
                description="Coefficient:",
                value=5
            )

            grade = widgets.FloatText(
                description="Grade:",
                value=0
            )

            subject_box = widgets.VBox([
                widgets.HTML(f"<b>Subject {i + 1}</b>"),
                subject_name,
                coefficient,
                grade
            ])

            subject_inputs.append(
                (subject_name, coefficient, grade)
            )

            subject_container.children += (subject_box,)

        calculate_button = widgets.Button(
            description="Calculate Results",
            button_style="success"
        )

        result_output = widgets.Output()

        button_container.children = (
            calculate_button,
            result_output
        )

        def calculate(button):
            """Validate inputs and display all results."""

            with result_output:
                clear_output()

                subjects = []
                coefficients = []
                grades = []

                for i, data in enumerate(subject_inputs):

                    subject = data[0].value.strip()
                    coefficient = data[1].value
                    grade = data[2].value

                    if subject == "":
                        print(
                            f"Please enter the name of Subject {i + 1}."
                        )
                        return

                    if not math.isfinite(coefficient):
                        print(
                            f"Coefficient for {subject} "
                            "must be a valid number."
                        )
                        return

                    if coefficient <= 0:
                        print(
                            f"Coefficient for {subject} "
                            "must be positive."
                        )
                        return

                    if not math.isfinite(grade):
                        print(
                            f"Grade for {subject} "
                            "must be a valid number."
                        )
                        return

                    if grade < 0 or grade > 20:
                        print(
                            f"Grade for {subject} "
                            "must be between 0 and 20."
                        )
                        return

                    subjects.append(subject)
                    coefficients.append(coefficient)
                    grades.append(grade)

                # -----------------------------
                # Core analysis
                # -----------------------------

                average = calculate_average(
                    grades,
                    coefficients
                )

                performance = get_performance(average)

                highest = max(grades)
                lowest = min(grades)

                highest_index = grades.index(highest)
                lowest_index = grades.index(lowest)

                # -----------------------------
                # Results
                # -----------------------------

                print("===================================")
                print("          ANALYSIS RESULTS")
                print("===================================")
                print()

                print(f"Student: {student_name}")
                print(f"Average: {average:.2f}/20")
                print(f"Performance: {performance}")

                # -----------------------------
                # Subjects
                # -----------------------------

                print()
                print("--- Subjects ---")

                for i in range(len(subjects)):
                    print(
                        f"{subjects[i]}: "
                        f"{grades[i]:.2f}/20 "
                        f"(Coefficient: "
                        f"{coefficients[i]:.2f})"
                    )

                # -----------------------------
                # Highest / Lowest
                # -----------------------------

                print()
                print("--- Highest / Lowest ---")

                print(
                    f"Highest: "
                    f"{subjects[highest_index]} - "
                    f"{highest:.2f}/20"
                )

                print(
                    f"Lowest: "
                    f"{subjects[lowest_index]} - "
                    f"{lowest:.2f}/20"
                )

                # -----------------------------
                # Personalized advice
                # -----------------------------

                print()
                print("--- Personalized Advice ---")

                for subject, grade in zip(
                    subjects,
                    grades
                ):
                    print(
                        f"{subject}: "
                        f"{get_advice(grade)}"
                    )

                # -----------------------------
                # CSV storage
                # -----------------------------

                csv_file = save_to_csv(
                    student_name,
                    subjects,
                    coefficients,
                    grades,
                    average
                )

                print()
                print(f"Data saved to: {csv_file}")

                # -----------------------------
                # Statistics
                # -----------------------------

                stats = calculate_statistics(grades)

                print()
                print("--- Statistics ---")
                print(f"Mean: {stats['mean']:.2f}")
                print(f"Median: {stats['median']:.2f}")
                print(f"Highest: {stats['highest']:.2f}")
                print(f"Lowest: {stats['lowest']:.2f}")

                # -----------------------------
                # Ranking
                # -----------------------------

                print()
                print("--- Subject Ranking ---")

                ranking = sorted(
                    zip(subjects, grades),
                    key=lambda x: x[1],
                    reverse=True
                )

                for position, (subject, grade) in enumerate(
                    ranking,
                    1
                ):
                    print(
                        f"{position}. "
                        f"{subject}: {grade:.2f}"
                    )

                # -----------------------------
                # Progress tracking
                # -----------------------------

                difference, percentage = calculate_progress(
                    previous_average,
                    average
                )

                print()
                print("--- Progress Tracking ---")
                print(
                    f"Previous average: "
                    f"{previous_average:.2f}/20"
                )
                print(
                    f"Current average: "
                    f"{average:.2f}/20"
                )
                print(
                    f"Difference: "
                    f"{difference:.2f}"
                )
                print(
                    f"Percentage change: "
                    f"{percentage:.2f}%"
                )

                show_progress_chart(
                    previous_average,
                    average
                )

                # -----------------------------
                # Smart insights
                # -----------------------------

                print()
                print("===================================")
                print("          SMART INSIGHTS")
                print("===================================")

                if average >= 18:
                    print(
                        "Overall: Outstanding performance."
                    )
                elif average >= 16:
                    print(
                        "Overall: Excellent performance."
                    )
                elif average >= 14:
                    print(
                        "Overall: Very good performance."
                    )
                elif average >= 12:
                    print(
                        "Overall: Good performance."
                    )
                else:
                    print(
                        "Overall: More practice is needed."
                    )

                print()

                print(
                    f"Strongest subject: "
                    f"{subjects[highest_index]} "
                    f"({highest:.2f}/20)"
                )

                print(
                    f"Subject to improve: "
                    f"{subjects[lowest_index]} "
                    f"({lowest:.2f}/20)"
                )

                important_index = coefficients.index(
                    max(coefficients)
                )

                print(
                    f"Highest coefficient subject: "
                    f"{subjects[important_index]}"
                )

                if lowest < 12:
                    print(
                        f"Recommendation: Focus more on "
                        f"{subjects[lowest_index]}."
                    )
                elif lowest < 14:
                    print(
                        f"Recommendation: Review "
                        f"{subjects[lowest_index]} regularly."
                    )
                else:
                    print(
                        "Recommendation: Keep your "
                        "current study routine."
                    )

                # -----------------------------
                # Grade visualization
                # -----------------------------

                print()
                print("Showing grade visualization...")

                show_grade_chart(
                    subjects,
                    grades
                )

                # -----------------------------
                # Automated testing
                # -----------------------------

                print()
                print("===================================")
                print("           AUTOMATED TESTS")
                print("===================================")

                tests = [
                    calculate_average([20], [5]) == 20,
                    get_performance(18) == "Excellent",
                    get_performance(15) == "Very Good",
                    get_performance(13) == "Good",
                    get_performance(10) == "Needs Improvement"
                ]

                passed = sum(tests)

                for index, condition in enumerate(
                    tests,
                    1
                ):
                    result = "PASS" if condition else "FAIL"
                    print(
                        f"Test {index}: {result}"
                    )

                print()
                print(
                    f"Tests passed: "
                    f"{passed}/{len(tests)}"
                )

                # -----------------------------
                # Portfolio information
                # -----------------------------

                print()
                print("===================================")
                print("           PORTFOLIO")
                print("===================================")
                print()

                print(
                    "Project: Student Grade Analyzer"
                )
                print("Language: Python")
                print(
                    "Features: Grade Analysis, "
                    "Statistics, CSV Storage, "
                    "Visualization, Progress Tracking, "
                    "GUI, Ranking and Smart Insights"
                )

                print()
                print(
                    "Portfolio status: "
                    "READY FOR GITHUB"
                )

                print()
                print("===================================")
                print("       ANALYSIS COMPLETE")
                print("===================================")

        calculate_button.on_click(calculate)


# Connect the Start button to the analysis function.
start_button.on_click(start_analysis)


# Display the application.
display(main_box)

print("GUI READY.")
