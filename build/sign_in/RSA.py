
from random import randrange, getrandbits
from pathlib import Path
from os import system
try:
    import sys
except:
    system("pip install sys")
    import sys

try:
    import numpy
except:
    system("pip install numpy")
    import numpy

try:
    from PIL import Image
except:
    system("pip install Pillow")
    from PIL import Image

# file = "tichcuc" 
# typeFile =".jpg" # png or jpg

# image_path = f"C:/Users/Public/IMG/{file}{typeFile}"

# decrypted_path = f"C:/Users/Public/IMG/{file}_decrypted{typeFile}"

# encrypted_path = f"C:/Users/Public/IMG/{file}_encrypted.bmp" 

# luu file ma hoa dang bitmap

# Đọc hình ảnh và gán cho biến my_img


# my_img = Image.open(image_path)

def power(a, d, n):
    ans = 1
    while d != 0:
        if d % 2 == 1:
            ans = ((ans % n) * (a % n)) % n
        a = ((a % n) * (a % n)) % n
        d >>= 1
    return ans

def MillerRabin(N, d):
    a = randrange(2, N - 1)
    x = power(a, d, N)
    if x == 1 or x == N - 1:
        return True
    else:
        while(d != N - 1):
            x = ((x % N) * (x % N)) % N
            if x == 1:
                return False
            if x == N - 1:
                return True
            d <<= 1
    return False

def is_prime(N, K):
    if N == 3 or N == 2:
        return True
    if N <= 1 or N % 2 == 0:
        return False
  
    # Tìm d sao cho d*(2^r)=X-1
    d = N - 1
    while d % 2 != 0:
        d /= 2

    for _ in range(K):
        if not MillerRabin(N, d):
            return False
    return True

def generate_prime_candidate(length):
    # Sinh các bit ngẫu nhiên
    p = getrandbits(length)
    # Áp dụng mặt nạ để đặt MSB và LSB thành 1
    # Đặt MSB thành 1 để đảm bảo chúng ta có một Số có 1024 bit.
    # Đặt LSB thành 1 để đảm bảo chúng ta nhận được Một Số Lẻ.
    p |= (1 << length - 1) | 1
    return p

def generatePrimeNumber(length):
    A = 4
    while not is_prime(A, 128):
        A = generate_prime_candidate(length)
    return A

def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)

