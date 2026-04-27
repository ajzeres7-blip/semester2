import csv
import json
from connect import db_connect

#csv import
def import_csv():
    conn = db_connect()
    if conn is None:
        print("Connection failed")
        return

    cur = conn.cursor()

    with open('contacts.csv') as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row["name"]
            email = row["email"]
            birthday = row["birthday"]
            group = row["group"]
            phone = row["phone"]
            ptype = row["type"]

            # insert group if not exists
            cur.execute("""
                INSERT INTO groups(name)
                VALUES(%s)
                ON CONFLICT (name) DO NOTHING
            """, (group,))

            # get group id
            cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
            group_row = cur.fetchone()
            if not group_row:
                continue
            group_id = group_row[0]

            # insert contact (avoid duplicates)
            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES(%s, %s, %s, %s)
                ON CONFLICT (name) DO NOTHING
            """, (name, email, birthday, group_id))

            # get contact id
            cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
            cid = cur.fetchone()[0]

            # insert phone
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES(%s, %s, %s)
            """, (cid, phone, ptype))

    conn.commit()
    conn.close()
    print("CSV imported!")

#filter by group
def filter_by_group(group_name):
    conn = db_connect()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group_name,))

    rows = cur.fetchall()
    if not rows:
        print("No results")

    for row in rows:
        print(row)

    conn.close()

#search
def search(query):
    conn = db_connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        rows = cur.fetchall()

        if not rows:
            print("No matches found")

        for row in rows:
            print(row)
    except Exception as e:
        print("Search error:", e)

    conn.close()

#sort
def sort_contacts(sort_by):
    if sort_by not in ["name", "birthday"]:
        sort_by = "name"

    conn = db_connect()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute(f"""
        SELECT name, email, birthday
        FROM contacts
        ORDER BY {sort_by}
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()

#export json
def export_json():
    conn = db_connect()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)

    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=4, default=str)

    conn.close()
    print("Exported to JSON")

#import json
def import_json():
    conn = db_connect()
    if conn is None:
        return

    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for row in data:
        name, email, birthday, group, phone, ptype = row

        # check duplicate
        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists (skip/overwrite): ")

            if choice == "skip":
                continue
            elif choice == "overwrite":
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

        # group
        cur.execute("""
            INSERT INTO groups(name)
            VALUES(%s)
            ON CONFLICT (name) DO NOTHING
        """, (group,))

        cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
        group_id = cur.fetchone()[0]

        # contact
        cur.execute("""
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES(%s, %s, %s, %s)
        """, (name, email, birthday, group_id))

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        cid = cur.fetchone()[0]

        # phone
        cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES(%s, %s, %s)
        """, (cid, phone, ptype))

    conn.commit()
    conn.close()
    print("JSON imported!")

#menu
def menu():
    while True:
        print("\n1.Import CSV")
        print("2.Search")
        print("3.Filter by group")
        print("4.Sort")
        print("5.Export JSON")
        print("6.Import JSON")
        print("0.Exit")

        choice = input("Choose: ")

        if choice == "1":
            import_csv()
        elif choice == "2":
            search(input("Search: "))
        elif choice == "3":
            filter_by_group(input("Group: "))
        elif choice == "4":
            sort_contacts(input("Sort by (name/birthday): "))
        elif choice == "5":
            export_json()
        elif choice == "6":
            import_json()
        elif choice == "0":
            break


if __name__ == "__main__":
    menu()