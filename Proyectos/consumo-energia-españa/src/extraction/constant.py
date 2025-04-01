# Constants for the ESIOS API
TOKEN_ESIOS = "EL_TEU_TOKEN" # Token for ESIOS API
API_KEY_AEMET = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJic2FuemdhbGxlZ29AZ21haWwuY29tIiwianRpIjoiNjI2ODFmOTktOWIxOS00ZjFhLWE4NWUtYjQ2ZWFhNTQyODI2IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3NDM1NDAxOTcsInVzZXJJZCI6IjYyNjgxZjk5LTliMTktNGYxYS1hODVlLWI0NmVhYTU0MjgyNiIsInJvbGUiOiIifQ.I8O4SXT0PlHBQv3EylVAoOtZ_LZ7NQlPOPySWedzvAE" # API key for AEMET
# Definició de constants per a la connexió a l'API ESIOS
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Token {TOKEN_ESIOS}"
}
# URLS para las APIs
URL_ESIOS = "https://api.esios.ree.es/indicators/1001"
URL_AEMET = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2023-01-01T00:00:00UTC/fechafin/2023-12-31T23:59:59UTC/todasprov/{API_KEY_AEMET}"

# Definir el període de consulta
START_DATE = "2023-01-01T00:00:00Z"
END_DATE = "2023-12-31T23:59:59Z"
ESIOSREQUEST = f"{URL_ESIOS}?start_date={START_DATE}&end_date={END_DATE}"
