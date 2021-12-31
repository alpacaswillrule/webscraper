import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
 
results = soup.find(id="ResultsContainer") #find is for one element
job_elements = results.find_all("div", class_="card-content") #find all returns a iterable with all divs of that class

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
#the above searches through the headers, looks for the word python in text
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs #now need to find sibling elements, so we go up here 
]

#once we find the title elements
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    link = job_element.find("a", string = lambda text: "apply" in text.lower())["href"]
    linkhref = link
    print(f"Apply here: {link}\n")