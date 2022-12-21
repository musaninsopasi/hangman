name = input("İsmini gir: ")
print("Oyuna hoş geldin, oyun toplam 5 bölümden oluşmaktadır ve her bölüm gittikçe zorlaşmaktadır (her bölümde sadece bir ipucu verilmektedir)")
print("Merhaba "+name+" hadi adam asmaca oynayalım")
ipucu_1 = "Mutfak eşyası/kesici"
print(ipucu_1)
key = "bıçak"
global_string = ""
lives = 10

#zorluk-1

while lives > 0:
    
    karakter_kaldi = 0
    
    for karakter in key:
        if karakter in global_string:
            print(karakter)
        else:
            print("-")    
            karakter_kaldi += 1  
    if karakter_kaldi == 0:
          print("Tebrikler "+name+" kelimeyi doğru tahmin ettin")
          break
    
    string = input("Kelimeyi tahmin edin: ")
    global_string += string
    if string not in key:
        lives -= 1
        print("Tahmin edemedin")
        print(f"{lives} canın kaldı")
        
    if lives == 0:
        print("Öldün!")
        

#zorluk-2

    
while karakter_kaldi == 0:
     devam_string = input("Devam etmek ister misin?(y/n):" )
     yes = "y"
     no = "n"   
            
    
     if  devam_string in yes:
        ipucu_2 = "Bitki/çay gibi içeceklere katılır"
        print(ipucu_2)
        key = "Zerdeçal"
        global_string = ""
        lives = 10

        while lives > 0:
            
            karakter_kaldi = 0
            
            for karakter in key:
                if karakter in global_string:
                    print(karakter)
                else:
                    print("-")    
                    karakter_kaldi += 1  
            if karakter_kaldi == 0:
                print("Tebrikler "+name+" kelimeyi doğru tahmin ettin")
                break
            
            string = input("Kelimeyi tahmin edin: ")
            global_string += string
            if string not in key:
                lives -= 1
                print("Tahmin edemedin")
                print(f"{lives} canın kaldı")
                
            if lives == 0:
                print("Öldün!")
                
     else:
          break
     break


#zorluk-3

     
while karakter_kaldi == 0:
     devam_string = input("Devam etmek ister misin?(y/n):" )
     yes = "y"
     no = "n"   
            
    
     if  devam_string in yes:
        ipucu_3 = "Breaking Bad'de Jesse Pinkmanın öldürdüğü kimyacının adı"
        print(ipucu_3)  
        key = "Victor"
        global_string = ""
        lives = 10

        while lives > 0:
            
            karakter_kaldi = 0
            
            for karakter in key:
                if karakter in global_string:
                    print(karakter)
                else:
                    print("-")    
                    karakter_kaldi += 1  
            if karakter_kaldi == 0:
                print("Tebrikler "+name+" kelimeyi doğru tahmin ettin")
                break
            
            string = input("Kelimeyi tahmin edin: ")
            global_string += string
            if string not in key:
                lives -= 1
                print("Tahmin edemedin")
                print(f"{lives} canın kaldı")
                
            if lives == 0:
                print("Öldün!")
                
     else:
          break
     break
        

#zorluk-4 
     
while karakter_kaldi == 0:
     devam_string = input("Devam etmek ister misin?(y/n):" )
     yes = "y"
     no = "n"   
            
    
     if  devam_string in yes:
        ipucu_3 = "Mustafa Kemal Atatürk'ün Çanakkale savaşında ki rütbesi"
        print(ipucu_3)  
        key = "Yarbay"
        global_string = ""
        lives = 10

        while lives > 0:
            
            karakter_kaldi = 0
            
            for karakter in key:
                if karakter in global_string:
                    print(karakter)
                else:
                    print("-")    
                    karakter_kaldi += 1  
            if karakter_kaldi == 0:
                print("Tebrikler "+name+" kelimeyi doğru tahmin ettin")
                break
            
            string = input("Kelimeyi tahmin edin: ")
            global_string += string
            if string not in key:
                lives -= 1
                print("Tahmin edemedin")
                print(f"{lives} canın kaldı")
                
            if lives == 0:
                print("Öldün!")
                
     else:
        print("Oyun bitti kazandınız")
        break
     break
 
        
#zorluk-5

while karakter_kaldi == 0:
     devam_string = input("Devam etmek ister misin?(y/n):" )
     yes = "y"
     no = "n"   
            
    
     if  devam_string in yes:
        ipucu_3 = "Dünyanın en yakışıklı adamı"
        print(ipucu_3)  
        key = "uğur"
        global_string = ""
        lives = 10

        while lives > 0:
            
            karakter_kaldi = 0
            
            for karakter in key:
                if karakter in global_string:
                    print(karakter)
                else:
                    print("-")    
                    karakter_kaldi += 1  
            if karakter_kaldi == 0:
                print("Tebrikler "+name+" oyunu başarılı bir şekilde kazandın")
                break
            
            string = input("Kelimeyi tahmin edin: ")
            global_string += string
            if string not in key:
                lives -= 1
                print("Tahmin edemedin")
                print(f"{lives} canın kaldı")
                
            if lives == 0:
                print("Öldün!")
                
     else:
        break
     break
