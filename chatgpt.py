import requests
from bs4 import BeautifulSoup

def search_top_sites(query):
    # 検索エンジンのAPIを使用して上位のサイトを取得する処理
    # APIリクエストを送信し、上位のサイトのリストを取得する
    # この部分は実際の検索エンジンのAPIに応じて実装する必要がある

    # 仮置きの検索エンジンAPIのURLとパラメータ
    api_url = "https://example.com/search"
    params = {
        "q": query,
        "num_results": 100
    }

    # APIリクエストを送信して上位のサイトを取得
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        # レスポンスから上位のサイトのリストを取得
        top_sites = response.json()["top_sites"]
        return top_sites
    else:
        print("検索エンジンAPIからのレスポンスがエラーです。")
        return []

def scrape_company_list_from_sites(top_sites):
    company_list = []

    for site in top_sites:
        # 各サイトから情報をスクレイピングする処理
        url = site["url"]
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
        else:
            print(f"サイト {url} からのレスポンスがエラーです。")

    return company_list

# 検索クエリ
query = "企業 研修 プログラム"

# 検索エンジンのAPIを使用して上位のサイトを取得
top_sites = search_top_sites(query)

# 上位のサイトから情報をスクレイピングして会社リストを取得
company_list = scrape_company_list_from_sites(top_sites)

# 取得した会社リストの表示
for company in company_list:
    print("会社名:", company["company_name"])
    print("業種:", company["industry"])
    print("課題:", company["challenges"])
    print("連絡先:", company["contact"])
    print("-----------------------")
