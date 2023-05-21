from PIL import Image
from serpapi import GoogleSearch
import requests
import os

SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

headers={'User-Agent': 'reachmujeebhere@gmail.com'}

def image_search(query):
    '''Image search function
    '''
    search_params = {
        'q': query,
        'tbm': 'isch',  # Specifies image search
        'api_key': SERPAPI_API_KEY
    }
    result = GoogleSearch(search_params).get_json()
    urls = [_['original'] for _ in result['images_results'] if _['original'].endswith(".jpg")]
    return urls[0]

def save_image_from_link(image_link, file_path):
    response = requests.get(image_link, stream=True, headers=headers)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image saved successfully at {file_path}")
    else:
        print("Error occurred while downloading the image.")
        
def resize_image(image_path, output_path, max_size):
    with Image.open(image_path) as image:
        # Calculate new dimensions while preserving aspect ratio
        width, height = image.size
        aspect_ratio = width / height
        if width > height:
            new_width = max_size
            new_height = int(max_size / aspect_ratio)
        else:
            new_width = int(max_size * aspect_ratio)
            new_height = max_size

        # Resize the image
        resized_image = image.resize((new_width, new_height))
        resized_image.save(output_path)
        print("Image resized and saved successfully.")

def get_image(query):
    file_path = f"{query.replace(' ','_')}.jpg"
    resized_image_path = f"{query.replace(' ','_')}_2.jpg"
    save_image_from_link(image_search(query), file_path)
    resize_image(file_path, resized_image_path, 200)
    return resized_image_path