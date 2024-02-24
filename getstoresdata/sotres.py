from requests import get
from search_data import searchData
from store_data import StoreData


class Store:
    
    def __init__(self, url: str, params: dict[str,str], headers:dict[str,str] ,end_count: int, start_count = 0) -> None:
        """
        Initializes the class with the provided url, parameters, headers, end_count, and optional start_count.
        
        Parameters:
            url (str): The URL for the request.
            params (dict): The parameters for the request.
            headers (dict): The headers for the request.
            end_count (int): The end count value.
            start_count (int, optional): The start count value (default is 0).
        Returns:
            None
        """
        self._url = url
        self._params = params
        self._headers = headers
        self._end_count = end_count
        self._start_count = start_count

    @property
    def store_id(self) -> list[int]:
        """
        This function returns a list of store IDs based on the provided start and end count parameters and the maximum result count. It uses the provided URL, headers, and parameters to make a GET request and retrieve the store IDs from the response items. The function then appends these IDs to the id_list and returns it at the end.
        """
        id_list: list[int] = []
        for skip_count in range(self._start_count, self._end_count, int(self._params["maxResultCount"])):
            self._params["skipCount"] = str(skip_count)
            response = get(f"{self._url}/search", headers=self._headers, params=self._params).json().get("items")
            for store_id in response:
                id_list.append(searchData(**store_id).id)
        return id_list

    def store_data(self) -> list[StoreData]:
        """
        Retrieve store data from the specified URLs and return a list of StoreData objects.
        """
        store_data_list: list[StoreData] = []
        for id in self.store_id:
            request = get(f"{self._url}/{id}", headers=self._headers, params=self._params).json()
            store_data_list.append(StoreData(**request))
        return store_data_list

