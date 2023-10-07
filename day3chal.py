

capital = int(input("Put here the amount of principal originally deposited into the account: "))
rate = int(input("Put here the interest rate paid by the account: "))
period = int(input("Put here the number of times per year: "))
years = int(input("Put here the number of year: "))

final = capital*(1+(rate/(period*100)))**(years*period)

print("After", years, " years you'll have the amount of ", final, "$ in your account")



# a = p(1+r/t)**n.t
