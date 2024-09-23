from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

# Define the route to accept SQL queries
@app.route('/', methods=['GET', 'POST'])
def query_db():
    result = None
    query = None
    if request.method == 'POST':
        query = request.form['query']
        try:
            # Connect to the database
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            
            # Execute the query
            cursor.execute(query)
            result = cursor.fetchall()
            
            # Get column names if available
            if cursor.description:
                columns = [desc[0] for desc in cursor.description]
                result.insert(0, columns)
            
        except mysql.connector.Error as err:
            result = str(err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    return render_template('index.html', result=result, query=query)

if __name__ == '__main__':
    app.run(debug=True)
