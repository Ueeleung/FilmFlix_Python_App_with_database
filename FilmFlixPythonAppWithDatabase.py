import sqlite3

# Function to create the filmflix.db database if it doesn't exist
def create_database():
    conn = sqlite3.connect("filmflix.db")
    c = conn.cursor()

    # Create tblfilms table
    c.execute("""
        CREATE TABLE IF NOT EXISTS tblfilms (
            filmID INTEGER PRIMARY KEY,
            title TEXT,
            yearReleased INTEGER,
            rating TEXT,
            duration INTEGER,
            genre TEXT
        )
    """)

    conn.commit()
    conn.close()

# Function to add a new film record
def add_film():
    conn = sqlite3.connect("filmflix.db")
    c = conn.cursor()

    # Gather film details from the user
    title = input("Enter film title: ")
    year = int(input("Enter year released: "))
    rating = input("Enter rating: ")
    duration = int(input("Enter duration (in minutes): "))
    genre = input("Enter genre: ")

    # Insert the film record into the database
    c.execute("""
        INSERT INTO tblfilms (title, yearReleased, rating, duration, genre)
        VALUES (?, ?, ?, ?, ?)
    """, (title, year, rating, duration, genre))

    conn.commit()
    conn.close()
    print("Film added successfully!")

# Function to delete a film record
def delete_film():
    conn = sqlite3.connect("filmflix.db")
    c = conn.cursor()

    film_id = int(input("Enter the film ID to delete: "))

    # Delete the film record from the database
    c.execute("DELETE FROM tblfilms WHERE filmID = ?", (film_id,))

    conn.commit()
    conn.close()
    print("Film deleted successfully!")

# Function to update a film record
def update_film():
    conn = sqlite3.connect("filmflix.db")
    c = conn.cursor()

    film_id = int(input("Enter the film ID to update: "))

    # Gather updated film details from the user
    title = input("Enter updated film title: ")
    year = int(input("Enter updated year released: "))
    rating = input("Enter updated rating: ")
    duration = int(input("Enter updated duration (in minutes): "))
    genre = input("Enter updated genre: ")

    # Update the film record in the database
    c.execute("""
        UPDATE tblfilms
        SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ?
        WHERE filmID = ?
    """, (title, year, rating, duration, genre, film_id))

    conn.commit()
    conn.close()
    print("Film updated successfully!")

# Function to print all records in tblfilms
def print_all_films():
    conn = sqlite3.connect("filmflix.db")
    c = conn.cursor()

    # Retrieve all film records from the database
    c.execute("SELECT * FROM tblfilms")
    films = c.fetchall()

    # Print the film records
    for film in films:
        print(f"Film ID: {film[0]}")
        print(f"Title: {film[1]}")
        print(f"Year Released: {film[2]}")
        print(f"Rating: {film[3]}")
        print(f"Duration: {film[4]} minutes")
        print(f"Genre: {film[5]}\n")

    conn.close()

# Function to print reports based on user's choice
def print_reports():
   