def gcdExtended(E, eulerTotient):
    a1, a2, b1, b2, d1, d2 = 1, 0, 0, 1, eulerTotient, E

    while d2 != 1:
        # k
        k = (d1 // d2)

        #a
        temp = a2
        a2 = a1 - (a2 * k)
        a1 = temp

        #b
        temp = b2
        b2 = b1 - (b2 * k)
        b1 = temp

        #d
        temp = d2
        d2 = d1 - (d2 * k)
        d1 = temp

        D = b2

    if D > eulerTotient:
        D = D % eulerTotient
    elif D < 0:
        D = D + eulerTotient

    return D

key_path = None

# Tiến hành mã hóa
def encryption_image(image):
    
    length = 5
    P = generatePrimeNumber(length)
    Q = generatePrimeNumber(length)

    # Bước 2: Tính toán N=P*Q và Euler Totient Function = (P-1)*(Q-1)
    N = P * Q
    eulerTotient = (P - 1) * (Q - 1)
    print("N:", N)

    # Bước 3: Tìm E sao cho GCD(E, eulerTotient)=1 (tức là E phải nguyên tố cùng nhau) sao cho nó thỏa điều kiện này: 1<E<eulerTotient
    E = generatePrimeNumber(4)
    while GCD(E, eulerTotient) != 1:
        E = generatePrimeNumber(4)
    print("Khóa công khai E:", E)

    # Bước 4: Tìm D. 
    # Đối với việc tìm D: Nó phải thỏa mãn tính chất này: (D*E)Mod(eulerTotient)=1;
    # Bây giờ chúng ta có hai lựa chọn
    # 1. Chúng ta chọn ngẫu nhiên D và kiểm tra xem điều kiện trên có thỏa mãn không.
    # 2. Để Tìm D, chúng ta có thể Sử dụng Thuật toán Euclid Mở rộng: ax+by=1 tức là eulerTotient(x)+E(y)=GCD(eulerTotient,E)
    # Ở đây, phương án tốt nhất là chọn phương án 2 (Thuật toán Euclid Mở rộng).
    D = gcdExtended(E, eulerTotient)
    print("Khóa riêng tư D:", D)

    # imgfile = Image.open(image_path)
    imgfile = Image.open(image)
    file_name = Path(image).stem
    extension = Path(image).suffix
    col,row = imgfile.size
    pixels = imgfile.load()
    
    #Encryted:
    ##Khởi tạo mảng rõng để chứa giá trị pixel sẽ được đọc từ ảnh.
    enc = [[0 for x in range(col)] for y in range(row)]

    #chạy 2 vòng for để đọc ra giá trị R,G,B của từng pixel sau đó mã hóa 3 giá trị này,
    #Rồi lưu vào mảng đã khởi tạo bên trên.
    
    for i in range(row):
        for j in range(col):
            r,g,b = pixels[j,i]
            r1 = pow(r+10,E,N)
            g1 = pow(g+10,E,N)
            b1 = pow(b+10,E,N)
            enc[i][j] = [r1,g1,b1]
                    
    ##-----
    ## Khởi tạo thêm 1 mảng có kích thước gấp đôi mảng cũ.
    ## ta sẽ thực hiện chai lấy thương cho 256 với từng giá trị màu cho từng pixel để được giá trị mày R,G,B luôn nằm trong (0,256)
    ## Ta lưu giá trị thương vào cột chẵn 0,2,4,.. và Giá trị dư vào cột lẻ 1,3,5,..
    enc_t = [[0 for x in range(col+col)] for y in range(row)]

    for i in range(row):
        for j in range(col):
            enc_t[i][j] = enc[i][j]
                
    for i in range(row):
        for j in range(col):
            r,g,b = enc[i][j]
                
            r1 = r//256
            g1 = g//256
            b1 = b//256
                
            r2 = r%256
            g2 = g%256
            b2 = b%256
                
            enc_t[i][j*2+1] = [r1,g1,b1]##right
            enc_t[i][j*2] = [r2,g2,b2]##left
            temp = enc_t[i][col+j]
    
    rdt = numpy.array(enc_t,dtype=numpy.uint8)
    ## Ta lưu mảng các pixel đã được mã hóa vào Ảnh định dạng .bmp.
    img1 = Image.fromarray(rdt,"RGB")
    # img1.save('./in.bmp')

    # Ghi khóa ra file

    encrypted_path = f"C:/Users/Public/IMG/{file_name}_encrypted.bmp"
    img1.save(encrypted_path)
    key_path = f"C:/Users/Public/IMG/{file_name}_key.txt"
    with open(key_path, 'w') as f:
        f.write(f"N:{N},Public Key E:{E},Private key D:{D},Extension:{extension}")
    print("Khóa đã được ghi ra file:", key_path)

    return key_path

# encrypted_path = f"C:/Users/Public/IMG/{file}_encrypted.bmp"
# my_img.save(encrypted_path)


## Hàm return_Ori giúp trả về giá trị ban đầu đã mã hóa với kích thước của mảng ban đầu.
## Bằng cách tính toán thương*256 + dư. Với 2 giá trị đầu vào là cột chẵn và cột lẽ kế bên nhau.
def return_Ori(enc_t1,enc_t2):
        result = [0,0,0]
        r1,g1,b1 = enc_t1
        r2,g2,b2 = enc_t2
        result[0] = r2*256+r1
        result[1] = g2*256+g1
        result[2] = b2*256+b1
        return result
      
def decryption_image(n, d, image, filename):
    # n = int(input("Nhập giá trị của N: "))
    # d = int(input("Nhập giá trị của D: "))
    # img = Image.open(encrypted_path)

    key_filename = image.replace("_encrypted.bmp", "_key.txt")
    print(key_filename)
    with open(key_filename, 'r') as f:
        key_info = f.read()
    
    extension_line = [line for line in key_info.split(",") if line.startswith("Extension:")][0]
    extension = extension_line.split(":")[1]

    imgfile = Image.open(image)
    pixels = imgfile.load()
    ## Lấy ra cột và dòng của mảng cần được giải mã.
    ## Vì kích thước mảng gấp đôi mảng ban đầu nên ta chia 2 ở số cột.
    col,row = imgfile.size
    col=col//2
    
    dec = [[0 for x in range(col)] for y in range(row)]
    ## ta thực hiện lấy giá trị R,G,B đã được mã hóa bằng hàm return_Ori.
    ## Sau đó giải mã 3 giá trị này ta sẽ được 1 điểm ảnh.
    for i in range(row):
        for j in range(col):
            r,g,b = return_Ori(pixels[j*2,i],pixels[j*2+1,i])
            r1 = pow(r,d,n)-10
            g1 = pow(g,d,n)-10
            b1 = pow(b,d,n)-10
            dec[i][j] = [r1,g1,b1]
    ## Lưu mảng đã được giải mã ta sẽ được hình ảnh ban đầu.		
    img2 = numpy.array(dec,dtype = numpy.uint8)
    img3 = Image.fromarray(img2,"RGB")
    filename = filename.split(".")[0]
    print(filename)

    decrypted_filename = filename.replace("_encrypted", "")
    # extension = Path(image).suffix
    decrypted_path = f"C:/Users/Public/IMG/{decrypted_filename}_decrypted{extension}"
    # decrypted_path = f"C:/Users/Public/IMG/decrypted_{filename}.jpg"
    # img3.save(decrypted_path)
    img3.save(decrypted_path)
    print(f"Hình ảnh đã được giải mã và lưu tại: {decrypted_path}")
    return decrypted_path


# Sử dụng hàm để giải mã hình ảnh


# encryption_image(N,E)
# decryption_image(N,D)

