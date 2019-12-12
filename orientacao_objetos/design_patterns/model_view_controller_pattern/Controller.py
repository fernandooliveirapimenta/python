from design_patterns.model_view_controller_pattern.Model import Person
import design_patterns.model_view_controller_pattern.View as view


def showAll():
    people_in_db = Person.getAll()
    return view.showAllView(people_in_db)


def start():
    view.startView()
    showAll()
    view.endView()


if __name__ == '__main__':
   start()


