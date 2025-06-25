from database.mysql import get_mysql_connection

def get_transactions():
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM transactions")
            return cursor.fetchall()
    finally:
        conn.close()

def add_transaction(
    client_name,
    stock_name,
    stock_symbol,
    transaction_type,
    quantity,
    price_per_unit,
    total_value,
    transaction_date,
    relationship_manager
):
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO transactions
                (client_name, stock_name, stock_symbol, transaction_type, quantity, price_per_unit, total_value, transaction_date, relationship_manager)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                client_name,
                stock_name,
                stock_symbol,
                transaction_type,
                quantity,
                price_per_unit,
                total_value,
                transaction_date,
                relationship_manager
            ))
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()


def get_users():
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
    finally:
        conn.close()

def add_user(name, age):
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()
