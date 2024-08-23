from flask import Flask, render_template, request, redirect, send_file
from scrapers import berlin_find_jobs, web3_find_jobs
import csv

app = Flask(__name__)

# 검색 결과 저장용 캐시 변수
db = {}
DATA_LIST_DICT = ["company_title", "job_name", "bjs_description", "job_link"]


# 메인 페이지
@app.route("/")
def home():
    return render_template("main.html", keyword="선택되지 않았습니다.", data_list=[])


# 검색 후
@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    site = request.args.get("site")
    string = keyword + "_" + site
    data_list = []
    if (string in db):
        data_list = db[string]
    else:
        if (site == "All"):
            web3_keyword = keyword + "-jobs"
            data_list = web3_find_jobs(web3_keyword, data_list)
            data_list = berlin_find_jobs(keyword, data_list)
        elif (site == "berlinstartupjobs"):
            data_list = berlin_find_jobs(keyword, data_list)
        elif (site == "web3"):
            web3_keyword = keyword + "-jobs"
            data_list = web3_find_jobs(keyword, data_list)
        else:
            return redirect("/")
        db[string] = data_list

        # csv로 데이터 저장하는 부분
        csv_file_name = f"files/{string}.csv"
        with open(csv_file_name, mode='w', newline='',
                  encoding='utf-8') as file:
            # CSV 작성자 생성
            writer = csv.DictWriter(file, fieldnames=DATA_LIST_DICT)

            # 헤더 작성
            writer.writeheader()

            # 데이터 작성
            for data in data_list:
                writer.writerow(data)
    return render_template("main.html",
                           keyword=keyword,
                           site=site,
                           data_list=data_list)


# 다운로드
@app.route("/download")
def download():
    keyword = request.args.get("keyword")
    site = request.args.get("site")
    string = keyword + "_" + site
    if (string in db):
        return send_file(f"files/{string}.csv", as_attachment=True)
    else:
        return redirect(f"/search?keyword={keyword}&site={site}")


if __name__ == "__main__":
    app.run("0.0.0.0")

# 새로운 스크립퍼가 작동 안함.

# 내용 화면에 뿌려주기
