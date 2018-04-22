from pymongo import MongoClient
import hashlib
import datetime

def get_index():
    client = MongoClient()
    db = client['Ledger']
    index_q = db['index']
    return index_q


def get_index_value():
    index_q = get_index()
    index = index_q.find_one()
    return index['value']


def increment_index():
    last_value = get_index_value()
    index_q = get_index()
    index_q.update_one(
        {'value': last_value},
        {
            "$set": {'value': last_value + 1}
        }
    )


def get_transactions():
    client = MongoClient()
    db = client['Ledger']
    transactions_q = db['transactions']
    return transactions_q


def get_transactions_values():
    transactions_q = get_transactions()
    return transactions_q.find()


def get_prev_hash():
    transactions_q = get_transactions()
    last_index = get_index_value()
    last_trans = transactions_q.find_one(
        {'index_trans': last_index}
    )
    if last_trans is None:
        return ''
    m = hashlib.md5()
    m.update(last_trans['index_trans'])
    m.update(last_trans['public_key_sender'])
    m.update(last_trans['public_key_whom'])
    m.update(last_trans['time'])
    m.update(last_trans['file_hash'])
    return m.digest()


def add_transaction(public_key_sender, public_key_whom, file_hash):
    transactions_q = get_transactions()
    time = datetime.datetime.utcnow()
    new_transaction = {'public_key_sender': public_key_sender,
                       'public_key_whom': public_key_whom,
                       'file_hash': get_prev_hash(),
                       'time': datetime.datetime.utcnow()
                       }
    increment_index()
    new_index = get_index_value()
    transactions_q.insert_one(
        {'index': new_index},
        new_transaction
    )




#index = get_index()
#index.insert_one(
#    {'values':0}
#)


#add_transaction('asdasd', 'fgdgfdg', 'qwe12eqweqweqw')
