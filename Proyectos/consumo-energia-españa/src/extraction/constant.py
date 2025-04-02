# Constants para las API 
TOKEN_ESIOS = "5ae823d803902c7e499ab183df777ed5120c9ec43a5e19da7cab617f3d74de19" # Token for ESIOS API
API_KEY_AEMET = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJic2FuemdhbGxlZ29AZ21haWwuY29tIiwianRpIjoiNjI2ODFmOTktOWIxOS00ZjFhLWE4NWUtYjQ2ZWFhNTQyODI2IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3NDM1NDAxOTcsInVzZXJJZCI6IjYyNjgxZjk5LTliMTktNGYxYS1hODVlLWI0NmVhYTU0MjgyNiIsInJvbGUiOiIifQ.I8O4SXT0PlHBQv3EylVAoOtZ_LZ7NQlPOPySWedzvAE" # API key for AEMET
# Definició de constants per a la connexió a l'API ESIOS
HEADERS_EOSIS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Token {TOKEN_ESIOS}"
}
PARAMS_EOSIS = {
    "start_date": "2023-01-01T00:00:00Z",
    "end_date": "2023-12-31T23:59:59Z",
    "time_trunc": "hour"  
}
PARAMS_AEMET = {
    "api_key": API_KEY_AEMET
}
# URLS para las APIs
URL_ESIOS = "https://api.esios.ree.es/indicators/1001"
URL_AEMET = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2023-01-01T00:00:00UTC/fechafin/2023-12-31T23:59:59UTC/todasestaciones/"

