from flask import Flask, jsonify , request
from database.createTableOperation import create_tables
from database.addOperation import create_user, create_product, order_product, create_user_stock
from database.auth import user_auth
from database.readOperation import getAllUsers, getAllProduct, getSpecificUser, getAllUserOrders, getAllStock, getSpecificProduct
import re
from database.deleteOperation import delete_specific_user, delete_all_users, delete_specific_product, delete_all_products, delete_specific_userStock, delete_all_userStock, delete_specific_userOrder, delete_all_userOrder
from database.updateOperation import update_userDetails, update_productDetails, check_userId_exists, check_productId_exists, update_userOrder


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home(): 
    return "Welcome API World"



@app.route('/createUser', methods = ['POST'])
def user_signUp():
    try:
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phoneNumber']
        address = request.form['address']
        pinCode = request.form['pinCode']

        # Check if any field is missing
        if not all([name, password, email, phone, address, pinCode]):
            return jsonify({"status": 400, "message": "All fields are required."}), 400
        
        # Validate email format
        if not validate_email(email):
            return jsonify({"status": 400, "message": "Invalid email format."}), 400
        
        # Validate phone number (must be 10 digits)
        if not validate_phone(phone):
            return jsonify({"status": 400, "message": "Phone number must be 10 digits."}), 400
        

        singUp_data = create_user(name= name, password= password, phone_number= phone, email= email, pin_code= pinCode, address= address)


        if singUp_data:
            return jsonify({"status": 200, "message": singUp_data}), 200
        else:
            return jsonify({"status": 500, "message": "An error occurred during signup."}), 500
    except KeyError as e:
        return jsonify({"status": 400, "message": f"Messing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"status": 500, "message": f"Internal Server Error: {str(e)}"}), 500
    

# Validation functions
def validate_email(email):
    """
    Validates email format using a regular expression.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    """
    Validates that the phone number is exactly 10 digits.
    """
    return phone.isdigit() and len(phone) == 10




@app.route('/userLogin', methods = ['POST'])
def user_login():
    try:
        # fetch email and password from the request
        email = request.form['email']
        password = request.form['password']

        # Validate email and password
        if not email or not password:
            return jsonify({"status": 400, "message": "Email and password are required"}), 400
        
        #Authenticate user
        login_data = user_auth(email= email, password= password)

        if login_data:
            block = login_data[6]
            isApproved = login_data[5] 

            if block == 1:
                return jsonify({"status": 403, "message": "Your account has been blocked"}), 403

            if isApproved == 1:
                return jsonify({"status": 200, "message": login_data[1]}), 200
            else:
                return jsonify({"status": 403, "message": "Your account is not approved yet"}), 403
        else:
            return jsonify({"status": 401, "message": "Invalid email or password"}), 401

    except KeyError as e:
        return jsonify({"status": 400, "message": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"status": 500, "message": f"Internal Server Error: {str(e)}"}), 500





@app.route('/addProduct', methods = ['POST'])
def add_product():
    try:
        product_name = request.form['productName']
        product_image = request.form['productImage']
        price = request.form['productPrice']
        category = request.form['productCategory']
        stock = request.form['productStock']
        expire_date = request.form['expireDate']

        if not all ([product_name, product_image, price, category, stock, expire_date]):
            return jsonify({"status": 400, "message": "All fields are required!"}), 400
        product_data = create_product(product_name= product_name, product_image= product_image, price= price, category= category, stock= stock, expire_date= expire_date)
        if(product_data):
            return jsonify({"status": 200, "message": "Product Add Successfully!"}), 200
        else:
            return jsonify({"status": 500, "message": "An error occurred during productAdd!"}), 500
        
    except KeyError as e:
        return jsonify({"status": 400, "message": f"Messing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"status": 500, "message": f"Internal Server Error: {str(e)}"}), 500
    


    
@app.route('/addUserStock', methods = ['POST'])
def add_userStock():
    try:
        product_id = request.form['product_id']
        product_name = request.form['productName']
        category = request.form['category']
        expire_date = request.form['expire_Date']
        price = request.form['price']
        stock = request.form['stock']

        if not all ([product_id, product_name, category, expire_date, price, stock]):
            return jsonify({"status": 200, "message": "All fields are required!"})
        product_data = create_user_stock(product_id= product_id, product_name= product_name, category= category, expire_date= expire_date, price= price, stock= stock)
        if(product_data):
            return jsonify({"status": 200, "message": "AddStock Successfully"})
        else:
            return jsonify({"status": 401, "message": "An error occurred during productAdd!"})
    except KeyError as e:
        return jsonify({"status": 400, "message": f"Messing field: {str(e)}"}), 400
    except Exception as e:
       return jsonify({"status": 500, "message": f"Internal Server Error: {str(e)}"}), 500



@app.route('/addUserOrder', methods = ['POST'])
def user_order():
    try:
        product_name = request.form['productName']
        product_id = request.form['productId']
        price = request.form['Price']
        category = request.form['Category']
        expire_date = request.form["ExpireDate"]
        quantity = request.form['Quantity']

        if not all ([product_name, price, category, expire_date, quantity]):
            return jsonify({"status": 400, "message": "All fields are required!"}), 400
        order_data = order_product(product_name= product_name, product_id= product_id, price= price, category= category, expire_date = expire_date, quantity= quantity)
        if(order_data):
            return jsonify({"status": 200, "message": "Complete Order Successfully"})
        else:
            return jsonify({"status": 500, "message": "An error occurred during Order!"}), 500
    except KeyError as e:
        return jsonify({"status": 400, "message": f"Messing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"status": 500, "message": f"Internal Server Error: {str(e)}"}), 500
    



@app.route('/getAllUsers', methods=['GET'])
def get_allUsers():
    users = getAllUsers()
    return jsonify(users)

@app.route('/getAllProducts', methods = ['GET'])
def get_AllProducts():
    products = getAllProduct()
    return jsonify(products)

@app.route('/getAllUserStock', methods = ['GET'])
def get_allUserStock():
    products = getAllStock()
    return jsonify(products)

@app.route('/getUserOrderProduct', methods= ['GET'])
def get_userOrder():
    orders = getAllUserOrders()
    return jsonify(orders)

@app.route('/getSpecificUser', methods = ['POST'])
def get_specific_users():
    try:
        userID = request.form['userID']
        getUserInfo = getSpecificUser(userID= userID)
        return jsonify(getUserInfo)
    except Exception as e:
        return jsonify({"status": 400, "message": str(e)}), 400
    
@app.route('/getSpecificProduct', methods = ['POST'])
def getSpecificProduct_routs():
    try:
        productID = request.form['productID']
        getProductInfo = getSpecificProduct(productID= productID)
        return jsonify(getProductInfo)
    except Exception as e:
        return jsonify({"status": 400, "message": str(e)}), 400


@app.route('/updateUserDetails', methods = ['PATCH'])
def update_userDetails_route():
    try:
        userID = request.form['userID']
        updateAllFealds = request.form.items()
        updateUser = {}

        for key, value in updateAllFealds:
            if key != 'userID':
                updateUser[key] = value
        if not check_userId_exists(userID= userID):
            return jsonify({"status": 200, "messge": "Please Enter Correct userId."})
        update_userDetails(userID= userID, **updateUser)

        return jsonify({"status": 200, "message": "UpdateUserDetails Successfully"})
    except Exception as e:
        return jsonify({"status": 400, "message": str(e)})
    
    

@app.route('/updateUserOrder', methods=['PATCH'])
def updateUserOrder_route():
    try:
        orderID = request.args.get('orderID')
        updateAllFields = request.args  
        updateOrder = {}

        for key, value in updateAllFields.items():
            if key != 'orderID':
                updateOrder[key] = value

        update_userOrder(orderID, **updateOrder)

        return jsonify({"status": 200, "message": "UpdateUserOrder Successfully"})
    except Exception as e:
        return jsonify({"status": 400, "message": str(e)})
    


@app.route('/updateProduct', methods = ['PATCH'])
def update_product():
    try:
        productID = request.form['productID']
        updataAllFields = request.form.items()
        updateProduct  = {}

        for key, value in updataAllFields:
            if key != 'productID':
                updateProduct[key] = value
        if not check_productId_exists(productId= productID):
            return jsonify({"status": 200, "messge": "Please Enter Correct productId."})
        update_productDetails(productID= productID, **updateProduct)
        return jsonify({"status": 200, "message": "UpdateProductDetails Successfully"})
    except Exception as e:
        return jsonify({"status": 400, "message": str(e)})



@app.route('/deleteSpecificUsers', methods=['DELETE'])
def delete_specific_user_route():
    try:
        user_id = request.args.get("userID")
        response_message = delete_specific_user(user_id)

        if "not found" in response_message:
            return jsonify({"status": 404, "message": response_message}), 404

        return jsonify({"status": 200, "message": response_message}), 200

    except Exception as e:
        return jsonify({"status": 400, "message": str(e)}), 400
    

@app.route('/deleteSpecificUserOrder', methods=['DELETE'])
def delete_specific_userOrder_route():
    try:
        order_id = request.args.get("orderID")
        response_message = delete_specific_userOrder(order_id)

        if "not found" in response_message:
            return jsonify({"status": 404, "message": response_message}), 404

        return jsonify({"status": 200, "message": response_message}), 200

    except Exception as e:
        return jsonify({"status": 400, "message": str(e)}), 400
    


@app.route('/deleteAllUsers', methods = ['DELETE'])
def delete_allUsers():
    try:
        delete_all_users()
        return jsonify({"status": 200, "message": "Delete All Users Successfully!"}), 200
    except Exception as e:
        jsonify({"status": 400, "message": str(e)}), 400


@app.route('/deleteSpecificProduct', methods = ['DELETE'])
def delete_specific_product():
    try:
        product_id = request.form['product_id']
        response_message = delete_specific_product(product_id)

        if "not found" in response_message:
            return jsonify({"status": 404, "message": response_message}), 404

        return jsonify({"status": 200, "message": response_message}), 200

    except Exception as e:
        return jsonify({"status": 400, "message": str(e)}), 400
    

@app.route('/deleteAllProducts', methods = ['DELETE'])
def delete_all_product():
    try:
        delete_all_products()
        return jsonify({"status": 200, "message": "Delete All Product Successfully!"}), 200
    except Exception as e:
        return jsonify({"status": 400, "message": str(e)}), 400
    

@app.route('/deleteSpecificUserStock', methods = ['DELETE'])
def delete_specific_user_stock():
    try:
        product_id = request.form['product_id']
        response_message = delete_specific_userStock(product_id)

        if "not found" in response_message:
            return jsonify({"status": 404, "message": response_message}), 404

        return jsonify({"status": 200, "message": response_message}), 200

    except Exception as e:
        return jsonify({"status": 400, "message": str(e)}), 400
    

@app.route('/delete_all_userStock', methods = ['DELETE'])
def deleteAllProduct():
    try:
        delete_all_userStock()
        return jsonify({"status": 200, "message": "Delete All UserStock Successfully!"}), 200
    except Exception as e:
        return jsonify({"status": 400, "message": str(e)}), 400


if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
