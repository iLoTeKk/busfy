"""
This Module is Responsible for Communicating over the IETT API.
"""
import zeep
import json

BASE_URL = "https://api.ibb.gov.tr/iett"

WSDL_URLS = {
    "Announcement" : f"{BASE_URL}/UlasimDinamikVeri/Duyurular.asmx?wsdl",
    "Static" : f"{BASE_URL}/UlasimAnaVeri/HatDurakGuzergah.asmx?wsdl",
    "Schedule" : f"{BASE_URL}/UlasimAnaVeri/HatDurakGuzergah.asmx?wsdl",
    "Live_Vehicle" : f"{BASE_URL}/FiloDurum/SeferGerceklesme.asmx?wsdl",
    "Planned": f"{BASE_URL}/UlasimAnaVeri/PlanlananSeferSaati.asmx?wsdl",
}

clients = {}


def connect_client(service_name: str, timeout: int = 20) -> zeep.Client:
    """
    This function will connect to the IETT API, and return a handle for that
    """
    if service_name not in clients:
        transport = zeep.Transport(timeout=timeout, operation_timeout=timeout)
        clients[service_name] = zeep.Client(WSDL_URLS[service_name], transport=transport)
    return clients[service_name]


def send_request(service: str, operation: str, retries: int = 2) -> str:
    """
    this function will send a SOAP POST request to the IETT API, and will retrieve the response.
    it take:
        IETT URL
        SOAP Action
        body_xml
        timeout
    it returns the aqquired info from the IETT API
    """

def can_make_request(state, max_rate=95):
    """
    This function checks if we can make a request to the IETT API, according to the max_rate.
    """
    pass

def record_request(state):
    """
    This function will add the request counter in our state dictionary after every request that have been made.
    """
    pass


def fetch_buses_for_line(line_code: str, state: dict) -> list[dict]:
    """
    This function will take the bus number and the state dictionary and it'll
        Check if it can make request
        it make request to GetHatOtoKonum_json endpoint from IETT API
        record that request
    """
    pass

def fetch_all_stops() -> list[dict]:
    """
    this function will get all the stops available in the IETT API from GetDurak_json endpoint.
    it'll return them
    """
    pass

def fetch_all_lines() -> list[dict]:
    """
    this function will get all the lines available in the IETT API from GetHat_json endpoint.
    it'll return them
    """
    pass

def fetch_announcements() -> list[dict]:
    """
    Get all announcements from the IETT API, from GetDuyurular_json endpoint.
    """
    pass