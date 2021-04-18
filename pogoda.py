provincy = input('Viloyatni tanlang: ')


if provincy == 'Jizzax':
    city = input('Shaxarni tanlang: ')
    if city == 'Jizzax':
        day = input('Qaysi kunning ob xavosi kerak: ')

        if day == 'Dushanba':
            print('Dushanba: kunduzi +28 , kechasi +15 va joylarda bulutli!')
        else:
            print('Dushanbadan boshqa kunlarning ma\'lumoti xa berilgani yuq!')
    else:
        print('Jizzaxdan boshqa tumanlarning ma\'lumoti xali berilgani yuq!')
else:
    print('Jizzaxdan boshqa viloyatlar uchun malumot yuq!')