# print the list of various things

def list_maker(l):
    for i in range(1, 11):
        print(f'{i} . {l[i]}')

def monument():
    print("\nMONUMETS\n")
    l1 = ["", "Taj Mahal", "Qutub Minar", "Jantar Mantar", "India Gate", "Red Fort",
           "Jama Masjid", "Statue of Unity", "Lotus Temple", "Akshar Dham Temple", "Gateway of India"]
    list_maker(l1)

def food():
    print("\nFOOD\n")
    l2 = ["", "Pav Bhaji", "Chole Bhature", "Dal Bati Churma", "Gulab Jamun",
          "Jalebi", "Gujia", "Poha", "Khakhra", "Bhole Kulche", "Rabri"]
    list_maker(l2)

def leaders():
    print("\nLEADERS\n")
    l3 = ["", "MK Gandhi", "SC Bose", "J Nehru", "Candarshekhar Azad",
          "Bhagat Singh", "Rajguru", "Sukdev", "Rani LaxmiBai", "Tantia Tope", "Shivaji Maharaj"]
    list_maker(l3)

monument()
food()
leaders()
