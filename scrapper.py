import requests
from bs4 import BeautifulSoup
import re
import os
from tqdm import tqdm
import fire

def download_images(url:str, min_width:int=1600, min_height:int=900, save_dir:str=None):
    """
    This script will scrape the images from the slidesgo theme provided by the url parameter, 
    and save the images with a resolution of min_width x min_height or higher (default is 1600 x 900) 
    in the directory save_dir (default is ./{name_of_the_theme})
    """
    if 'https://slidesgo.com/theme/' not in url:
        raise ValueError("The url should be a them from slidesgo. Ex : https://slidesgo.com/theme/clinical-case-in-neurology")
    name = url.replace('https://slidesgo.com/theme/', '')
    if save_dir is None:
        save_dir = f"./{name}"
    os.makedirs(save_dir, exist_ok=True)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    img_tags = soup.find_all("img")
    img_urls = [img.get('srcset').split(',') for img in img_tags if img.get('srcset') is not None]
    img_urls += [img.get('src').split(',') for img in img_tags if img.get('src') is not None]
    img_urls = sum(img_urls, [])

    for img_url in (pbar := tqdm(img_urls)):
        matches = re.findall(rf"(https://media\.slidesgo\.com/storage/\d+/responsive-images/(\d+).*___media_library_original_(\d+)_(\d+)\.jpg)", img_url)
        if len(matches) == 1:
            match = matches.pop()
            width = int(match[2])
            height = int(match[3])
            if width >= min_width and height >= min_height and name in match[0]:
                file_name = f"{match[1]}_{name}.jpg"
                file_path = os.path.join(save_dir, file_name)

                response = requests.get(match[0], stream=True)
                if response.status_code == 200:

                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    pbar.set_description(f"{file_name} saved to {save_dir}")
                else:
                    pbar.set_description(f"Error: Failed to download {file_name}")
        else:
            pbar.set_description("No match")

if __name__ == "__main__":
    fire.Fire(download_images)