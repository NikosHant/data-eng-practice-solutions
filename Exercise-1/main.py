import zipfile, io, aiohttp, asyncio
import os

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


async def main():
    directory_name = "downloads"

    try:
        os.mkdir(directory_name)
    except Exception as e:
        print(f"An error occurred: {e}")
    async with aiohttp.ClientSession() as sess:     
        for uri in download_uris:
            try:
                # r = requests.get(uri)
                async with sess.get(uri) as r:
                    data = await r.read()
                    z = zipfile.ZipFile(io.BytesIO(data))
                    z.extractall(directory_name)
            except Exception as e:
                print(f"GET error fetching from uri: {uri}\n{e}")

if __name__ == "__main__":
    asyncio.run(main())
