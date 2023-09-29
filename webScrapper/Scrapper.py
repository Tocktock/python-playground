from requests import get
from bs4 import BeautifulSoup
base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"

response = get(f'{base_url}{search_term}')

if response.status_code != 200:
    print(f"request is not successful: {response.status_code}")
else:
    soups = BeautifulSoup(response.text, "html.parser")
    jobs = soups.find_all('section', class_="jobs")
    results = []

    for job_section in jobs:
        job_post = job_section.find_all('li')
        job_post.pop(-1)
        for post in job_post:
            anchors = post.find_all("a")
            anchor = anchors[1]
            link = anchor["href"]
            company, kind, region = anchor.find_all("span", class_="company")
            title = anchor.find("span", class_="title")
            job_data = {
                company: company.string,
                kind: kind.string,
                region: region.string,
                title: title.string,
            }
            results.append(job_data)

    for result in results:
        print(result)



