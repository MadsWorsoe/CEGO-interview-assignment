mariadb = dict(
    ip_address = 'localhost',
    port = 3307,
    user = 'root',
    password = 'password',
    db = 'cego',
    users_table = 'users'
)
test = dict(
    query = 'SELECT id, firstName, lastName, email FROM users',
    filename = 'Test.txt'
)