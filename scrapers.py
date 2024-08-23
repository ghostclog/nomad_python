import requests
from bs4 import BeautifulSoup

# 변수들
BASE_URL1 = "https://berlinstartupjobs.com/skill-areas/"
BASE_URL2 = "https://web3.career/"


# 특정 url에서 구한 직업 결과를 담는 def
def berlin_find_jobs(keyword, job_list):
    url = BASE_URL1 + keyword
    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
    soup = BeautifulSoup(response.content, "html.parser")
    job_list_htmls = soup.find_all("div", class_="bjs-jlid__wrapper")
    for job in job_list_htmls:
        job_data = {
            "company_title":  # 회사명
            job.find("a", class_="bjs-jlid__b").text,
            "job_name":  # 직업 이름
            job.find("h4", class_="bjs-jlid__h").find("a").text,
            "bjs_description":  # 직업 설명
            job.find("div", class_="bjs-jlid__description").text.strip(),
            "job_link":  #링크
            job.find("h4", class_="bjs-jlid__h").find("a")["href"]
        }
        job_list.append(job_data)

    return job_list


def web3_find_jobs(keyword, job_list):
    url = BASE_URL2 + keyword
    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
    soup = BeautifulSoup(response.content, "html.parser")
    job_list_htmls = soup.find_all("tr", class_="table_row")

    for job in job_list_htmls:
        a_tags = job.find_all("a")

        job_name = a_tags[0].text.strip()
        company_title = a_tags[1].text.strip()
        link = a_tags[0]
        job_data = {
            "company_title":  # 회사명
            company_title,
            "job_name":  # 직업 이름
            job_name,
            "bjs_description":  # 직업 설명
            "",
            "job_link":  #링크
            BASE_URL2 + link["href"]
        }
        job_list.append(job_data)
    return job_list
