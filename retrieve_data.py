
import urllib.request
import json
import ssl


def get_air_quality():
    
    context = ssl._create_unverified_context()
    API_KEY = 'eacd6c69cbec4827a22c2f8c0b5daab8'  # Replace with your actual API key

    # Constructing the URL with the postal code and country code
    url = f"https://api.weatherbit.io/v2.0/history/airquality?postal_code=91710&country=US&start_date=2024-02-01&end_date=2024-02-29&tz=local&key={API_KEY}"
    
    print("Requesting URL:", url)  # Print the URL to verify its correctness

    try:
        with urllib.request.urlopen(url, context=context) as response:
            source = response.read()
            api_data_obj = json.loads(source)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error encountered: {e.code} - {e.reason}")
        return

    filename_out = input("Enter the file name you wish to save:")

    with open(filename_out, 'w') as file_out:
        json.dump(api_data_obj, file_out)
    return filename_out

