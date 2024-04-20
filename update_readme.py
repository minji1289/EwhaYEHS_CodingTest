import re


def update_readme(commit_message):
    # Extract information from the commit message
    match = re.match(r"\[(\d+)\]\s*풀이\s*완료\((\d+)\)", commit_message)
    if not match:
        print("Invalid commit message format")
        return

    problem_number = match.group(1)
    meeting_date = match.group(2)

    # Read the existing contents of the README.md file
    with open('README.md', 'r') as file:
        lines = file.readlines()

    # Find the row corresponding to the meeting date
    row_index = None
    for i, line in enumerate(lines):
        if meeting_date in line:
            row_index = i
            break

    # If the row doesn't exist, add it at the end
    if row_index is None:
        lines.append(f"|{meeting_date}| {problem_number} | | | | |\n")
    else:
        # Update the row with the problem number and your name
        lines[row_index] = re.sub(r"\|\s*$", f"| {problem_number} | 풀이 완료 | | | | |\n", lines[row_index])

    # Write the updated contents back to the README.md file
    with open('README.md', 'w') as file:
        file.writelines(lines)

# Example usage
commit_message = '[3758] 풀이 완료(240410)'
update_readme(commit_message)