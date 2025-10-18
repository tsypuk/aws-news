import json


def main():
    # Read the JSON file
    with open('../rss_config.json', 'r') as json_file:
        data = json.load(json_file)

    # Define the table header
    table_header = "| Name | Link |\n|------|------|\n"

    # Create the table content
    table_content = ""
    table_content2 = ""
    for entry in data:
        table_content += f"| {entry['name']} | {entry['link']} |\n"
        table_content2 += f"| {entry['name']} | https://tsypuk.github.io/aws-news/news/{entry['name'].lower().replace(' ', '_')}.json |\n"

    # Write the table to a Markdown file
    with open('output.md', 'w') as md_file:
        md_file.write(table_header)
        md_file.write(table_content)

    with open('output_json.md', 'w') as md_file:
        md_file.write(table_header)
        md_file.write(table_content2)

    'https://tsypuk.github.io/aws-news/news/architecture.json'


if __name__ == "__main__":
    main()
