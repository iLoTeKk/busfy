"""
This Module Help Solve the error that happens between WSDL and zeep library.
"""
import os
import requests
import re
from pathlib import Path

WSDL_DIR = Path(__file__).resolve().parent.parent / "wsdl"

BASE_URL = "https://api.ibb.gov.tr/iett"

ENDPOINTS ={
    "Announcement" : f"{BASE_URL}/UlasimDinamikVeri/Duyurular.asmx?wsdl",
    "Schedule" : f"{BASE_URL}/UlasimAnaVeri/HatDurakGuzergah.asmx?wsdl",
    "Live_Vehicle" : f"{BASE_URL}/FiloDurum/SeferGerceklesme.asmx?wsdl",
    "Planned": f"{BASE_URL}/UlasimAnaVeri/PlanlananSeferSaati.asmx?wsdl",
}

#regex is AI Generated.
def clean_wsdl(raw_xml: str) -> str:
    """
    Strips out phantom <soap:header> and <soap12:header> tags
    that reference undefined AuthHeader messages.
    """
    # 1. Remove multi-line soap headers
    cleaned = re.sub(r'<soap1?2?:header[^>]*>.*?</soap1?2?:header>','', raw_xml, flags=re.DOTALL)
    # 2. Remove self-closing soap headers
    cleaned = re.sub(r'<soap1?2?:header[^>]*/>', '', cleaned)
    return cleaned


def get_wsdl(service):
    """
    this function will get a clean fixed WSDL that zeep will accept, and write it to the system.
    after writing the valid WSDL it returns it path.
    """
    os.makedirs(WSDL_DIR, exist_ok=True)
    local_path = WSDL_DIR / f"{service}.wsdl"
    if os.path.exists(local_path):
        return str(local_path)
    url = ENDPOINTS[service]
    response = requests.get(url, timeout=20)
    fixed_xml = clean_wsdl(response.text)
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(fixed_xml)
    return str(local_path)
