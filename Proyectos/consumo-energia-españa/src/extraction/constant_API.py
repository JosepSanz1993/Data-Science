# Constants para las API 
TOKEN_ESIOS = "5ae823d803902c7e499ab183df777ed5120c9ec43a5e19da7cab617f3d74de19" # Token for ESIOS API
API_KEY_AEMET = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJic2FuemdhbGxlZ29AZ21haWwuY29tIiwianRpIjoiNjI2ODFmOTktOWIxOS00ZjFhLWE4NWUtYjQ2ZWFhNTQyODI2IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3NDM1NDAxOTcsInVzZXJJZCI6IjYyNjgxZjk5LTliMTktNGYxYS1hODVlLWI0NmVhYTU0MjgyNiIsInJvbGUiOiIifQ.I8O4SXT0PlHBQv3EylVAoOtZ_LZ7NQlPOPySWedzvAE" # API key for AEMET
# Definició de constants per a la connexió a l'API ESIOS
PARAMS_AEMET = {
    "api_key": API_KEY_AEMET
}
Headers_ESIOS = {
    'Accept': 'application/json; application/vnd.esios-api-v1+json',
    'Content-Type': 'application/json',
    'x-api-key':TOKEN_ESIOS
}
# URL para las API ESIOS
URL_ESIOS = "https://api.esios.ree.es/indicators/1001?start_date=2023-01-1T00%3A00%3A00Z&end_date=2023-12-31T07%3A34%3A17Z"


