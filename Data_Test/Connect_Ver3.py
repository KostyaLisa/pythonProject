import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',  # replace with your MySQL root username
    'password': '',  # replace with your MySQL root password
    'host': '127.0.0.1',  # replace with your MySQL host if different
    'port': '3306',  # replace with your MySQL port if different
    'raise_on_warnings': True,
     # 'database': 'my_test'  # replace with your desired database name if different from

}
database_name = 'my_test'  # replace with your desired database name if different from

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Check if the database already exists
    cursor.execute("SHOW DATABASES LIKE %s;", (database_name,))
    db_exists = cursor.fetchone()

    if db_exists:
        print(f"Database '{database_name}' already exists.")
    else:
        # Create the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE {database_name};")
        print(f"Database '{database_name}' created successfully.")
    # Create the database
    # cursor.execute("CREATE DATABASE IF NOT EXISTS my_test;")
    # cursor.execute(f"CREATE DATABASE IF NOT EXISTS{database_name};"
    #                if database_name!= 'your_database_name' else "USE")
    # Use the database
    cursor.execute(f"USE {database_name};")

    # Create the messages table
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    role ENUM('admin', 'user', 'guest')
);
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_id INT,
    recipient_id INT,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES users(id),
    FOREIGN KEY (recipient_id) REFERENCES users(id)
);
""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS user_counters (
    id INT PRIMARY KEY CHECK (id = 1),
    admin_count INT DEFAULT 0,
    user_count INT DEFAULT 0,
    guest_count INT DEFAULT 0
);
""")

    cursor.execute("INSERT IGNORE INTO user_counters (id) VALUES (1);")


    # Function to create users and update counters
    def create_user(role, username, password):
        try:
            cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';")
            cursor.execute("INSERT INTO users (username, role) VALUES (%s, %s);", (username, role))

            if role == 'admin':
                cursor.execute(f"GRANT ALL PRIVILEGES ON my_test.* TO '{username}'@'localhost';")
                cursor.execute("UPDATE user_counters SET admin_count = admin_count + 1 WHERE id = 1;")
            elif role == 'user':
                cursor.execute(f"GRANT SELECT, INSERT ON my_test.* TO '{username}'@'localhost';")
                cursor.execute("UPDATE user_counters SET user_count = user_count + 1 WHERE id = 1;")
            elif role == 'guest':
                cursor.execute(f"GRANT SELECT ON my_test.* TO '{username}'@'localhost';")
                cursor.execute("UPDATE user_counters SET guest_count = guest_count + 1 WHERE id = 1;")

            cnx.commit()
            print(f"User '{username}' with role '{role}' created successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            cnx.rollback()


    # Function to delete users and update counters
    def delete_user(username):
        try:
            cursor.execute("SELECT role FROM users WHERE username = %s;", (username,))
            result = cursor.fetchone()
            if result:
                role = result[0]
                cursor.execute(f"DROP USER '{username}'@'localhost';")
                cursor.execute("DELETE FROM users WHERE username = %s;", (username,))

                if role == 'admin':
                    cursor.execute("UPDATE user_counters SET admin_count = admin_count - 1 WHERE id = 1;")
                elif role == 'user':
                    cursor.execute("UPDATE user_counters SET user_count = user_count - 1 WHERE id = 1;")
                elif role == 'guest':
                    cursor.execute("UPDATE user_counters SET guest_count = guest_count - 1 WHERE id = 1;")

                cnx.commit()
                print(f"User '{username}' deleted successfully.")
            else:
                print(f"User '{username}' not found.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            cnx.rollback()


    # Function to write messages to users
    def write_message(sender, recipient, message):
        try:
            # cursor.execute("SELECT id FROM users WHERE username = %s;", (sender,))
            # sender_id = cursor.fetchone()[0]
            # cursor.execute("SELECT id FROM users WHERE username = %s;", (recipient,))
            # recipient_id = cursor.fetchone()[0]

            cursor.execute("SELECT id FROM users WHERE username = %s;", (sender,))
            sender_result = cursor.fetchone()
            if sender_result is None:
                raise ValueError("Sender does not exist")
            sender_id = sender_result[0]

            cursor.execute("SELECT id FROM users WHERE username = %s;", (recipient,))
            recipient_result = cursor.fetchone()
            if recipient_result is None:
                raise ValueError("Recipient does not exist")
            recipient_id = recipient_result[0]

            cursor.execute("INSERT INTO messages (sender_id, recipient_id, message) VALUES (%s, %s, %s);",
                           (sender_id, recipient_id, message))
            cnx.commit()
            print(f"Message from '{sender}' to '{recipient}' sent successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            cnx.rollback()


    # Function to list all users
    def list_all_users():
        try:
            cursor.execute("SELECT username, role FROM users;")
            users = cursor.fetchall()
            for user in users:
                print(f"Username: {user[0]}, Role: {user[1]}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    # Function to list all admins
    def list_admins():
        try:
            cursor.execute("SELECT username FROM users WHERE role = 'admin';")
            admins = cursor.fetchall()
            for admin in admins:
                print(f"Admin Username: {admin[0]}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    # Example usage of the functions
    create_user('admin', 'admin1', 'admin_password1')
    create_user('user', 'user1', 'user_password1')
    create_user('guest', 'guest1', 'guest_password1')

    write_message('admin1', 'user1', 'Hello user1, this is admin1.')
    write_message('user1', 'admin1', 'Hello admin1, this is user1.')

    list_all_users()
    list_admins()

    delete_user('guest1')

    list_all_users()

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
finally:
    if cnx.is_connected():
        cnx.close()
