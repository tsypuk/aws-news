import hashlib
import json
import os
from datetime import datetime, timezone

import feedparser


def main():
    file_path = './rss_config.json'  # Replace with the actual path to your file
    with open(file_path, 'r') as file:
        data = json.load(file)

    output_data = []

    for item in data:
        feed_url = item["link"]
        file_name = item["name"].lower().replace(" ", "_")
        file_path = f'../news/{file_name}.json'

        feed = feedparser.parse(feed_url)

        entries = [{'title': entry.title, 'link': entry.link} for entry in feed.entries]

        with open(f'../news/{file_name}.json', 'w') as json_file:
            json.dump(entries, json_file, indent=4)

        size = os.path.getsize(file_path)
        timestamp = os.path.getmtime(file_path)
        with open(file_path, 'rb') as f:
            content = f.read()
            sha256_hash = hashlib.sha256(content).hexdigest()

        file_info = {
            'name': file_name,
            'size': size,
            'timestamp': timestamp,
            'utc': datetime.fromtimestamp(timestamp, timezone.utc).isoformat(),
            'hash': sha256_hash,
            'path': f'https://blog.tsypuk.com/aws-news/news/{file_name}.json'
        }

        output_data.append(file_info)

    with open('../index.json', 'w') as output_file:
        json.dump(output_data, output_file, indent=4)

if __name__ == "__main__":
    main()
