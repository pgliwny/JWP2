# call-analyze-api.ps1
# Skrypt do wywołania API Flask z analizą sentymentu (POST /analyze)

# Treść zapytania w formacie JSON
$json = '{"text": "I love learning Python and AI!"}'

# Nagłówki HTTP
$headers = @{
    "Content-Type" = "application/json"
}

# URL API (lokalne Flask)
$uri = "http://127.0.0.1:5000/analyze"

# Wywołanie REST API
$response = Invoke-RestMethod -Uri $uri `
                              -Method POST `
                              -Headers $headers `
                              -Body $json

# Wyświetlenie wyniku
Write-Host "Wynik analizy:"
$response | ConvertTo-Json -Depth 3
