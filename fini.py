import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def setup_driver():
    #configuringcChrome WebDriver options
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def classify_exhibitor(description, products_services):
    # Exhibitor categorization based on description and products/services
    categories = {
        "Energy Efficiency": ["energy efficiency", "energy saving", "fuel efficiency"],
        "Alternative Fuels": ["alternative fuel", "electrification", "battery", "lng"],
        "Low-Carbon Economy": ["low carbon", "carbon neutral", "decarbonization"],
        "Autonomous Shipping": ["autonomous", "unmanned", "self-navigating"],
        "Advanced Materials": ["material", "sensor", "composite", "3d printing"],
        "Marine Technologies": ["marine", "subsea", "underwater", "offshore"],
        "Ocean Research": ["research", "data analytics", "oceanography"],
        "Robotics": ["robot", "automation", "drone", "rov", "auv"],
        "Sustainability": ["sustainability", "eco-friendly", "carbon-neutral"]
    }
    # Combine description and products/services for classification
    text = (description + " " + products_services).lower()
    # Check for keywords in the combined text and categorize accordingly
    for category, keywords in categories.items():
        if any(keyword in text for keyword in keywords):
            return category
    # If no keywords match, return "Other"
    return "Other"

def extract_exhibitor_data(exhibitor, base_url):
    #Extract all data from an exhibitor
    data = {
        # default values for missing data
        'Name': "Not Available",
        'Stand': "Not Available",
        'About': "Not Available",
        'Products & Services': "Not Available",
        'Website': "Not Available",
        'Category': "Not Available"
    }

    # Extract company name
    try:
        name_element = exhibitor.find('h4', class_='company-name')
        data['Name'] = name_element.text.strip() if name_element else "Name Not Found"
        #incase of errors
    except Exception as e:
        print(f"Name extraction error: {str(e)}")
        data['Name'] = "Error: Name Extraction"

    # Extract stand number
    try:
        stand_element = exhibitor.find('p', style=lambda x: x and "color: #d6e342" in x.lower())
        if stand_element:
            data['Stand'] = stand_element.text.replace('Stand:', '').strip()
            #incase of errors
    except Exception as e:
        print(f"Stand extraction error for {data['Name']}: {str(e)}")

    # Extract company description
    try:
        profile_div = exhibitor.find('div', class_='company-profile')
        if profile_div:
            about_para = profile_div.find('p')
            data['About'] = about_para.text.strip() if about_para else "No description"
            #incase of errors
    except Exception as e:
        print(f"Description extraction error for {data['Name']}: {str(e)}")

    # Extract products and services
    try:
        products_div = exhibitor.find('div', class_='products-list')
        if products_div:
            service_field = products_div.find('div', class_='service-field')
            if service_field:
                data['Products & Services'] = service_field.text.strip()
                #incase of errors
    except Exception as e:
        print(f"Products extraction error for {data['Name']}: {str(e)}")

    # Extract website URL
    try:
        find_more_div = exhibitor.find('div', class_='find-out-more')
        if find_more_div:
            website_anchor = find_more_div.find('a')
            if website_anchor and 'href' in website_anchor.attrs:
                url = website_anchor['href']
                data['Website'] = url if url.startswith(('http://', 'https://')) else urljoin(base_url, url)
                #incase of errors
    except Exception as e:
        print(f"Website extraction error for {data['Name']}: {str(e)}")

    # Classify the exhibitor
    try:
        data['Category'] = classify_exhibitor(data['About'], data['Products & Services'])
        #incase of errors
    except Exception as e:
        print(f"Classification error for {data['Name']}: {str(e)}")

    return data

def main():
    # Scraping function
    print("Starting Ocean Business exhibitor scraping...")

    #setup the driver and URL
    driver = setup_driver()
    url = "https://exhibitormanual.oceanbusiness.com/exhibitor-list-search/"
    exhibitor_data = []
    print("Driver and URL setup complete.")

    ## Load the webpage and scroll to load all content
    try:
        print("Loading webpage...")
        driver.get(url)
        time.sleep(7)

        print("Scrolling to load all content...")
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        print("Parsing exhibitor data...")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        exhibitors = soup.find_all('div', class_='exhibitor-listing')
        print(f"Found {len(exhibitors)} exhibitors")

        for exhibitor in exhibitors:
            exhibitor_data.append(extract_exhibitor_data(exhibitor, url))

        if exhibitor_data:
            df = pd.DataFrame(exhibitor_data)
            output_file = 'ocean_business_exhibitors.xlsx'
            df.to_excel(output_file, index=False)
            print(f"\nSuccessfully extracted data for {len(exhibitor_data)} exhibitors")
            print(f"Data saved to {output_file}")
        else:
            print("No exhibitor data was extracted")

    except Exception as e:
        print(f"Fatal error during scraping: {str(e)}")
    finally:
        driver.quit()
        print("Browser session closed")

if __name__ == "__main__":
    main()