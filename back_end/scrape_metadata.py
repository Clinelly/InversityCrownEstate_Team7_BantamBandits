import requests
from bs4 import BeautifulSoup
import os

if __name__ == "__main__":
    url = "https://www.marinedataexchange.co.uk/details/TCE-2245/2003---2009-wave-hub-test-centre-development-wave-hub-hayle-environmental-assessment"
    # Step 1: Fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Step 2: Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        summary_paragraph = soup.find('pre', class_='summary-text')
        print(summary_paragraph)
        
        # Filter and collect download links
        download_links = []
        for link in download_links:
            href = link['href']
            # Check if the href attribute points to a downloadable file (example file extensions)
            if href.endswith(('.xml')):
                # Ensure the link is complete (prepend base URL if necessary)
                if not href.startswith('http'):
                    href = os.path.join(os.path.dirname(url), href)
                download_links.append(href)
        
        # Step 4: Print or save the download links
        if download_links:
            print("Download links found:")
            for download_link in download_links:
                print(download_link)
                # Optionally, you can download the files here
                # file_response = requests.get(download_link)
                # if file_response.status_code == 200:
                #     filename = os.path.basename(download_link)
                #     with open(filename, 'wb') as file:
                #         file.write(file_response.content)
                #     print(f"File {filename} downloaded successfully")
                # else:
                #     print(f"Failed to download the file from {download_link}. Status code: {file_response.status_code}")
        else:
            print("No download links found on the page.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    