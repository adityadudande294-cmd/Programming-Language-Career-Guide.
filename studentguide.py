data = {

    "python": {
        "definition": "Python is a beginner-friendly programming language used in AI, Data Science and Web Development.",
        "difficulty": "Easy",
        "time": "2-4 Weeks",
        "jobs": "AI Engineer, Data Scientist, Data Analyst",
        "salary": "4 LPA - 25+ LPA"
    },

    "java": {
        "definition": "Java is an object-oriented programming language.",
        "difficulty": "Medium",
        "time": "4-6 Weeks",
        "jobs": "Java Developer, Android Developer",
        "salary": "4 LPA - 20+ LPA"
    },

    "c": {
        "definition": "C is a powerful programming language used in system programming.",
        "difficulty": "Medium",
        "time": "3-5 Weeks",
        "jobs": "Software Developer, Embedded Engineer",
        "salary": "3 LPA - 15+ LPA"
    },

    "html": {
        "definition": "HTML is used to create the structure of web pages.",
        "difficulty": "Very Easy",
        "time": "3-5 Days",
        "jobs": "Frontend Developer, Web Developer",
        "salary": "3 LPA - 10+ LPA"
    },

    "css": {
        "definition": "CSS is used to design web pages.",
        "difficulty": "Easy",
        "time": "1-2 Weeks",
        "jobs": "Frontend Developer, UI Designer",
        "salary": "3 LPA - 12+ LPA"
    }
}

print("=" * 50)
print("              PROGRAMMING LANGUAGE CAREER GUIDE")
print ("Created by : ADITYA DUDANDE ")
print("=" * 50)

print("\nWelcome!")
print("This project helps you learn about programming languages.\n")

while True:

    language = input("Enter a programming language: ").lower()

    if language in data:

        info = data[language]

        print("\n" + "-" * 40)
        print("Language :", language.upper())
        print("-" * 40)

        print("Definition :", info["definition"])
        print("Difficulty :", info["difficulty"])
        print("Time Needed :", info["time"])
        print("Career Options :", info["jobs"])
        print("Salary Range :", info["salary"])

    else:
        print("\nSorry! Information not available.")

    choice = input(
        "\nDo you want information about another language? (yes/no): "
    ).lower()

    if choice == "no":
        print("\nThank you for using my project.")
        print("Keep Learning and Keep Growing 🚀")
        break

print("\nProgram Ended Successfully.")