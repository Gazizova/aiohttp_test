import postgresql

db = postgresql.open('pq://postgres:postgres@localhost:5432/mydb')

db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, "
  "login CHAR(64), password CHAR(64))")

ins = db.prepare("INSERT INTO users (login, password) VALUES ($1, $2)")

ins("afiskon", "123")
# ('INSERT', 1)
ins("eax", "456")
# ('INSERT', 1)

db.query("SELECT id, trim(login), trim(password) FROM users")