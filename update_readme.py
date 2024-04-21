import re
import sys

# Dictionary to map GitHub IDs to display names
github_ids = {
    "minyouki": "김민영",
    "minji": "김민지",
    "kshjessica": "김서현",
    "chhaewxn": "송채원"
}

def update_readme(commit_message, commit_author, lines):
    # Extract information from the commit message
    match = re.match(r"\[(\d+)\]\s*(풀이\s*(중|완료))\((\d+)\)", commit_message)
    if not match:
        print("Invalid commit message format")
        return

    problem_number = match.group(1)
    solve_status = match.group(2)
    meeting_date = match.group(4)

    # Find the row corresponding to the meeting date and problem number
    row_index = None
    for i, line in enumerate(lines):
        if f"|{meeting_date}|{problem_number}" in line:
            row_index = i
            break

    # If both meeting date and problem number exist, update the row
    if meeting_date and problem_number:
        # If a row exists for the meeting date and problem number, update it
        if row_index is not None:
            # Update the solve status for the corresponding author
            lines[row_index] = re.sub(r"\|[^\|]*\|", f"|{solve_status if github_ids[commit_author] == commit_author else '-'}|", lines[row_index])
        # If there is no row for the meeting date and problem number, add a new row
        else:
            new_row = f"|{meeting_date}|{problem_number}|"
            for github_id in github_ids:
                new_row += f"{solve_status if github_id == commit_author else '-'}|"
            new_row += "\n"
            lines.append(new_row)

    return lines

# Read the commit message from command line arguments
commit_message = sys.argv[1]
commit_author = sys.argv[2]

# Read the existing contents of the README.md file
with open('README.md', 'r') as file:
    lines = file.readlines()

updated_lines = update_readme(commit_message, commit_author, lines)

# Write the updated contents back to the README.md file
with open('README.md', 'w') as file:
    file.writelines(updated_lines)
