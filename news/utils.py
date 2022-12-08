class My_ex():
    my_ex = ''

    def get_prob(self):
        return self.my_ex.upper()

    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()