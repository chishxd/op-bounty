# One Piece Bounty Poster Generator

This is a Flask app made for Slushies YSWS by Hack Club!

Generate your own One Piece-style bounty poster from a name + image URL.

## Quick Start (UV)

```bash
git clone https://github.com/chishxd/op-bounty.git
cd op-bounty
uv sync
uv run python main.py
```

Open `http://127.0.0.1:5000`

## Endpoints

- `GET /` - Form page where you enter a name and image URL
- `POST /create-bounty` - Generates bounty data and creates a poster ID
- `GET /poster/<poster_id>` - Renders the generated bounty poster

## Example Usage

1. Open `/`
2. Enter:
   - Name: `Monkey D. Luffy`
   - Image URL: any public image URL
3. Submit the form
4. You will be redirected to `/poster/<poster_id>`

## Project Structure

```text
.
├── bounties.db
├── LICENSE
├── main.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── static
│   └── style.css
├── templates
│   ├── index.html
│   └── poster.html
└── uv.lock
```

## Tech Stack

- Flask
- Jinja2 templates
- HTML/CSS
- uv (recommended dependency/project manager)

## Installation

I use `uv` for this app, but `requirements.txt` is also included due to YSWS requirements.

### Option 1: Using UV (Recommended)

- Install UV if you haven't already:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Clone the repository and enter it:
```
git clone https://github.com/chishxd/op-bounty.git && cd op-bounty
```

- Install dependencies and run:
```
uv sync
uv run python main.py
```

### Option 2: Using pip and venv

- Clone the repository and enter it:
```
git clone https://github.com/chishxd/op-bounty.git && cd op-bounty
```

- Create a virtual environment:
```
python -m venv .venv
```

- Activate the virtual environment:

For UNIX based systems:
```
source .venv/bin/activate
```

For Windows:
```
source .venv\Scripts\activate
```

- Install requirements:
```
pip install -r requirements.txt
```

Run the app:
```
python main.py
```

Then visit `http://127.0.0.1:5000`

## Development

Run with Flask debug mode:

```bash
FLASK_APP=main.py FLASK_ENV=development flask run
```

For Windows PowerShell:

```powershell
$env:FLASK_APP = "main.py"
$env:FLASK_ENV = "development"
flask run
```

## Troubleshooting

- Port already in use:
	- Run on a different port, for example `flask run -p 5001`
- Image does not load in poster:
	- Make sure the image URL is public and directly points to an image file
- `uv` command not found:
	- Reopen your terminal after installation, or reinstall from https://docs.astral.sh/uv/
- Missing dependencies errors:
	- Re-run `uv sync` or `pip install -r requirements.txt`

## Contributing

Pull requests are welcome. Feel free to open an issue first if you want to discuss major changes.

## LICENSE
This project uses the [MIT License](LICENSE).