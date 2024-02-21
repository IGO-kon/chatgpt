import requests
from bs4 import BeautifulSoup

def scrape_company_list():
    company_list = []
    
    # スクレイピング対象のウェブサイトのURL
    url = "https://example.com/companies"
    
    # ページの取得
    response = requests.get(url)
    
    if response.status_code == 200:
        # BeautifulSoupを使ってHTMLを解析
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 会社情報が含まれる要素を特定し取得
        companies = soup.find_all("div", class_="company-info")
        
        for company in companies:
            # 会社名を取得
            company_name = company.find("h2", class_="company-name").text.strip()
            
            # 会社の業種や課題、連絡先などの情報を取得
            industry = company.find("p", class_="industry").text.strip()
            challenges = company.find("p", class_="challenges").text.strip()
            contact = company.find("p", class_="contact").text.strip()
            
            
            # 会社情報を辞書としてリストに追加
            company_info = {
                "company_name": company_name,
                "industry": industry,
                "challenges": challenges,
                "contact": contact
            }
            company_list.append(company_info)
    
    return company_list

# スクレイピング実行
company_list = scrape_company_list()

# 取得した会社リストの表示
for company in company_list:
    print("会社名:", company["company_name"])
    print("業種:", company["industry"])
    print("課題:", company["challenges"])
    print("連絡先:", company["contact"])
    print("-----------------------")
