import json
import feedparser

def main():
    file_path = '../rss_config.json'  # Replace with the actual path to your file
    with open(file_path, 'r') as file:
        data = json.load(file)

    for item in data:
        feed_url = item["link"]
        file_name = item["name"].lower().replace(" ", "_")

        # Parse the RSS feed
        feed = feedparser.parse(feed_url)

        # Extract titles and links
        entries = [{'title': entry.title, 'link': entry.link} for entry in feed.entries]

        # Write to JSON file
        with open(f'../../news/{file_name}.json', 'w') as json_file:
            json.dump(entries, json_file, indent=4)


if __name__ == "__main__":
    main()
