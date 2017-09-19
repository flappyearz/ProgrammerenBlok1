def new_password(oldpassword, newpassword):
    ##char = newpassword.count()
    if oldpassword != newpassword: ## and char > 7:
        return True
    else:
        return False

##print(new_password(input("wat is je oude wachtwoord?"), input(('wat is je nieuwe wachtwoord?'))))
print(new_password('jantje', 'johantje'))