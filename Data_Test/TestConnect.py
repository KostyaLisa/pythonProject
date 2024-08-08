

import mysql.connector
from mysql.connector import errorcode


# Database configuration
config = {
    'user': 'root',  # replace with your MySQL root username
    'password': '',  # replace with your MySQL root password
    'host': '127.0.0.1',  # replace with your MySQL host if different
    'raise_on_warnings': True,
    'database': 'my_test_rols'  # replace with your desired database name if different from 'my_test_Rols'
}

# Connect to MySQL
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS my_test_rols;")
    cursor.execute("USE my_test_rols;")

    # Create the messages table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Create user counters table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_counters (
        id INT PRIMARY KEY CHECK (id = 1),
        admin_count INT DEFAULT 0,
        user_count INT DEFAULT 0,
        guest_count INT DEFAULT 0
    );
    """)

    # Insert initial counters if they don't exist
    cursor.execute("INSERT IGNORE INTO user_counters (id) VALUES (1);")


    # Function to create users and update counters
    def create_user(role, username, password):
        try:
            cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';")

            if role == 'admin':
                cursor.execute(f"GRANT ALL PRIVILEGES ON my_test_rols.* TO '{username}'@'localhost';")
                cursor.execute("UPDATE user_counters SET admin_count = admin_count + 1 WHERE id = 1;")
            elif role == 'user':
                cursor.execute(f"GRANT SELECT, INSERT ON my_test_rols.* TO '{username}'@'localhost';")
                cursor.execute("UPDATE user_counters SET user_count = user_count + 1 WHERE id = 1;")
            elif role == 'guest':
                cursor.execute(f"GRANT SELECT ON my_test_rols.* TO '{username}'@'localhost';")
                cursor.execute("UPDATE user_counters SET guest_count = guest_count + 1 WHERE id = 1;")

            cnx.commit()
            print(f"User '{username}' with role '{role}' created successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            cnx.rollback()


    # Create example users
    create_user('admin', 'admin1', 'admin_password1')
    create_user('user', 'user1', 'user_password1')
    create_user('guest', 'guest1', 'guest_password1')

    # Fetch and display the counters
    cursor.execute("SELECT * FROM user_counters WHERE id = 1;")
    counters = cursor.fetchone()
    print(f"Admin count: {counters[1]}, User count: {counters[2]}, Guest count: {counters[3]}")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor.close()
    cnx.close()
