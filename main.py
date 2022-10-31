

class User:
    def __init__(self, id, name, rank):
        self.id = id
        self.name = name
        self.rank = rank

users = []

def addUser(user):
    users.append(user)

def showUsers():
    users.sort(key=lambda x: x.rank)
    print('All users by rank: ')
    count = 0
    for i in users:
        count += 1
        print(f' {count} ) {i.name}  rank =  {i.rank}  id of user = {i.id}')

def PatchRankOfUserByName(name, newRank):
    k = 0
    for i in users:
        if i.name == name:
            i.rank = newRank
            k = 1
    if not k:
        print('There is not such name')

def PatchRankOfUserById(id, newRank):
    k = 0
    for i in users:
        if i.id == id:
            i.rank = newRank
            k = 1
    if not k:
        print('There is noy such id')

def PatchRankOfUserByOrder(number, newRank):
    if (len(users) >= number and number > 0):
        users[number - 1].rank = newRank
    else:
        print('There is not such sequence number')

def DeleteUserByName(name):
    k = 0
    for i in range(len(users)):
        if users[i].name == name:
            users.pop(i)
            k = 1
    if not k:
        print('There is not such name')


def DeleteUserById(id):
    k = 0
    for i in range(len(users)):
        if users[i].id == id:
            users.pop(i)
            k = 1
    if not k:
        print('There is not such id')


def DeleteUserByOrder(number):
    if(len(users) >= number and number > 0):
        users.pop(number - 1)
    else:
        print('There is not such sequence number')

def DeleteUserByRank(rank):
    k = 0
    for i in range(len(users)):
        if users[i].rank == rank:
            users.pop(i)
            k = 1
    if not k:
        print('There is not such rank')
b = 1
countId = 1
while b:
    n = int(input('Enter 1 if you want add new user \n'
                  'Enter 2 if you want to see all users \n'
                  'Enter 3 if you want to edit rank of user \n'
                  'Enter 4 if you want to delete user \n'
                  'Enter 0 if you want to finish \n'))

    if n == 1:
        name = input('Enter name of user \n')
        rank = float(input('Enter rank of user \n'))
        user = User(countId, name, rank)
        addUser(user)
        countId += 1

    if n == 2:
        showUsers()

    if n == 3:
        m = int(input('Enter 1 if you want to edit by name \n'
                      'Enter 2 if you want to edit by id \n'
                      'Enter 3 if you want to edit by sequence number \n'))
        if m == 1:
            name = input('Enter name \n')
            newRank = float(input('Enter new rank'))
            PatchRankOfUserByName(name, newRank)
        if m == 2:
            id = int(input('Enter id \n'))
            newRank = float(input('Enter new rank '))
            PatchRankOfUserById(id, newRank)
        if m == 3:
            number = int(input('Enter sequence number \n'))
            newRank = float(input('Enter new rank '))
            PatchRankOfUserByOrder(number, newRank)
    if n == 4:
        m = int(input('Enter 1 if you want to delete by name \n'
                      'Enter 2 if you want to delete by id \n'
                      'Enter 3 if you want to delete by sequence number \n'
                      'Enter 4 if you want to delete by rank \n'))
        if m == 1:
            name = input('Enter name ')
            DeleteUserByName(name)
        if m == 2:
            id = int(input('Enter id '))
            DeleteUserById(id)
        if m == 3:
            number = int(input('Enter sequence number '))
            DeleteUserByOrder(number)
        if m == 4:
            rank = float(input('Enter rank '))
            DeleteUserByRank(rank)
    if n == 0:
        break