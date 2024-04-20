import re
from datetime import datetime

# Define the filename for README.md
README_FILE = "README.md"

# Parse commit messages and update the README.md file
def update_readme():
    # Read the content of README.md
    with open(README_FILE, "r") as file:
        readme_content = file.readlines()

    # Extract existing data from README.md
    table_data = []
    for line in readme_content:
        match = re.match(r"\|(\d{6})\s*\|(\d+)\s*\|(.+)\s*\|(.+)\s*\|(.+)\s*\|(.+)\s*\|", line)
        if match:
            table_data.append(match.groups())

    # Get the latest commit message and extract question number, solve status, and meeting date
    latest_commit_message = input()  # You need to capture the latest commit message here
    match = re.match(r"\[(\d+)\]\s*(.+)\((\d{6})\)", latest_commit_message)
    if match:
        question_number, solve_status, meeting_date = match.groups()
        meeting_date = datetime.strptime(meeting_date, "%y%m%d").strftime("%y%m%d")

        # Update table data with the latest commit
        for i, row in enumerate(table_data):
            if row[0] == meeting_date:
                table_data[i] = (row[0], row[1], *["풀이 완료" if idx == int(question_number) else cell for idx, cell in enumerate(row[2:], start=1)])

    # Update README.md with the updated table data
    with open(README_FILE, "w") as file:
        for row in table_data:
            file.write(f"|{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} |\n")

# Run the function to update README.md
update_readme()
