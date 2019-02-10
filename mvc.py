from server_global import *
from flask import Flask, request, jsonify
from file_utils import *
app = Flask(__name__)

def __init__(self):
    self.file_config = CreateFile()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def file_as_bytes(file):
    with file:
        return file.read()

@app.route('/')
def register_product():
    flashmessge=[]
    return render_template('user_registration.html',flashmessge=flashmessge)

@app.route('/generate_productkey' , methods=['GET', 'POST'])
def generate_product_key():
    flashmessge=[]
    print(request.json())

    data=request.form['prerecord1']


    print(data)
    Userdata = data.split(",")
    print(Userdata)
    customer_name=Userdata[0]
    serial_key=Userdata[9]
    customer_emailid=Userdata[3]
    if serial_key in product_serial_numbers:
        #### Logic to generate the product authentication key
        random_number = ''.join(random.choice(string.digits) for _ in range(length))
        product_key = customer_name + random_number
        authentication_key = sha256_crypt.encrypt(product_key)

        print("authentication_key",authentication_key)
        # sending email
        message = 'Subject: Authentication key' + '\n' + authentication_key
        print("message",message)
        #server.sendmail(Sender_emailid,customer_emailid,message)
        print("message sent")
        product_keys.append(authentication_key)
        print("product_keys",product_keys)
        flashmessge.append("Product has been register successfully")
    else:
        flashmessge.append("User is not authorized . Product key is not matching")
    return json.dump(Userdata, indent=4)







@app.route('/list')
def register_product1():
    flashmessge=[]



    flash = {"test": "a"}
    retdata = json.dumps(flash)
    return retdata




if __name__ == "__main__":
    app.secret_key = os.urandom(SECREAT_KEY)
    ip="127.0.0.1"
    app.run(host=ip,port=5000)



