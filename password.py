from string import ascii_letters, digits, punctuation


# possible US keys in the keyboard if use only ascii_letters: 94 x 94 x 94 x 94 = 78,074,896
# if the password is 8 long there are 94 to the root of 8 posibilities. 6 quadtrilians 

for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i, j, k ,l)