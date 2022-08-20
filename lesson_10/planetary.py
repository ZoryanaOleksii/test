
def Foo(planetary, circus, stadium, pl_cir, pl_st, cir_st, ill):

    print((planetary - pl_st - pl_cir) + (circus - pl_cir - cir_st) + (stadium - pl_st - cir_st) + pl_cir + pl_st + cir_st + ill)

    pass
Foo(19, 10, 6, 5, 3, 1, 3)
