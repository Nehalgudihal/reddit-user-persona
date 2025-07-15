import os
import praw
import re
from dotenv import load_dotenv
from urllib.parse import urlparse

# Load API keys
load_dotenv()
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Debug print
print("\n✅ Debug: Loaded environment variables:")
print("CLIENT ID:", REDDIT_CLIENT_ID)
print("CLIENT SECRET:", "[HIDDEN]" if REDDIT_CLIENT_SECRET else None)
print("USER AGENT:", REDDIT_USER_AGENT)

# Validate environment variables
if not all([REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT]):
    print("\n❌ ERROR: One or more Reddit environment variables are missing. Please check your .env file.")
    exit()

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def extract_username_from_url(url):
    return urlparse(url).path.split("/")[2]

def get_user_activity(username, limit=30):
    user = reddit.redditor(username)
    posts = []
    comments = []

    try:
        for submission in user.submissions.new(limit=limit):
            posts.append({
                "title": submission.title,
                "body": submission.selftext,
                "subreddit": submission.subreddit.display_name,
                "url": f"https://www.reddit.com{submission.permalink}"
            })

        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "subreddit": comment.subreddit.display_name,
                "url": f"https://www.reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"⚠️ Error fetching data: {e}")

    return posts, comments

def generate_prompt(posts, comments):
    examples = ""

    for p in posts:
        examples += f"[POST] Subreddit: r/{p['subreddit']}\nTitle: {p['title']}\nBody: {p['body'][:300]}\nLink: {p['url']}\n\n"
    for c in comments:
        examples += f"[COMMENT] Subreddit: r/{c['subreddit']}\nText: {c['body'][:300]}\nLink: {c['url']}\n\n"

    prompt = (
        "You're an expert social analyst. Based on the Reddit posts and comments below, "
        "generate a detailed user persona. Include traits like interests, tone, subreddit preferences, hobbies, and personality. "
        "Also, cite specific post or comment links for each trait.\n\n"
        f"{examples}"
        "\n---\n"
        "User Persona:"
    )

    return prompt

def save_prompt_to_file(username, prompt):
    filename = f"manual_prompt_{username}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"\n📋 Prompt saved to: {filename}")
    print("👉 Open this file, copy the entire content, and paste it into ChatGPT (chat.openai.com).")

def main():
    url = input("\n🔗 Enter Reddit profile URL (e.g., https://www.reddit.com/user/kojied/): ").strip()
    username = extract_username_from_url(url)
    print(f"\n🔍 Fetching data for: u/{username} ...")

    posts, comments = get_user_activity(username)
    print(f"📝 {len(posts)} posts and {len(comments)} comments fetched.")

    prompt = generate_prompt(posts, comments)
    save_prompt_to_file(username, prompt)

if __name__ == "__main__":
    main()
