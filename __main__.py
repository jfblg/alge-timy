from timy import Timy

DATABASE_URI = "sqlite:////Users/uze/uze-sprinter/TimyDB/db1.sqlite"
'''
0011 C0  14:37:22.8549 00
 0011 c0  00:00:00.0169 01
 0011 c0  00:00:00.0560 02
 0011 c0  00:00:05.6351 03
 0011 c0  00:00:05.9051 04
 0011 c1  00:00:08.2780 01
 0011 c1  00:00:11.6849 02
 0011 c1  00:00:15.7115 03

'''
def main():

    timy = Timy(db_uri=DATABASE_URI)
    timy.capture_start()

if __name__ == '__main__':
    main()