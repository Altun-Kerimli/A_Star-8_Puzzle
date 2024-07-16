
class Dugum:  
    def __init__(self, spuz, hedf, prevmx):
        self.data = spuz                            #problem matris(puzzle)
        self.hedf = hedf                            #hedef matris(puzzle)
        self.prevmx = prevmx                        #Bir onceki matris
        self.Islem = Ajan(self.data, self.hedf)     #Ajan clasinin fonksiyonlarinin kullanilmasini saglayan temsilci
        
    def bmove(self,arr,case, prevmx):                       #None matrisi silir.
        if arr == 0:                                #None'dan farkli matrisleri listeye ekle
            del arr
        elif prevmx == arr:
            del arr
        else:
            case.append(arr)

    def find(self, arr):                #bos hanenin(0'in)oldugu konumu bulur ve geri donderir
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == 0:
                    return i,j
                
    def shuffle(self, spuz, x1, y1, x2, y2):    #probllem matrisinin bos konumunu gosterilen yonde haraket ettiri
        if (x2>=0 and x2<3) and (y2>=0 and y2<3):
        
            temp_puz = []
            temp_puz = self.copy(spuz)
            temp_puz[x1][y1] , temp_puz[x2][y2] = temp_puz[x2][y2] , temp_puz[x1][y1]
            
            return temp_puz    
        else:
            return 0
        
    #bir matrisi kopyalar ve geri gonderir    
    def copy(self,arr):    
        temp = []
        
        for i in arr:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        
        return temp

    #Generate_Child: her adimda yaranan cocuk matrislerden toplam maliyeti en dusuk olanin matrisi secib geri gonderilmesi   
    def generate_child(self):                       
        x,y = self.find(self.data)

        child = []              #siradaki matris
        mnval = []              #minimum deger
        val_list = []           #harakerlerden sonraki fn sayilari
             
        
        up   = [x-1,y]          
        down = [x+1,y]
        left = [x  ,y-1]
        right= [x  ,y+1]
        
        children1 = self.shuffle(self.data, x, y, up[0], up[1])             #Yukari haraket olunmus matris
        children2 = self.shuffle(self.data, x, y, down[0], down[1])         #Asagi haraket olunmus matris
        children3 = self.shuffle(self.data, x, y, left[0], left[1])         #sola haraket olunmus matris
        children4 = self.shuffle(self.data, x, y, right[0], right[1])       #saga haraket olunmus matris
        
        self.bmove(children1, val_list,self.prevmx)                         #4 tarafa None\cerciveden  disari 
        self.bmove(children2, val_list,self.prevmx)                         #matrisleri silen 
        self.bmove(children3, val_list,self.prevmx)                         #fonksiyonuna atama
        self.bmove(children4, val_list,self.prevmx)
        
        for i in range(len(val_list)):                   #childern matrislerinin fn degerini 
            a = self.Islem.fn(val_list[i] , self.hedf)   #min value listesine ekle
            mnval.append(a)
                
        #minimum value listesini siralayarak 0'ci indexine en kucuk deger ataniyor
        mnval.sort()

        for i in range(0, len(val_list)):                #value listdeki matrislerin fn degerlerini
            a = self.Islem.fn( val_list[i] , self.hedf)  #min value listeinin 0ci indexi ile karsilastirir
            if a == mnval[0]:                            #val_list deki matrisin fn degeri min value'nun 
                child = val_list[i]                      #0ci indexine esitse child matsine atar ve geri dondurur
        
        
        return child

class Ajan:     #Islemin gerceklestirecek uygulama
    def __init__(self, puzl, hedef):
        self.spuz = puzl            #Problem matris
        self.hdef = hedef           #Hedef matris
        self.gn = 0                 #Baslangic adim maliyet
        self.temp = self.spuz
        
    def hn(self, arr, arr2):        #hedef ve problem martrislerinde bos haneden(0'dan) baska uyusmayan hanelerin sayi
        hn = 0
        for i in range(len(arr2)):
            for j in range(len(arr2)):
                if (arr[i][j] != arr2[i][j]) :
                    
                    if arr2[i][j] == 0:
                        continue
                    
                    hn+=1
                    
        return hn
    
    def fn(self, arr, arr2):                        #fn = hn + gn
        return self.hn(arr, arr2) + self.gn 
    
    def display(self, arr):                         #fn, gn, hn degerlerinin ve problem matrisinin goruntulenmesi
        print('hn = ', self.hn(arr, self.hdef))
        print('gn = ', self.gn)
        print('fn = ', self.fn(arr, self.hdef))
        for i in range(len(arr)):
            print(arr[i], '\n')
        print('\n')
    
    def procs(self):                                #problem matris hedef matrise esit olana kadar
            
        self.display(self.spuz)                     #problem matrise Dugum clasinda generate_child fonksiyonunun ciktisini atar
        while True:                                 # ve adim maliyeti 1 arttiri
            
            self.spuz = Dugum(self.spuz, self.hdef, self.temp).generate_child()
            if self.gn > 0:
                self.temp = self.spuz

            self.gn += 1
            self.display(self.spuz)
            
            if self.spuz == self.hdef:
                print('matris tamamlandi')
                break
        
"""
#Hedef matris
hdf = [[1,2,3], 
       [8,0,4], 
       [7,6,5]]

#Problem matris
spuz= [[0,3,4], 
       [1,2,5], 
       [8,7,6]]

"""
#Hedef matris
hdf = [[1,2,3], 
       [4,5,6], 
       [7,8,0]]

#Problem matris
spuz= [[4,1,3], 
       [7,2,5], 
       [0,8,6]]

Agt = Ajan(spuz, hdf)
Agt.procs()
 