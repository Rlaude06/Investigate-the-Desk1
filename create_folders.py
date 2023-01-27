import os, string
path = "files"
ch = string.ascii_lowercase
def rec():
    for a_1 in ch:
        #os.mkdir(path+"/%s" % (a_1))
        for a_2 in ch:
            os.mkdir(path+"/%s/%s" % (a_1, a_2))
            for a_3 in ch:
                os.mkdir(path+"/%s/%s/%s" % (a_1, a_2, a_3))
                for a_4 in ch:
                    os.mkdir(path+"/%s/%s/%s/%s" % (a_1, a_2, a_3, a_4))

rec()