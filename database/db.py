from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select


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
    Column("front", String),
    Column("back", String),
)
meta.create_all(engine)

def get_decks():
    with engine.connect() as conn:
        res = conn.execute(select(decks.c))
        rows = res.fetchall()
    return rows

