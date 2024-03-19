# from googlesearch import search

keyword = [
    "python dictionary",
    "python dictionary methods",
    "Python Flask",
    "Python From Scratch",
    "Python itertools",
]


# from googlesearch import search

# def search_and_save(keyword_list, output_file):
#     with open(output_file, 'w') as file:
#         for keyword in keyword_list:
#             file.write(f"{keyword}\n")
#             results = search(keyword, num=10, stop=15, pause=2)  # Adjust the number of results and pause time as needed
#             for i, result in enumerate(results, start=1):
#                 if "geeksforgeeks" in result:
#                     file.write(f"{i}. {result}\n")
#             file.write("\n")
#         print("j")

# if __name__ == "__main__":
#     keywords = keyword  # List of keywords to search
#     output_filename = "search_results.txt"  # Output file name

#     search_and_save(keywords, output_filename)
#     print("Search results saved successfully.")



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scrape_ubersuggest(keywords, output_file):
    # Initialize Selenium WebDriver (assuming you have ChromeDriver installed)
    driver = webdriver.Chrome()

    try:
        with open(output_file, 'w') as file:
            for keyword in keywords:
                # Open Google and search for the keyword
                driver.get("https://www.google.com")
                search_box = driver.find_element("name", "q")
                search_box.send_keys(keyword)
                search_box.send_keys(Keys.RETURN)

                # Wait for the page to load
                time.sleep(2)

                # Find the Ubersuggest table and extract data
                try:
                    ue_keyword_info_table = driver.find_element_by_id("ueKeywordInfoTable")
                    rows = ue_keyword_info_table.find_elements_by_css_selector(".keyword-info-table tbody tr")
                    keyword_info = []
                    for row in rows[:6]:  # Extracting data for the first 6 rows
                        cells = row.find_elements_by_css_selector("td")
                        row_data = [cell.text for cell in cells]
                        keyword_info.append(row_data)
                    
                    # Save the keyword, its rank, and table row data to file
                    file.write(f"Keyword: {keyword}\n")
                    file.write(f"Rank: {keywords.index(keyword) + 1}\n")
                    file.write("Table Data:\n")
                    for data in keyword_info:
                        file.write('\t'.join(data) + '\n')
                    file.write("\n")
                except:
                    file.write(f"No Ubersuggest data found for '{keyword}'\n")
    finally:
        driver.quit()

# Example usage:
keywords = keyword  # Replace with your list of keywords
output_file = "ubersuggest_data.txt"
scrape_ubersuggest(keywords, output_file)
print("Data scraped and saved to", output_file)
