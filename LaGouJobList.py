import requests
import json



def get_json(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    job_data = requests.get(url,headers).content
    print(job_data)
    return job_data

def parse_json(job_data):
    job = json.loads(job_data.decode('utf-8'))
    job_list = job['content']['positionResult']['result']
    for _,job_detail in job_list:
        company_name = job_detail['companyFullName']
        city = job_detail['city']
        salary = job_detail['salary']
        workyear = job_detail['workYear']
        education = job_detail['education']
        job_name = job_detail['positionName']
        print('公司名：{company_name}\n城市：{city}\n职位：{job_name}\n工作年限：{workyear}\n薪资：{salary}\n教育水平：{education}'.format(
            company_name,city,job_name,workyear,salary,education
        ))

def main():
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    job_data = get_json(url)
    parse_json(job_data)


if __name__ == '__main__':
    main()