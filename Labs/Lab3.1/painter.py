from person import Person

class Painter(Person):
    def __init__(self, firstname:str, lastname:str, birthday_date:str, painting_style:str) -> None:
        super().__init__(firstname, lastname, birthday_date)
        self.painting_style = painting_style

    def painter_info(self):
        return f"{super().person_info()} My painting style is {self.painting_style}."