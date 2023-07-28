from requests.auth import HTTPBasicAuth


class Settings:
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    BaseUrl = "https://apitesting1.atlassian.net/rest/api/3"
    auth = HTTPBasicAuth("emukhlygin@gmail.com",
                         "ATATT3xFfGF0CszB8Au_rxNPejoJ3l-9T6zErdVgEYhS8dXo6uOC4locLk5khCzvwqU26RnSstrNKil9GZ47R"
                         + "-TuheahG4ftIEzLYodmxa"
                         + "FKFuvcaZE54rdKfAGHjamFa0YrBOrujbj36jqd-g5wuH8H53CEwNYgndvEVSajfM89KsDxJr2oRUE=636643D0")
