from bs4 import BeautifulSoup
from LoginLinked import Login
from time import sleep
# import json

session = Login()

print("Don't Abuse it, it won't work :), remember it's only a simple practice for some learning purposes.")
query = str(input("What job ur looking for ? "))
# query.replace(' ', '%20')

request = session.get(
    f'https://www.linkedin.com/jobs/search/?keywords={query}&origin=SWITCH_SEARCH_VERTICAL')

soup = BeautifulSoup(request.text, 'html.parser')
jobs_links = [i['href'] for i in soup.find_all(
    href=True, class_='base-card__full-link')]

jobs = []

print("It only scrapes 2 jobs, for the sake of learning.")
for job in jobs_links[:2]:
    new_req = session.get(job)
    # print(new_req.status_code)
    new_soup = BeautifulSoup(new_req.text, 'html.parser')

    jobData = {}

    try:
        title_of_job = new_soup.find(
            'h1', {'class': 'top-card-layout__title'}).get_text(strip=True)
        jobData['Title'] = title_of_job
    except:
        jobData['Title'] = 'NOT SCRAPED'

    Time_Released = new_soup.find(
        'span', {'class': 'posted-time-ago__text'}).get_text(strip=True)
    jobData['Time Released'] = Time_Released

    Number_Of_Applicants = new_soup.find_all(
        'span', {'class': 'tvm__text--low-emphasis'})
    jobData['Number Of Applicants'] = Number_Of_Applicants

    Job_Criteria = ' '.join(i.get_text(strip=True) for i in new_soup.find_all(
        'span', {'class': 'description__job-criteria-text'}))
    jobData['Job Criteria'] = Job_Criteria

    jobData['JobLink'] = job

    jobs.append(jobData)

    sleep(1.5)

with open('jobs.txt', 'a') as jobsFile:
    jobsFile.write(jobs)
    jobsFile.write(
        "-----------------------------\nThe Links of all the other jobs:")
    jobsFile.write(jobs_links[2:])
