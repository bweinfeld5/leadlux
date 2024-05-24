import requests
import openpyxl

def get_facebook_posts(page_id, access_token):
    url = f"https://graph.facebook.com/v13.0/{page_id}/posts"
    params = {
        'access_token': access_token,
        'fields': 'message,created_time'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

def save_posts_to_excel(posts_data, filename):
    # Create a new Excel workbook and select the active worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Facebook Posts'
    
    # Write headers to the first row
    headers = ['Time', 'Message']
    sheet.append(headers)

    # Write post data to the worksheet
    if posts_data:
        for post in posts_data.get('data', []):
            time = post['created_time']
            message = post.get('message', 'No message')
            sheet.append([time, message])
    
    # Save the workbook
    workbook.save(filename)
    print(f"Data saved to {filename}")

# Replace with your Facebook page ID and access token
page_id = '1891279731302318'
access_token = 'EAANzmAQY8k8BO02bBDnpPFgnnR5PuXH3cLhJkrbItWFlvCbwQSQZBjBq7W79nloSQ3ZBHOgmSi6uPQ2ByncM28ZA8CZA0nCR5tPOOiWgiD2cTscuJX8Ks0oKxBEeF3GqAGVDG7gOUIxDm2e0w73b5WDOqp80MG2h2I42QGLk9ZBIcycmVqW4wiNL3m905eJmsDpupLVQP9ib5yFsEzEXEtTz3YIxZBx81iac8ZD'

# Retrieve posts from the Facebook page
posts_data = get_facebook_posts(page_id, access_token)

# Save the posts data to an Excel file
if posts_data:
    save_posts_to_excel(posts_data, 'facebook_posts.xlsx')
    