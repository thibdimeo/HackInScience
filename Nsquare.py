def draw_n_squares(n=5):
    Ncap = "+---"
    Ccap ="+\n"
    Nwall = "|   "
    Cwall = "|\n"
    construct = Ncap*n+Ccap+Nwall*n+Cwall+(Ncap*n+Ccap+Nwall*n+Cwall)*(n-1)+Ncap*n+Ccap
    return(construct)

print(draw_n_squares())