from sqlalchemy import insert

primary_keys = []

def seed(decks, cards, engine):
    with engine.connect() as conn:
        for val in ["deck1", "deck2", "deck3"]:
            stmt = insert(decks).values(name=val)
            res = conn.execute(stmt)
            primary_keys.append(res.inserted_primary_key)
            conn.commit()

    with engine.connect() as conn:
        for val in ["card1.1", "card1.2", "card1.3"]:
            stmt = insert(cards).values(front=val+" front", back = val + " back", deck_id = primary_keys[0][0])
            conn.execute(stmt)
            conn.commit()


    with engine.connect() as conn:
        for val in ["card2.1", "card2.2", "card2.3"]:
            stmt = insert(cards).values(front=val+" front", back = val + " back", deck_id = primary_keys[1][0])
            conn.execute(stmt)
            conn.commit()






