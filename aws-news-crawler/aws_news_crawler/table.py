import json

def main():
    # Read the JSON file
    with open('../rss_config.json', 'r') as json_file:
        data = json.load(json_file)

    # Define the table header
    table_header = "| Name | Link |\n|------|------|\n"

    # Create the table content
    table_content = ""
    for entry in data:
        table_content += f"| {entry['name']} | {entry['link']} |\n"

    # Write the table to a Markdown file
    with open('output.md', 'w') as md_file:
        md_file.write(table_header)
        md_file.write(table_content)


if __name__ == "__main__":
    main()