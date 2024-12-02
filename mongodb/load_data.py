import datetime
import sys
import pymongo
import os
import time

start = time.time()

URI = os.getenv('MONGODB_ATLAS')
URI2 = 'mongodb://root:example@192.168.88.251:27017'
client = pymongo.MongoClient(URI, )
db = client["test_db"]
col = db["test_col"]
col.find_one({})

doc = {
    'str': 'The value of first element is the number of milliseconds since midnight. The value of the second element is the number of seconds corresponding to the time zone offset (zero in this instance, as no time zone was specified).',
    'u32': 1239873,
    'u64': 1234567890123456789,
    'i32': -1239873,
    'i64': -1234567890123456789,
    'f32': 0.32394823423948,
    'f64': 2.49234823948293842983,
    'bool': True,
    'vec_int': [123, 4123, 41, 234, 1234, 123, 4, 6243, 632, 456, 3456, 345, 63, 4],
    'vec_str': ['234234', 'dsfgsdafg', 'sdfgnio43', '23459eg84', '34g9j348', '03g434gj34'],
    'vec_float': [0.234923489234] * 2048,
    'datetime': datetime.datetime.now(),
    'obj': {
        'str': 'The value of first element is the number of milliseconds since midnight. The value of the second element is the number of seconds corresponding to the time zone offset (zero in this instance, as no time zone was specified).',
        'u32': 1239873,
        'u64': 1234567890123456789,
        'i32': -1239873,
        'i64': -1234567890123456789,
        'f32': 0.32394823423948,
        'f64': 2.49234823948293842983,
        'bool': True,
        'vec_int': [123, 4123, 41, 234, 1234, 123, 4, 6243, 632, 456, 3456, 345, 63, 4],
        'vec_str': ['234234', 'dsfgsdafg', 'sdfgnio43', '23459eg84', '34g9j348', '03g434gj34'],
        'vec_float': [0.234923489234] * 2048,
        'datetime': str(datetime.datetime.now()),
        'obj': {
            'str': 'The value of first element is the number of milliseconds since midnight. The value of the second element is the number of seconds corresponding to the time zone offset (zero in this instance, as no time zone was specified).',
            'u32': 1239873,
            'u64': 1234567890123456789,
            'i32': -1239873,
            'i64': -1234567890123456789,
            'f32': 0.32394823423948,
            'f64': 2.49234823948293842983,
            'bool': True,
            'vec_int': [123, 4123, 41, 234, 1234, 123, 4, 6243, 632, 456, 3456, 345, 63, 4],
            'vec_str': ['234234', 'dsfgsdafg', 'sdfgnio43', '23459eg84', '34g9j348',
                        '03g434gj34'],
            'vec_float': [0.234923489234] * 2048,
            'datetime': str(datetime.datetime.now()),
            'obj': {
                'str': 'The value of first element is the number of milliseconds since midnight. The value of the second element is the number of seconds corresponding to the time zone offset (zero in this instance, as no time zone was specified).',
                'u32': 1239873,
                'u64': 1234567890123456789,
                'i32': -1239873,
                'i64': -1234567890123456789,
                'f32': 0.32394823423948,
                'f64': 2.49234823948293842983,
                'bool': True,
                'vec_int': [123, 4123, 41, 234, 1234, 123, 4, 6243, 632, 456, 3456, 345, 63, 4],
                'vec_str': ['234234', 'dsfgsdafg', 'sdfgnio43', '23459eg84', '34g9j348',
                            '03g434gj34'],
                'vec_float': [0.234923489234] * 2048,
                'datetime': str(datetime.datetime.now()),
                'obj': {
                    'str': 'The value of first element is the number of milliseconds since midnight. The value of the second element is the number of seconds corresponding to the time zone offset (zero in this instance, as no time zone was specified).',
                    'u32': 1239873,
                    'u64': 1234567890123456789,
                    'i32': -1239873,
                    'i64': -1234567890123456789,
                    'f32': 0.32394823423948,
                    'f64': 2.49234823948293842983,
                    'bool': True,
                    'vec_int': [123, 4123, 41, 234, 1234, 123, 4, 6243, 632, 456, 3456, 345, 63, 4],
                    'vec_str': ['234234', 'dsfgsdafg', 'sdfgnio43', '23459eg84', '34g9j348',
                                '03g434gj34'],
                    'vec_float': [0.234923489234] * 2048,
                    'datetime': str(datetime.datetime.now())
                }
            }
        }
        }
}
doc1 = {
    'text': 'hola mundo'
}
for _ in range(10):
    print(_)
    cursor = col.insert_one(doc.copy())

print(f'{time.time() - start}s')
