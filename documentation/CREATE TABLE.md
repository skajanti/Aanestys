CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        role VARCHAR(32) NOT NULL,
        PRIMARY KEY (id)
)

CREATE TABLE candidate (
        id INTEGER NOT NULL,
        name VARCHAR(144),
        party VARCHAR(32),
        PRIMARY KEY (id)
)

CREATE TABLE election (
        year INTEGER NOT NULL,
        active BOOLEAN NOT NULL,
        PRIMARY KEY (year),
        CHECK (active IN (0, 1))
)

CREATE TABLE vote (
        id INTEGER NOT NULL,
        candidate_id INTEGER NOT NULL,
        voter_id INTEGER NOT NULL,
        election_year INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(candidate_id) REFERENCES candidate (id),
        FOREIGN KEY(voter_id) REFERENCES account (id),
        FOREIGN KEY(election_year) REFERENCES election (year)
)