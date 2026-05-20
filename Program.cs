using System.Text;

var client = new HttpClient();

var url = "http://127.0.0.1:8000/predict";

var json = "{\"age\":45,\"salary\":75000}";

var content = new StringContent(
    json,
    Encoding.UTF8,
    "application/json"
);

var response = await client.PostAsync(url, content);

var result = await response.Content.ReadAsStringAsync();

Console.WriteLine(result);

# dotnet new console -n DotNetClient
# dotnet run