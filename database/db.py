from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert
from sqlalchemy.schema import ForeignKey


engine = create_engine(f"sqlite:///data/db.sqlite", echo = True)
meta = MetaData()
decks = Table(
    "decks", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)
cards = Table(
    "cards", meta,
    Column("id", Integer, primary_key=True),
    Column("deck_id", Integer, ForeignKey("decks.id")),
    Column("front", String),
    Column("back", String),
)

def create_tables():
    meta.create_all(engine)

def get_decks():
    with engine.connect() as conn:
        res = conn.execute(select(decks.c))
        rows = res.fetchall()
    return rows

def get_cards():
    with engine.connect() as conn:
        res = conn.execute(select(cards.c))
        rows = res.fetchall()
    return rows


def get_cards(deck_id=None):
    with engine.connect() as conn:
        if deck_id is None:
            res = conn.execute(select(cards.c))
        else:
            res = conn.execute(select(cards).where(cards.c.deck_id == deck_id))
        rows = res.fetchall()
    return rows

def add_deck(deck_name):
    with engine.connect() as conn:
        stmt = insert(decks).values(name = deck_name)
        conn.execute(stmt)
        conn.commit()


def add_card(deck_id, front, back):
    with engine.connect() as conn:
        stmt = insert(cards).values(deck_id = deck_id, front = front, back = back)
        conn.execute(stmt)
        conn.commit()

def get_stats():
    card_count = 0
    deck_count = 0
    with engine.connect() as conn:
        card_count =  len(conn.execute(select(cards.c.id)).fetchall())
        deck_count = len(conn.execute(select(decks.c.id)).fetchall())
    return {"cards":card_count, "decks":deck_count}
    

