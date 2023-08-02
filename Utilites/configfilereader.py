import configparser

def get_data():
    config = configparser.ConfigParser()
    config.read(r'D:\KekaPOM\utilites\ConfigFile.properties')
    url=config.get("db", "url")
    user=config.get("db", "username")
    password=config.get("db", "password")
    plateformname=config.get("db",'platformName')
    employeename=config.get('db','employeename')
    return url,user,password,plateformname,employeename



# print(url)
# print(user)
# print(password)
# print(plateformname)
# print(employeename)