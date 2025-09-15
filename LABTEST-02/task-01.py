import re

def extract_mentions_hashtags(text):
    # Regex to match @mentions and #hashtags, ignoring punctuation around them
    mention_pattern = r'(?<!\w)@([a-zA-Z0-9_]+)'
    hashtag_pattern = r'(?<!\w)#([a-zA-Z0-9_]+)'

    mentions = re.findall(mention_pattern, text, re.IGNORECASE)
    hashtags = re.findall(hashtag_pattern, text, re.IGNORECASE)

    # Convert to lowercase
    mentions = [m.lower() for m in mentions]
    hashtags = [h.lower() for h in hashtags]

    return mentions, hashtags

if __name__ == "__main__":
    user_input = input("Enter text: ")
    mentions, hashtags = extract_mentions_hashtags(user_input)
    print("Mentions:", mentions)
    print("Hashtags:", hashtags)