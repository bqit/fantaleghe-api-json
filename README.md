# Fantacalcio API

An automated, serverless Python backend designed to fetch daily player quotes and data for the Serie A. 

This project uses **GitHub Actions** to automatically download the official Excel list, convert it into a lightweight, developer-friendly `JSON` format, and dynamically map the official player images (campioncini) using their unique IDs. 
Perfect for building custom fantasy football auction apps or dashboards.

---

## <img src="https://api.iconify.design/lucide/sparkles.svg?color=%234755c4" width="17"> Features
* **Serverless Automation:** Runs entirely on GitHub Actions via a daily Cron Job.
* **Data Parsing:** Converts heavy `.xlsx` files into clean `.json` for fast fetching.
* **Dynamic Media Mapping:** Automatically generates direct CDN links for each player's image based on their unique system ID.
* **FVM Included:** Extracts full stats, including Fantacalcio Virtual Market (FVM) values and daily quotation differences.

## <img src="https://api.iconify.design/lucide/settings.svg?color=%234755c4" width="17"> How it works
1. The GitHub Action triggers automatically every day at 04:00 AM (UTC).
2. The Python script authenticates and fetches the latest `.xlsx` player list.
3. Data is cleaned, parsed, and enriched with image URLs.
4. The script overwrites `players.json` and pushes the updated file directly to the `main` branch.
5. The JSON file can be fetched by any front-end application using raw GitHub URLs or CDN services (like jsDelivr).

Endpoint for live players data: <span style="color: #4755c4;">`https://cdn.jsdelivr.net/gh/bqit/fantaleghe-api-json@main/players.json`</span>

---

## <span style="color: #f22e2e;"><img src="https://api.iconify.design/lucide/triangle-alert.svg?color=%23f22e2e" width="17"> Disclaimer</span>
**This is an unofficial, educational project built for portfolio purposes.**  
It is not affiliated with, maintained, authorized, endorsed, or sponsored by Quadronica S.r.l. or Fantacalcio.it. All data, images, and trademarks belong to their respective and rightful owners. This script is intended for personal use and learning purposes only.
