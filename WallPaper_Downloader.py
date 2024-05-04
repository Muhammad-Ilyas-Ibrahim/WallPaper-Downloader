try:
    import asyncio
    import os
    import logging
    import requests
    from bs4 import BeautifulSoup
    import aiohttp
except ImportError as e:
    print("Installing dependencies...")
    import os
    os.system("pip install aiohttp requests bs4 logging")
    import asyncio
    import logging
    import requests
    from bs4 import BeautifulSoup
    
logging.basicConfig(filename='scrape.log', level=logging.INFO)
counter = 0
total_urls = 0    
     
async def download_image(image_url, file_path):
    global counter
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(image_url) as response:
                if response.status == 200:
                    with open(file_path, 'wb') as f:
                        f.write(await response.read())
                    counter += 1
                    print(f"Images Downloaded: {counter}/{total_urls}", end="\r")
                else:
                    logging.error(f"Image could not be found: {image_url}")
        except Exception as e:
            logging.error(f"Image could not be downloaded: {image_url} | Exception: {e}")

async def get_image_direct_url(image_url):
    global counter
    try:
        image_response = await asyncio.to_thread(requests.get, image_url)
        image_soup = BeautifulSoup(image_response.content, 'html.parser')

        section_found = image_soup.find(
            'section', {'itemscope': '', 'itemtype': 'http://schema.org/ImageObject'})

        image_found = section_found.find('img', {'id': 'show_img'})
        if image_found and 'src' in image_found.attrs:
            image_url = image_found['src']
            counter += 1
            print(f"URLs Scraped: {counter}", end="\r")
    except (requests.exceptions.Timeout, ConnectionError) as e:
        logging.error(f'Timeout or connection reset error when fetching URL {image_url}')
    except Exception as e:
        logging.error(f'Unexpected error {type(e)}: {e}')

    return image_url

async def main():
    # Make the HTTP GET request
    url = 'https://www.wallpaperflare.com/search?wallpaper='

    keyword = input("Enter the Keyword: ")
    print("\nNote: type n and hit enter if you need as much as possible")
    number = input("How much images do you want: ")
    if number != "n":
        number = int(number)
    keyword_splitted = keyword.split(' ')
    for index, i in enumerate(keyword_splitted):
        if index == len(keyword_splitted) - 1:
            url += i
        else:
            url += i + "+"

    response = await asyncio.to_thread(requests.get, url)

    soup = BeautifulSoup(response.content, 'html.parser')

    ul_element = soup.find(
        'ul', {'itemscope': '', 'itemtype': 'http://schema.org/ImageGallery'})

    # Iterate over each <li> element within the <ul>
    image_urls = []
    for index, li_element in enumerate(ul_element.find_all('li')):
        # Find the <img> element within the <li>
        img_element = li_element.find('a', {'itemprop': "url"})
        if img_element and 'href' in img_element.attrs:
            # Get the value of the 'data-src' attribute
            image_urls.append(img_element['href'] + "/download")
            if number != "n" and index + 1 == number: 
                break

    print("Scraping Direct Urls...")
    direct_urls = await asyncio.gather(*[get_image_direct_url(url) for url in image_urls])
    global total_urls
    global counter
    counter = 0
    total_urls = len(direct_urls)
    
    if not os.path.exists(f"Images/{keyword}"):
        os.makedirs(f"Images/{keyword}")
        
    if direct_urls:
        # Download paths with filenames
        download_paths = []
        for index, image_url in enumerate(direct_urls):
            file_name = image_url.split('/')[-1]
            file_name = file_name[:-37] + file_name[-4:]
            download_paths.append(f"Images/{keyword}/{file_name}")
        print("Downloading Images...")
        await asyncio.gather(*[download_image(url, path) for url, path in zip(direct_urls, download_paths)])
       
        print(f"{counter} images have been downloaded successfully!")
    else:
        print("No images found for the given keyword")
        
if __name__ == "__main__":
    asyncio.run(main())