from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)

low_crimes = [
    "Stole meat from a Marine cafeteria",
    "Sailed without a license",
    "Insulted a Marine captain on Den Den Mushi",
    "Disturb basic laws of a city/village"
]

mid_crimes = [
    "Attacked a Marine ship",
    "Robbed a government supply convoy",
    "Destroyed a Marine base cannon",
    "Escaped Impel Down Level 1"
]

high_crimes = [
    "Attacked a Celestial Dragon",
    "Destroyed a Marine base",
    "Stole a Devil Fruit shipment",
    "Escaped Impel Down Level 6",
    "Tried to study poneglyph"
]

crime_tiers = {
    "low": {
        "crimes": low_crimes,
        "bounty_range": (1000, 100000)
    },
    "mid": {
        "crimes": mid_crimes,
        "bounty_range": (1_000_000, 100_000_000)
    },
    "high": {
        "crimes": high_crimes,
        "bounty_range": (300_000_000, 3_000_000_000)
    }
}

def init_db():
    conn = sqlite3.connect('bounties.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS bounties(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            photo_url TEXT NOT NULL,
            crime TEXT NOT NULL,
            bounty_amount TEXT NOT NULL,
            tier TEXT NOT NULL
        )
    '''
    )

    conn.commit()
    conn.close()

def generate_bounty_data(name, photo_url):
    tier = random.choice(list(crime_tiers.keys()))

    crime = random.choice(crime_tiers[tier]["crimes"])

    low, high = crime_tiers[tier]["bounty_range"]
    bounty = round(random.randint(low, high),-3)

    return {
        'name': name,
        'photo_url': photo_url,
        'crime': crime,
        'bounty': bounty,
        'tier': tier
    }







