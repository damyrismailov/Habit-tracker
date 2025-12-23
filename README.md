# Habit Tracker – Pixela Trading Journal

Short Python script that sends a daily numeric value to the Pixela API and shows it as a graph on the web. I use it as a trading P&L journal, but you can adapt it to any habit (study minutes, workout time, pages read, etc.).

## Main features

- Connects to the Pixela API (`https://pixe.la/v1/users`) to store one value per day as a “pixel” on a graph.
- Creates a Pixela user and a graph (ID, name, unit, type, colour) via HTTP `POST` requests (run once, then comment out).
- Uses `datetime` to format today’s date as `YYYYMMDD`.
- Asks you for today’s value with `input()` (for me: “What is the PNL for today?”).
- Sends a `POST` request so Pixela adds a pixel for today’s date with the given quantity.
- Includes optional code to update or delete a specific date using `PUT` and `DELETE` requests.
- Example graph is called “Trading Journal” with `unit="USD"`, `type="float"` and `color="ajisai"`.

## What I learned

- Talking to a REST API with the `requests` library (`POST`, `PUT`, `DELETE`).
- Sending JSON payloads and custom headers (Pixela token in `X-USER-TOKEN`).
- Working with dates and formatting them for APIs.
- Separating one-time setup (user + graph) from everyday usage (sending the daily value).
- Turning a simple script into a reusable tool for tracking real-world habits.

## How to run

1. Install Python 3 and the `requests` package (`pip install requests`).
2. In `main.py`, set your own values at the top:
   - `USERNAME` – your Pixela username  
   - `PASSWORD` – your Pixela token  
   - `graph_id` – any ID you want for this graph (for example `graph2`)
3. First run:
   - Uncomment the user-creation block (`user_params` and the `requests.post` that sends it).
   - Run `python main.py` once to create your Pixela user.
   - Comment that block again.
4. Graph setup:
   - Configure `graph_config` (name, unit, type, colour).
   - Uncomment the code that posts `graph_config` to `graph_endpoint`.
   - Run `python main.py` once to create the graph, then comment this block again.
5. Daily use:
   - Keep the “add today’s value” section active.
   - Run `python main.py`.
   - Enter today’s number when asked; the script sends it to Pixela and prints the response.
6. Optional corrections:
   - To fix a past day, update the date in the update/delete section and run the script with the `PUT` (to change `quantity`) or `DELETE` (to remove the pixel).

After setup, you can view your graph in the browser at `https://pixe.la/v1/users/YOUR_PIXELA_USERNAME/graphs/YOUR_GRAPH_ID` and watch your habit (or trading P&L) build up over time.
