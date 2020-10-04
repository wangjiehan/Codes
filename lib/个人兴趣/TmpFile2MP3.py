with open ("1364973839-128-2fe108c7d24fb66f55524f8b72cdfd61.uc",'rb') as f:
    btay = bytearray(f.read())
with open("t.mp3",'wb') as out:
    for i,j in enumerate(btay):
        btay[i] = j ^ 0xa3
    out.write(bytes(btay))
