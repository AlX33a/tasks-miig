from main import database


database.start() # start the database

# создал 3 роли, по дефолту новым юзерам присваивается роль с id = 0
database.add_new_role('0', 'new user role', '0', '50-46-03 15-06-2022', 'dolbaeb_sozdatel')
database.add_new_role('1', 'kykyebati', '1000', '50-46-03 15-06-2022', 'dolbaeb_sozdatel')
database.add_new_role('2', 'женя гей (нет)', '2010', '50-46-03 15-06-2022', 'sozdatel2')

database.add_new_user('22', "50-46-03 16-06-2022") # create a new user 22
print('время регистрации: ', database.check_time('22')) # print create time

database.set_money('22', '990') # set money for user 22 to 990
print('всего денег: ', database.check_money('22')) # print users money 

database.set_warn('22','7') # set warn status to 7
print('варнов всего: ', database.check_warn('22')) # print warn status of user 22

database.set_mute('22', '50-46-03 16-06-2022') # give mute to user 22 for 33-02-12 18-06-2022 date 
print('время снятия текущего мута: ', database.check_mute('22')) # print mute date of user 22

print('роли:', database.check_role_id('22')) # print role id of user 22
print('имя роли пользователя под номером 22: ', database.role_check_name(database.check_role_id('22')))

database.set_role_id(database.check_role_id('22'), "")