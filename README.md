# AirBnB_clone
Holberton Clone of AirBnB Website
# Description
This project will eventually become part of a full cloning of the AirBNB backend. For now we are
focusing on inheritance, abstraction, and information hiding as we build our abilities in object-oriented programming.
AirBnB Website parts:

1. A website (front-end) that shows the final product.
2. An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
3. A database or files that store data (data = objects)
4. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

**Authors**
- **David Knoppers**, \<david.knoppers@holbertonschool.com>
- **Stuart Fosse**, \<stuart.fosse@holbertonschool.com>

Start the console by typing ./console.py or python3 console.py in your shell.

You can operate the console much like a linux terminal, typing a command and then pressing enter.

Some examples:

The 'help' command will bring up a list of available commands, and typing 'help' with the name of a command will give you a description.

(hbnb) help create

        creates one instance of an object with a random id
        Can be called directly or through object type
        example: create User

Let's use the create command to make a User and then use show to look at it.

(hbnb) create User
827d9074-994e-4558-98de-2b309e84fdcd
(hbnb) show User 827d9074-994e-4558-98de-2b309e84fdcd
[User] (827d9074-994e-4558-98de-2b309e84fdcd) {'email': '', 'id': '827d9074-994e-4558-98de-2b309e84fdcd', 'first_name': '', 'last_name': '', 'updated_at': datetime.datetime(2017, 2, 13, 7, 16, 27, 284978), 'password': '', 'created_at': datetime.datetime(2017, 2, 13, 7, 16, 27, 277107)}

The functionality of the shell is basic at this point, so most of what you can do involves creating objects.

You can also call methods using classes themselves, like so:

(hbnb) create BaseModel
54f43c75-4bfd-4e18-85f3-ec72d8590f78
(hbnb) BaseModel.all()
[BaseModel] (ea782cf8-3976-4433-b1be-a146a8bc1b08) {'created_at': datetime.datetime(2017, 2, 13, 7, 17, 43, 829439), 'id': 'ea782cf8-3976-4433-b1be-a146a8bc1b08', 'updated_at': datetime.datetime(2017, 2, 13, 7, 17, 43, 830429)}
[BaseModel] (54f43c75-4bfd-4e18-85f3-ec72d8590f78) {'created_at': datetime.datetime(2017, 2, 13, 7, 18, 1, 189596), 'id': '54f43c75-4bfd-4e18-85f3-ec72d8590f78', 'updated_at': datetime.datetime(2017, 2, 13, 7, 18, 1, 189893)}

More functionality will be added as we implement modules and debug the code.