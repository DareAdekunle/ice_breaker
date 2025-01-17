import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrap_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from a LinkedIn profile,
    Manually scrape the information from a linkedin profile"""

    if mock == True:
        linkedin_profile_url = "https://gist.githubusercontent.com/DareAdekunle/997e4978958b67381efb381fcec98680/raw/e41001dd429afb3f1c651fb244665aa124f15854/oludare_adekunle.json"
        response = requests.get(linkedin_profile_url, timeout=10)

    else: 
        headers_dict = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        linkedin_profile_url = linkedin_profile_url

        response = requests.get(api_endpoint,
                                params={'url': linkedin_profile_url},
                                headers=headers_dict, 
                                timeout=10)
    
    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None, " ", "  ")
        and k not in ["people_also_viewed", "people_also_viewed_urls", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(
        scrap_linkedin_profile(
            linkedin_profile_url= "www.linkedin.com/in/oludare-adekunle", mock= False
        )
    )
