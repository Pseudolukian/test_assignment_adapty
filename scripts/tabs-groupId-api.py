import os
import re

# Define the directory path
DIRECTORY = "/Users/liudmilanemkova/Desktop/adapty-docs/versioned_docs/version-3.0"

# Define filename patterns to include
INCLUDE_PREFIXES = ("server-side-api", "ss", "web-api", "export-analytics-api")

# Regular expressions
TABS_PATTERN = re.compile(r'<Tabs(?:\s+groupId="[^"]*")?(\s+queryString)?>')


def update_tabs_in_file(file_path):
    """Updates the <Tabs> tag in the given markdown file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the <Tabs> occurrences ensuring groupId is set to "api-lang"
    updated_content = TABS_PATTERN.sub(r'<Tabs groupId="api-lang" queryString>', content)
    
    # Write back only if changes were made
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        print(f"Updated: {file_path}")
    else:
        print(f"No changes: {file_path}")


def process_md_files(directory):
    """Processes all .md files in the directory, including specific prefixes."""
    for filename in os.listdir(directory):
        if filename.endswith(".md") and filename.startswith(INCLUDE_PREFIXES):
            file_path = os.path.join(directory, filename)
            update_tabs_in_file(file_path)


if __name__ == "__main__":
    process_md_files(DIRECTORY)
