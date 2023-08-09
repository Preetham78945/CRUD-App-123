from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id":1,"title": "book1", "author" : "Author1"},
    {"id":2,"title": "book2", "author" : "Author2"},
    {"id":3,"title": "book3", "author" : "Author3"},
]

#Get all books
@app.route('/books' , methods=['GET'])
def get_books():
    return books

#Get 1 book in specific
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
        
        return{'error':'Book not found'}

#Create a book
@app.route('/books',methods=['POST'])
def create_book():
    new_book={'id':len(books)+1, 'title':request.json['title'], 'author':request.json['author']}
    books.append(new_book)
    return new_book

#Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id']==book_id:
            book['title']=request.json['title']
            book['author']=request.json['author']
            return book
    return{'error':'book not found'}

#Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return{"data":"book deleted successfully"}
        
        return{'error':'Book not found'}


if __name__ == '__main__':
    app.run(debug=True)