from app import app

if __name__ == '__main__':
   try:
      app.run(debug=True, port=2222)
   except Exception as e:
        print(f"An error occurred: {e}")