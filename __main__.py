from timy import Timy

DATABASE_URI = "sqlite:////Users/ferojanus/Repos/timy_database/db1.sqlite"

def main():

    timy = Timy(db_uri=DATABASE_URI)
    timy.capture_start()

if __name__ == '__main__':
    main()